# -*- coding: utf-8 -*-
"""This file contains a WinRAR history Windows Registry plugin."""

from parsers.events import general


class WinRARHistoryEventData(general.PlasoGeneralEvent):
    """WinRAR history event data attribute container.

    Attributes:
      entries (str): archive history entries.
      key_path (str): Windows Registry key path.
    """

    DATA_TYPE = 'winrar:history'

    def __init__(self):
        """Initializes event data."""
        super(WinRARHistoryEventData, self).__init__(data_type=self.DATA_TYPE)
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
        return not self.__eq__(other)
