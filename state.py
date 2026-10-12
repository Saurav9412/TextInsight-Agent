from typing import TypedDict, List, NotRequired
from domain_types import Category, EntityType

class Entity(TypedDict):
    name: str
    entity_type: EntityType


class State(TypedDict):
    text: str
    classification: NotRequired[Category]
    entities: NotRequired[List[Entity]]
    summary: NotRequired[str]