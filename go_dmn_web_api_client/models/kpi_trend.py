from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kpi_trend_data_item import KpiTrendDataItem


T = TypeVar("T", bound="KpiTrend")


@_attrs_define
class KpiTrend:
    """
    Attributes:
        kpi_id (str | Unset):
        name (str | Unset):
        data (list[KpiTrendDataItem] | Unset):
    """

    kpi_id: str | Unset = UNSET
    name: str | Unset = UNSET
    data: list[KpiTrendDataItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kpi_id = self.kpi_id

        name = self.name

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kpi_id is not UNSET:
            field_dict["kpiId"] = kpi_id
        if name is not UNSET:
            field_dict["name"] = name
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kpi_trend_data_item import KpiTrendDataItem

        d = dict(src_dict)
        kpi_id = d.pop("kpiId", UNSET)

        name = d.pop("name", UNSET)

        _data = d.pop("data", UNSET)
        data: list[KpiTrendDataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = KpiTrendDataItem.from_dict(data_item_data)

                data.append(data_item)

        kpi_trend = cls(
            kpi_id=kpi_id,
            name=name,
            data=data,
        )

        kpi_trend.additional_properties = d
        return kpi_trend

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
