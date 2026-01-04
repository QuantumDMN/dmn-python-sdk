from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.tier import Tier
from ...types import Response


def _get_kwargs(
    tier_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tiers/{tier_id}".format(
            tier_id=quote(str(tier_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Tier | None:
    if response.status_code == 200:
        response_200 = Tier.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Tier]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tier_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | Tier]:
    """Get Tier

    Args:
        tier_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Tier]
    """

    kwargs = _get_kwargs(
        tier_id=tier_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tier_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | Tier | None:
    """Get Tier

    Args:
        tier_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Tier
    """

    return sync_detailed(
        tier_id=tier_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tier_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | Tier]:
    """Get Tier

    Args:
        tier_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Tier]
    """

    kwargs = _get_kwargs(
        tier_id=tier_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tier_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | Tier | None:
    """Get Tier

    Args:
        tier_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Tier
    """

    return (
        await asyncio_detailed(
            tier_id=tier_id,
            client=client,
        )
    ).parsed
