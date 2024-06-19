import reflex as rx
from typing import Optional, List
from sqlmodel import Field, SQLModel, create_engine, Session, select, Relationship

class Workspace(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    collections: List["Collection"] = Relationship(back_populates="workspace")

class Collection(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    
    workspace_id: int = Field(foreign_key="workspace.id")
    workspace: Optional[Workspace] = Relationship(back_populates="collections")
    

engine = create_engine("sqlite:///database.db", echo=True) # echo=True will print all SQL queries to the terminal
SQLModel.metadata.create_all(engine)    # Create the database schema for all the SQLModel classes

class State(rx.State):
    
    def add_collection_to_db(self, form_data: dict):
        collection = Collection(name=form_data["name"],workspace_id=form_data["workspace_id"])
        with rx.session() as session:
            session.add(collection)
            session.commit()
        return rx.toast.info(f"Collection {form_data["name"]} has been added.", variant="outline", position="bottom-right")
 