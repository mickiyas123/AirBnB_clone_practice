#!/usr/bin/python3
"""Init File"""

# Local Application Imports
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()