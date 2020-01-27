# -*- coding: utf-8 -*-
"""This file contains BagMRU Windows Registry plugins (shellbags)."""




class BagMRUEventData(general.PlasoGeneralEvent):
  """BagMRU event data attribute container.

  Attributes:
    entries (str): most recently used (MRU) entries.
    key_path (str): Windows Registry key path.
  """

  DATA_TYPE = 'windows:registry:bagmru'

  def __init__(self):
    """Initializes event data."""
    super(BagMRUEventData, self).__init__(data_type=self.DATA_TYPE)
    self.entries = None
    self.key_path = None

