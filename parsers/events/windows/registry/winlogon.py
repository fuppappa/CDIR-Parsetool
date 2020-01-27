# -*- coding: utf-8 -*-
"""This file contains the Winlogon Registry plugin."""

from parsers.events import general


class WinlogonEventData(general.PlasoGeneralEvent):
    """Winlogon event data attribute container.

    Attributes:
      application (str): Winlogon application.
      command (str): Winlogon command.
      handler (str): Winlogon handler.
      key_path (str): Windows Registry key path.
      trigger (str): Winlogon trigger.
    """

    DATA_TYPE = 'windows:registry:winlogon'

    def __init__(self):
        """Initializes event data."""
        super(WinlogonEventData, self).__init__(data_type=self.DATA_TYPE)
        self.application = None
        self.command = None
        self.handler = None
        self.key_path = None
        self.trigger = None
