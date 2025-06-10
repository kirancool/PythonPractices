import msal

CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
TENANT_ID = 'YOUR_TENANT_ID'

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]

# Create a confidential client
app = msal.ConfidentialClientApplication(
    CLIENT_ID,
    authority=AUTHORITY,
    client_credential=CLIENT_SECRET
)

# Get token
token_result = app.acquire_token_for_client(scopes=SCOPE)

access_token = token_result['access_token']


import requests

# Replace with the email or user id of the mailbox you want to read
USER_ID = 'user@example.com'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Accept': 'application/json'
}

# Example: get the top 10 latest emails from Inbox
url = f'https://graph.microsoft.com/v1.0/users/{USER_ID}/mailFolders/Inbox/messages?$top=10'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    messages = response.json().get('value')
    for msg in messages:
        print(f"Subject: {msg['subject']}")
        print(f"From: {msg['from']['emailAddress']['address']}")
        print(f"Received: {msg['receivedDateTime']}")
        print(f"Body Preview: {msg['bodyPreview']}\n")
else:
    print(f"Error {response.status_code}: {response.text}")
