
import json
from pydantic import BaseModel, Field, ValidationError


# 1. Define the required data structure
class Person(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=0, le=120)
    email: str = Field(min_length=5)
    skills: list[str]


# 2. Raw, unformatted text
raw_text = """
Name: Saksham Paudel
Age: 20
Email: saksham@example.com
Skills: Python, Java, SQL
"""


# 3. Extract fields from the raw text
def extract_data(text):
    extracted = {}

    for line in text.strip().splitlines():
        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip().lower()
        value = value.strip()

        if key == "name":
            extracted["name"] = value

        elif key == "age":
            extracted["age"] = int(value)

        elif key == "email":
            extracted["email"] = value

        elif key == "skills":
            extracted["skills"] = [
                skill.strip()
                for skill in value.split(",")
            ]

    return extracted


# 4. Validate the extracted data
try:
    data = extract_data(raw_text)
    person = Person.model_validate(data)

    # 5. Display the validated JSON
    print("Validated Pydantic Object:")
    print(person)

    print("\nJSON Output:")
    print(json.dumps(person.model_dump(), indent=4))

except (ValueError, ValidationError) as error:
    print("Data extraction or validation failed:")
    print(error)
