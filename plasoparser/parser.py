import time, sys
from datetime import datetime, timezone, timedelta
from plasoparser.events import general, browser, evtx

JST = timezone(timedelta(hours=+9), "JST")

"""
@Parser Object
GeneralParser is General purpose analysing Class
Instance of This class is analyser object each data type 
"""


class PlasoLogParser:
    _SUPPORTED_BROWSER_VALUE = {
        "chrome": {"history": ["page_visited", "file_downloaded"]},
        "firefox": {"places": ["bookmark_annotation", "bookmark_folder", "bookmark", "page_visited"],
                    "downloads": ["download"]},
        "msie": {"webcache": ["containers", "container", "leak_file", "partitions"],
                 "msiecf": ["leak", "redirected", "url"]}
    }

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
        self.parser = self.event["parser"]
        self.timestamp = self.event["timestamp"]
        self.PlasoEvent = self.GetParserObject()

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

    def GetParserObject(self):
        """未完成　パーサの分岐を増やす"""
        type = self.data_type.split(":")

        if self._SUPPORTED_BROWSER_VALUE in type:
            if self._SUPPORTED_BROWSER_VALUE["chrome"] in type:
                if self._SUPPORTED_BROWSER_VALUE["chrome"]["history"] in type:
                    index = self._SUPPORTED_BROWSER_VALUE[type[0]][type[1]].index(type[2])
                    if index == 0:
                        return browser.ChromeHistoryPageVisitedEvent(self.event)
                    elif index == 1:
                        return browser.ChromeHistoryFileDownloadedEvent(self.event)

            elif self._SUPPORTED_BROWSER_VALUE["firefox"] in type:
                if self._SUPPORTED_BROWSER_VALUE["firefox"]["places"] in type:
                    index = self._SUPPORTED_BROWSER_VALUE[type[0]][type[1]].index(type[2])
                    if index == 0:
                        """firefox:places:bookmark_annotation"""
                        pass
                    elif index == 1:
                        """firefox:places:bookmark_folder"""
                        pass
                    elif index == 2:
                        """firefox:places:bookmark"""
                        pass
                    elif index == 3:
                        """firefox:places:page_visited"""
                        pass
                elif self._SUPPORTED_BROWSER_VALUE["firefox"]["downloads"] in type:
                    """firefox:downloads:download"""
                    pass
            elif self._SUPPORTED_BROWSER_VALUE["msie"] in type:
                if "msiecf" in type:
                    index = self._SUPPORTED_BROWSER_VALUE["msie"][type[0]].index(type[1])
                    if index == 0:
                        """msiecf:leak"""
                        pass
                    elif index == 1:
                        """msiecf:redirected"""
                        pass
                    elif index == 2:
                        """msiecf:url"""
                        pass
                elif self._SUPPORTED_BROWSER_VALUE["msie"]["webcache"] in type:
                    index = self._SUPPORTED_BROWSER_VALUE[type[0]][type[1]].index(type[2])
                    if index == 0:
                        """msie:webcache:containers"""
                        pass
                    elif index == 1:
                        """msie:webcache:container"""
                        pass
                    elif index == 2:
                        """msie:webcache:leak_file"""
                        pass
                    elif index ==3:
                        """msie:webcache:partitions"""
                        pass










        return None


class PlasoLogStreamParser:
    def __init__(self, path):
        self.log_path = path
        self.event = None
        self.total_event = None
