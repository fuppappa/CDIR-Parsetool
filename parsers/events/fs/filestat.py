from parsers.events import general


class FileStatEventData(general.PlasoGeneralEvent):
    """File system stat event data.
    Attributes:
      file_entry_type (int): dfVFS file entry type.
      file_size (int): file size in bytes.
      file_system_type (str): file system type.
      inode (int): inode of the file related to the event.
      is_allocated (bool): True if the file is allocated.
    """

    DATA_TYPE = 'fs:stat'

    def __init__(self):
        """Initializes event data."""
        super(FileStatEventData, self).__init__(data_type=self.DATA_TYPE)
        self.file_entry_type = None
        self.file_size = None
        self.file_system_type = None
        self.inode = None
        self.is_allocated = None

    def SetEventAttribute(self, event):
        self.file_entry_type = event['file_entry_type']
        self.file_size = event['file_size']
        self.file_system_type = event['file_system_type']
        self.inode = event['inode']
        self.is_allocated = event['is_allocated']

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)
