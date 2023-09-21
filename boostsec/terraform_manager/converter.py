"""Converters for Terraform HCL."""
from typing import Any

from pydantic import BaseModel


def convert_pydantic_to_hcl(model: BaseModel) -> str:
    """Convert JSON data to .tfvars format."""
    tfvars = [
        f"{key} = {process_value(value)}"
        for key, value in model.dict(by_alias=True).items()
        if value is not None
    ]

    return "\n".join(tfvars)


def process_value(value: str | bool | list[Any] | dict[str, Any]) -> str:
    """Convert a value to a string."""
    match value:
        case str():
            return f'"{value}"'
        case bool():
            return str(value).lower()
        case list():
            return (
                "["
                + ", ".join(
                    [process_value(item) for item in value if value is not None]
                )
                + "]"
            )
        case dict():
            formatted_dict = []
            for subkey, subvalue in value.items():
                if subvalue is not None:
                    formatted_dict.append(f"{subkey} = {process_value(subvalue)}")
            if formatted_dict:
                return "{\n  " + "\n  ".join(formatted_dict) + "\n}"
            return "{}"
        case _:
            return f'"{value}"'
