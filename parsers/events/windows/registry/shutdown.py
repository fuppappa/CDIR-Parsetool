# -*- coding: utf-8 -*-
"""Windows Registry plugin for parsing the last shutdown time of a system."""

from parsers.events import general


class ShutdownWindowsRegistryEventData(general.PlasoGeneralEvent):
    """Shutdown Windows Registry event data.

    Attributes:
      key_path (str): Windows Registry key path.
      value_name (str): name of the Windows Registry value.
    """

    DATA_TYPE = 'windows:registry:shutdown'

    def __init__(self):
        """Initializes event data."""
        super(ShutdownWindowsRegistryEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.key_path = None
        self.value_name = None

    def SetEventAttribute(self, event):
        self.key_path = event['key_path']
        self.value_name = event['value_name']

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__ne__(other)
