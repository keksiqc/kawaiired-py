import httpx

from kawaiired.utils import BASE_URL, APIException, EndpointType, GifType


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
        self.session = httpx.Client(headers={"token": self.token})

    def __del__(self):
        """Ensure the session is closed when the client is deleted."""
        self.session.close()

    def _request(self, endpoint: EndpointType, category: str) -> str | None:
        """
        Make a request to the API and return the response.

        Args:
            endpoint (EndpointType): The endpoint to make the request to.
            category (str): The category to make the request to.

        Returns:
            Optional[str]: The response from the API, or None if not found.

        Raises:
            APIException: If the request fails.
        """
        url = f"{self.base_url}/{endpoint}/{category}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json().get("response")
        except httpx.HTTPStatusError as e:
            raise APIException(e.response.status_code, e.response.reason_phrase, e.response.text) from e

    def get(self, endpoint: EndpointType, category: str) -> str | None:
        """
        Get a response from the API.

        Args:
            endpoint (EndpointType): The endpoint to make the request to.
            category (str): The category to make the request to.

        Returns:
            Optional[str]: The response from the API, or None if not found.
        """
        return self._request(endpoint, category)

    def gif(self, category: GifType) -> str | None:
        """
        Get a GIF from the API.

        Args:
            category (str): The category to make the request to.

        Returns:
            Optional[str]: The GIF URL, or None if not found.
        """
        return self._request("gif", category)

    def image(self, category: str) -> str | None:
        """
        Get an image from the API.

        Args:
            category (str): The category to make the request to.

        Returns:
            Optional[str]: The image URL, or None if not found.
        """
        raise NotImplementedError("This endpoint is not implemented yet.")

    def text(self, category: str) -> str | None:
        """
        Get text from the API.

        Args:
            category (str): The category to make the request to.

        Returns:
            Optional[str]: The text response, or None if not found.
        """
        raise NotImplementedError("This endpoint is not implemented yet.")
