from typing import List

from data_classes.table import Table


class Game:
    def __init__(self, tables : List[Table]):
        self.tables = tables