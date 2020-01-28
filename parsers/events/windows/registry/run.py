# -*- coding: utf-8 -*-
"""This file contains the Run/RunOnce key plugins for Plaso."""

from parsers.events import general


class RunKeyEventData(general.PlasoGeneralEvent):
    """Run/RunOnce key event data attribute container.

    Attributes:
      entries (str): Run/RunOnce entries.
      key_path (str): Windows Registry key path.
    """

    DATA_TYPE = 'windows:registry:run'

    def __init__(self):
        """Initializes event data."""
        super(RunKeyEventData, self).__init__(data_type=self.DATA_TYPE)
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
        return not self.__ne__(other)
