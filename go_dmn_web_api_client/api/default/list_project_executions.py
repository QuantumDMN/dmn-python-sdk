from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: UUID,
    *,
    xml_definition_id: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["xmlDefinitionId"] = xml_definition_id

    params["page"] = page

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/executions".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | None:
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    xml_definition_id: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
) -> Response[Error]:
    """List All Executions for Project

    Args:
        project_id (UUID):
        xml_definition_id (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        xml_definition_id=xml_definition_id,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    xml_definition_id: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
) -> Error | None:
    """List All Executions for Project

    Args:
        project_id (UUID):
        xml_definition_id (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        xml_definition_id=xml_definition_id,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    xml_definition_id: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
) -> Response[Error]:
    """List All Executions for Project

    Args:
        project_id (UUID):
        xml_definition_id (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        xml_definition_id=xml_definition_id,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    xml_definition_id: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
) -> Error | None:
    """List All Executions for Project

    Args:
        project_id (UUID):
        xml_definition_id (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            xml_definition_id=xml_definition_id,
            page=page,
            page_size=page_size,
        )
    ).parsed
