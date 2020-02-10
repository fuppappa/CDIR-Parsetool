# -*- coding: utf-8 -*-
"""MountPoints2 Windows Registry parser plugin."""

from parsers.events import general


class MountPoints2EventData(general.PlasoGeneralEvent):
    """Windows MountPoints2 event data attribute container.

    Attributes:
      key_path (str): Windows Registry key path.
      label (str): mount point label.
      name (str): name of the mount point source.
      server_name (str): name of the remote drive server or None if not set.
      share_name (str): name of the remote drive share or None if not set.
      type (str): type of the mount point source, which can be "Drive",
          "Remove Drive" or "Volume".
    """

    DATA_TYPE = 'windows:registry:mount_points2'

    def __init__(self):
        """Initializes event data."""
        super(MountPoints2EventData, self).__init__(data_type=self.DATA_TYPE)
        self.key_path = None
        self.label = None
        self.name = None
        self.server_name = None
        self.share_name = None
        self.type = None

    def SetEventAttribute(self, event):
        self.key_path = event['key_path']
        if 'label' in event.keys():
            self.label = event['label']
        self.name = event['name']
        self.server_name = event['server_name']
        if 'share_name' in event.keys():
            self.share_name = event['share_name']
        if 'type' in event.keys():
            self.type = event['type']

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)
