import os
import requests # this is used to send request to API

baseUrl = "https://reqres.in" # this is the address to the requres API
apiKey = os.getenv("apiKeys") #this will read the API key from env, rather than storing it in code

print("API key used:", apiKey)

HEADERS = {"x-api-key": apiKey} # It store API key in this header with every request


# Test 1 -> Check that a valid request is successful
def test_validate_success_responce_200():
    response = requests.get(f"{baseUrl}/api/users?page=2", headers=HEADERS) # requests page 2 of user list
    assert response.status_code == 200 # 200 mean it was success
    body = response.json()
    
    # below will check the responce has page key and it is the exact page we asked for
    assert "page" in body
    assert body["page"] == 2
    
    
# Test 2 -> Check that the API returns the correct user details
def test_user_has_correct_details():
    response = requests.get(f"{baseUrl}/api/users/12", headers=HEADERS) #request user with ID = 12
    assert response.status_code == 200
    user = response.json()["data"]
    
    #BElow will compare each field with the correct value present
    assert user["id"] == 12
    assert user["first_name"] == "Rachel"
    assert user["last_name"] == "Howell"
    assert user["email"] == "rachel.howell@reqres.in"
    
    
# Test 3 -> Check the API handles a user that does not exist    
def test_incorrect_user_id():
    response = requests.get(f"{baseUrl}/api/users/999", headers=HEADERS) #request user with ID = 999
    assert response.status_code == 404 # 404 means NOT FOUND, which is expected
    
    
# Test 4 ->  Check the API rejects a login with a missing password
def test_login_without_password():
    payload = {"email": "arpit.tomar@reqres.in"} # sends only email not the password
    response = requests.post(f"{baseUrl}/api/login", json=payload, headers=HEADERS) #requests for user with the email send in payload
    assert response.status_code == 400 # 400 means a bad request means something is missing 
    assert response.json()["error"] == "Missing password" # API will response exactly what is missing. 