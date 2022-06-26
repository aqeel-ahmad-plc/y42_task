
import json
import os
import pickle

import unittest

class DataStorageLibrary:

    def __init__(self, storage_format, destination):
        self.storage_format = storage_format
        self.destination = destination
        self.records = {}

    def insert(self, record):
        self.records[record['id']] = record

    def get(self, id):
        return self.records[id]

    def get_all(self):
        return self.records

    def delete(self, id):
        del self.records[id]

    def update(self, id, record):
        self.records[id] = record

    def insert_batch(self, records):
        for record in records:
            self.records[record['id']] = record

    def get_by_filter(self, filter_dict):
        return [record for record in self.records.values() if self.filter_record(record, filter_dict)]

    def filter_record(self, record, filter_dict):
        for key, value in filter_dict.items():
            if record[key] != value:
                return False
        return True

    def get_by_filter_with_limit_and_offset(self, filter_dict, limit, offset):
        records = self.get_by_filter(filter_dict)
        return records[offset:offset + limit]

    def get_by_filter_with_limit_and_offset_and_order_by(self, filter_dict, limit, offset, order_by):
        records = self.get_by_filter(filter_dict)
        records.sort(key=lambda x: x[order_by])
        return records[offset:offset + limit]

    def get_by_filter_with_limit_and_offset_and_order_by_and_sort_order(self, filter_dict, limit, offset, order_by, sort_order):
        records = self.get_by_filter(filter_dict)
        if sort_order == 'asc':
            records.sort(key=lambda x: x[order_by])
        else:
            records.sort(key=lambda x: x[order_by], reverse=True)

        return records[offset:offset + limit]


class DataStorageLibraryTest(unittest.TestCase):

    def setUp(self):
        self.library = DataStorageLibrary('json', 'local')
        self.library.insert_batch([{'id': '1', 'name': 'John', 'age': '30'},
                                   {'id': '2', 'name': 'Jane', 'age': '25'},
                                   {'id': '3', 'name': 'Jack', 'age': '20'},
                                   {'id': '4', 'name': 'Jill', 'age': '35'},
                                   {'id': '5', 'name': 'Joe', 'age': '30'}])
    def test_insert(self):
        self.library.insert({'id': '6', 'name': 'John', 'age': '30'})
        assert self.library.get('6')['name'] == 'John'

    def test_get(self):
        assert self.library.get('1')['name'] == 'John'

    def test_get_all(self):
        assert len(self.library.get_all()) == 5

    def test_delete(self):
        self.library.delete('1')
        assert len(self.library.get_all()) == 4

    def test_update(self):
        self.library.update('1', {'name': 'John', 'age': '30'})
        assert self.library.get('1')['name'] == 'John'

    def test_insert_batch(self):
        self.library.insert_batch([{'id': '6', 'name': 'John', 'age': '30'},
                                   {'id': '7', 'name': 'Jane', 'age': '25'},
                                   {'id': '8', 'name': 'Jack', 'age': '20'},
                                   {'id': '9', 'name': 'Jill', 'age': '35'},
                                   {'id': '10', 'name': 'Joe', 'age': '40'}])
        assert len(self.library.get_all()) == 10

    def test_get_by_filter(self):
        assert len(self.library.get_by_filter({'age': '30'})) == 2

    def test_filter_record(self):
        assert self.library.filter_record({'age': '30'}, {'age': '30'})


# class DataStorageLibraryTest2:
#     def __init__(self):
#         self.library = DataStorageLibrary('pickle', 'local')
#         self.library.insert_batch([{'id': '1', 'name': 'John', 'age': '30'},
#                                    {'id': '2', 'name': 'Jane', 'age': '25'},
#                                    {'id': '3', 'name': 'Jack', 'age': '20'},
#                                    {'id': '4', 'name': 'Jill', 'age': '35'},
#                                    {'id': '5', 'name': 'Joe', 'age': '40'}])
#
#     def test_insert(self):
#         self.library.insert({'id': '6', 'name': 'John', 'age': '30'})
#         assert self.library.get('6')['name'] == 'John'
#
#     def test_get(self):
#         assert self.library.get('1')['name'] == 'John'
#
#     def test_get_all(self):
#         assert len(self.library.get_all()) == 5
#
#     def test_delete(self):
#         self.library.delete('1')
#         assert len(self.library.get_all()) == 4
#
#     def test_update(self):
#         self.library.update('1', {'name': 'John', 'age': '30'})
#         assert self.library.get('1')['name'] == 'John'
#
#     def test_insert_batch(self):
#         self.library.insert_batch([{'id': '6', 'name': 'John', 'age': '30'},
#                                    {'id': '7', 'name': 'Jane', 'age': '25'},
#                                    {'id': '8', 'name': 'Jack', 'age': '20'},
#                                    {'id': '9', 'name': 'Jill', 'age': '35'},
#                                    {'id': '10', 'name': 'Joe', 'age': '40'}])
#         assert len(self.library.get_all()) == 10
#
#     def test_get_by_filter(self):
#         assert len(self.library.get_by_filter({'age': '30'})) == 2
#
#     def test_filter_record(self):
#         assert self.library.filter_record({'age': '30'}, {'age': '30'})
#
#
# class DataStorageLibraryTest3:
#     def __init__(self):
#         self.library = DataStorageLibrary('json', 's3')
#         self.library.insert_batch([{'id': '1', 'name': 'John', 'age': '30'},
#                                    {'id': '2', 'name': 'Jane', 'age': '25'},
#                                    {'id': '3', 'name': 'Jack', 'age': '20'},
#                                    {'id': '4', 'name': 'Jill', 'age': '35'},
#                                    {'id': '5', 'name': 'Joe', 'age': '40'}])
#
#     def test_insert(self):
#         self.library.insert({'id': '6', 'name': 'John', 'age': '30'})
#         assert self.library.get('6')['name'] == 'John'
#
#     def test_get(self):
#         assert self.library.get('1')['name'] == 'John'
#
#     def test_get_all(self):
#         assert len(self.library.get_all()) == 5
#
#     def test_delete(self):
#         self.library.delete('1')
#         assert len(self.library.get_all()) == 4
#
#     def test_update(self):
#         self.library.update('1', {'name': 'John', 'age': '30'})
#         assert self.library.get('1')['name'] == 'John'
#
#     def test_insert_batch(self):
#         self.library.insert_batch([{'id': '6', 'name': 'John', 'age': '30'},
#                                    {'id': '7', 'name': 'Jane', 'age': '25'},
#                                    {'id': '8', 'name': 'Jack', 'age': '20'},
#                                    {'id': '9', 'name': 'Jill', 'age': '35'},
#                                    {'id': '10', 'name': 'Joe', 'age': '40'}])
#         assert len(self.library.get_all()) == 10
#
#     def test_get_by_filter(self):
#         assert len(self.library.get_by_filter({'age': '30'})) == 2
#
#     def test_filter_record(self):
#         assert self.library.filter_record({'age': '30'}, {'age': '30'})




#
if __name__ == '__main__':
    unittest.main()
