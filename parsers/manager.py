import sys
from parsers.events.browser import chrome, firefox, msie, opera, safari
from parsers.events.fs import ntfs, filestat


class BrowserEventManager(object):
    """
    Reference plaso/plaso/analysis/browser_search.py
    """
    OBJTYPE = "browser"

    SUPPORTED_EVENT_DATA_TYPES = {
        'chrome:autofill:entry':
            ("", chrome),
        'chrome:cache:entry':
            ("", chrome),
        'chrome:cookie:entry':
            ("", chrome),
        'chrome:extension_activity:activity_log':
            ("", chrome),
        'chrome:history:file_downloaded':
            ("ChromeHistoryFileDownloadedEvent", chrome),
        'chrome:history:page_visited':
            ("ChromeHistoryPageVisitedEvent", chrome),
        'firefox:cache:record':
            ("", firefox),
        'firefox:cookie:entry':
            ("", firefox),
        'firefox:places:bookmark_annotation':
            ("FirefoxPlacesBookmarkAnnotationEventData", firefox),
        'firefox:places:bookmark_folder':
            ("FirefoxPlacesBookmarkFolderEventData", firefox),
        'firefox:places:bookmark':
            ("FirefoxPlacesBookmarkEventData", firefox),
        'firefox:places:page_visited':
            ("FirefoxPlacesPageVisitedEventData", firefox),
        'firefox:downloads:download':
            ("FirefoxDownloadEventData", firefox),
        'cookie:google:analytics:utma':
            ("",),
        'cookie:google:analytics:utmb':
            ("",),
        'cookie:google:analytics:utmt':
            ("",),
        'cookie:google:analytics:utmz':
            ("",),
        'msiecf:leak':
            ("", msie),
        'msiecf:redirected':
            ("", msie),
        'msiecf:url':
            ("", msie),
        'msie:webcache:container':
            ("", msie),
        'msie:webcache:containers':
            ("", msie),
        'msie:webcache:leak_file':
            ("", msie),
        'msie:webcache:partitions':
            ("", msie),
        'opera:history:entry':
            ("OperaGlobalHistoryEventData", opera),
        'opera:history:typed_entry':
            ("OperaTypedHistoryEventData", opera),
        'safari:cookie:entry':
            ("SafariBinaryCookieEventData", safari),
        'safari:history:visit':
            ("", safari),
        'safari:history:visit_sqlite':
            ("SafariHistoryPageVisitedEventData", safari)
    }

    def __init__(self):
        super(BrowserEventManager, self).__init__()


class FileSystemEventManager(object):
    OBJ_TYPE = "file_system"

    SUPPORTED_EVENT_DATA_TYPES = {
        'fs:stat': ("NTFSFileStatEventData", filestat),
        'fs:stat:ntfs': ("NTFSFileStatEventData", ntfs),
        'fs:ntfs:usn_change': ("NTFSUSNChangeEventData", ntfs)}


class EventManagerInterface(object):
    _SUPPORT_EVENT_CATEGORY = (
        BrowserEventManager,
        FileSystemEventManager
    )

    def __init__(self):
        super(EventManagerInterface, self).__init__()

    def DataType2Category(self, data_type):
        """return tupple type SUPPORT_EVENTDATA_TYPES(dictionary) member
        """
        manager_obj = [category_obj.SUPPORTED_EVENT_DATA_TYPES for category_obj in self._SUPPORT_EVENT_CATEGORY]

        for category in manager_obj:
            if data_type in category:
                try:
                    eventobj_set = category[data_type]
                    event_initializer = getattr(eventobj_set[0], eventobj_set[1])

                    return event_initializer()

                except KeyError as e:
                    print(sys.exc_info())
                    print(e)
                    return False

        return None

