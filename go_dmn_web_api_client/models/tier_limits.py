from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TierLimits")


@_attrs_define
class TierLimits:
    """
    Attributes:
        projects (int | Unset):
        seats (int | Unset):
        definitions_per_project (int | Unset):
        history_retention_days (int | Unset):
    """

    projects: int | Unset = UNSET
    seats: int | Unset = UNSET
    definitions_per_project: int | Unset = UNSET
    history_retention_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        projects = self.projects

        seats = self.seats

        definitions_per_project = self.definitions_per_project

        history_retention_days = self.history_retention_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if projects is not UNSET:
            field_dict["projects"] = projects
        if seats is not UNSET:
            field_dict["seats"] = seats
        if definitions_per_project is not UNSET:
            field_dict["definitionsPerProject"] = definitions_per_project
        if history_retention_days is not UNSET:
            field_dict["historyRetentionDays"] = history_retention_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        projects = d.pop("projects", UNSET)

        seats = d.pop("seats", UNSET)

        definitions_per_project = d.pop("definitionsPerProject", UNSET)

        history_retention_days = d.pop("historyRetentionDays", UNSET)

        tier_limits = cls(
            projects=projects,
            seats=seats,
            definitions_per_project=definitions_per_project,
            history_retention_days=history_retention_days,
        )

        tier_limits.additional_properties = d
        return tier_limits

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
