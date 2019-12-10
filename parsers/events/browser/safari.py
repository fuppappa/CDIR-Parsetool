from parsers.events import general

class SafariHistoryPageVisitedEventData(events.EventData):
    """Safari history event data.
    Attributes:
      host (str): hostname of the server.
      title (str): title of the webpage visited.
      url (str): URL visited.
      visit_count (int): number of times the website was visited.
      was_http_non_get (bool): True if the webpage was visited using a
          non-GET HTTP request.
    """

    DATA_TYPE = 'safari:history:visit_sqlite'

    def __init__(self):
        """Initializes event data."""
        super(SafariHistoryPageVisitedEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.host = None
        self.title = None
        self.url = None
        self.visit_count = None
        self.visit_redirect_source = None
        self.was_http_non_get = None


class SafariBinaryCookieEventData(events.EventData):
    """Safari binary cookie event data.
    Attributes:
      cookie_name (str): cookie name.
      cookie_value (str): cookie value.
      flags (int): cookie flags.
      path (str): path of the cookie.
      url (str): URL where this cookie is valid.
    """

    DATA_TYPE = 'safari:cookie:entry'

    def __init__(self):
        """Initializes event data."""
        super(SafariBinaryCookieEventData, self).__init__(data_type=self.DATA_TYPE)
        self.cookie_name = None
        self.cookie_value = None
        self.flags = None
        self.path = None
        self.url = None
