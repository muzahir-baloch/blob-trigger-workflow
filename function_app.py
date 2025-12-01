import logging
import azure.functions as func

app = func.FunctionApp()

@app.blob_trigger(
    arg_name="myblob",
    path="incoming/{name}",
    connection="AzureWebJobsStorage"
)
def BlobLogger(myblob: func.InputStream):
    logging.info(
        "Blob trigger function processed blob\n"
        f"Name: {myblob.name}\n"
        f"Size: {myblob.length} bytes"
    )
