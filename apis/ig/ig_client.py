import os
import requests
from dotenv import load_dotenv

load_dotenv()


class IGClient:
    def __init__(self, username, password, api_key, acc_type="DEMO"):
        self.username = username
        self.password = password
        self.api_key = api_key
        self.acc_type = acc_type

        if acc_type == "LIVE":
            self.base_url = "https://api.ig.com/gateway/deal"
        else:
            self.base_url = "https://demo-api.ig.com/gateway/deal"

        self.session = requests.Session()
        self.cst = None
        self.x_security_token = None
        self.account_id = None

    def login(self):
        url = f"{self.base_url}/session"
        headers = {
            "X-IG-API-KEY": self.api_key,
            "Version": "2",
            "Content-Type": "application/json",
            "Accept": "application/json; charset=UTF-8",
        }
        data = {"identifier": self.username, "password": self.password}

        response = self.session.post(url, headers=headers, json=data)

        if response.status_code == 200:
            self.cst = response.headers.get("CST")
            self.x_security_token = response.headers.get("X-SECURITY-TOKEN")

            response_data = response.json()
            self.account_id = response_data.get("currentAccountId")
            print(f"Logged in successfully. Account ID: {self.account_id}")
            return response_data
        else:
            print(f"Login failed: {response.status_code} - {response.text}")
            response.raise_for_status()

    def get_positions(self):
        if not self.cst or not self.x_security_token:
            raise Exception("Not logged in. Call login() first.")

        url = f"{self.base_url}/positions"
        headers = {
            "X-IG-API-KEY": self.api_key,
            "CST": self.cst,
            "X-SECURITY-TOKEN": self.x_security_token,
            "Version": "2",
            "Content-Type": "application/json",
            "Accept": "application/json; charset=UTF-8",
        }

        response = self.session.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to get positions: {response.status_code} - {response.text}")
            response.raise_for_status()


if __name__ == "__main__":
    USERNAME = os.getenv("IG_USERNAME")
    PASSWORD = os.getenv("IG_PASSWORD")
    API_KEY = os.getenv("IG_API_KEY")
    ACC_TYPE = os.getenv("IG_ACC_TYPE", "DEMO")

    if not all([USERNAME, PASSWORD, API_KEY]):
        print("Please set IG_USERNAME, IG_PASSWORD, and IG_API_KEY in your .env file.")

    else:
        try:
            client = IGClient(USERNAME, PASSWORD, API_KEY, acc_type=ACC_TYPE)
            client.login()
            positions = client.get_positions()
            print("Positions:", positions)
        except Exception as e:
            print(f"An error occurred: {e}")
