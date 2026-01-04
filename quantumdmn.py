"""
QuantumDMN Python SDK wrapper with authentication support.
"""

from collections.abc import Callable

from go_dmn_web_api_client import AuthenticatedClient

TokenProvider = Callable[[], str]


class QuantumDMN:
    """
    QuantumDMN client wrapper with authentication support.

    Example:
        >>> sdk = QuantumDMN("https://api.quantumdmn.com", token="your-token")
        >>> # or with dynamic token provider
        >>> sdk = QuantumDMN("https://api.quantumdmn.com", token_provider=get_token)
    """

    def __init__(
        self,
        base_url: str,
        token: str | None = None,
        token_provider: TokenProvider | None = None,
    ):
        """
        Initialize the QuantumDMN client.

        Args:
            base_url: API base URL (e.g., "https://api.quantumdmn.com")
            token: Static bearer token for authentication
            token_provider: Function that returns a valid access token
        """
        self.base_url = base_url
        self._token = token
        self._token_provider = token_provider
        self._client: AuthenticatedClient | None = None

    def _get_token(self) -> str:
        """Get the current access token."""
        if self._token_provider:
            return self._token_provider()
        if self._token:
            return self._token
        raise ValueError("No token or token_provider configured")

    @property
    def client(self) -> AuthenticatedClient:
        """Get the authenticated client instance."""
        if self._client is None:
            self._client = AuthenticatedClient(
                base_url=self.base_url,
                token=self._get_token(),
            )
        return self._client

    def refresh_token(self) -> None:
        """Refresh the client with a new token (useful for token rotation)."""
        self._client = None


# convenience function
def create_client(base_url: str, token: str) -> AuthenticatedClient:
    """Create an authenticated client with a static token."""
    return AuthenticatedClient(base_url=base_url, token=token)
