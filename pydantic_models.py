from pydantic import BaseModel, Field
from typing import List
from domain_types import Category, EntityType


class ClassificationResultSchema(BaseModel):
    classification: Category = Field(
        description="The category that best describes the input text"
    )

class Entity(BaseModel):
    name: str = Field(
        description="The entity's name"
    )

    entity_type: EntityType = Field(
        description="The entity category"
    )

class EntityExtractionResultSchema(BaseModel):
    entities: List[Entity] = Field(
        default_factory=List,
        description="All entities found in the input text"
    )

class SummarizationResultSchema(BaseModel):
    summary: str = Field(
        description="'''A concise summary."
    )