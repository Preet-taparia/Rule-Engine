import requests

class Communication:
    def __init__(self, console_url):
        self.console_url = console_url

    def send_log(self, log_data):
        try:
            response = requests.post(f"{self.console_url}/api/logs", json=log_data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error sending log: {e}")

    def get_policies(self):
        try:
            response = requests.get(f"{self.console_url}/api/policies")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting policies: {e}")
            return []
