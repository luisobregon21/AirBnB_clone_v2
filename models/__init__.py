#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

print(os.getenv('HBNB_TYPE_STORAGE'))

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    print("HEY SEXY\n\n")
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
