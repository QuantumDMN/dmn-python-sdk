from typing import Any, Dict, List, Union, Optional
from enum import Enum
import datetime
from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema

class FeelType(str, Enum):
    STRING = "string"
    NUMBER = "number"
    BOOLEAN = "boolean"
    LIST = "list"
    CONTEXT = "context"
    DATE = "date"
    TIME = "time"
    DATE_TIME = "date and time"
    DURATION = "duration" # simplified
    NULL = "null"

class FeelValue:
    """
    Represents a FEEL value in the QuantumDMN engine.
    This class handles type conversion and serialization for DMN evaluation.
    """
    def __init__(self, value: Any = None, type_name: Optional[Union[FeelType, str]] = None):
        self._value = value
        self._type = type_name
    
    @property
    def value(self):
        return self._value
        
    @property
    def type(self):
        return self._type

    @staticmethod
    def of_number(value: Union[int, float]):
        return FeelValue(value, FeelType.NUMBER)

    @staticmethod
    def of_string(value: str):
        return FeelValue(value, FeelType.STRING)

    @staticmethod
    def of_boolean(value: bool):
        return FeelValue(value, FeelType.BOOLEAN)

    @staticmethod
    def of_list(value: List['FeelValue']):
        return FeelValue(value, FeelType.LIST)

    @staticmethod
    def of_context(value: Dict[str, 'FeelValue']):
        return FeelValue(value, FeelType.CONTEXT)

    @staticmethod
    def from_python(value: Any) -> 'FeelValue':
        """Autodetect FEEL type from Python value."""
        if value is None:
            return FeelValue(None, FeelType.NULL)
        if isinstance(value, bool):
            return FeelValue(value, FeelType.BOOLEAN)
        if isinstance(value, (int, float)):
            return FeelValue(value, FeelType.NUMBER)
        if isinstance(value, str):
            return FeelValue(value, FeelType.STRING)
        if isinstance(value, list):
            items = [FeelValue.from_python(v) for v in value]
            return FeelValue(items, FeelType.LIST)
        if isinstance(value, dict):
            ctx = {k: FeelValue.from_python(v) for k, v in value.items()}
            return FeelValue(ctx, FeelType.CONTEXT)
        if hasattr(value, "isoformat"): # dates
             return FeelValue(value.isoformat(), FeelType.DATE_TIME)
             
        # Validation for generated code which might pass an existing FeelValue
        if isinstance(value, FeelValue):
            return value

        return FeelValue(str(value), FeelType.STRING)

    def to_dict(self):
        """Serializer for OpenAPI generator (pydantic/json)"""
        if self._type == FeelType.LIST and isinstance(self._value, list):
             return [v.to_dict() if isinstance(v, FeelValue) else v for v in self._value]
        if self._type == FeelType.CONTEXT and isinstance(self._value, dict):
             return {k: (v.to_dict() if isinstance(v, FeelValue) else v) for k, v in self._value.items()}
        return self._value

    def to_raw(self):
        """Unwrap to standard Python types"""
        if self._type == FeelType.LIST:
            return [v.to_raw() for v in self._value]
        if self._type == FeelType.CONTEXT:
             return {k: v.to_raw() for k, v in self._value.items()}
        return self._value

    def __repr__(self):
        return f"FeelValue({self._value}, type={self._type})"

    # Aliases to satisfy generated code that might look for certain props if it was treating it as 'Any'
    # but actually the generator treats mapped types opaquely, so `to_dict` is the key for serialization 
    # if using generic serializer, or we might need `to_json`.
    
    @classmethod
    def from_dict(cls, data: Any) -> 'FeelValue':
        """Deserializer used by generated code"""
        # The API returns raw JSON (number, string, etc.), not a specific object wrapper.
        # But if the API result is explicitly typed as FeelValue in our mapping, the generator
        # might try to pass the raw data here.
        return cls.from_python(data)
    
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        """Pydantic validator for FeelValue - accepts any type and converts via from_python"""
        return core_schema.no_info_plain_validator_function(
            cls.from_python,
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: x.to_dict() if isinstance(x, FeelValue) else x,
                return_schema=core_schema.any_schema()
            )
        )
