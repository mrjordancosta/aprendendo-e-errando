import requests
import os
from dotenv import load_dotenv
from google.cloud import talent_v4beta1

# Load the environment variables from the .env file
load_dotenv()

# Checks if the environment variable exists
google_apis_endpoint = os.getenv("GOOGLE_APIS_ENDPOINT")
google_apis_apikey = os.getenv("GOOGLE_APIS_APIKEY")


if not google_apis_endpoint or not google_apis_apikey:
    print("A variável de ambiente GOOGLE_APIS_ENDPOINT ou GOOGLE_APIS_APIKEY não está definida no arquivo .env")
    exit(1)

# Define the search query
query = "suporte"

# Set the headers
headers = {
    "Authorization": f"Bearer {google_apis_apikey}",
    "Content-Type": "application/json",
}

# Set the request body
body = {
    "query": query,
    "location": "Brasil",
    "radius": "100km",
    "remoteWork": True,
}

# Make the request
try:
    response = requests.post(google_apis_endpoint, headers=headers, json=body)

    # Check if the request was successful
    if response.status_code == 200:
        # Analize and check the response as a JSON
        results = response.json()

        # Print the results
        for job in results.get("jobs", []):
            print(job.get("title", "Título não disponível"))
    else:
        print(f"Erro: {response.status_code}, {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Erro na solicitação HTTP: {e}")