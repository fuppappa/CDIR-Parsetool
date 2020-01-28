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

    def SetEventAttribute(self, event):
        self.binary_path = event["binary_path"]
        self.user_sid = event["user_sid"]

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__ne__(other)
