import os
import uuid
import yaml

def add_id_to_yml_entries(data_dir="_data"):
    for filename in os.listdir(data_dir):
        if filename.endswith(".yml"):
            filepath = os.path.join(data_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                try:
                    data = yaml.safe_load(file)
                except yaml.YAMLError as e:
                    print(f"Failed to parse {filename}: {e}")
                    continue

            if not isinstance(data, list):
                print(f"Skipping {filename}: not a list of entries.")
                continue

            updated = False
            for entry in data:
                if isinstance(entry, dict) and 'id' not in entry:
                    entry['id'] = str(uuid.uuid4())
                    updated = True

            if updated:
                with open(filepath, 'w', encoding='utf-8') as file:
                    yaml.dump(data, file, allow_unicode=True, default_flow_style=False, sort_keys=False)
                print(f"Updated {filename}")
            else:
                print(f"No changes needed in {filename}")

# Run the function
add_id_to_yml_entries()
