# -*- coding: utf-8 -*-
"""Windows Registry plugin to parse the Background Activity Moderator keys."""

from parsers.events import general


class BackgroundActivityModeratorEventData(general.PlasoGeneralEvent):
    """Background Activity Moderator event data.

    Attributes:
      binary_path (str): binary executed.
      user_sid (str): user SID associated with entry.
    """

    DATA_TYPE = 'windows:registry:bam'

    def __init__(self):
        """Initializes event data."""
        super(
            BackgroundActivityModeratorEventData,
            self).__init__(data_type=self.DATA_TYPE)
        self.binary_path = None
        self.user_sid = None
