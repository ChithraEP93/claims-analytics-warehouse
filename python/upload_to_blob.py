
from azure.storage.blob import BlobServiceClient
import os

# Azure Storage connection string
connection_string = "connection string"

# Connect to Blob Storage
blob_service_client=BlobServiceClient.from_connection_string(connection_string)


# Container name
container_name = "silver"

# Local folder path
local_folder = "data/silver"

# Upload files
for file_name in os.listdir(local_folder):

    file_path = os.path.join(local_folder, file_name)

    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=file_name
    )

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    print(f"{file_name} uploaded successfully")

