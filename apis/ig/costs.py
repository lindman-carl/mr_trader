class IndicativeCosts:
    def __init__(self, client):
        self.client = client

    # Note: These endpoints might require specific parameters not fully detailed in the summary list.
    # Implementing basic structure.

    def get_costs_and_charges(self):
        # This seems to be a general endpoint or maybe a typo in my understanding of the list.
        # The list had /indicativecostsandcharges/close etc.
        pass

    def calculate_close_costs(self, data):
        """Calculates the indicative costs and charges for closing a position."""
        return self.client.request(
            "POST", "/indicativecostsandcharges/close", data=data, version="1"
        )

    def calculate_open_costs(self, data):
        """Calculates the indicative costs and charges for opening a position."""
        return self.client.request(
            "POST", "/indicativecostsandcharges/open", data=data, version="1"
        )
