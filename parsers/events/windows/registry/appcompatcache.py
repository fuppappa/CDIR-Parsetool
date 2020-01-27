from parsers.events import general

"""Windows Registry plugin to parse the Application Compatibility Cache key."""


class AppCompatCacheEventData(general.PlasoGeneralEvent):
    """Application Compatibility Cache event data.

    Attributes:
      entry_index (int): cache entry index number for the record.
      key_path (str): Windows Registry key path.
      path (str): full path to the executable.
    """

    DATA_TYPE = 'windows:registry:appcompatcache'

    def __init__(self):
        """Initializes event data."""
        super(AppCompatCacheEventData, self).__init__(data_type=self.DATA_TYPE)
        self.entry_index = None
        self.key_path = None
        self.path = None


class AppCompatCacheHeader(object):
    """Application Compatibility Cache header."""

    def __init__(self):
        """Initializes the header object."""
        super(AppCompatCacheHeader, self).__init__()
        self.number_of_cached_entries = 0
        self.header_size = 0


class AppCompatCacheCachedEntry(object):
    """Application Compatibility Cache cached entry."""

    def __init__(self):
        """Initializes the cached entry object."""
        super(AppCompatCacheCachedEntry, self).__init__()
        self.cached_entry_size = 0
        self.data = None
        self.file_size = None
        self.insertion_flags = None
        self.last_modification_time = None
        self.last_update_time = None
        self.shim_flags = None
        self.path = None
