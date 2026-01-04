from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_permissions_projects import UserPermissionsProjects


T = TypeVar("T", bound="UserPermissions")


@_attrs_define
class UserPermissions:
    """
    Attributes:
        global_role (str): User's global organization role (admin or user)
        projects (UserPermissionsProjects): Map of projectID to project permissions
    """

    global_role: str
    projects: UserPermissionsProjects
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        global_role = self.global_role

        projects = self.projects.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "global_role": global_role,
                "projects": projects,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_permissions_projects import UserPermissionsProjects

        d = dict(src_dict)
        global_role = d.pop("global_role")

        projects = UserPermissionsProjects.from_dict(d.pop("projects"))

        user_permissions = cls(
            global_role=global_role,
            projects=projects,
        )

        user_permissions.additional_properties = d
        return user_permissions

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
