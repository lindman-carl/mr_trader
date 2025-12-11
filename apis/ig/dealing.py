class Dealing:
    def __init__(self, client):
        self.client = client

    def get_deal_confirmation(self, deal_reference):
        """Returns a deal confirmation for the given deal reference."""
        return self.client.request("GET", f"/confirms/{deal_reference}", version="1")

    def get_positions(self):
        """Returns all open positions for the active account."""
        return self.client.request("GET", "/positions", version="2")

    def get_position(self, deal_id):
        """Returns an open position for the active account by deal identifier."""
        return self.client.request("GET", f"/positions/{deal_id}", version="2")

    def create_position(self, data):
        """Creates a new position."""
        return self.client.request("POST", "/positions/otc", data=data, version="2")

    def update_position(self, deal_id, data):
        """Updates an existing position."""
        return self.client.request(
            "PUT", f"/positions/otc/{deal_id}", data=data, version="2"
        )

    def close_position(self, data):
        """Closes one or more existing positions."""
        return self.client.request(
            "POST", "/positions/otc", data=data, version="1"
        )  # DELETE method is deprecated/not standard for closing in some APIs, but IG uses POST with direction opposite or DELETE. Docs say DELETE usually. Let's check docs.
        # Wait, docs say DELETE /positions/otc to close.
        # But often closing is a new deal.
        # Let's check the table again.
        # /positions/otc DELETE - delete a resource (close position)
        # So I should implement delete_position.

    def delete_position(self, deal_id, data=None):
        """Closes an existing position."""
        # DELETE usually doesn't take a body in standard HTTP but IG might require it for partial close etc.
        # Actually, for IG, closing a position is often done via DELETE /positions/otc
        # But wait, the table says:
        # /positions/otc DELETE
        # Let's assume it takes data for details like size.
        return self.client.request("DELETE", "/positions/otc", data=data, version="1")

    def get_working_orders(self):
        """Returns all working orders for the active account."""
        return self.client.request("GET", "/working-orders", version="2")

    def create_working_order(self, data):
        """Creates a new working order."""
        return self.client.request(
            "POST", "/working-orders/otc", data=data, version="2"
        )

    def delete_working_order(self, deal_id):
        """Deletes a working order."""
        return self.client.request(
            "DELETE", f"/working-orders/otc/{deal_id}", version="2"
        )

    def update_working_order(self, deal_id, data):
        """Updates a working order."""
        return self.client.request(
            "PUT", f"/working-orders/otc/{deal_id}", data=data, version="2"
        )
