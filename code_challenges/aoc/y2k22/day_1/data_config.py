import os
from pydantic import BaseModel, validator


class DataConfig(BaseModel):
    file_path: str

    @validator("file_path")
    def validate_file_path(cls, file_path: str) -> str:
        if not file_path:
            raise ValueError("File path must not be empty.")
        if not isinstance(file_path, str):
            raise TypeError("File path must be a string.")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        return file_path

