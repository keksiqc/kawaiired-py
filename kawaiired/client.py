import httpx

from kawaiired.utils import BASE_URL


class KawaiiClient:
    """Wrapper Client for the kawaii.red API."""

    def __init__(self, token: str, base_url: str = BASE_URL) -> None:
        """
        Initialize the client.

        Args:
            token (str): The token to use for the API.
            base_url (str): The base URL to use for the API.
        """
        self.token = token
        self.base_url = base_url

    def get(self, endpoint: str, category: str) -> str:
        """
        Make a request to the API.

        Args:
            endpoint (str): The endpoint to make the request to.
            category (str): The category to make the request to.
        """
        response = httpx.get(
            f"{self.base_url}/{endpoint}/{category}",
            headers={"token": self.token},
        )
        return response.json().get("response")

    def gif(self, category: str) -> str:
        """
        Make a request to the API.

        Args:
            category (str): The category to make the request to.
        """
        return self.get("gif", category)

    def image(self, category: str) -> str:
        """
        Make a request to the API.

        Args:
            category (str): The category to make the request to.
        """
        raise NotImplementedError("This endpoint is not implemented yet.")

    def text(self, category: str) -> str:
        """
        Make a request to the API.

        Args:
            category (str): The category to make the request to.
        """
        raise NotImplementedError("This endpoint is not implemented yet.")
