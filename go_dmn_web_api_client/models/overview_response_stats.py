from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.daily_stat import DailyStat
    from ..models.kpi_trend import KpiTrend


T = TypeVar("T", bound="OverviewResponseStats")


@_attrs_define
class OverviewResponseStats:
    """
    Attributes:
        total_requests (int | Unset):
        total_credits (int | Unset):
        requests_trend (list[DailyStat] | Unset):
        credits_trend (list[DailyStat] | Unset):
        kpi_trends (list[KpiTrend] | Unset):
    """

    total_requests: int | Unset = UNSET
    total_credits: int | Unset = UNSET
    requests_trend: list[DailyStat] | Unset = UNSET
    credits_trend: list[DailyStat] | Unset = UNSET
    kpi_trends: list[KpiTrend] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_requests = self.total_requests

        total_credits = self.total_credits

        requests_trend: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.requests_trend, Unset):
            requests_trend = []
            for requests_trend_item_data in self.requests_trend:
                requests_trend_item = requests_trend_item_data.to_dict()
                requests_trend.append(requests_trend_item)

        credits_trend: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.credits_trend, Unset):
            credits_trend = []
            for credits_trend_item_data in self.credits_trend:
                credits_trend_item = credits_trend_item_data.to_dict()
                credits_trend.append(credits_trend_item)

        kpi_trends: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.kpi_trends, Unset):
            kpi_trends = []
            for kpi_trends_item_data in self.kpi_trends:
                kpi_trends_item = kpi_trends_item_data.to_dict()
                kpi_trends.append(kpi_trends_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_requests is not UNSET:
            field_dict["totalRequests"] = total_requests
        if total_credits is not UNSET:
            field_dict["totalCredits"] = total_credits
        if requests_trend is not UNSET:
            field_dict["requestsTrend"] = requests_trend
        if credits_trend is not UNSET:
            field_dict["creditsTrend"] = credits_trend
        if kpi_trends is not UNSET:
            field_dict["kpiTrends"] = kpi_trends

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.daily_stat import DailyStat
        from ..models.kpi_trend import KpiTrend

        d = dict(src_dict)
        total_requests = d.pop("totalRequests", UNSET)

        total_credits = d.pop("totalCredits", UNSET)

        _requests_trend = d.pop("requestsTrend", UNSET)
        requests_trend: list[DailyStat] | Unset = UNSET
        if _requests_trend is not UNSET:
            requests_trend = []
            for requests_trend_item_data in _requests_trend:
                requests_trend_item = DailyStat.from_dict(requests_trend_item_data)

                requests_trend.append(requests_trend_item)

        _credits_trend = d.pop("creditsTrend", UNSET)
        credits_trend: list[DailyStat] | Unset = UNSET
        if _credits_trend is not UNSET:
            credits_trend = []
            for credits_trend_item_data in _credits_trend:
                credits_trend_item = DailyStat.from_dict(credits_trend_item_data)

                credits_trend.append(credits_trend_item)

        _kpi_trends = d.pop("kpiTrends", UNSET)
        kpi_trends: list[KpiTrend] | Unset = UNSET
        if _kpi_trends is not UNSET:
            kpi_trends = []
            for kpi_trends_item_data in _kpi_trends:
                kpi_trends_item = KpiTrend.from_dict(kpi_trends_item_data)

                kpi_trends.append(kpi_trends_item)

        overview_response_stats = cls(
            total_requests=total_requests,
            total_credits=total_credits,
            requests_trend=requests_trend,
            credits_trend=credits_trend,
            kpi_trends=kpi_trends,
        )

        overview_response_stats.additional_properties = d
        return overview_response_stats

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
