class Watchlists:
    def __init__(self, client):
        self.client = client

    def get_watchlists(self):
        """Returns all watchlists belonging to the active account."""
        return self.client.request("GET", "/watchlists", version="1")

    def create_watchlist(self, name, epics=None):
        """Creates a new watchlist."""
        data = {"name": name}
        if epics:
            data["epics"] = epics
        return self.client.request("POST", "/watchlists", data=data, version="1")

    def delete_watchlist(self, watchlist_id):
        """Deletes a watchlist."""
        return self.client.request("DELETE", f"/watchlists/{watchlist_id}", version="1")

    def get_watchlist_details(self, watchlist_id):
        """Returns the details of the given watchlist."""
        return self.client.request("GET", f"/watchlists/{watchlist_id}", version="1")

    def add_market_to_watchlist(self, watchlist_id, epic):
        """Adds a market to a watchlist."""
        data = {"epic": epic}
        return self.client.request(
            "PUT", f"/watchlists/{watchlist_id}", data=data, version="1"
        )

    def remove_market_from_watchlist(self, watchlist_id, epic):
        """Removes a market from a watchlist."""
        return self.client.request(
            "DELETE", f"/watchlists/{watchlist_id}/{epic}", version="1"
        )
