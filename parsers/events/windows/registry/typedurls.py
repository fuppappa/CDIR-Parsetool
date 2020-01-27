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
