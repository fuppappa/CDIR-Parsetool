# -*- coding: utf-8 -*-
"""Plug-in to collect information about the Windows version."""

from parsers.events import general


class WindowsRegistryInstallationEventData(general.PlasoGeneralEvent):
    """Windows installation event data attribute container.

    Attributes:
      build_number (str): Windows build number.
      key_path (str): Windows Registry key path.
      owner (str): registered owner.
      product_name (str): product name.
      service_pack (str): service pack.
      version (str): Windows version.
    """

    DATA_TYPE = 'windows:registry:installation'

    def __init__(self):
        """Initializes event data."""
        super(WindowsRegistryInstallationEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.build_number = None
        self.key_path = None
        self.owner = None
        self.product_name = None
        self.service_pack = None
        self.version = None

    def SetEventAttribute(self, event):
        self.build_number = event['build_number']
        self.key_path = event['key_path']
        self.owner = event['owner']
        self.product_name = event['product_name']
        if 'service_pack' in event.keys():
            self.service_pack = event['service_pack']
        self.version = event['version']

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__ne__(other)
