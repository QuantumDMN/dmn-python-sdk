from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetVersionResponse200")


@_attrs_define
class GetVersionResponse200:
    """
    Attributes:
        version (str | Unset):  Example: 1.0.0.
        build_time (str | Unset):  Example: 2023-10-27T10:00:00Z.
        commit (str | Unset):  Example: abcdef123.
    """

    version: str | Unset = UNSET
    build_time: str | Unset = UNSET
    commit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        build_time = self.build_time

        commit = self.commit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if build_time is not UNSET:
            field_dict["build_time"] = build_time
        if commit is not UNSET:
            field_dict["commit"] = commit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version", UNSET)

        build_time = d.pop("build_time", UNSET)

        commit = d.pop("commit", UNSET)

        get_version_response_200 = cls(
            version=version,
            build_time=build_time,
            commit=commit,
        )

        get_version_response_200.additional_properties = d
        return get_version_response_200

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
