from imagekitio import ImageKit
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions
from core.settings import (
    IMAGEKIT_URL_ENDPOINT,
    IMAGEKIT_PRIVATE_API_KEY,
    IMAGEKIT_PUBLIC_API_KEY,
)

imagekit = ImageKit(
    private_key=IMAGEKIT_PRIVATE_API_KEY,
    public_key=IMAGEKIT_PUBLIC_API_KEY,
    url_endpoint=IMAGEKIT_URL_ENDPOINT,
)


def upload_media(file, file_name, folder):
    # check if path exists and then create it if it doesn't and then upload the file to that path folder
    upload_options = UploadFileRequestOptions(folder=folder)
    return imagekit.upload_file(file=file, file_name=file_name, options=upload_options)
