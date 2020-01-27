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
