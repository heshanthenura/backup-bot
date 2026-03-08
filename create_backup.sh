#!/bin/bash
set -e

TIMESTAMP=$(date +%Y_%m_%d_%H_%M)
BACKUP_FILE="backup_$TIMESTAMP.gz"

echo "Creating MongoDB backup..."

mongodump --uri="$MONGO_URI" --archive="$BACKUP_FILE" --gzip

echo "Backup created: $BACKUP_FILE"
echo "ZIP_FILE=$BACKUP_FILE" >> $GITHUB_OUTPUT