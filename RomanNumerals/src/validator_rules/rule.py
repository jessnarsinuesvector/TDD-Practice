import logging


class Rule:

    def __init__(self, name:str = None, description:str = None):
        self.name = name
        self.description = description

    def is_valid(self, input_str: str) -> bool:
        raise NotImplementedError()
