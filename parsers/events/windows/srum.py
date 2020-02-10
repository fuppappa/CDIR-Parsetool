# -*- coding: utf-8 -*-
"""Parser for the System Resource Usage Monitor (SRUM) ESE database.
For more information about the database format see:
https://github.com/libyal/esedb-kb/blob/master/documentation/
    System%20Resource%20Usage%20Monitor%20(SRUM).asciidoc
"""

from parsers.events import general


class SRUMApplicationResourceUsageEventData(general.PlasoGeneralEvent):
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
        super(SRUMApplicationResourceUsageEventData, self).__init__(
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

    def SetEventAttribute(self, event):
        self.application = event['application']
        self.background_bytes_read = event['background_bytes_read']
        self.background_bytes_written = event['background_bytes_written']
        self.background_context_switches = event['background_context_switches']
        self.background_cycle_time = event['background_cycle_time']
        self.background_number_for_flushes = event['background_number_for_flushes']
        self.background_number_for_read_operations = event['background_number_for_read_operations']
        self.background_number_for_write_operations = event['background_number_for_write_operations']
        self.face_time = event['face_time']
        self.foreground_bytes_read = event['foreground_bytes_read']
        self.foreground_bytes_written = event['foreground_bytes_written']
        self.foreground_context_switches = event['foreground_context_switches']
        self.foreground_cycle_time = event['foreground_cycle_time']
        self.foreground_number_for_flushes = event['foreground_number_for_flushes']
        self.foreground_number_for_read_operations = event['foreground_number_for_read_operations']
        self.foreground_number_for_write_operations = event['foreground_number_for_write_operations']
        self.identifier = event['identifier']
        self.user_identifier = event['user_identifier']

    def __eq__(self, other):
        if not isinstance(other, SRUMApplicationResourceUsageEventData):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


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

    def SetEventAttribute(self, event):
        self.application = event['application']
        self.identifier = event['identifier']
        self.interface_luid = event['interface_luid']
        self.l2_profile_flags = event['l2_profile_flags']
        self.l2_profile_identifier = event['l2_profile_identifier']
        self.user_identifier = event['user_identifier']

    def __eq__(self, other):
        if not isinstance(other, SRUMNetworkConnectivityUsageEventData):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


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

    def SetEventAttribute(self, event):
        self.application = event['application']
        if 'bytes_received' in event.keys():
            self.bytes_received = event['bytes_received']
        self.bytes_sent = event['bytes_sent']
        self.identifier = event['identifier']
        self.interface_luid = event['interface_luid']
        self.l2_profile_flags = event['l2_profile_flags']
        self.l2_profile_identifier = event['l2_profile_identifier']
        self.user_identifier = event['user_identifier']

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)
