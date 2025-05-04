import requests
import os
import time
import re

headers = {}

count = 50
base_url = "https://www.linkedin.com/learning-api/me?q=history&start={offset}&count={count}"
all_items = []
offset = 0

while True:
    url = base_url.format(offset=offset, count=count)
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch page at offset {offset}, status: {response.status_code}")
        break

    data = response.json().get('data', {})
    print(data.get('paging').get('total'))
    
    elements = data.get('*elements', [])
    if not elements:
        print("No more items found.")
        break

    all_items.extend(elements)
    print(f"Fetched {len(elements)} items at offset {offset}")
    
    paging = data.get('paging', {})
    total = paging.get('total', 0)
    offset += count

    if offset >= total:
        break

    time.sleep(1)  # Optional delay to avoid rate-limiting

# Ensure the certs directory exists
os.makedirs('certs', exist_ok=True)

headers = {}

for idx, item in enumerate(all_items):
    try:

        course_number = item.split(":")[-1]
        learner_urn = f"urn:li:learnerCertificate:(urn:li:enterpriseProfile:(urn:li:enterpriseAccount:2154233,86293540),urn:li:lyndaCourse:{course_number},urn:li:lyndaCredentialingProgram:(urn:li:lyndaCredentialingAgency:10,10))"
        encoded_urn = requests.utils.quote(learner_urn, safe='')
        cert_url = f"https://www.linkedin.com/learning-api/contentCertificate?learnerCertificateUrn={encoded_urn}"

        response = requests.get(cert_url, headers=headers)
        if response.status_code != 200:
            print(f"[{idx+1}] Failed to fetch certificate JSON for {course_number}")
            continue

        content_disposition = response.headers['Content-Disposition']
        match = re.search(r'filename="([^"]+)"', content_disposition)
        filename = match.group(1)
        filename = f"certs/{filename}"

        # Download the actual PDF

        with open(filename, 'wb') as f:
            f.write(response.content)
            print(f"[{idx+1}] Saved certificate: {filename}")


    except Exception as e:
        print(f"[{idx+1}] Error processing item: {e}")