from typing import List, Optional

from sqlmodel import Field, SQLModel

class Itinerary(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    destination: Optional[str] = None
    created_by: int = Field(foreign_key="user.id")
