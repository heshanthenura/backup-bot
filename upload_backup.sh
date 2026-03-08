#!/bin/bash
set -euo pipefail

echo "Uploading backup to Dropbox..."

curl -X POST https://content.dropboxapi.com/2/files/upload \
  --header "Authorization: Bearer $ACCESS_TOKEN" \
  --header "Dropbox-API-Arg: {\"path\": \"/backups/$ZIP_FILE\",\"mode\": \"add\",\"autorename\": true,\"mute\": false}" \
  --header "Content-Type: application/octet-stream" \
  --http1.1 \
  --data-binary @"$ZIP_FILE"

echo "Backup uploaded: $ZIP_FILE"