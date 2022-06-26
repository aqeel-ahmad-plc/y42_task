

import json
import os
import pickle

import unittest

from data_storage_library import DataStorageLibrary


class DataStorageLibraryTest(unittest.TestCase):

    def setUp(self):
        self.library = DataStorageLibrary('json', 'local')
        self.library.insert_batch([{'id': '1', 'name': 'aqeel', 'age': '30'},
                                   {'id': '2', 'name': 'ahmad', 'age': '45'},
                                   {'id': '3', 'name': 'salman', 'age': '50'},
                                   {'id': '4', 'name': 'taufeeq', 'age': '15'},
                                   {'id': '5', 'name': 'shahzad', 'age': '30'}])
    def test_insert(self):
        self.library.insert({'id': '6', 'name': 'aqeel', 'age': '30'})
        assert self.library.get('6')['name'] == 'aqeel'

    def test_get(self):
        assert self.library.get('1')['name'] == 'aqeel'

    def test_get_all(self):
        assert len(self.library.get_all()) == 5

    def test_delete(self):
        self.library.delete('1')
        assert len(self.library.get_all()) == 4

    def test_update(self):
        self.library.update('1', {'name': 'John', 'age': '30'})
        assert self.library.get('1')['name'] == 'John'

    def test_insert_batch(self):
        self.library.insert_batch([{'id': '6', 'name': 'aqeel', 'age': '30'},
                                   {'id': '7', 'name': 'ahmad', 'age': '45'},
                                   {'id': '8', 'name': 'salman', 'age': '50'},
                                   {'id': '9', 'name': 'taufeeq', 'age': '15'},
                                   {'id': '10', 'name': 'shahzad', 'age': '20'}])
        assert len(self.library.get_all()) == 10

    def test_get_by_filter(self):
        assert len(self.library.get_by_filter({'age': '30'})) == 2
        assert len(self.library.get_by_filter({'age': '45'})) == 1
        assert len(self.library.get_by_filter({'name': 'aqeel'})) == 1
        assert len(self.library.get_by_filter({'name': 'ahmad'})) == 1

    def test_filter_record(self):
        assert self.library.filter_record({'age': '30'}, {'age': '30'})

    def test_get_by_filter_with_limit_and_offset(self):
        self.library.insert_batch([{'id': '6', 'name': 'salman', 'age': '30'},
                                   {'id': '7', 'name': 'ali', 'age': '45'},
                                   {'id': '8', 'name': 'usman', 'age': '50'},
                                   {'id': '9', 'name': 'salman', 'age': '15'},
                                   {'id': '10', 'name': 'salman', 'age': '20'}])

        assert len(self.library.get_by_filter_with_limit_and_offset({'name': 'salman'}, 2,1)) == 2




if __name__ == '__main__':
    unittest.main()
