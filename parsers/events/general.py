class PlasoGeneralEvent(object):
    """plaso general parser
    "TIMEZONE = parser.PARSE_TIMEZONE"""

    def __init__(self, data_type=None):
        self.data_type = data_type
        self.display_name = None
        self.offset = None
        self.parser = None
        self.hash = None
        self.time_stamp = None
        self.time_dsec = None

    def SetEventAttribute(self, event):
        pass

    def GetAnalysisTimestamp(self):
        pass
        """もうすこしかしこいタイムゾーン設定を
        return datetime.now(self.TIMEZONE).timestamp()"""

    def __eq__(self, other):
        if not isinstance(other, PlasoGeneralEvent):
            return NotImplemented
        return self.time_stamp == other.time_stamp

    def __lt__(self, other):
        if not isinstance(other, PlasoGeneralEvent):
            return NotImplemented
        return self.time_stamp < other.time_stamp

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
