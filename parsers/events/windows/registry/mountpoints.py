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