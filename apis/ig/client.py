import requests
import os
from dotenv import load_dotenv
from .accounts import Accounts
from .dealing import Dealing
from .markets import Markets
from .watchlists import Watchlists
from .sentiment import Sentiment
from .general import General
from .costs import IndicativeCosts

load_dotenv()


class IGClient:
    def __init__(self, username=None, password=None, api_key=None, acc_type=None):
        self.username = username or os.getenv("IG_USERNAME")
        self.password = password or os.getenv("IG_PASSWORD")
        self.api_key = api_key or os.getenv("IG_API_KEY")
        self.acc_type = acc_type or os.getenv("IG_ACC_TYPE", "demo")

        if self.acc_type == "live":
            self.base_url = "https://api.ig.com/gateway/deal"
        else:
            self.base_url = "https://demo-api.ig.com/gateway/deal"

        self.session = requests.Session()
        self.cst = None
        self.x_security_token = None
        self.account_id = None

        # Initialize endpoint groups
        self.accounts = Accounts(self)
        self.dealing = Dealing(self)
        self.markets = Markets(self)
        self.watchlists = Watchlists(self)
        self.sentiment = Sentiment(self)
        self.general = General(self)
        self.costs = IndicativeCosts(self)

    def _get_headers(self, version="2"):
        headers = {
            "X-IG-API-KEY": self.api_key,
            "Content-Type": "application/json",
            "Accept": "application/json; charset=UTF-8",
            "Version": version,
        }
        if self.cst:
            headers["CST"] = self.cst
        if self.x_security_token:
            headers["X-SECURITY-TOKEN"] = self.x_security_token
        return headers

    def login(self):
        url = f"{self.base_url}/session"
        headers = self._get_headers()
        # Remove auth tokens for login request
        headers.pop("CST", None)
        headers.pop("X-SECURITY-TOKEN", None)

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

    def logout(self):
        if not self.cst or not self.x_security_token:
            return

        url = f"{self.base_url}/session"
        headers = self._get_headers(version="1")
        self.session.delete(url, headers=headers)
        self.cst = None
        self.x_security_token = None
        self.account_id = None
        print("Logged out.")

    def request(self, method, endpoint, params=None, data=None, version="2"):
        if not self.cst or not self.x_security_token:
            raise Exception("Not logged in. Call login() first.")

        url = f"{self.base_url}{endpoint}"
        headers = self._get_headers(version=version)

        response = self.session.request(
            method, url, headers=headers, params=params, json=data
        )

        if response.status_code >= 400:
            print(f"Request failed: {response.status_code} - {response.text}")
            response.raise_for_status()

        return response.json()
