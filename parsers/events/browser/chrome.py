from parsers.events import general


class ChromeHistoryPageVisitedEvent(general.PlasoGeneralEvent):
    TRANSITION_TYPE = ("link", "typed", "auto_bookmark", "auto_subframe", "manual_subframe", "generated",
                       "auto_toplevel", "form_submit", "reload", "keyword", "keyword_generated"
                       )

    DATA_TYPE = "chrome:history:page_visited"

    def __init__(self):
        super(ChromeHistoryPageVisitedEvent, self).__init__(data_type=self.DATA_TYPE)
        self.from_visit = None
        self.transition_type = None
        self.title = None
        self.url = None
        self.url_hidden = None

    def SetEventAttribute(self, event):
        self.from_visit = event["from_visit"]
        self.transition_type = event["page_transition_type"]
        self.title = event["title"]
        self.url = event["url"]
        self.url_hidden = event["url_hidden"]

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


class ChromeHistoryFileDownloadedEvent(general.PlasoGeneralEvent):
    CONTAINER_VALUE = {"received_path": "full_path", "received_bytes": "received_bytes", "total_bytes": "total_bytes",
                       "url": "url"
                       }

    DATA_TYPE = "chrome:history:file_downloaded"

    def __init__(self):
        super(ChromeHistoryFileDownloadedEvent, self).__init__(data_type=self.DATA_TYPE)
        self.received_path = None
        self.received_bytes = None
        self.total_bytes = None
        self.url = None

    def SetEventAttribute(self, event):
        self.received_path = event["received_path"]
        self.received_bytes = event["received_bytes"]
        self.total_bytes = event["total_bytes"]
        self.url = event["url"]

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)
