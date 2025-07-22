from google.cloud import storage
import os

def upload_to_gcs(local_path: str, bucket_name: str, dest_blob: str) -> str:
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(dest_blob)
    blob.upload_from_filename(local_path)
    return blob.public_url
