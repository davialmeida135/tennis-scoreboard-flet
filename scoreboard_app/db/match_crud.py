import requests


def create_match(api_url, match_data, token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    response = requests.post(f"{api_url}/matches/new", headers=headers, json=match_data)
    if response.status_code == 201:
        return response.json().get('message')
    else:
        response.raise_for_status()
        
def update_match(api_url, match_id, match_info, token):
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    data = {
        'idMatch': match_id,
        'match_info': match_info
    }
    response = requests.post(f"{api_url}/matches/update", headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get('message')
    else:
        response.raise_for_status()

def delete_match(api_url, match_id, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.delete(f"{api_url}/matches/{match_id}", headers=headers)
    if response.status_code == 200:
        return response.json().get('message')
    else:
        response.raise_for_status()
