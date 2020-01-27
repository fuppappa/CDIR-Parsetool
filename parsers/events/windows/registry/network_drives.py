# -*- coding: utf-8 -*-
"""This file contains the Network drive Registry plugin."""

from parsers.events import general


class NetworkDriveEventData(general.PlasoGeneralEvent):
    """Network drive event data attribute container.

    Attributes:
      drive_letter (str): drive letter assigned to network drive.
      key_path (str): Windows Registry key path.
      server_name (str): name of the server of the network drive.
      share_name (str): name of the share of the network drive.
    """

    DATA_TYPE = 'windows:registry:network_drive'

    def __init__(self):
        """Initializes event data."""
        super(NetworkDriveEventData, self).__init__(data_type=self.DATA_TYPE)
        self.drive_letter = None
        self.key_path = None
        self.server_name = None
        self.share_name = None

    def SetEventAttribute(self, event):
        self.drive_letter = event['drive_letter']
        self.key_path = event['key_path']
        self.server_name = event['server_name']
        self.share_name = event['share_name']
