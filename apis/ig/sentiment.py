class Sentiment:
    def __init__(self, client):
        self.client = client

    def get_client_sentiment(self, market_ids):
        """Returns the client sentiment for the given market(s)."""
        # market_ids can be a single ID or a comma-separated string of IDs
        return self.client.request(
            "GET", "/client-sentiment", params={"marketIds": market_ids}, version="1"
        )

    def get_market_sentiment(self, market_id):
        """Returns the client sentiment for the given market."""
        return self.client.request("GET", f"/client-sentiment/{market_id}", version="1")

    def get_related_sentiment(self, market_id):
        """Returns the client sentiment for the given market and related markets."""
        return self.client.request(
            "GET", f"/client-sentiment/related/{market_id}", version="1"
        )
