import reflex as rx
from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session, select

class Collection(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

engine = create_engine("sqlite:///database.db")
# SQLModel.metadata.create_all(engine)

class State(rx.State):
    
    def add_collection_to_db(self, form_data: dict):
        collection = Collection(name=form_data["name"])
        with Session(engine) as session:
            session.add(collection)
            session.commit()
        return rx.toast.info(f"Collection {form_data["name"]} has been added.", variant="outline", position="bottom-right")
