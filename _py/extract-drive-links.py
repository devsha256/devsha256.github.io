import os
import yaml
import re
from PyPDF2 import PdfReader
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
from datetime import datetime

# CONFIG
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
CREDENTIALS_FILE = './_py/credentials.json'  # OAuth desktop credentials JSON
TOKEN_FILE = 'token.pickle'
DRIVE_FOLDER_ID = '1NtMgtu9lOvfPVeNeepjNKXNKtleHMcVa'
LOCAL_PDF_FOLDER = './certs/'
OUTPUT_YAML = './_data/archives.yml'

# AUTHENTICATE USING OAUTH DESKTOP FLOW
def authenticate():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
    return creds

# GET ALL PDF FILES FROM DRIVE FOLDER (with pagination)
def get_drive_files(service):
    all_files = []
    page_token = None

    while True:
        response = service.files().list(
            q=f"'{DRIVE_FOLDER_ID}' in parents and mimeType='application/pdf'",
            fields="nextPageToken, files(id, name)",
            pageSize=1000,  # Adjust as needed (max 1000)
            pageToken=page_token
        ).execute()

        files = response.get('files', [])
        all_files.extend(files)

        page_token = response.get('nextPageToken')
        if not page_token:
            break

    return all_files

# EXTRACT DATA FROM LOCAL PDF
def extract_info_from_pdf(filepath):
    try:
        reader = PdfReader(filepath)
        first_page = reader.pages[0]
        text = first_page.extract_text() or ""

        lines = text.splitlines()
        lines = [line.strip() for line in lines if line.strip()]

        # First non-empty line is the course name
        course_name = lines[0] if lines else 'Unknown Course'

        # Look for the date in the format 'Mmm dd, yyyy'
        date = 'Unknown Date'
        date_pattern = re.compile(r'([A-Za-z]{3,9} \d{1,2}, \d{4})')
        for line in lines:
            match = date_pattern.search(line)
            if match:
                try:
                    parsed_date = datetime.strptime(match.group(1), '%b %d, %Y')
                except ValueError:
                    parsed_date = datetime.strptime(match.group(1), '%B %d, %Y')  # handle full month name
                date = parsed_date.strftime('%Y-%m-%d')
                break

        return course_name, date

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return 'Unknown Course', 'Unknown Date'


# MAIN FUNCTION
def main():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    files = get_drive_files(service)
    certs = []

    for file in files:
        name = file['name']
        file_id = file['id']
        local_path = os.path.join(LOCAL_PDF_FOLDER, name)
        if not os.path.exists(local_path):
            print(f"Local file missing: {name}")
            continue

        course_name, date = extract_info_from_pdf(local_path)
        certs.append({
            'name': course_name,
            'authority': 'LinkedIn Learning',
            'date': date,
            'image': 'linkedin_learning.png',
            'cred_link': 'http://linkedin.com/learning',
            'drive_link': f'https://drive.google.com/file/d/{file_id}/view'
        })

    os.makedirs(os.path.dirname(OUTPUT_YAML), exist_ok=True)
    with open(OUTPUT_YAML, 'w') as f:
        yaml.dump(certs, f, sort_keys=False)

    print(f'✅ Saved {len(certs)} entries to {OUTPUT_YAML}')

if __name__ == '__main__':
    main()

# 1NtMgtu9lOvfPVeNeepjNKXNKtleHMcVa