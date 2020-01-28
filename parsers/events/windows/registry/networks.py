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

    def SetEventAttribute(self, event):
        self.connection_type = event['connection_type']
        self.default_gateway_mac = event['default_gateway_mac']
        self.description = event['description']
        self.dns_suffix = event['dns_suffix']
        self.ssid = event['ssid']

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__ne__(other)
