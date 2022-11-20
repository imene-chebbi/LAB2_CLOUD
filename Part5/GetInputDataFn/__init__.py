# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

from azure.storage.blob import BlobServiceClient
from azure.storage.blob.aio import BlobClient
import os
"""
The GetInputDataFn allows us to use the blob store API and connection string to pull down the files from Azure
It will take us input the name of each file and as output a list of paris <indexline,the line string>
"""

def read_file(filename: str) -> list :
    string_name=your_string_name
    blob_service_client = BlobServiceClient.from_connection_string(string_name)
    container_client = blob_service_client.get_container_client(container="container_name")
    file = container_client.download_blob(filename).readall()
    
    line_index = 0
    lines = list()
    for line in file.decode().split("\n") :
        lines.append([line_index,line.rstrip()])
        line_index += 1            
    return lines


def main(filename: str) -> str:
    return read_file(filename)
