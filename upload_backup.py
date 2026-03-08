import os
import dropbox


ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ZIP_FILE = os.environ.get("ZIP_FILE")

if not ACCESS_TOKEN:
    raise ValueError("ACCESS_TOKEN is not set")
if not ZIP_FILE or not os.path.exists(ZIP_FILE):
    raise ValueError(f"ZIP_FILE '{ZIP_FILE}' does not exist")

dbx = dropbox.Dropbox(ACCESS_TOKEN)

dest_path = f"/backups/{ZIP_FILE}"

with open(ZIP_FILE, "rb") as f:
    print(f"Uploading {ZIP_FILE} to Dropbox at {dest_path}...")
    dbx.files_upload(f.read(), dest_path, mode=dropbox.files.WriteMode.add)

print("Upload completed!")