class General:
    def __init__(self, client):
        self.client = client

    def get_application_operations(self):
        """Returns the application operations."""
        return self.client.request("GET", "/operations/application", version="1")

    def disable_application_operations(self):
        """Disables the application operations."""
        return self.client.request(
            "PUT", "/operations/application/disable", version="1"
        )  # PUT usually takes data, but maybe not here.
