# -*- coding: utf-8 -*-
"""This file contains a WinRAR history Windows Registry plugin."""

from __future__ import unicode_literals

import re

from plaso.containers import events
from plaso.containers import time_events
from plaso.lib import definitions
from plaso.parsers import winreg
from plaso.parsers.winreg_plugins import interface


class WinRARHistoryEventData(general.PlasoGeneralEvent):
    """WinRAR history event data attribute container.

    Attributes:
      entries (str): archive history entries.
      key_path (str): Windows Registry key path.
    """

    DATA_TYPE = 'winrar:history'

    def __init__(self):
        """Initializes event data."""
        super(WinRARHistoryEventData, self).__init__(data_type=self.DATA_TYPE)
        self.entries = None
        self.key_path = None
