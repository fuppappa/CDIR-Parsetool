from parsers.events import general


class SRUMApplicationResourceUsageEvent(general.PlasoGeneralEvent):
    """SRUM application resource usage event data.
    Note that the interpretation of some of these values is undocumented
    as far as currently known.
    Attributes:
      application (str): application.
      background_bytes_read (int): background number of bytes read.
      background_bytes_written (int): background number of bytes written.
      background_context_switches (int): number of background context switches.
      background_cycle_time (int): background cycle time.
      background_number_for_flushes (int): background number of flushes.
      background_number_for_read_operations (int): background number of read
          operations.
      background_number_for_write_operations (int): background number of write
          operations.
      face_time (int): face time.
      foreground_bytes_read (int): foreground number of bytes read.
      foreground_bytes_written (int): foreground number of bytes written.
      foreground_context_switches (int): number of foreground context switches.
      foreground_cycle_time (int): foreground cycle time.
      foreground_number_for_flushes (int): foreground number of flushes.
      foreground_number_for_read_operations (int): foreground number of read
          operations.
      foreground_number_for_write_operations (int): foreground number of write
          operations.
      identifier (int): record identifier.
      user_identifier (str): user identifier, which is a Windows NT security
          identifier.
    """

    DATA_TYPE = 'windows:srum:application_usage'

    def __init__(self):
        """Initializes event data."""
        super(SRUMApplicationResourceUsageEvent, self).__init__(
            data_type=self.DATA_TYPE)
        self.application = None
        self.background_bytes_read = None
        self.background_bytes_written = None
        self.background_context_switches = None
        self.background_cycle_time = None
        self.background_number_for_flushes = None
        self.background_number_for_read_operations = None
        self.background_number_for_write_operations = None
        self.face_time = None
        self.foreground_bytes_read = None
        self.foreground_bytes_written = None
        self.foreground_context_switches = None
        self.foreground_cycle_time = None
        self.foreground_number_for_flushes = None
        self.foreground_number_for_read_operations = None
        self.foreground_number_for_write_operations = None
        self.identifier = None
        self.user_identifier = None


class SRUMNetworkConnectivityUsageEventData(general.PlasoGeneralEvent):
    """SRUM network connectivity usage event data.
    Note that the interpretation of some of these values is undocumented
    as far as currently known.
    Attributes:
      application (str): application.
      identifier (int): record identifier.
      interface_luid (int): interface locally unique identifier (LUID).
      l2_profile_flags (int): L2 profile flags.
      l2_profile_identifier (int): L2 profile identifier.
      user_identifier (str): user identifier, which is a Windows NT security
          identifier.
    """

    DATA_TYPE = 'windows:srum:network_connectivity'

    def __init__(self):
        """Initializes event data."""
        super(SRUMNetworkConnectivityUsageEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.application = None
        self.identifier = None
        self.interface_luid = None
        self.l2_profile_flags = None
        self.l2_profile_identifier = None
        self.user_identifier = None


class SRUMNetworkDataUsageEventData(general.PlasoGeneralEvent):
    """SRUM network data usage event data.
    Note that the interpretation of some of these values is undocumented
    as far as currently known.
    Attributes:
      application (str): application.
      bytes_received (int): number of bytes received.
      bytes_sent (int): number of bytes sent.
      identifier (int): record identifier.
      interface_luid (int): interface locally unique identifier (LUID).
      l2_profile_flags (int): L2 profile flags.
      l2_profile_identifier (int): L2 profile identifier.
      user_identifier (str): user identifier, which is a Windows NT security
          identifier.
    """

    DATA_TYPE = 'windows:srum:network_usage'

    def __init__(self):
        """Initializes event data."""
        super(SRUMNetworkDataUsageEventData, self).__init__(
            data_type=self.DATA_TYPE)
        self.application = None
        self.bytes_received = None
        self.bytes_sent = None
        self.identifier = None
        self.interface_luid = None
        self.l2_profile_flags = None
        self.l2_profile_identifier = None
        self.user_identifier = None
