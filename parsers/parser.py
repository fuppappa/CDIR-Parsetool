import time, sys
from datetime import datetime, timezone, timedelta
from parsers import manager

JST = timezone(timedelta(hours=+9), "JST")

"""
@Parser Object
GeneralParser is General purpose analysing Class
Instance of This class is analyser object each data type 
"""


class PlasoLogParser:

    def __init__(self, event):
        """Plaso json_line log Parser Object

        Attributes:
            event: Dictionary object generated Plaso json_line log
            data_type: Event of Plaso event data type @https://github.com/log2timeline/plaso/blob/master/plaso/parsers
            parser: Plaso parser type analysed self event
            timestamp: Event occurrence time
            PlasoEvent　Plaso event management object
        """

        self.event = event
        self.data_type = self.event["data_type"]
        self.timestamp = self.event["timestamp"]
        self.PlasoEvent = None

    def AnalyseTimeRange(self, time_range):
        """Determine if timestamp is within specified range

        Args:
            time_range : Posix Time   ex. <start>-<end>
        """
        time = []
        time_str = time_range.split("-")
        time.append(int(time_str[0]))
        time.append(int(time_str[1]))

        if not time[0] / 10 == self.timestamp / 10 and time[1] / 10 == self.timestamp:
            return False

        if time[0] <= self.timestamp <= time[1]:
            return True

        return False

    def SetPlasoParserObject(self):
        event_manager = manager.EventManagerInterface()

        self.PlasoEvent = event_manager.DataType2Category(self.data_type)


class PlasoLogStreamParser:
    def __init__(self, path):
        self.log_path = path
        self.event = None
        self.total_event = None
