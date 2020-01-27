import sys
from parsers.events.browser import chrome, firefox, msie, opera, safari
from parsers.events.fs import filestat, ntfs
from parsers.events.windows import win_eventlog, win_prefetch, srum
from parsers.events.windows.registry import appcompatcache, bagmru, bam, ccleaner, lfu, mountpoints, mrulist, mrulistex, \
    msie_zones, network_drives, networks, officemru, outlook, programscache, run, sam_users, services, shutdown, \
    task_scheduler, terminal_server, timezone, \
    typedurls, usb, usbstor, userassist, windows_version, winlogon, winrar, winreg


class BrowserEventManager(object):
    """
    Reference plaso/plaso/analysis/browser_search.py
    """
    OBJ_TYPE = 'browser'

    SUPPORTED_EVENT_DATA_TYPES = {
        'chrome:autofill:entry':
            ('', chrome),
        'chrome:cache:entry':
            ('', chrome),
        'chrome:cookie:entry':
            ('', chrome),
        'chrome:extension_activity:activity_log':
            ('', chrome),
        'chrome:history:file_downloaded':
            ('ChromeHistoryFileDownloadedEvent', chrome),
        'chrome:history:page_visited':
            ('ChromeHistoryPageVisitedEvent', chrome),
        'firefox:cache:record':
            ('', firefox),
        'firefox:cookie:entry':
            ('', firefox),
        'firefox:places:bookmark_annotation':
            ('FirefoxPlacesBookmarkAnnotationEventData', firefox),
        'firefox:places:bookmark_folder':
            ('FirefoxPlacesBookmarkFolderEventData', firefox),
        'firefox:places:bookmark':
            ('FirefoxPlacesBookmarkEventData', firefox),
        'firefox:places:page_visited':
            ('FirefoxPlacesPageVisitedEventData', firefox),
        'firefox:downloads:download':
            ('FirefoxDownloadEventData', firefox),
        'cookie:google:analytics:utma':
            ('',),
        'cookie:google:analytics:utmb':
            ('',),
        'cookie:google:analytics:utmt':
            ('',),
        'cookie:google:analytics:utmz':
            ('',),
        'msiecf:leak':
            ('', msie),
        'msiecf:redirected':
            ('', msie),
        'msiecf:url':
            ('', msie),
        'msie:webcache:container':
            ('', msie),
        'msie:webcache:containers':
            ('', msie),
        'msie:webcache:leak_file':
            ('', msie),
        'msie:webcache:partitions':
            ('', msie),
        'opera:history:entry':
            ('OperaGlobalHistoryEventData', opera),
        'opera:history:typed_entry':
            ('OperaTypedHistoryEventData', opera),
        'safari:cookie:entry':
            ('SafariBinaryCookieEventData', safari),
        'safari:history:visit':
            ('', safari),
        'safari:history:visit_sqlite':
            ('SafariHistoryPageVisitedEventData', safari)
    }


class FileSystemEventManager(object):
    OBJ_TYPE = 'file_system'

    SUPPORTED_EVENT_DATA_TYPES = {
        'fs:stat': ('FileStatEventData', filestat),
        'fs:stat:ntfs': ('NTFSFileStatEventData', ntfs),
        'fs:ntfs:usn_change': ('NTFSUSNChangeEventData', ntfs)}


class WinEvtxEventManager(object):
    OBJ_TYPE = 'win_evtx'

    SUPPORTED_EVENT_DATA_TYPES = {
        'windows:evtx:record': ('WinEvtxRecordEventData', win_eventlog)}


class WinPrefetchEventManager(object):
    OBJ_TYPE = 'win_prefetch'

    SUPPORTED_EVENT_DATA_TYPES = {
        'windows:prefetch:execution': ('WinPrefetchExecutionEventData', win_prefetch)}


