from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class RAGResponse_medical(BaseModel):
    """
        parse the response from ollama
    """
    Rank: str = Field(description="The determined injury rank")
    Justification: list[str]|str = Field(description="The reasoning behind the ranking")
    
    Key_Medical_Indicators: list[str]|str = Field(
        alias="Key Medical Indicators", 
        description="List of key medical indicators"
    )
output_parser_medical = PydanticOutputParser(pydantic_object=RAGResponse_medical)