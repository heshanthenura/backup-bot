import os
import sys
import dropbox

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise ValueError("ACCESS_TOKEN is not set")

if len(sys.argv) < 2:
    raise ValueError("Usage: python upload.py <file_path>")

FILE_PATH = sys.argv[1]

if not os.path.exists(FILE_PATH):
    raise ValueError(f"File '{FILE_PATH}' does not exist")

FILE_NAME = os.path.basename(FILE_PATH)

dbx = dropbox.Dropbox(ACCESS_TOKEN)

dest_path = f"/backups/{FILE_NAME}"

with open(FILE_PATH, "rb") as f:
    print(f"Uploading {FILE_NAME} to Dropbox at {dest_path}...")
    dbx.files_upload(f.read(), dest_path, mode=dropbox.files.WriteMode.add)

print("Upload completed!")