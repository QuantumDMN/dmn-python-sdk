from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_usage import ProjectUsage


T = TypeVar("T", bound="DefinitionsQuota")


@_attrs_define
class DefinitionsQuota:
    """
    Attributes:
        limit (int | Unset): Max definitions allowed per project (tier limit)
        projects (list[ProjectUsage] | Unset):
    """

    limit: int | Unset = UNSET
    projects: list[ProjectUsage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        projects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()
                projects.append(projects_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limit is not UNSET:
            field_dict["limit"] = limit
        if projects is not UNSET:
            field_dict["projects"] = projects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_usage import ProjectUsage

        d = dict(src_dict)
        limit = d.pop("limit", UNSET)

        _projects = d.pop("projects", UNSET)
        projects: list[ProjectUsage] | Unset = UNSET
        if _projects is not UNSET:
            projects = []
            for projects_item_data in _projects:
                projects_item = ProjectUsage.from_dict(projects_item_data)

                projects.append(projects_item)

        definitions_quota = cls(
            limit=limit,
            projects=projects,
        )

        definitions_quota.additional_properties = d
        return definitions_quota

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
