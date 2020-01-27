# -*- coding: utf-8 -*-
"""Windows Registry plugin to parse the Explorer ProgramsCache key."""

from parsers.events import general


class ExplorerProgramsCacheEventData(general.PlasoGeneralEvent):
    """Explorer ProgramsCache event data attribute container.

    Attributes:
      entries (str): entries in the program cache.
      key_path (str): Windows Registry key path.
      known_folder_identifier (str): known folder identifier.
      value_name (str): Windows Registry value name.
    """

    DATA_TYPE = 'windows:registry:explorer:programcache'

    def __init__(self):
        """Initializes event data."""
        super(ExplorerProgramsCacheEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.entries = None
        self.key_path = None
        self.known_folder_identifier = None
        self.value_name = None