import time, sys
import json
from datetime import datetime, timezone, timedelta

JST = timezone(timedelta(hours=+9), "JST")


class Summary:
    def __init__(self):
        self.total_record = 0
        self.start_time = time.time()
        self.end_time = None

    def add_record(self):
        self.total_record += 1

    def display_halfway(self):
        self.add_record()
        sys.stdout.write("\rAnalysing %d record now..." % self.total_record)
        sys.stdout.flush()
        time.sleep(0.001)

    def display_time(self):
        self.end_time = time.time()
        ms = self.elapsed_time()

        print("\nAnalysing finished [time:{}m {}s]".format(ms[-1], ms[1]))

    def elapsed_time(self):
        elapsed = round(self.end_time - self.start_time)
        ms = [elapsed // 59, elapsed % 60]
        return ms


class PlasoGeneralLogParser():
    """plaso general parser"""

    GENERAL_CONTAINER_VALUE = {"container_type": "__container_type__", "type": "__type__", "data_type": "data_type",
                               "display_type": "display_name", "offset": "offset", "parser": "parser",
                               "pathspec": "pathspec", "hash": "sha256_hash", "time_stamp": "timestamp",
                               "time_dsec": "timestamp_desc"}

    TIMEZONE = JST

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
        self.general_event = event

    def GetEventContainerValue(self, event, tag):
        """ここに値が存在するか確認する"""

        return event[self.GENERAL_CONTAINER_VALUE[tag]]

    def GetSubEventContainerValue(self, event, tag):
        pass


    def GetAnalysisTimestamp(self):
        """もうすこしかしこいタイムゾーン設定を"""
        return datetime.now(self.TIMEZONE).timestamp()

    def __eq__(self, other):
        if not isinstance(other, PlasoGeneralLogParser):
            return NotImplemented
        return self.time_stamp == other.time_stamp

    def __lt__(self, other):
        if not isinstance(other, PlasoGeneralLogParser):
            return NotImplemented
        return self.time_stamp < other.time_stamp

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def IsUserEvent(self, **target):
        pass


class ChromeHistoryPageVisitedEvent(PlasoGeneralLogParser):
    CONTAINER_VALUE = {"from_visit": "from_visit", "transition": "page_transition_type", "title": "title",
                       "typed_count": "typed_count", "url": "url", "url_hidden": "url_hidden",
                       "visited_source": "visit_source"
                       }
    TRANSITION_TYPE = ("link", "typed", "auto_bookmark", "auto_subframe", "manual_subframe", "generated",
                       "auto_toplevel", "form_submit", "reload", "keyword", "keyword_generated"
                       )
    EVENT_TYPE = "Chrome"

    def __init__(self, event):
        super(ChromeHistoryPageVisitedEvent, self).__init__(event)
        self.from_vistit = self.GetSubEventContainerValue(event, "from_visit")
        self.transition = self.GetSubEventContainerValue(event, "transition")
        self.title = self.GetSubEventContainerValue(event, "title")
        self.typed_count = self.GetSubEventContainerValue(event, "typed_count")
        self.url = self.GetSubEventContainerValue(event, "url")
        self.url_hidden = self.GetSubEventContainerValue(event, "url_hidden")
        #self.visited_source = self.GetSubEventContainerValue(event, "visited_source")


    def GetSubEventContainerValue(self, event, tag):
        return event[self.CONTAINER_VALUE[tag]]

    def IsUserEvent(self, **target):
        if self.from_vistit != target["from_visit"]:
            return False
        if self.url == target["url"]:
            if self.title != target["title"]:
                return False

        return True

    def TransitionType(self):
        return self.TRANSITION_TYPE[self.transition]


class ChromeHistoryFileDownloadedEvent(PlasoGeneralLogParser):
    CONTAINER_VALUE = {"received_path": "full_path", "received_bytes": "received_bytes", "total_bytes": "total_bytes",
                       "url": "url"
                       }

    def __init__(self, event):
        super(ChromeHistoryFileDownloadedEvent, self).__init__(event)
        self.received_path = self.GetSubEventContainerValue(event, "received_path")
        self.received_bytes = self.GetSubEventContainerValue(event, "received_bytes")
        self.total_bytes = self.GetSubEventContainerValue(event, "total_bytes")
        self.url = self.GetSubEventContainerValue(event, "url")

    def GetSubEventContainerValue(self, event, tag):
        return event[self.CONTAINER_VALUE[tag]]

    def IsUserEvent(self, **target):
        if self.received_path != target["received_path"]:
            return False
        return True


class BrowserParser:
    CHROME_EVENT_ID = {"browser": "chrome", "parser": ["page_visited", "file_download"]
                       }

    def __init__(self, event):
        self.parser = event["parser"]
        self.data_type = event["data_type"]
        self.BrowserEvent = self.GetBrowserEvent(event)

    def GetBrowserEvent(self, event):
        event_type = self.data_type.split(":")
        if self.CHROME_EVENT_ID["browser"] in event_type:
            if self.CHROME_EVENT_ID["parser"][0] in event_type:
                return ChromeHistoryPageVisitedEvent(event)
            elif self.CHROME_EVENT_ID["parser"][1] in event_type:
                return ChromeHistoryFileDownloadedEvent(event)
        else:
            pass

        return None

    def Analyse(self, **before):
        if not self.BrowserEvent:
            return False

        if issubclass(self.BrowserEvent, ChromeHistoryPageVisitedEvent):
            if self.BrowserEvent.IsUserEvent(from_visit=before["from_visit"], url=before["url"]):
                return True

        if issubclass(self.BrowserEvent, ChromeHistoryFileDownloadedEvent):
            return True

        return False
