# -*- coding: utf-8 -*-
""""Windows Registry plugin for SAM Users Account information."""

from parsers.events import general


class SAMUsersWindowsRegistryEventData(general.PlasoGeneralEvent):
    """Class that defines SAM users Windows Registry event data.

    Attributes:
      account_rid (int): account relative identifier (RID).
      comments (str): comments.
      fullname (str): full name.
      key_path (str): Windows Registry key path.
      login_count (int): login count.
      username (str): a string containing the username.
    """
    DATA_TYPE = 'windows:registry:sam_users'

    def __init__(self):
        """Initializes event data."""
        super(SAMUsersWindowsRegistryEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.account_rid = None
        self.comments = None
        self.fullname = None
        self.key_path = None
        self.login_count = None
        self.username = None

    def SetEventAttribute(self, event):
        self.account_rid = event['account_rid']
        self.comments = event['comments']
        self.fullname = event['fullname']
        self.key_path = event['key_path']
        self.login_count = event['login_count']
        self.username = event['username']

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__ne__(other)
