from enum import Enum

class Category(Enum):
    NEWS = "News"
    BLOG = "Blog"
    RESEARCH = "Research"
    OTHER = "Other"

class EntityType(Enum):
    PERSON = "Person"
    ORGANIZATION = "Organization"
    LOCATION = "Location"