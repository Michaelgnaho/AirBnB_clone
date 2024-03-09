#!/usr/bin/python3
'''initialization file'''

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
