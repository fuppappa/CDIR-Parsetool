# -*- coding: utf-8 -*-
"""This file contains the Task Scheduler Registry keys plugins."""

from parsers.events import general


class TaskCacheEventData(general.PlasoGeneralEvent):
    """Task Cache event data.

    Attributes:
      key_path (str): Windows Registry key path.
      task_name (str): name of the task.
      task_identifier (str): identifier of the task.
    """

    DATA_TYPE = 'task_scheduler:task_cache:entry'

    def __init__(self):
        """Initializes event data."""
        super(TaskCacheEventData, self).__init__(data_type=self.DATA_TYPE)
        self.key_path = None
        self.task_name = None
        self.task_identifier = None

    def SetEventAttribute(self, event):
        self.key_path = event['key_path']
        self.task_name = event['task_name']
        self.task_identifier = event['task_identifier']
