
import json
from pydantic import BaseModel, Field


class AIResponse(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=0, le=120)
    skills: list[str]


def parse_ai_response(raw_response: str) -> AIResponse:
    """Parse JSON text and validate it using Pydantic."""
    data = json.loads(raw_response)
    return AIResponse.model_validate(data)


if __name__ == "__main__":
    mock_response = """
    {
        "name": "Saksham",
        "age": 20,
        "skills": ["Python", "AI", "SQL"]
    }
    """

    result = parse_ai_response(mock_response)
    print("Validated AI response:")
    print(result.model_dump_json(indent=4))
