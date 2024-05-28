# TODO | Update docblocks
"""
Datareader
"""

from data_reader import DataReader
from typing import List, Union


class AocDataReader(DataReader):
    """
    Add a docstring here.
    """

    def read_data(self, file_path: str) -> List[Union[int, str]]:
        """
        Reads data from a file and returns a list of integers or empty strings.

        Parameters
        ----------
        file_path: str
            The path to the file to be read.

        Returns
        -------
        List[Union[int, str]]
            A list containing integers or empty strings.

        """
        with open(file_path, "r", encoding="utf-8") as file:
            return [int(line) if line.strip() else "" for line in file]
