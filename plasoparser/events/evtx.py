from plasoparser.events import general
class WinEvtxRecordEventData(general.PlasoGeneralEvent):
  """Windows XML EventLog (EVTX) record event data.
  Attributes:
    computer_name (str): computer name stored in the event record.
    event_identifier (int): event identifier.
    event_level (int): event level.
    message_identifier (int): event message identifier.
    record_number (int): event record number.
    recovered (bool): True if the record was recovered.
    source_name (str): name of the event source.
    strings (list[str]): event strings.
    strings_parsed ([dict]): parsed information from event strings.
    user_sid (str): user security identifier (SID) stored in the event record.
    xml_string (str): XML representation of the event.
  """

  DATA_TYPE = 'windows:evtx:record'

  def __init__(self):
    """Initializes event data."""
    super(WinEvtxRecordEventData, self).__init__(data_type=self.DATA_TYPE)
    self.computer_name = None
    self.event_identifier = None
    self.event_level = None
    self.message_identifier = None
    self.record_number = None
    self.recovered = None
    self.source_name = None
    self.strings = None
    self.strings_parsed = None
    self.user_sid = None
    self.xml_string = None