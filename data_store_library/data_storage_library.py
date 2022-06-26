
import json
import os
import pickle


class DataStorageLibrary:

    """
    The DataStorageLibrary class will be used to store and retrieve data in multiple
    formats and destinations.

    The library support the following functinality:


    1. Record insertion/ Batch insertion
    2. Record query/retrieval
    3. Query filters (equality operations only), limit & offset
    4. Update and delete operations
    """

    # === __init__ ===
    def __init__(self, storage_format, destination):
        # This function will initilize the storage_format and destination, it will call when object is created

        # **storage_format :** Which formats of data can be stored like (Json, xml)
        # **destination :** where to store the data (local, aws, ftp)
        # **records :** initilize dictionary to save the data locally
        self.storage_format = storage_format
        self.destination = destination
        self.records = {}

    # === __insert__ ===
    def insert(self, record):
        # This function will insert single record in local storage.

        # **record :** User will send the single record in key:value format and it will save.
        self.records[record['id']] = record

    # === get ===
    def get(self, id):
        # This function will get single record from local storage.

        # **id :** User will send the Id of record and it will get the record the of that ID
        return self.records[id]

    # === get_all ===
    def get_all(self):
        # This function will get all record from local storage, irrespective of the record.
        return self.records

    # === delete ===
    def delete(self, id):
        # This function will delete single record from local storage.

        # **id :** User will send the Id of record and it will delete the record the of that ID
        del self.records[id]

    # === update ===
    def update(self, id, record):
        # This function will update single record in local storage. User will send Id and record to update the record

        # **id :** User will send the Id of record that wants to update <br>
        # **record :** User will send the updated record here
        self.records[id] = record

    # === insert_batch ===
    def insert_batch(self, records):
        # This function will insert list of records in local storage

        # **records :** List of records send by user and it will insert in local storage
        for record in records:
            self.records[record['id']] = record

    # === get_by_filter ===
    def get_by_filter(self, filter_dict):
        # This function will get records by filter (name, age etc)

        # **records :** If user wants all records whose name is aqeel etc, it will get all the records where name is aqeel
        return [record for record in self.records.values() if self.filter_record(record, filter_dict)]

    # === filter_record ===
    def filter_record(self, record, filter_dict):
        # This function will get records by filter (name, age etc)

        # **records :** If user wants all records whose name is aqeel etc, it will get all the records where name is aqeel
        for key, value in filter_dict.items():
            if record[key] != value:
                return False
        return True

    # === get_by_filter_with_limit_and_offset ===
    def get_by_filter_with_limit_and_offset(self, filter_dict, limit, offset):
        # This function will get records by filter (name, age etc) and limit + offset

        # **filter_dict :** User will pass the filter on which the user want to search for example {name : 'aqeel'} <br>
        # **limit :** How many records user wants from filtered records <br>
        # **offset :** From where user want to start <br>
        # Example :  Total filtered records are 5 and user limit 3 and offset is 1 then it will fetch records id (2,3,4)
        records = self.get_by_filter(filter_dict)
        return records[offset:offset + limit]
