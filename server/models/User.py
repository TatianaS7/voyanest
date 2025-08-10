from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

from server.models.Itinerary import Itinerary

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    is_active: bool = Field(default=True)
    itineraries: List[Itinerary] = Relationship(back_populates="user")
