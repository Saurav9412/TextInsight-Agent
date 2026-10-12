from prompts import classification_prompt, entity_extraction_prompt, summarization_prompt
from langchain_core.messages import HumanMessage
from state import State
from llm import build_llm
from pydantic_models import ClassificationResultSchema, EntityExtractionResultSchema, SummarizationResultSchema

def classification_node(state: State) -> ClassificationResultSchema:
    ''' Classify the text into one of the categories: News, Blog, Research, or Other '''
    formated_prompt = classification_prompt.format(text=state["text"])

    llm = build_llm()

    structured_llm = llm.with_structured_output(ClassificationResultSchema)

    response =  structured_llm.invoke([
            HumanMessage(content=formated_prompt)
        ])
    
    return {
        "classification": response.classification
    }
    

def entity_extraction_node(state: State) -> EntityExtractionResultSchema:
    ''' Extract all the entities (Person, Organization, Location) from the text      '''
    
    formated_prompt = entity_extraction_prompt.format(text=state["text"])
    
    llm = build_llm()

    structured_llm = llm.with_structured_output(EntityExtractionResultSchema)

    response = structured_llm.invoke([
        HumanMessage(content=formated_prompt)
    ])

    return {
        "entities": response.entities
    }

def summarization_node(state: State) -> SummarizationResultSchema:
    ''' Summarize the text in one short sentence '''

    formated_prompt = summarization_prompt.format(text=state["text"])

    llm = build_llm()

    structured_llm = llm.with_structured_output(SummarizationResultSchema)

    response = structured_llm.invoke([
        HumanMessage(content = formated_prompt)
    ])

    return {
        "summary": response.summary
    }