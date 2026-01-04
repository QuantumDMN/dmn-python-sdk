from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_flags import FeatureFlags
    from ..models.tier_limits import TierLimits


T = TypeVar("T", bound="TierFeaturesConfig")


@_attrs_define
class TierFeaturesConfig:
    """
    Attributes:
        credits_ (int | Unset):
        overcharge_price_per_100_credits (int | Unset):
        limits (TierLimits | Unset):
        features (FeatureFlags | Unset):
    """

    credits_: int | Unset = UNSET
    overcharge_price_per_100_credits: int | Unset = UNSET
    limits: TierLimits | Unset = UNSET
    features: FeatureFlags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credits_ = self.credits_

        overcharge_price_per_100_credits = self.overcharge_price_per_100_credits

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        features: dict[str, Any] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = self.features.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if overcharge_price_per_100_credits is not UNSET:
            field_dict["overchargePricePer100Credits"] = overcharge_price_per_100_credits
        if limits is not UNSET:
            field_dict["limits"] = limits
        if features is not UNSET:
            field_dict["features"] = features

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feature_flags import FeatureFlags
        from ..models.tier_limits import TierLimits

        d = dict(src_dict)
        credits_ = d.pop("credits", UNSET)

        overcharge_price_per_100_credits = d.pop("overchargePricePer100Credits", UNSET)

        _limits = d.pop("limits", UNSET)
        limits: TierLimits | Unset
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = TierLimits.from_dict(_limits)

        _features = d.pop("features", UNSET)
        features: FeatureFlags | Unset
        if isinstance(_features, Unset):
            features = UNSET
        else:
            features = FeatureFlags.from_dict(_features)

        tier_features_config = cls(
            credits_=credits_,
            overcharge_price_per_100_credits=overcharge_price_per_100_credits,
            limits=limits,
            features=features,
        )

        tier_features_config.additional_properties = d
        return tier_features_config

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
