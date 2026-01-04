from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectMember")


@_attrs_define
class ProjectMember:
    """
    Attributes:
        project_id (UUID | Unset):
        user_id (str | Unset):
        role (str | Unset):
        username (str | Unset):
        email (str | Unset):
        created_at (datetime.datetime | Unset):
    """

    project_id: UUID | Unset = UNSET
    user_id: str | Unset = UNSET
    role: str | Unset = UNSET
    username: str | Unset = UNSET
    email: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id: str | Unset = UNSET
        if not isinstance(self.project_id, Unset):
            project_id = str(self.project_id)

        user_id = self.user_id

        role = self.role

        username = self.username

        email = self.email

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if role is not UNSET:
            field_dict["role"] = role
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _project_id = d.pop("project_id", UNSET)
        project_id: UUID | Unset
        if isinstance(_project_id, Unset):
            project_id = UNSET
        else:
            project_id = UUID(_project_id)

        user_id = d.pop("user_id", UNSET)

        role = d.pop("role", UNSET)

        username = d.pop("username", UNSET)

        email = d.pop("email", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        project_member = cls(
            project_id=project_id,
            user_id=user_id,
            role=role,
            username=username,
            email=email,
            created_at=created_at,
        )

        project_member.additional_properties = d
        return project_member

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
