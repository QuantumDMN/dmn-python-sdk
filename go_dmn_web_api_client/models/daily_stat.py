from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DailyStat")


@_attrs_define
class DailyStat:
    """
    Attributes:
        date (datetime.date | Unset):
        requests (int | Unset):
        credits_ (int | Unset):
    """

    date: datetime.date | Unset = UNSET
    requests: int | Unset = UNSET
    credits_: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        requests = self.requests

        credits_ = self.credits_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if requests is not UNSET:
            field_dict["requests"] = requests
        if credits_ is not UNSET:
            field_dict["credits"] = credits_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        requests = d.pop("requests", UNSET)

        credits_ = d.pop("credits", UNSET)

        daily_stat = cls(
            date=date,
            requests=requests,
            credits_=credits_,
        )

        daily_stat.additional_properties = d
        return daily_stat

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
