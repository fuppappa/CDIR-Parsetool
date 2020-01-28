# -*- coding: utf-8 -*-
"""Plug-in to collect the Less Frequently Used Keys."""

from parsers.events import general


class WindowsBootExecuteEventData(general.PlasoGeneralEvent):
    """Windows Boot Execute event data attribute container.

    Attributes:
      key_path (str): Windows Registry key path.
      value (str): boot execute value, contains the value obtained from
          the BootExecute Registry value.
    """

    DATA_TYPE = 'windows:registry:boot_execute'

    def __init__(self):
        """Initializes event data."""
        super(WindowsBootExecuteEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.key_path = None
        self.value = None

    def SetEventAttribute(self, event):
        self.key_path = event['key_path']
        self.value = event['value']

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__ne__(other)


class WindowsBootVerificationEventData(general.PlasoGeneralEvent):
    """Windows Boot Verification event data attribute container.

    Attributes:
      image_path (str): location of the boot verification executable, contains
          the value obtained from the ImagePath Registry value.
      key_path (str): Windows Registry key path.
    """

    DATA_TYPE = 'windows:registry:boot_verification'

    def __init__(self):
        """Initializes event data."""
        super(WindowsBootVerificationEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.image_path = None
        self.key_path = None

    def SetEventAttribute(self, event):
        self.image_path = event['image_path']
        self.key_path = event['key_path']

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__ne__(other)
