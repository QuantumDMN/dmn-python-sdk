from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProjectPermissions")


@_attrs_define
class ProjectPermissions:
    """
    Attributes:
        role (str): Project role (admin, editor, executor, viewer)
        can_manage_members (bool):
        can_edit_definitions (bool):
        can_execute (bool):
        can_view (bool):
    """

    role: str
    can_manage_members: bool
    can_edit_definitions: bool
    can_execute: bool
    can_view: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        can_manage_members = self.can_manage_members

        can_edit_definitions = self.can_edit_definitions

        can_execute = self.can_execute

        can_view = self.can_view

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "can_manage_members": can_manage_members,
                "can_edit_definitions": can_edit_definitions,
                "can_execute": can_execute,
                "can_view": can_view,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = d.pop("role")

        can_manage_members = d.pop("can_manage_members")

        can_edit_definitions = d.pop("can_edit_definitions")

        can_execute = d.pop("can_execute")

        can_view = d.pop("can_view")

        project_permissions = cls(
            role=role,
            can_manage_members=can_manage_members,
            can_edit_definitions=can_edit_definitions,
            can_execute=can_execute,
            can_view=can_view,
        )

        project_permissions.additional_properties = d
        return project_permissions

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
