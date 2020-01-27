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
