from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectUsage")


@_attrs_define
class ProjectUsage:
    """
    Attributes:
        project_id (UUID | Unset):
        name (str | Unset):
        usage (int | Unset):
        limit (int | Unset):
    """

    project_id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    usage: int | Unset = UNSET
    limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id: str | Unset = UNSET
        if not isinstance(self.project_id, Unset):
            project_id = str(self.project_id)

        name = self.name

        usage = self.usage

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if name is not UNSET:
            field_dict["name"] = name
        if usage is not UNSET:
            field_dict["usage"] = usage
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _project_id = d.pop("projectId", UNSET)
        project_id: UUID | Unset
        if isinstance(_project_id, Unset):
            project_id = UNSET
        else:
            project_id = UUID(_project_id)

        name = d.pop("name", UNSET)

        usage = d.pop("usage", UNSET)

        limit = d.pop("limit", UNSET)

        project_usage = cls(
            project_id=project_id,
            name=name,
            usage=usage,
            limit=limit,
        )

        project_usage.additional_properties = d
        return project_usage

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
