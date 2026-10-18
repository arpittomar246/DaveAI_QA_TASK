import os
from locust import HttpUser, task, constant

class ReqresUser(HttpUser):
    host = "https://reqres.in"      # the website we are testing
    wait_time = constant(40)        # each user waits for 40 sec

    @task
    def get_users(self):
        self.client.get("/api/users?page=2", headers={"x-api-key": os.getenv("apiKeys")}) #every user will ask for page 2