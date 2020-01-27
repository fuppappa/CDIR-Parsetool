# -*- coding: utf-8 -*-
"""This file contains MRUListEx Windows Registry plugins.

Also see:
  https://github.com/libyal/winreg-kb/wiki/MRU-keys
"""

from parsers.events import general


class MRUListExEventData(general.PlasoGeneralEvent):
    """MRUListEx event data attribute container.

    Attributes:
      entries (str): most recently used (MRU) entries.
      key_path (str): Windows Registry key path.
    """

    DATA_TYPE = 'windows:registry:mrulistex'

    def __init__(self):
        """Initializes event data."""
        super(MRUListExEventData, self).__init__(data_type=self.DATA_TYPE)
        self.entries = None
        self.key_path = None

    def SetEventAttribute(self, event):
        self.entries = event['entries']
        self.key_path = event['key_path']
