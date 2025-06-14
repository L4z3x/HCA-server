from cloudinary import uploader


def upload_image(file, filename: str, folder: str):
    # service = get_drive_service()
    res = uploader.upload(
        file,
        folder=folder,
        public_id=filename,
        resource_type="image",
        overwrite=True,
    )

    return res
