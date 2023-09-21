from pydantic import BaseModel


def convert_pydantic_to_hcl(model: BaseModel):
    """Convert a pydantic model to HCL."""