# -*- coding: utf-8 -*-
"""The UserAssist Windows Registry plugin."""

from parsers.events import general


class UserAssistWindowsRegistryEventData(general.PlasoGeneralEvent):
    """UserAssist Windows Registry event data.

    Attributes:
      application_focus_count (int): application focus count.
      application_focus_duration (int): application focus duration.
      entry_index (int): entry index.
      key_path (str): Windows Registry key path.
      number_of_executions (int): nubmer of executions.
      value_name (str): name of the Windows Registry value.
    """

    DATA_TYPE = 'windows:registry:userassist'

    def __init__(self):
        """Initializes event data."""
        super(UserAssistWindowsRegistryEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.application_focus_count = None
        self.application_focus_duration = None
        self.entry_index = None
        self.key_path = None
        self.number_of_executions = None
        self.value_name = None

    def SetAttribute(self, event):
        self.application_focus_count = event["application_focus_count"]
        self.application_focus_duration = event["application_focus_duration"]
        self.entry_index = event["entry_index"]
        self.key_path = event["key_path"]
        self.number_of_executions = event["number_of_executions"]
        self.value_name = event["value_name"]
