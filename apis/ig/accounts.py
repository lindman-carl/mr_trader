class Accounts:
    def __init__(self, client):
        self.client = client

    def get_accounts(self):
        """Returns a list of accounts belonging to the logged-in client."""
        return self.client.request("GET", "/accounts", version="1")

    def get_preferences(self):
        """Gets the preferences for the logged-in account."""
        return self.client.request("GET", "/accounts/preferences", version="1")

    def update_preferences(self, trailing_stops_enabled=None):
        """Updates the preferences for the logged-in account."""
        data = {}
        if trailing_stops_enabled is not None:
            data["trailingStopsEnabled"] = trailing_stops_enabled
        return self.client.request(
            "PUT", "/accounts/preferences", data=data, version="1"
        )

    def get_activity_history(
        self,
        from_date=None,
        to_date=None,
        last_period=None,
        detailed=False,
        page_size=20,
    ):
        """
        Returns the activity history for the logged-in account.

        Args:
            from_date (str): Start date (yyyy-MM-ddTHH:mm:ss)
            to_date (str): End date (yyyy-MM-ddTHH:mm:ss)
            last_period (str): Period in seconds (e.g. 600)
            detailed (bool): Whether to return detailed history
            page_size (int): Page size
        """
        params = {"detailed": str(detailed).lower(), "pageSize": page_size}

        if last_period:
            return self.client.request(
                "GET", f"/history/activity/{last_period}", params=params, version="3"
            )
        elif from_date and to_date:
            return self.client.request(
                "GET",
                f"/history/activity/{from_date}/{to_date}",
                params=params,
                version="3",
            )
        else:
            return self.client.request(
                "GET", "/history/activity", params=params, version="3"
            )

    def get_transaction_history(
        self,
        transaction_type,
        from_date=None,
        to_date=None,
        last_period=None,
        page_size=20,
    ):
        """
        Returns the transaction history for the logged-in account.

        Args:
            transaction_type (str): Transaction type (ALL, ALL_DEAL, DEPOSIT, WITHDRAWAL)
            from_date (str): Start date (yyyy-MM-ddTHH:mm:ss)
            to_date (str): End date (yyyy-MM-ddTHH:mm:ss)
            last_period (str): Period in seconds
            page_size (int): Page size
        """
        params = {"pageSize": page_size}

        if last_period:
            return self.client.request(
                "GET",
                f"/history/transactions/{transaction_type}/{last_period}",
                params=params,
                version="2",
            )
        elif from_date and to_date:
            return self.client.request(
                "GET",
                f"/history/transactions/{transaction_type}/{from_date}/{to_date}",
                params=params,
                version="2",
            )
        else:
            return self.client.request(
                "GET", "/history/transactions", params=params, version="2"
            )