class WinRegistryEventManager(object):
    OBJ_TYPE = 'win_reg'

    SUPPORTED_EVENT_DATA_TYPES = {
        'windows:registry:appcompatcache': ('AppCompatCacheEventData', appcompatcache),
        'windows:registry:bagmru': ('BagMRUEventData', bagmru),
        'windows:registry:bam': ('BackgroundActivityModeratorEventData', bam),
        'ccleaner:configuration': ('CCleanerConfigurationEventData', ccleaner),
        'ccleaner:update': ('CCleanerUpdateEventData', ccleaner),
        'windows:registry:boot_execute': ('WindowsBootExecuteEventData', lfu),
        'windows:registry:boot_verification': ('WindowsBootVerificationEventData', lfu),
        'windows:registry:mount_points2': ('MountPoints2EventData', mountpoints),
        'windows:registry:mrulist': ('MRUListEventData', mrulist),
        'windows:registry:mrulistex': ('MRUListExEventData', mrulistex),
        'windows:registry:msie_zone_settings': ('MSIEZoneSettingsEventData', msie_zones),
        'windows:registry:network_drive': ('NetworkDriveEventData', network_drives),
        'windows:registry:network': ('WindowsRegistryNetworkListEventData', networks),
        'windows:registry:office_mru': ('OfficeMRUWindowsRegistryEventData', officemru),
        'windows:registry:office_mru_list': ('OfficeMRUListWindowsRegistryEventData', officemru),
        'windows:registry:outlook_search_mru': ('OutlookSearchMRUEventData', outlook),
        'windows:registry:explorer:programcache': ('ExplorerProgramsCacheEventData', programscache),
        'windows:registry:run': ('RunKeyEventData', run),
        'windows:registry:sam_users': ('SAMUsersWindowsRegistryEventData', sam_users),
        'windows:registry:service': ('WindowsRegistryServiceEventData', services),
        'windows:registry:shutdown': ('ShutdownWindowsRegistryEventData', shutdown),
        'task_scheduler:task_cache:entry': ('TaskCacheEventData', task_scheduler),
        'windows:registry:mstsc:connection': ('TerminalServerClientConnectionEventData', terminal_server),
        'windows:registry:mstsc:mru': ('TerminalServerClientMRUEventData', terminal_server),
        'windows:registry:timezone': ('WindowsTimezoneSettingsEventData', timezone),
        'windows:registry:typedurls': ('TypedURLsEventData', typedurls),
        'windows:registry:usb': ('WindowsUSBDeviceEventData', usb),
        'windows:registry:usbstor': ('USBStorEventData', usbstor),
        'windows:registry:userassist': ('UserAssistWindowsRegistryEventData', userassist),
        'windows:registry:installation': ('WindowsRegistryInstallationEventData', windows_version),
        'windows:registry:winlogon': ('WinlogonEventData', winlogon),
        'winrar:history': ('WinRARHistoryEventData', winrar),
        'windows:distributed_link_tracking:creation': ('WindowsDistributedLinkTrackingEventData', winreg),
        'windows:registry:key_value': ('WindowsRegistryEventData', winreg),
        'windows:volume:creation': ('WindowsVolumeEventData', winreg)
    }


class SrumEventManager(object):
    OBJ_TYPE = 'srum'

    SUPPORTED_EVENT_DATA_TYPES = {
        'windows:srum:application_usage': ('SRUMApplicationResourceUsageEventData', srum),
        'windows:srum:network_connectivity': ('SRUMNetworkConnectivityUsageEventData', srum),
        'windows:srum:network_usage': ('SRUMNetworkDataUsageEventData', srum)
    }


class EventManagerInterface(object):
    _SUPPORT_EVENT_CATEGORY = (
        BrowserEventManager,
        FileSystemEventManager,
        WinPrefetchEventManager,
        WinEvtxEventManager,
        WinRegistryEventManager,
        SrumEventManager
    )

    def __init__(self):
        super(EventManagerInterface, self).__init__()

    @classmethod
    def GetEventObject(self, data_type):
        """return tupple type SUPPORT_EVENTDATA_TYPES(dictionary) member
        """
        manager_obj = [category_obj.SUPPORTED_EVENT_DATA_TYPES for category_obj in self._SUPPORT_EVENT_CATEGORY]

        for category in manager_obj:
            if data_type in category:
                try:
                    eventobj_set = category[data_type]
                    event_initializer = getattr(eventobj_set[1], eventobj_set[0])

                    return event_initializer()

                except KeyError as e:
                    print(sys.exc_info())
                    print(e)
                    return False

        return None
