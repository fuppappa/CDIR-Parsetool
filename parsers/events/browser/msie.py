from parsers.events import general


class MsieWebCacheContainersEventData(general.PlasoGeneralEvent):
    """MSIE WebCache Containers table event data.
    Attributes:
      container_identifier (int): container identifier.
      directory (str): name of the cache directory.
      name (str): name of the cache container.
      set_identifier (int): set identifier.
    """

    DATA_TYPE = 'msie:webcache:containers'

    def __init__(self):
        """Initializes event data."""
        super(MsieWebCacheContainersEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.container_identifier = None
        self.directory = None
        self.name = None
        self.set_identifier = None


class MsieWebCacheContainerEventData(general.PlasoGeneralEvent):
    """MSIE WebCache Container table event data.
    Attributes:
      access_count (int): access count.
      cached_filename (str): name of the cached file.
      cached_file_size (int): size of the cached file.
      cache_identifier (int): cache identifier.
      container_identifier (int): container identifier.
      entry_identifier (int): entry identifier.
      file_extension (str): file extension.
      redirect_url (str): URL from which the request was redirected.
      request_headers (str): request headers.
      response_headers (str): response headers.
      sync_count (int): sync count.
      url (str): URL.
    """

    DATA_TYPE = 'msie:webcache:container'

    def __init__(self):
        """Initializes event data."""
        super(MsieWebCacheContainerEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.access_count = None
        self.cached_filename = None
        self.cached_file_size = None
        self.cache_identifier = None
        self.container_identifier = None
        self.entry_identifier = None
        self.file_extension = None
        self.redirect_url = None
        self.request_headers = None
        self.response_headers = None
        self.sync_count = None
        self.url = None


class MsieWebCacheLeakFilesEventData(general.PlasoGeneralEvent):
    """MSIE WebCache LeakFiles event data.
    Attributes:
      cached_filename (str): name of the cached file.
      leak_identifier (int): leak identifier.
    """

    DATA_TYPE = 'msie:webcache:leak_file'

    def __init__(self):
        """Initializes event data."""
        super(MsieWebCacheLeakFilesEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.cached_filename = None
        self.leak_identifier = None


class MsieWebCachePartitionsEventData(general.PlasoGeneralEvent):
    """MSIE WebCache Partitions table event data.
    Attributes:
      directory (str): directory.
      partition_identifier (int): partition identifier.
      partition_type (int): partition type.
      table_identifier (int): table identifier.
    """

    DATA_TYPE = 'msie:webcache:partitions'

    def __init__(self):
        """Initializes event data."""
        super(MsieWebCachePartitionsEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.directory = None
        self.partition_identifier = None
        self.partition_type = None
        self.table_identifier = None


"""msiecf"""


class MSIECFLeakEventData(general.PlasoGeneralEvent):
    """MSIECF leak event data.
    Attributes:
      cached_filename (str): name of the cached file.
      cached_file_size (int): size of the cached file.
      cache_directory_index (int): index of the cache directory.
      cache_directory_name (str): name of the cache directory.
      recovered (bool): True if the item was recovered.
    """

    DATA_TYPE = 'msiecf:leak'

    def __init__(self):
        """Initializes event data."""
        super(MSIECFLeakEventData, self).__init__(data_type=self.DATA_TYPE)
        self.cached_filename = None
        self.cached_file_size = None
        self.cache_directory_index = None
        self.cache_directory_name = None
        self.recovered = None


class MSIECFRedirectedEventData(general.PlasoGeneralEvent):
    """MSIECF redirected event data.
    Attributes:
      recovered (bool): True if the item was recovered.
      url (str): location URL.
    """

    DATA_TYPE = 'msiecf:redirected'

    def __init__(self):
        """Initializes event data."""
        super(MSIECFRedirectedEventData, self).__init__(data_type=self.DATA_TYPE)
        self.recovered = None
        self.url = None


class MSIECFURLEventData(general.PlasoGeneralEvent):
    """MSIECF URL event data.
    Attributes:
      cached_filename (str): name of the cached file.
      cached_file_size (int): size of the cached file.
      cache_directory_index (int): index of the cache directory.
      cache_directory_name (str): name of the cache directory.
      http_headers (str): HTTP headers.
      number_of_hits (int): number of hits.
      recovered (bool): True if the item was recovered.
      url (str): location URL.
    """

    DATA_TYPE = 'msiecf:url'

    def __init__(self):
        """Initializes event data."""
        super(MSIECFURLEventData, self).__init__(data_type=self.DATA_TYPE)
        self.cached_filename = None
        self.cached_file_size = None
        self.cache_directory_index = None
        self.cache_directory_name = None
        self.http_headers = None
        self.number_of_hits = None
        self.offset = None
        self.recovered = None
        self.url = None
