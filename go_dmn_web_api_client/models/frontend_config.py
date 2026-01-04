from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frontend_config_oidc import FrontendConfigOidc
    from ..models.frontend_config_paddle import FrontendConfigPaddle


T = TypeVar("T", bound="FrontendConfig")


@_attrs_define
class FrontendConfig:
    """
    Attributes:
        oidc (FrontendConfigOidc):
        paddle (FrontendConfigPaddle | Unset):
    """

    oidc: FrontendConfigOidc
    paddle: FrontendConfigPaddle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oidc = self.oidc.to_dict()

        paddle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paddle, Unset):
            paddle = self.paddle.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "oidc": oidc,
            }
        )
        if paddle is not UNSET:
            field_dict["paddle"] = paddle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frontend_config_oidc import FrontendConfigOidc
        from ..models.frontend_config_paddle import FrontendConfigPaddle

        d = dict(src_dict)
        oidc = FrontendConfigOidc.from_dict(d.pop("oidc"))

        _paddle = d.pop("paddle", UNSET)
        paddle: FrontendConfigPaddle | Unset
        if isinstance(_paddle, Unset):
            paddle = UNSET
        else:
            paddle = FrontendConfigPaddle.from_dict(_paddle)

        frontend_config = cls(
            oidc=oidc,
            paddle=paddle,
        )

        frontend_config.additional_properties = d
        return frontend_config

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
