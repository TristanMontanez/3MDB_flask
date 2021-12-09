from csv import reader
from typing import List, Dict
import os.path

DATABASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../table'))
DATABASE_PATH = os.path.join(DATABASE_PATH, 'customer_db.csv')


class BaseControllerClass:
    """Base Controller Class"""
    def __init__(self, entry_db):
        self.entry_db = entry_db
        self.entry_db = DATABASE_PATH

    def get_all_by_column(self, column: int, alphabetical: bool = True) -> List:
        """
        Returns all entries in a column as a List
        :param column: DB Column
        :param alphabetical: if False returns by order in DB
        :return: List of all items in DB
        """
        db = reader(open(self.entry_db, 'r'), delimiter=',')
        items = []
        for row in db:
            items.append(row[column])
        items.pop(0)
        if alphabetical:
            return sorted(items)
        else:
            return items

    def search_db(self, query: Dict) -> List:
        """
        Returns DB item
        :param query: Dictionary with format {search_parameter: term}
        :return: Item Dictionary with given query
        """
        db = reader(open(self.entry_db, 'r'), delimiter=',')
        parameters_list = list(query.keys())
        parameters_dict = {}
        first_row = next(db)
        for parameter in parameters_list:
            if parameter in first_row:
                parameters_dict[parameter] = first_row.index(parameter)

        second_row = next(db)
        for parameter in parameters_list:
            print(parameter)
            print(1)
            if not second_row[parameters_dict.get(parameter)] == query.get(parameter):
                print(2)
                break
            else:
                continue

        print(3)