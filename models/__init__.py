"""
reloads all stored objects from storage file each time module is lauvhed
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
