from parsers.events import general


class NTFSFileStatEventData(general.PlasoGeneralEvent):
    """NTFS file system stat event data.
    Attributes:
      attribute_type (int): attribute type for example "0x00000030", which
          represents "$FILE_NAME".
      file_attribute_flags (int): NTFS file attribute flags.
      file_reference (int): NTFS file reference.
      file_system_type (str): file system type.
      is_allocated (bool): True if the MFT entry is allocated (marked as in use).
      name (str): name associated with the stat event, for example that of
          a $FILE_NAME attribute or None if not available.
      parent_file_reference (int): NTFS file reference of the parent.
    """

    DATA_TYPE = 'fs:stat:ntfs'

    def __init__(self):
        """Initializes event data."""
        super(NTFSFileStatEventData, self).__init__(data_type=self.DATA_TYPE)
        self.attribute_type = None
        self.file_attribute_flags = None
        self.file_reference = None
        self.file_system_type = 'NTFS'
        self.is_allocated = None
        self.name = None
        self.parent_file_reference = None

    def SetEventAttribute(self, event):
        self.attribute_type = event['attribute_type']
        self.file_attribute_flags = event['file_attribute_flags']
        self.file_reference = event['file_reference']
        self.file_system_type = 'NTFS'
        self.is_allocated = event['is_allocated']
        self.name = event['name']
        self.parent_file_reference = event['parent_file_reference']

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


class NTFSUSNChangeEventData(general.PlasoGeneralEvent):
    """NTFS USN change event data.
    Attributes:
      file_attribute_flags (int): NTFS file attribute flags.
      filename (str): name of the file associated with the event.
      file_reference (int): NTFS file reference.
      file_system_type (str): file system type.
      parent_file_reference (int): NTFS file reference of the parent.
      update_reason_flags (int): update reason flags.
      update_sequence_number (int): update sequence number.
      update_source_flags (int): update source flags.
    """

    DATA_TYPE = 'fs:ntfs:usn_change'

    def __init__(self):
        """Initializes event data."""
        super(NTFSUSNChangeEventData, self).__init__(data_type=self.DATA_TYPE)
        self.file_attribute_flags = None
        self.filename = None
        self.file_reference = None
        self.parent_file_reference = None
        self.update_reason_flags = None
        self.update_sequence_number = None
        self.update_source_flags = None

    def SetEventAttribute(self, event):
        self.file_attribute_flags = event['file_attribute_flags']
        self.filename = event['file_name']
        self.file_reference = event['file_reference']
        self.parent_file_reference = event['parent_file_reference']
        self.update_reason_flags = event['update_reason_flags']
        self.update_sequence_number = event['update_sequence_number']
        self.update_source_flags = event['update_source_flags']

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)
