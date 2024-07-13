import requests
from . import API_URL
def create_match(match_data, access_token, refresh_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.post(f"{API_URL}/matches/new", headers=headers, json=match_data)
    if response.status_code == 201:
        return response.json().get('message')
    else:
        response.raise_for_status()
        
def update_match(match_info, access_token, refresh_token):
    headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}
    data = match_info
    response = requests.post(f"{API_URL}/matches/update", headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get('message')
    else:
        response.raise_for_status()

def delete_match(match_id, access_token, refresh_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.delete(f"{API_URL}/matches/{match_id}", headers=headers)
    if response.status_code == 200:
        return response.json().get('message')
    else:
        response.raise_for_status()

def get_user_matches(token, conditions=None):
    headers = {'Authorization': f'Bearer {token}'}
    params = {"conditions": conditions} if conditions else {}
    response = requests.get(f"{API_URL}/user/matches", headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data: {response.status_code} - {response.text}")
        return None
    
def get_match_by_id(match_id):
    
    response = requests.get(f"{API_URL}/matches/{match_id}")
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()