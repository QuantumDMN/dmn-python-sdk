from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tier_features_config import TierFeaturesConfig


T = TypeVar("T", bound="Tier")


@_attrs_define
class Tier:
    """
    Attributes:
        id (str):
        name (str):
        price (float | Unset):
        features (TierFeaturesConfig | Unset):
        paddle_price_id (str | Unset):
    """

    id: str
    name: str
    price: float | Unset = UNSET
    features: TierFeaturesConfig | Unset = UNSET
    paddle_price_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        price = self.price

        features: dict[str, Any] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = self.features.to_dict()

        paddle_price_id = self.paddle_price_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if price is not UNSET:
            field_dict["price"] = price
        if features is not UNSET:
            field_dict["features"] = features
        if paddle_price_id is not UNSET:
            field_dict["paddlePriceId"] = paddle_price_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tier_features_config import TierFeaturesConfig

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        price = d.pop("price", UNSET)

        _features = d.pop("features", UNSET)
        features: TierFeaturesConfig | Unset
        if isinstance(_features, Unset):
            features = UNSET
        else:
            features = TierFeaturesConfig.from_dict(_features)

        paddle_price_id = d.pop("paddlePriceId", UNSET)

        tier = cls(
            id=id,
            name=name,
            price=price,
            features=features,
            paddle_price_id=paddle_price_id,
        )

        tier.additional_properties = d
        return tier

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
