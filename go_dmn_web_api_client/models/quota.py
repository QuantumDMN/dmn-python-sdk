from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credits_quota import CreditsQuota
    from ..models.definitions_quota import DefinitionsQuota
    from ..models.quota_item import QuotaItem


T = TypeVar("T", bound="Quota")


@_attrs_define
class Quota:
    """
    Attributes:
        tier_id (str): The ID of the current tier (e.g., developer, starter, scale)
        credits_ (CreditsQuota | Unset):
        history (QuotaItem | Unset):
        projects (QuotaItem | Unset):
        definitions (DefinitionsQuota | Unset):
        users (QuotaItem | Unset):
    """

    tier_id: str
    credits_: CreditsQuota | Unset = UNSET
    history: QuotaItem | Unset = UNSET
    projects: QuotaItem | Unset = UNSET
    definitions: DefinitionsQuota | Unset = UNSET
    users: QuotaItem | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tier_id = self.tier_id

        credits_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credits_, Unset):
            credits_ = self.credits_.to_dict()

        history: dict[str, Any] | Unset = UNSET
        if not isinstance(self.history, Unset):
            history = self.history.to_dict()

        projects: dict[str, Any] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = self.projects.to_dict()

        definitions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.definitions, Unset):
            definitions = self.definitions.to_dict()

        users: dict[str, Any] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = self.users.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tierId": tier_id,
            }
        )
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if history is not UNSET:
            field_dict["history"] = history
        if projects is not UNSET:
            field_dict["projects"] = projects
        if definitions is not UNSET:
            field_dict["definitions"] = definitions
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credits_quota import CreditsQuota
        from ..models.definitions_quota import DefinitionsQuota
        from ..models.quota_item import QuotaItem

        d = dict(src_dict)
        tier_id = d.pop("tierId")

        _credits_ = d.pop("credits", UNSET)
        credits_: CreditsQuota | Unset
        if isinstance(_credits_, Unset):
            credits_ = UNSET
        else:
            credits_ = CreditsQuota.from_dict(_credits_)

        _history = d.pop("history", UNSET)
        history: QuotaItem | Unset
        if isinstance(_history, Unset):
            history = UNSET
        else:
            history = QuotaItem.from_dict(_history)

        _projects = d.pop("projects", UNSET)
        projects: QuotaItem | Unset
        if isinstance(_projects, Unset):
            projects = UNSET
        else:
            projects = QuotaItem.from_dict(_projects)

        _definitions = d.pop("definitions", UNSET)
        definitions: DefinitionsQuota | Unset
        if isinstance(_definitions, Unset):
            definitions = UNSET
        else:
            definitions = DefinitionsQuota.from_dict(_definitions)

        _users = d.pop("users", UNSET)
        users: QuotaItem | Unset
        if isinstance(_users, Unset):
            users = UNSET
        else:
            users = QuotaItem.from_dict(_users)

        quota = cls(
            tier_id=tier_id,
            credits_=credits_,
            history=history,
            projects=projects,
            definitions=definitions,
            users=users,
        )

        quota.additional_properties = d
        return quota

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
