from pydantic import BaseModel, ConfigDict
from typing import Optional

class PostalCodeBase(BaseModel):
    postal_code: str
    town_name: Optional[str] = None

class PostalCodeCreate(PostalCodeBase):
    pass

class PostalCode(PostalCodeBase):
    model_config = ConfigDict(from_attributes=True)

# Schema for postal code with related addresses
# class PostalCodeWithAddresses(PostalCode):
#     addresses: list['AddressSimple'] = []

class PostalCodeDBSchema(BaseModel):
    cPostalCode: str
    cTownName: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)