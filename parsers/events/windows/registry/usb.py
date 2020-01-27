# -*- coding: utf-8 -*-
"""File containing a Windows Registry plugin to parse the USB Device key."""

from parsers.events import general


class WindowsUSBDeviceEventData(general.PlasoGeneralEvent):
    """Windows USB device event data attribute container.

    Attributes:
      key_path (str): Windows Registry key path.
      product (str): product of the USB device.
      serial (str): serial number of the USB device.
      subkey_name (str): name of the Windows Registry subkey.
      vendor (str): vendor of the USB device.
    """

    DATA_TYPE = 'windows:registry:usb'

    def __init__(self):
        """Initializes event data."""
        super(WindowsUSBDeviceEventData, self).__init__(data_type=self.DATA_TYPE)
        self.key_path = None
        self.product = None
        self.serial = None
        # TODO: rename subkey_name to something that closer matches its purpose.
        self.subkey_name = None
        self.vendor = None
