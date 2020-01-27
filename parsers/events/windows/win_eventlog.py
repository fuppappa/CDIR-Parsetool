from parsers.events import general


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

    def SetEventAttribute(self, event):
        self.computer_name = event['computer_name']
        self.event_identifier = event['event_identifier']
        self.event_level = event['event_level']
        self.message_identifier = event['message_identifier']
        self.record_number = event['record_number']
        self.recovered = event['recovered']
        self.source_name = event['source_name']
        self.strings = event['strings']
        self.strings_parsed = event['strings_parsed']
        self.user_sid = event['user_sid']
        self.xml_string = event['xml_string']
