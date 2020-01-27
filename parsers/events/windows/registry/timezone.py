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
