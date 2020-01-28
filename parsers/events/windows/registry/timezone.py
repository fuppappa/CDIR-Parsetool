# -*- coding: utf-8 -*-
"""Plug-in to collect information about the Windows timezone settings."""

from parsers.events import general


class WindowsTimezoneSettingsEventData(general.PlasoGeneralEvent):
    """Timezone settings event data attribute container.

    Attributes:
      configuration (str): timezone configuration.
      key_path (str): Windows Registry key path.
    """

    DATA_TYPE = 'windows:registry:timezone'

    def __init__(self):
        """Initializes event data."""
        super(WindowsTimezoneSettingsEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.configuration = None
        self.key_path = None

    def SetEventAttribute(self, event):
        self.configuration = event['configuration']
        self.key_path = event['key_path']

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__ne__(other)
