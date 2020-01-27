# -*- coding: utf-8 -*-
""""Windows Registry plugin for the Microsoft Office MRU."""

from parsers.events import general


class OfficeMRUWindowsRegistryEventData(general.PlasoGeneralEvent):
    """Microsoft Office MRU Windows Registry event data.

    Attributes:
      key_path (str): Windows Registry key path.
      value_string (str): MRU value.
    """
    DATA_TYPE = 'windows:registry:office_mru'

    def __init__(self):
        """Initializes event data."""
        super(OfficeMRUWindowsRegistryEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.key_path = None
        self.value_string = None

    def SetEventAttribute(self, event):
        self.key_path = event['key_path']
        self.value_string = event['value_string']


class OfficeMRUListWindowsRegistryEventData(general.PlasoGeneralEvent):
    """Microsoft Office MRU list Windows Registry event data.

    Attributes:
      entries (str): most recently used (MRU) entries.
      key_path (str): Windows Registry key path.
    """
    DATA_TYPE = 'windows:registry:office_mru_list'

    def __init__(self):
        """Initializes event data."""
        super(OfficeMRUListWindowsRegistryEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.entries = None
        self.key_path = None

    def SetEventAttribute(self, event):
        self.entries = event['entries']
        self.key_path = event['key_path']
