"""
Fetcher module to retrieve job data from the USAJOBS API
Returns job data in JSON format
Version: 1.0.0
Created by: Cory Miglis
app/fetcher.py
"""

import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_jobs():
    """
    Fetches job data from the USAJOBS API.
    
    Returns:
        dict: The JSON response from the API containing job data.
    """
    api_key = os.getenv('USAJOBS_API_KEY')
    user_email = os.getenv('USAJOBS_USER_EMAIL')

    headers = {
        "Host": "data.usajobs.gov",
        "User-Agent": user_email,
        "Authorization-Key": api_key
    }

    url = 'https://data.usajobs.gov/api/Search'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code} - {response.text}")