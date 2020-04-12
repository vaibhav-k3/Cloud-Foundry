from flask import Flask
import os
import sys
import ibm_boto3
from ibm_botocore.client import Config
from ibm_botocore.exceptions import ClientError

COS_ENDPOINT = "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints" # example: https://s3.us-south.cloud-object-storage.appdomain.cloud
COS_API_KEY_ID = "3ZJ5HIu-qh2qVGlBuQWHKDnKZBtRCwWID_qfQI12XO5D" # example: xxxd12V2QHXbjaM99G9tWyYDgF_0gYdlQ8aWALIQxXx4
COS_AUTH_ENDPOINT = "https://iam.cloud.ibm.com/identity/token"
COS_SERVICE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/725b776f255f4fbcbc709b0c4dc32e04:972488d0-fd95-4a05-b837-67d297538bdd::"
 # example: crn:v1:bluemix:public:cloud-object-storage:global:a/xx999cd94a0dda86fd8eff3191349999:9999b05b-x999-4917-xxxx-9d5b326a1111::
COS_STORAGE_CLASS = "jp-tok-standard" # example: us-south-standard

# Create client connection
cos_cli = ibm_boto3.client("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_SERVICE_CRN,
    ibm_auth_endpoint=COS_AUTH_ENDPOINT,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)

app = Flask(__name__)
port = int(os.getenv('PORT', 8000))
@app.route('/')
def baseRoute():
    return 'Flask app on cloud foundry' + sys.version

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=port)
