from langchain_core.prompts import PromptTemplate

classification_prompt = PromptTemplate.from_template(
    'Classify the text into one of the categories: News, Blog, Research, or Other.\n\nText: {text}\n\nClassification: '
)

entity_extraction_prompt = PromptTemplate.from_template(
    'Extract all the entities (Person, Organization, Location) from the following  text. Provide the result in comma seperated list.\n\nText: {text}\n\nEntities: '
)

summarization_prompt = PromptTemplate.from_template(
    'Summarize the text in one concise paragraph.\n\nText: {text}\n\nSummary: '
)