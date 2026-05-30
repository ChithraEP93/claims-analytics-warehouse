
from azure.storage.blob import BlobServiceClient
import os

def upload_files():
    #Azure connection string
    connection_string="Connection String"

    #Connect to Azure Blob
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    #containers and folders
    folders={
        "silver":"data/silver",
        "gold":"data/gold"
    }

    #upload files
    for container_name ,local_folder in folders.items():
        for file_name in os.listdir(local_folder):
            file_path=os.path.join(local_folder,file_name)

            blob_client=blob_service_client.get_blob_client(
                container=container_name,
                blob=file_name)
        
            with open(file_path,"rb") as data:
                blob_client.upload_blob(data,overwrite=True)
            print(f"{file_name} uploaded to {container_name}")


upload_files()