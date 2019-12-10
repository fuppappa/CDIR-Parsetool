from datetime import datetime, timezone, timedelta
from parsers import parser

class PlasoGeneralEvent():
    """plaso general parser"""

    CONTAINER_VALUE = {"container_type": "__container_type__", "type": "__type__", "data_type": "data_type",
                               "display_type": "display_name", "offset": "offset", "parser": "parser",
                               "pathspec": "pathspec", "hash": "sha256_hash", "time_stamp": "timestamp",
                               "time_dsec": "timestamp_desc"}

    TIMEZONE = parser.JST

    def __init__(self, event):
        self.container_type = self.GetEventContainerValue(event, "container_type")
        self.type = self.GetEventContainerValue(event, "type")
        self.data_type = self.GetEventContainerValue(event, "data_type")
        self.display_name = self.GetEventContainerValue(event, "display_type")
        self.offset = self.GetEventContainerValue(event, "offset")
        self.parser = self.GetEventContainerValue(event, "parser")
        self.pathspec = self.GetEventContainerValue(event, "pathspec")
        self.hash = self.GetEventContainerValue(event, "hash")
        self.time_stamp = self.GetEventContainerValue(event, "time_stamp")
        self.time_dsec = self.GetEventContainerValue(event, "time_dsec")
        self.time_analysis_time = self.GetAnalysisTimestamp()

    def GetEventContainerValue(self, event, tag):
        """ここに値が存在するか確認する"""

        return event[self.CONTAINER_VALUE[tag]]

    def GetSubEventContainerValue(self, event, tag):
        pass

    def GetAnalysisTimestamp(self):
        """もうすこしかしこいタイムゾーン設定を"""
        return datetime.now(self.TIMEZONE).timestamp()

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

    def IsUserEvent(self, **target):
        pass
