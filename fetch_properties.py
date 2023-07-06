import requests
import os
from dotenv import load_dotenv

load_dotenv()

# HubSpot API credentials
api_key = os.getenv("HUBSPOT_API_KEY")
company_id = "10270578490"

# Endpoint URL
url = f"https://api.hubapi.com/companies/v2/companies/{company_id}"

# Request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}

# Send GET request to retrieve company data
response = requests.get(url, headers=headers)
data = response.json()

# Check if request was successful
if response.status_code == 200:
    # Extract the properties
    properties = data["properties"]

    # Print all properties
    for prop in properties:
        print(f"{prop}: {properties[prop]['value']}")
else:
    print("Failed to retrieve company data.")
