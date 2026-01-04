from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.definition import Definition
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    project_id: UUID,
    definition_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/definitions/{definition_id}".format(
            project_id=quote(str(project_id), safe=""),
            definition_id=quote(str(definition_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Definition | Error | None:
    if response.status_code == 200:
        response_200 = Definition.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Definition | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: UUID,
    definition_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Definition | Error]:
    """Get Definition

    Args:
        project_id (UUID):
        definition_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Definition | Error]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        definition_id=definition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: UUID,
    definition_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Definition | Error | None:
    """Get Definition

    Args:
        project_id (UUID):
        definition_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Definition | Error
    """

    return sync_detailed(
        project_id=project_id,
        definition_id=definition_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    definition_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Definition | Error]:
    """Get Definition

    Args:
        project_id (UUID):
        definition_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Definition | Error]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        definition_id=definition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    definition_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Definition | Error | None:
    """Get Definition

    Args:
        project_id (UUID):
        definition_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Definition | Error
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            definition_id=definition_id,
            client=client,
        )
    ).parsed
