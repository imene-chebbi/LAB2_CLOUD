import time 
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    @task
    def numericalintegralservice(self):
        self.client.get("/numericalintegralservice/0/3.14159")