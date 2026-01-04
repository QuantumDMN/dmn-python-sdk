from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Definition")


@_attrs_define
class Definition:
    """
    Attributes:
        id (UUID):
        name (str):
        definition_id (str):
        xml (str):
        version (int):
        created_at (datetime.datetime):
        created_by (str | Unset):
    """

    id: UUID
    name: str
    definition_id: str
    xml: str
    version: int
    created_at: datetime.datetime
    created_by: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        definition_id = self.definition_id

        xml = self.xml

        version = self.version

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "definition_id": definition_id,
                "xml": xml,
                "version": version,
                "created_at": created_at,
            }
        )
        if created_by is not UNSET:
            field_dict["created_by"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        definition_id = d.pop("definition_id")

        xml = d.pop("xml")

        version = d.pop("version")

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by", UNSET)

        definition = cls(
            id=id,
            name=name,
            definition_id=definition_id,
            xml=xml,
            version=version,
            created_at=created_at,
            created_by=created_by,
        )

        definition.additional_properties = d
        return definition

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
