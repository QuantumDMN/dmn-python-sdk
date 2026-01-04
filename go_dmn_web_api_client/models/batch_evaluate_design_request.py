from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_evaluate_design_request_inputs_item import BatchEvaluateDesignRequestInputsItem


T = TypeVar("T", bound="BatchEvaluateDesignRequest")


@_attrs_define
class BatchEvaluateDesignRequest:
    """
    Attributes:
        xml (str | Unset): The DMN XML definition to evaluate
        inputs (list[BatchEvaluateDesignRequestInputsItem] | Unset): List of input contexts (rows) to evaluate
    """

    xml: str | Unset = UNSET
    inputs: list[BatchEvaluateDesignRequestInputsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        xml = self.xml

        inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = []
            for inputs_item_data in self.inputs:
                inputs_item = inputs_item_data.to_dict()
                inputs.append(inputs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if xml is not UNSET:
            field_dict["xml"] = xml
        if inputs is not UNSET:
            field_dict["inputs"] = inputs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_evaluate_design_request_inputs_item import BatchEvaluateDesignRequestInputsItem

        d = dict(src_dict)
        xml = d.pop("xml", UNSET)

        _inputs = d.pop("inputs", UNSET)
        inputs: list[BatchEvaluateDesignRequestInputsItem] | Unset = UNSET
        if _inputs is not UNSET:
            inputs = []
            for inputs_item_data in _inputs:
                inputs_item = BatchEvaluateDesignRequestInputsItem.from_dict(inputs_item_data)

                inputs.append(inputs_item)

        batch_evaluate_design_request = cls(
            xml=xml,
            inputs=inputs,
        )

        batch_evaluate_design_request.additional_properties = d
        return batch_evaluate_design_request

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
