# -*- coding: utf-8 -*-
"""File containing a Windows Registry plugin to parse the typed URLs key."""

from parsers.events import general


class TypedURLsEventData(general.PlasoGeneralEvent):
    """Typed URLs event data attribute container.

    Attributes:
      entries (str): typed URLs or paths entries.
      key_path (str): Windows Registry key path.
    """

    DATA_TYPE = 'windows:registry:typedurls'

    def __init__(self):
        """Initializes event data."""
        super(TypedURLsEventData, self).__init__(data_type=self.DATA_TYPE)
        self.entries = None
        self.key_path = None

    def SetEventAttribute(self, event):
        if 'entries' in event.keys():
            self.entries = event['entries']
        self.key_path = event['key_path']

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)
