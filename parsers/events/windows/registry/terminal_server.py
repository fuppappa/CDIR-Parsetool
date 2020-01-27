# -*- coding: utf-8 -*-
"""This file contains the Terminal Server client Windows Registry plugins."""

from parsers.events import general


class TerminalServerClientConnectionEventData(general.PlasoGeneralEvent):
    """Terminal Server client connection event data attribute container.

    Attributes:
      entries (str): most recently used (MRU) entries.
      key_path (str): Windows Registry key path.
      username (str): username, provided by the UsernameHint value.
    """

    DATA_TYPE = 'windows:registry:mstsc:connection'

    def __init__(self):
        """Initializes event data."""
        super(TerminalServerClientConnectionEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.entries = None
        self.key_path = None
        self.username = None

    def SetEventAttribute(self, event):
        self.entries = event['entries']
        self.key_path = event['key_path']
        self.username = event['username']


class TerminalServerClientMRUEventData(general.PlasoGeneralEvent):
    """Terminal Server client MRU event data attribute container.

    Attributes:
      entries (str): most recently used (MRU) entries.
      key_path (str): Windows Registry key path.
    """

    DATA_TYPE = 'windows:registry:mstsc:mru'

    def __init__(self):
        """Initializes event data."""
        super(TerminalServerClientMRUEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.entries = None
        self.key_path = None

    def SetEventAttribute(self, event):
        self.entries = event['entries']
        self.key_path = event['key_path']
