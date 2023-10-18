from locust import HttpUser, task

class WriteFiles(HttpUser):
    @task
    def write_files_in_background(self):
        self.client.post("/write-file/")