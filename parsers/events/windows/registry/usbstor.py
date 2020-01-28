# -*- coding: utf-8 -*-
"""File containing a Windows Registry plugin to parse the USBStor key."""

from parsers.events import general


class USBStorEventData(general.PlasoGeneralEvent):
    """USBStor event data attribute container.

    Attributes:
      device_type (str): type of USB device.
      display_name (str): display name of the USB device.
      key_path (str): Windows Registry key path.
      parent_id_prefix (str): parent identifier prefix of the USB device.
      product (str): product of the USB device.
      serial (str): serial number of the USB device.
      revision (str): revision number of the USB device.
      subkey_name (str): name of the Windows Registry subkey.
      vendor (str): vendor of the USB device.
    """

    DATA_TYPE = 'windows:registry:usbstor'

    def __init__(self):
        """Initializes event data."""
        super(USBStorEventData, self).__init__(data_type=self.DATA_TYPE)
        self.device_type = None
        self.display_name = None
        self.key_path = None
        self.parent_id_prefix = None
        self.product = None
        self.revision = None
        self.serial = None
        # TODO: rename subkey_name to something that closer matches its purpose.
        self.subkey_name = None
        self.vendor = None

    def SetEventAttribute(self, event):
        self.device_type = event['device_type']
        self.display_name = event['display_name']
        self.key_path = event['key_path']
        self.parent_id_prefix = event['parent_id_prefix']
        self.product = event['product']
        self.revision = event['revision']
        self.serial = event['serial']
        # TODO: rename subkey_name to something that closer matches its purpose.
        self.subkey_name = event['subkey_name']
        self.vendor = event['vendor']

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__ne__(other)
