# -*- coding: utf-8 -*-
"""This file contains the MSIE zone settings plugin."""

from parsers.events import general


class MSIEZoneSettingsEventData(general.PlasoGeneralEvent):
    """MSIE zone settings event data attribute container.

    Attributes:
      key_path (str): Windows Registry key path.
      settings (str): MSIE zone settings.
    """

    DATA_TYPE = 'windows:registry:msie_zone_settings'

    def __init__(self):
        """Initializes event data."""
        super(MSIEZoneSettingsEventData, self).__init__(data_type=self.DATA_TYPE)
        self.key_path = None
        self.settings = None
