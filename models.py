from pydantic import BaseModel


# Pydantic model for the update request
class CompanyUpdate(BaseModel):
    name: str = None
    size: str = None
    revenue: str = None
    location: dict = None
    industry: str = None
    other_fields: dict = None  # Additional fields to update in the company document


class LocationUpdate(BaseModel):
    country: str = None
    state: str = None
    city: str = None
    latitude: str = None
    longitude: str = None
    other_fields: str = None  # Additional fields to update in the location document