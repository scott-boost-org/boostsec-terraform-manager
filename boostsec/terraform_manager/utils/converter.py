"""Converters for Terraform HCL."""
import subprocess
import tempfile
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
        case _:  # pragma: no cover
            raise TypeError()


def format_terraform_code(tf_code: str) -> str:
    """Format Terraform code using terraform fmt."""
    with tempfile.NamedTemporaryFile(
        mode="w+t", suffix=".tfvars", delete=True
    ) as tmpfile:
        tmpfile.write(tf_code)
        tmpfile.flush()  # Ensure the data is written to disk.

        try:
            # Run terraform fmt on the temporary file.
            subprocess.run(
                ["terraform", "fmt", tmpfile.name],  # noqa: S603,S607
                check=True,
            )

            # Move the cursor to the beginning of the file and read its content.
            tmpfile.seek(0)
            formatted_code = tmpfile.read()
            return f"{formatted_code}\n"

        except subprocess.CalledProcessError:
            return tf_code
