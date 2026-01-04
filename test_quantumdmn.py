"""Tests for QuantumDMN wrapper."""

import pytest

from go_dmn_web_api_client import AuthenticatedClient
from quantumdmn import QuantumDMN, create_client


def test_create_with_static_token():
    """Test creating SDK with static token."""
    sdk = QuantumDMN("https://api.quantumdmn.com", token="test-token")
    assert sdk.base_url == "https://api.quantumdmn.com"
    assert sdk._get_token() == "test-token"


def test_create_with_token_provider():
    """Test creating SDK with token provider function."""
    call_count = 0

    def token_provider():
        nonlocal call_count
        call_count += 1
        return "dynamic-token"

    sdk = QuantumDMN("https://api.quantumdmn.com", token_provider=token_provider)
    assert sdk._get_token() == "dynamic-token"
    assert call_count == 1


def test_client_property():
    """Test that client property returns AuthenticatedClient."""
    sdk = QuantumDMN("https://api.quantumdmn.com", token="test-token")
    client = sdk.client
    assert isinstance(client, AuthenticatedClient)


def test_create_client_helper():
    """Test create_client convenience function."""
    client = create_client("https://api.quantumdmn.com", "test-token")
    assert isinstance(client, AuthenticatedClient)


def test_no_credentials_raises():
    """Test that missing credentials raises error."""
    sdk = QuantumDMN("https://api.quantumdmn.com")
    with pytest.raises(ValueError, match="No token or token_provider"):
        sdk._get_token()
