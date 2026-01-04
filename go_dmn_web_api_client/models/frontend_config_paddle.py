from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrontendConfigPaddle")


@_attrs_define
class FrontendConfigPaddle:
    """
    Attributes:
        client_token (str | Unset): Paddle client-side token for checkout Example: test_....
        sandbox (bool | Unset): Whether to use Paddle sandbox environment Example: True.
    """

    client_token: str | Unset = UNSET
    sandbox: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_token = self.client_token

        sandbox = self.sandbox

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_token is not UNSET:
            field_dict["clientToken"] = client_token
        if sandbox is not UNSET:
            field_dict["sandbox"] = sandbox

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_token = d.pop("clientToken", UNSET)

        sandbox = d.pop("sandbox", UNSET)

        frontend_config_paddle = cls(
            client_token=client_token,
            sandbox=sandbox,
        )

        frontend_config_paddle.additional_properties = d
        return frontend_config_paddle

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
