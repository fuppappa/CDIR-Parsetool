# -*- coding: utf-8 -*-
"""Windows drivers and services Registry key parser plugin."""

from parsers.events import general


class WindowsRegistryServiceEventData(general.PlasoGeneralEvent):
    """Windows Registry driver or service event data attribute container.

    Attributes:
      error_control (int): error control value of the Windows driver or service
          executable.
      image_path (str): path of the Windows driver or service executable.
      key_path (str): Windows Registry key path.
      name (str): name of the Windows driver or service.
      object_name (str): Windows service object name.
      service_dll (str): Windows service DLL.
      service_type (int): Windows driver or service type.
      start_type (int): Device or service start type.
      values (str): names and data of additional values in the key.
    """

    DATA_TYPE = 'windows:registry:service'

    def __init__(self):
        """Initializes event data."""
        super(WindowsRegistryServiceEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.error_control = None
        self.image_path = None
        self.key_path = None
        self.name = None
        self.service_dll = None
        self.object_name = None
        self.service_type = None
        self.start_type = None
        self.values = None