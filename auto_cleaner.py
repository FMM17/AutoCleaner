import os
import json
import time
from datetime import datetime, timedelta

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def is_old(file_path, days_unused):
    last_access_time = os.path.getatime(file_path)
    return datetime.now() - datetime.fromtimestamp(last_access_time) > timedelta(days=days_unused)

def main():
    config = load_config()
    folder = config['folder_path']
    extensions = tuple(config['extensions_to_delete'])
    days = config['days_unused']
    whitelist = config['whitelist']

    deleted_files = []

    for root, _, files in os.walk(folder):
        for file in files:
            if file in whitelist:
                continue
            file_path = os.path.join(root, file)
            if file.endswith(extensions) and is_old(file_path, days):
                try:
                    os.remove(file_path)
                    deleted_files.append(file_path)
                    print(f"🗑️  Eliminado: {file_path}")
                except Exception as e:
                    print(f"⚠️  Error eliminando {file_path}: {e}")

    print(f"\n✅ Limpieza completada. Archivos eliminados: {len(deleted_files)}")

if __name__ == "__main__":
    main()
Add main script
