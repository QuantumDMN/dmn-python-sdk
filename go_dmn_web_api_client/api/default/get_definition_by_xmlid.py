from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.definition import Definition
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: UUID,
    xml_definition_id: str,
    *,
    version: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/definitions/by-xml-id/{xml_definition_id}".format(
            project_id=quote(str(project_id), safe=""),
            xml_definition_id=quote(str(xml_definition_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Definition | Error | None:
    if response.status_code == 200:
        response_200 = Definition.from_dict(response.json())

        return response_200

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
    xml_definition_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: int | Unset = UNSET,
) -> Response[Definition | Error]:
    """Get definition by XML definition ID

     Get the latest version of a definition by its XML definition ID, or a specific version if provided

    Args:
        project_id (UUID):
        xml_definition_id (str):
        version (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Definition | Error]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        xml_definition_id=xml_definition_id,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: UUID,
    xml_definition_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: int | Unset = UNSET,
) -> Definition | Error | None:
    """Get definition by XML definition ID

     Get the latest version of a definition by its XML definition ID, or a specific version if provided

    Args:
        project_id (UUID):
        xml_definition_id (str):
        version (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Definition | Error
    """

    return sync_detailed(
        project_id=project_id,
        xml_definition_id=xml_definition_id,
        client=client,
        version=version,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    xml_definition_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: int | Unset = UNSET,
) -> Response[Definition | Error]:
    """Get definition by XML definition ID

     Get the latest version of a definition by its XML definition ID, or a specific version if provided

    Args:
        project_id (UUID):
        xml_definition_id (str):
        version (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Definition | Error]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        xml_definition_id=xml_definition_id,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    xml_definition_id: str,
    *,
    client: AuthenticatedClient | Client,
    version: int | Unset = UNSET,
) -> Definition | Error | None:
    """Get definition by XML definition ID

     Get the latest version of a definition by its XML definition ID, or a specific version if provided

    Args:
        project_id (UUID):
        xml_definition_id (str):
        version (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Definition | Error
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            xml_definition_id=xml_definition_id,
            client=client,
            version=version,
        )
    ).parsed
