# -*- coding: utf-8 -*-
"""Parser for the CCleaner Registry key."""

from parsers.events import general


class CCleanerConfigurationEventData(general.PlasoGeneralEvent):
    """CCleaner configuration event data.

    Attributes:
      configuration (str): CCleaner configuration.
      key_path (str): Windows Registry key path.
    """

    DATA_TYPE = 'ccleaner:configuration'

    def __init__(self):
        """Initializes event data."""
        super(CCleanerConfigurationEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.configuration = None
        self.key_path = None

    def SetEventAttribute(self, event):
        self.configuration = event['configuration']
        self.key_path = event['key_path']


class CCleanerUpdateEventData(general.PlasoGeneralEvent):
    """CCleaner update event data.

    Attributes:
      key_path (str): Windows Registry key path.
    """

    DATA_TYPE = 'ccleaner:update'

    def __init__(self):
        """Initializes event data."""
        super(CCleanerUpdateEventData, self).__init__(data_type=self.DATA_TYPE)
        self.key_path = None

    def SetEventAttribute(self, event):
        self.key_path = event['key_path']
