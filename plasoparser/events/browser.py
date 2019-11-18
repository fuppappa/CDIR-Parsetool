from plasoparser.events import general


class ChromeHistoryPageVisitedEvent(general.PlasoGeneralEvent):
    CONTAINER_VALUE = {"from_visit": "from_visit", "transition": "page_transition_type", "title": "title",
                       "typed_count": "typed_count", "url": "url", "url_hidden": "url_hidden",
                       "visited_source": "visit_source"
                       }
    TRANSITION_TYPE = ("link", "typed", "auto_bookmark", "auto_subframe", "manual_subframe", "generated",
                       "auto_toplevel", "form_submit", "reload", "keyword", "keyword_generated"
                       )

    DATA_TYPE = "chrome:history:page_visited"

    def __init__(self, event):
        super(ChromeHistoryPageVisitedEvent, self).__init__(event)
        self.from_vistit = self.GetSubEventContainerValue(event, "from_visit")
        self.transition = self.GetSubEventContainerValue(event, "transition")
        self.title = self.GetSubEventContainerValue(event, "title")
        self.typed_count = self.GetSubEventContainerValue(event, "typed_count")
        self.url = self.GetSubEventContainerValue(event, "url")
        self.url_hidden = self.GetSubEventContainerValue(event, "url_hidden")
        # self.visited_source = self.GetSubEventContainerValue(event, "visited_source")

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


class ChromeHistoryFileDownloadedEvent(general.PlasoGeneralEvent):
    CONTAINER_VALUE = {"received_path": "full_path", "received_bytes": "received_bytes", "total_bytes": "total_bytes",
                       "url": "url"
                       }

    DATA_TYPE = "chrome:history:downloaded"

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


class BrowserPlasoParser:
    CHROME_EVENT_ID = {"browser": "chrome", "parser": ["page_visited", "file_downloaded"]
                       }

    def __init__(self, event):
        self.type = None
        self.BrowserEvent = self.GetBrowserEvent(event)

    def GetBrowserEvent(self, event):
        event_type = event[general.PlasoGeneralEvent.GENERAL_CONTAINER_VALUE["data_type"]].split(":")
        if self.CHROME_EVENT_ID["browser"] in event_type:
            if self.CHROME_EVENT_ID["parser"][0] in event_type:
                self.type = self.CHROME_EVENT_ID["browser"] + "/" + self.CHROME_EVENT_ID["parser"][0]
                return ChromeHistoryPageVisitedEvent(event)
            elif self.CHROME_EVENT_ID["parser"][1] in event_type:
                self.type = self.CHROME_EVENT_ID["browser"] + "/" + self.CHROME_EVENT_ID["parser"][1]
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
            if self.BrowserEvent.IsUserEvent(received_path=before["received_path"]):
                return True

        return False
