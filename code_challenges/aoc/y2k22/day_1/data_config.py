from pydantic import BaseModel, validator
import os


class DataConfig(BaseModel):
    file_path: str

    @validator("file_path")
    def validate_file_path(cls, validator):
        if not validator:
            raise ValueError("File path must not be empty.")
        if not isinstance(validator, str):
            raise TypeError("File path must be a string.")
        if not os.path.exists(validator):
            raise FileNotFoundError(f"File not found: {validator}")

        return validator
