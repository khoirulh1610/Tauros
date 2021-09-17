from pydantic import BaseModel
from typing import List, Optional


class WALocationMessage(BaseModel):
    "Send a location message to a WhatsApp number"

    degreesLatitude: int
    """
    Latitude of the location
    """
    degreesLongitude: int
    """
    Longitude of the location 
    """
    address: Optional[str]
    """
    Address of the location
    """
