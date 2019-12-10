#!/usr/bin/env python3
from argparse import ArgumentParser
from lib import json_interface, csv_interface
import json
from datetime import datetime
import sys

__author__ = "yfujieda"
__version__ = "0.1"
__date__ = "2019_10_24"


def AnalyseTimeRange(timestamp, time_range):
    """Determine if timestamp is within specified range

    Args:
        time_range : Posix Time   ex. <start>-<end>
    """
    time = []
    time_str = time_range.split("-")
    time.append(int(time_str[0]))
    time.append(int(time_str[1]))

    if time[0] <= timestamp <= time[1]:
        return True

    return False


def divide_timerange(export_path, logs_path, timerange):
    with open(export_path, "a", encoding="utf-8") as f:
        for log in json_interface.JsonloadLiner(logs_path):
            if AnalyseTimeRange(log["timestamp"], timerange):
                json.dump(log, f)
                f.write("\n")
        print("finished!! export >> " + export_path)




def write_timeline(logs_path, export_path=None):
    all_list = []
    data_id = 1
    writer = csv_interface.CsvInterface(export_path)
    writer.CsvLineExport([["id", "file", "dsec", "timestamp", "run_count"]])

    for event_data in json_interface.JsonloadLiner(logs_path):
        if not "windows:prefetch:execution" == event_data["data_type"]:
            continue
        raw_data = []
        raw_data.append(data_id)
        raw_data.append(event_data["display_name"].split("/")[-1])

        raw_data.append(event_data["timestamp_desc"])
        timestamp = str(event_data["timestamp"])
        timestamp_sec = timestamp[:10]
        dt = datetime.fromtimestamp(int(timestamp_sec))
        raw_data.append(
            "{}/{}/{}/{}/{}/{}/{}".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, timestamp[-6:]))

        run_count = event_data["message"].split("\\")[0].split(" ")[-3]
        raw_data.append(run_count)
        data_id = data_id + 1
        all_list.append(raw_data.copy())

    writer.CsvExport(all_list)


def get_args():
    parser = ArgumentParser(description="Parse Program CDIR logs after Plaso conversion")

    parser.add_argument("Windows10 Log", type=str, help="Path to Log collected using CDIR after Plaso conversion ")
    parser.add_argument("-o", "--out", type=str, help="Path to export file")
    parser.add_argument("-i", "--interactive", action="store_true", help="switch interactive mode")
    parser.add_argument("-p", type=str, help="grep target program name")
    parser.add_argument("-t", "--timerange", type=str, help="time range in analysis(StartTime-EndTime)")
    parser.add_argument("--total_record", action="store_true", help="analysis only total record")

    args = parser.parse_args()

    return args


def main():
    args = get_args()
    logs_path = args.CDIR_Logs
    export_path = args.out
    divide_timerange(export_path, logs_path, args.timerange)


if __name__ == '__main__':
    main()
