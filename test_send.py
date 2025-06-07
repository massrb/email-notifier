import requests
from google.auth.transport.requests import Request
from google.oauth2 import service_account

# Path to your service account JSON key
KEY_FILE = 'key.json'

# The Cloud Run service URL (audience)
CLOUD_RUN_URL = "https://email-alerts-kg20250607-474201645944.us-east4.run.app/send"

# Load credentials from JSON key file
credentials = service_account.IDTokenCredentials.from_service_account_file(
    KEY_FILE,
    target_audience=CLOUD_RUN_URL
)

# Refresh the token (fetches a fresh token)
credentials.refresh(Request())

# Get the identity token
id_token = credentials.token

# Prepare request to Cloud Run with Authorization header
headers = {
    "Authorization": f"Bearer {id_token}",
    "Content-Type": "application/json"
}

data = {
    "subject": "Hello from Larzman!",
    "body": "This is a test email sent via Cloud Run",
    "to": "wbsurfver@gmail.com"
}

response = requests.post(CLOUD_RUN_URL, json=data, headers=headers)

print("Status code:", response.status_code)
print("Response body:", response.text)


if response.ok:
    print("Email sent successfully")
else:
    print("Failed to send email:", response.text)