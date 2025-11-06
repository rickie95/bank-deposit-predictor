from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

class JobType(Enum):
    ADMIN = "admin"
    BLUE_COLLAR = "blue_collar"
    ENTREPRENEUR = "entrepreneur"
    HOUSEMAID = "housemaid"
    MANAGEMENT = "management"
    RETIRED = "retired"
    SELF_EMPLOYED = "self_employed"
    SERVICES = "services"
    STUDENT = "student"
    TECHNICIAN = "technician"
    UNEMPLOYED = "unemployed"
    UNKNOWN = "unknown"

class MaritalStatus(Enum):
    MARRIED = "married"
    DIVORCED = "divorced"
    SINGLE = "single"

class ContactType(Enum):
    TELEPHONE = "telephone"
    CELLULAR = "cellular"
    UNKOWN = "unknown"

class DepositFeatures(BaseModel):
    age: int = Field(gt=0, lt=150, description="Age of the customer")
    job: JobType = Field(description="Customer's job")
    education: int = Field(description="Education degree")
    married: MaritalStatus = Field(description="Customer's marital status")
    contact: ContactType = Field(description="Type of contact during last campaign")
    default: bool = Field(description="Has credit in default?")
    balance: int = Field(description="Balance amount in the subject's account.")
    housing: bool = Field(description="Wheter the subject is an home owwer or not.")
    loan: bool = Field(description="Wheter the subject has at least one loan at his name.")
    duration: int = Field(description="Last contact duration in seconds.")
    campaign: int = Field(description="Number of contact performed during last campaign")
    pdays: Optional[int] = Field(description="Number of days since the client was last contacted from a previous campaign.")
    previous: int = Field(description="Number of contact performed before this campaign")
