from parsers.events import general


class OperaTypedHistoryEventData(general.PlasoGeneralEvent):
  """Opera typed history entry data.
  Attributes:
    entry_selection (str): information about whether the URL was directly
        typed in or the result of the user choosing from the auto complete.
    entry_type (str): information about whether the URL was directly typed in
        or the result of the user choosing from the auto complete.
    url (str): typed URL or hostname.
  """

  DATA_TYPE = 'opera:history:typed_entry'

  def __init__(self):
    """Initializes event data."""
    super(OperaTypedHistoryEventData, self).__init__()
    self.entry_selection = None
    self.entry_type = None
    self.url = None


class OperaGlobalHistoryEventData(general.PlasoGeneralEvent):
  """Opera global history entry data.
  Attributes:
    description (str): description.
    popularity_index (int): popularity index.
    title (str): title.
    url (str):  URL.
  """

  DATA_TYPE = 'opera:history:entry'

  def __init__(self):
    """Initializes event data."""
    super(OperaGlobalHistoryEventData, self).__init__()
    self.description = None
    self.popularity_index = None
    self.title = None
    self.url = None