from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditsQuota")


@_attrs_define
class CreditsQuota:
    """
    Attributes:
        used (int | Unset):
        limit (int | Unset):
        overcharge_price (int | Unset):
        overcharge_enabled (bool | Unset):
    """

    used: int | Unset = UNSET
    limit: int | Unset = UNSET
    overcharge_price: int | Unset = UNSET
    overcharge_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        used = self.used

        limit = self.limit

        overcharge_price = self.overcharge_price

        overcharge_enabled = self.overcharge_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if used is not UNSET:
            field_dict["used"] = used
        if limit is not UNSET:
            field_dict["limit"] = limit
        if overcharge_price is not UNSET:
            field_dict["overchargePrice"] = overcharge_price
        if overcharge_enabled is not UNSET:
            field_dict["overchargeEnabled"] = overcharge_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        used = d.pop("used", UNSET)

        limit = d.pop("limit", UNSET)

        overcharge_price = d.pop("overchargePrice", UNSET)

        overcharge_enabled = d.pop("overchargeEnabled", UNSET)

        credits_quota = cls(
            used=used,
            limit=limit,
            overcharge_price=overcharge_price,
            overcharge_enabled=overcharge_enabled,
        )

        credits_quota.additional_properties = d
        return credits_quota

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
