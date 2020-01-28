from parsers.events import general


class FirefoxPlacesBookmarkAnnotationEventData(general.PlasoGeneralEvent):
    """Firefox bookmark annotation event data.
    Attributes:
      content (str): annotation content.
      title (str): title of the bookmark folder.
      url (str): bookmarked URL.
    """

    DATA_TYPE = 'firefox:places:bookmark_annotation'

    def __init__(self):
        """Initializes event data."""
        super(FirefoxPlacesBookmarkAnnotationEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.content = None
        self.title = None
        self.url = None

    def SetEventAttribute(self, event):
        self.content = event['content']
        self.title = event['title']
        self.url = event['url']

    def __eq__(self, other):
        if not isinstance(other, FirefoxPlacesBookmarkAnnotationEventData):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__ne__(other)


class FirefoxPlacesBookmarkFolderEventData(general.PlasoGeneralEvent):
    """Firefox bookmark folder event data.
    Attributes:
      title (str): title of the bookmark folder.
    """

    DATA_TYPE = 'firefox:places:bookmark_folder'

    def __init__(self):
        """Initializes event data."""
        super(FirefoxPlacesBookmarkFolderEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.title = None

    def SetEventAttribute(self, event):
        self.title = event['title']

    def __eq__(self, other):
        if not isinstance(other, FirefoxPlacesBookmarkFolderEventData):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__ne__(other)


class FirefoxPlacesBookmarkEventData(general.PlasoGeneralEvent):
    """Firefox bookmark event data.
    Attributes:
      host (str): visited hostname.
      places_title (str): places title.
      title (str): title of the bookmark folder.
      type (int): bookmark type.
      url (str): bookmarked URL.
      visit_count (int): visit count.
    """

    DATA_TYPE = 'firefox:places:bookmark'

    def __init__(self):
        """Initializes event data."""
        super(FirefoxPlacesBookmarkEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.host = None
        self.places_title = None
        self.title = None
        self.type = None
        self.url = None
        self.visit_count = None

    def SetEventAttribute(self, event):
        self.host = event['host']
        self.places_title = event['places_title']
        self.title = event['title']
        self.type = event['type']
        self.url = event['url']
        self.visit_count = event['visit_count']

    def __eq__(self, other):
        if not isinstance(other, FirefoxPlacesBookmarkEventData):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__ne__(other)


# TODO: refactor extra attribute.
class FirefoxPlacesPageVisitedEventData(general.PlasoGeneralEvent):
    """Firefox page visited event data.
    Attributes:
      extra (list[object]): extra event data.
      host (str): visited hostname.
      title (str): title of the visited page.
      url (str): URL of the visited page.
      visit_count (int): visit count.
      visit_type (str): transition type for the event.
    """

    DATA_TYPE = 'firefox:places:page_visited'

    def __init__(self):
        """Initializes event data."""
        super(FirefoxPlacesPageVisitedEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.extra = None
        self.host = None
        self.title = None
        self.url = None
        self.visit_count = None
        self.visit_type = None

    def SetEventAttribute(self, event):
        self.extra = event['extra']
        self.host = event['host']
        self.title = event['title']
        self.url = event['url']
        self.visit_count = event['visit_count']
        self.visit_type = event['visit_type']

    def __eq__(self, other):
        if not isinstance(other, FirefoxPlacesPageVisitedEventData):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__ne__(other)


class FirefoxDownloadEventData(general.PlasoGeneralEvent):
    """Firefox download event data.
    Attributes:
      full_path (str): full path of the target of the download.
      mime_type (str): mime type of the download.
      name (str): name of the download.
      received_bytes (int): number of bytes received.
      referrer (str): referrer URL of the download.
      temporary_location (str): temporary location of the download.
      total_bytes (int): total number of bytes of the download.
      url (str): source URL of the download.
    """

    DATA_TYPE = 'firefox:downloads:download'

    def __init__(self):
        """Initializes event data."""
        super(FirefoxDownloadEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.full_path = None
        self.mime_type = None
        self.name = None
        self.offset = None
        self.received_bytes = None
        self.referrer = None
        self.temporary_location = None
        self.total_bytes = None
        self.url = None

    def SetEventAttribute(self, event):
        self.full_path = event['full_path']
        self.mime_type = event['mime_type']
        self.name = event['name']
        self.offset = event['offset']
        self.received_bytes = event['received_bytes']
        self.referrer = event['referrer']
        self.temporary_location = event['temporary_location']
        self.total_bytes = event['total_bytes']
        self.url = event['url']

    def __eq__(self, other):
        if not isinstance(other, FirefoxDownloadEventData):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__ne__(other)


"""
Cookie
"""


class FirefoxCookieEventData(general.PlasoGeneralEvent):
    """Firefox Cookie event data.
    Attributes:
      cookie_name (str): name field of the cookie.
      data (str): cookie data.
      httponly (bool): True if the cookie cannot be accessed through client
          side script.
      host (str): hostname of host that set the cookie value.
      path (str): URI of the page that set the cookie.
      secure (bool): True if the cookie should only be transmitted over a secure
          channel.
    """

    DATA_TYPE = 'firefox:cookie:entry'

    def __init__(self):
        """Initializes event data."""
        super(FirefoxCookieEventData, self).__init__(data_type=self.DATA_TYPE)
        self.cookie_name = None
        self.data = None
        self.host = None
        self.httponly = None
        self.path = None
        self.secure = None
        self.url = None

    def SetEventAttribute(self, event):
        self.cookie_name = event['cookie_name']
        self.data = event['data']
        self.host = event['host']
        self.httponly = event['httponly']
        self.path = event['path']
        self.secure = event['secure']
        self.url = event['url']

    def __eq__(self, other):
        if not isinstance(other, FirefoxCookieEventData):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__ne__(other)
