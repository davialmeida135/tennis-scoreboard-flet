import requests

API_URL = "http://localhost:5000"

def create_user(username, password):
    payload = {"username": username, "password": password.decode('utf-8')}
    response = requests.post(f"{API_URL}/users/new", json=payload)
    if 'error' in response.json():
        raise Exception(f"{response.json()['error']}")
    return f'User {username} created successfully'

def delete_user(username, password, access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    payload = {"username": username, "password": password}
    response = requests.post(f"{API_URL}/users/delete", json=payload, headers=headers)
    if response.status_code == 200:
        print("User deleted successfully")
    else:
        raise Exception(f"Failed to delete user: {response.status_code} - {response.text}")

def update_user(username, password, access_token, newpassword=None, ):
    headers = {'Authorization': f'Bearer {access_token}'}
    if newpassword is not None:
        payload = {"username": username, "password": password, "new_password": newpassword}
    else:
        payload = {"username": username, "password": password}
    response = requests.put(f"{API_URL}/users/update", json=payload, headers=headers)
    if response.status_code == 200:
        return response
    else:
        raise Exception(f"Failed to update user: {response.status_code} - {response.text}")

def auth_user(username, password):
    payload = {"username": username, "password": password}
    response = requests.post(f"{API_URL}/auth", json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to authenticate user: {response.status_code} - {response.text}")

