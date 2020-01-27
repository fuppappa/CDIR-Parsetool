# -*- coding: utf-8 -*-
"""This file contains the NetworkList Registry plugin."""

from parsers.events import general


class WindowsRegistryNetworkListEventData(general.PlasoGeneralEvent):
    """Windows NetworkList event data.

    Attributes:
      connection_type (str): type of connection.
      default_gateway_mac (str): MAC address for the default gateway.
      description (str): description of the wireless connection.
      dns_suffix (str): DNS suffix.
      ssid (str): SSID of the connection.
    """

    DATA_TYPE = 'windows:registry:network'

    def __init__(self):
        """Initializes event data."""
        super(WindowsRegistryNetworkListEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.connection_type = None
        self.default_gateway_mac = None
        self.description = None
        self.dns_suffix = None
        self.ssid = None
