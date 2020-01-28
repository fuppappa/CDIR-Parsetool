# -*- coding: utf-8 -*-
"""This file contains an Outlook search MRU Registry parser."""

from parsers.events import general


class OutlookSearchMRUEventData(general.PlasoGeneralEvent):
    """Outlook search MRU event data attribute container.

    Attributes:
      entries (str): most recently used (MRU) entries.
      key_path (str): Windows Registry key path.
    """

    DATA_TYPE = 'windows:registry:outlook_search_mru'

    def __init__(self):
        """Initializes event data."""
        super(OutlookSearchMRUEventData, self).__init__(data_type=self.DATA_TYPE)
        self.entries = None
        self.key_path = None

    def SetEventAttribute(self, event):
        self.entries = event['entries']
        self.key_path = event['key_path']

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__ne__(other)
