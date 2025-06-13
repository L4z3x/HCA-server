import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from core.settings import GOOGLE_DRIVE_SERVICE_ACCOUNT_JSON

SCOPES = ["https://www.googleapis.com/auth/drive"]


def get_drive_service():
    if not GOOGLE_DRIVE_SERVICE_ACCOUNT_JSON:
        raise RuntimeError("Service account JSON not found in env var.")

    info = json.loads(GOOGLE_DRIVE_SERVICE_ACCOUNT_JSON)
    creds = service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
    return build("drive", "v3", credentials=creds)


def upload_to_drive(file, filename: str, folder: str):
    service = get_drive_service()
    media = MediaIoBaseUpload(file, mimetype="image/jpeg")
    file_metadata = {
        "name": filename,
        "parents": [folder],
    }
    file = (
        service.files()
        .create(
            body=file_metadata,
            media_body=media,
            fields="id, name",
        )
        .execute()
    )
    return file
