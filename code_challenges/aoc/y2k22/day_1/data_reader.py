"""
This module contains an abstract base class `DataReader` that defines the interface for reading
data from a file.
"""

from abc import ABC, abstractmethod
from typing import List, Union


class DataReader(ABC):
    """
    An abstract base class that defines the interface for reading data from a file.
    """

    @abstractmethod
    def read_data(self, file_path: str) -> List[Union[int, str]]:
        """
        Reads data from the specified file.

        Args:
            file_path (str): The path to the file.

        Returns:
            List[Union[int, str]]: A list of data read from the file.
        """
        pass
