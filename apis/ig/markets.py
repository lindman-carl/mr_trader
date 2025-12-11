class Markets:
    def __init__(self, client):
        self.client = client

    def get_market_categories(self, category_id=None):
        """Returns all top-level nodes (market categories) in the market navigation hierarchy."""
        if category_id:
            return self.client.request(
                "GET", f"/categories/{category_id}/instruments", version="1"
            )  # This seems to be sub-nodes
        return self.client.request("GET", "/categories", version="1")  # Top level

    def get_market_navigation(self, node_id=None):
        """Returns the market navigation hierarchy."""
        if node_id:
            return self.client.request(
                "GET", f"/market-navigation/{node_id}", version="1"
            )
        return self.client.request("GET", "/market-navigation", version="1")

    def search_markets(self, search_term):
        """Returns all markets matching the search term."""
        return self.client.request(
            "GET", "/markets", params={"searchTerm": search_term}, version="1"
        )

    def get_market_details(self, epic):
        """Returns the details of the given market."""
        return self.client.request("GET", f"/markets/{epic}", version="3")

    def get_prices(
        self,
        epic,
        resolution,
        num_points=None,
        start_date=None,
        end_date=None,
        page_size=20,
    ):
        """
        Returns historical prices for a given market.

        Args:
            epic (str): The epic of the market
            resolution (str): The resolution of the prices (e.g. MINUTE, MINUTE_5, HOUR, DAY)
            num_points (int): The number of data points to return
            start_date (str): Start date (yyyy-MM-ddTHH:mm:ss)
            end_date (str): End date (yyyy-MM-ddTHH:mm:ss)
            page_size (int): Page size
        """
        if start_date and end_date:
            return self.client.request(
                "GET",
                f"/prices/{epic}/{resolution}",
                params={
                    "startdate": start_date,
                    "enddate": end_date,
                    "pageSize": page_size,
                },
                version="3",
            )
        elif num_points:
            return self.client.request(
                "GET", f"/prices/{epic}/{resolution}/{num_points}", version="3"
            )
        else:
            # Default or error? Let's assume numPoints is required if no dates
            return self.client.request(
                "GET", f"/prices/{epic}/{resolution}/{10}", version="3"
            )
