# Testing a Struct interface
This will test all the functionality of stack data structure, mainly push, pop, peak, size and empty.

## How to run the file

```bash
cd testing_struct_interface/
python3 test_stack.py -vv
```

# Data Store Library

This is library that can be used to store
and retrieve arbitrary data in multiple formats & destinations.

## Usage

```python
from data_storage_library import DataStorageLibrary

# returns 'object'
library = DataStorageLibrary('json', 'local')

# save single record
library.insert({'id': '6', 'name': 'aqeel', 'age': '30'})

# get single record
library.get('6')['name'] == 'aqeel'

# get all record
library.get_all()

# delete a single record

library.delete('1')

# update single record

library.update('1', {'name': 'ali', 'age': '30'})

# save multiple record

library.insert_batch([{'id': '6', 'name': 'aqeel', 'age': '30'},
                                   {'id': '7', 'name': 'ahmad', 'age': '45'},
                                   {'id': '10', 'name': 'shahzad', 'age': '20'}])

# get by filter (any parameter you can pass)

self.library.get_by_filter({'age': '30'})

# get by filter with limit and offset

library.get_by_filter_with_limit_and_offset({'name': 'salman'}, 2,1)
```
