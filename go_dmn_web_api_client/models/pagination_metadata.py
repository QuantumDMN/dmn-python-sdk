from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PaginationMetadata")


@_attrs_define
class PaginationMetadata:
    """
    Attributes:
        page (int): Current page number (1-indexed)
        page_size (int): Number of items per page
        total (int): Total number of items
        total_pages (int): Total number of pages
    """

    page: int
    page_size: int
    total: int
    total_pages: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        page_size = self.page_size

        total = self.total

        total_pages = self.total_pages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "pageSize": page_size,
                "total": total,
                "totalPages": total_pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page = d.pop("page")

        page_size = d.pop("pageSize")

        total = d.pop("total")

        total_pages = d.pop("totalPages")

        pagination_metadata = cls(
            page=page,
            page_size=page_size,
            total=total,
            total_pages=total_pages,
        )

        pagination_metadata.additional_properties = d
        return pagination_metadata

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
