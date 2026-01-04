from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FrontendConfigOidc")


@_attrs_define
class FrontendConfigOidc:
    """
    Attributes:
        authority (str): OIDC authority URL (issuer) Example: http://localhost:8080.
        client_id (str): OIDC client ID for the web application Example: 123456789@dmn-engine.
    """

    authority: str
    client_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authority = self.authority

        client_id = self.client_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authority": authority,
                "clientId": client_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authority = d.pop("authority")

        client_id = d.pop("clientId")

        frontend_config_oidc = cls(
            authority=authority,
            client_id=client_id,
        )

        frontend_config_oidc.additional_properties = d
        return frontend_config_oidc

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
