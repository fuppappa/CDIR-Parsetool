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
