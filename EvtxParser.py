#!/usr/bin/env python3
import Evtx.Evtx as evtx
import Evtx.Views as e_views
import sys
import time
import xml.etree.ElementTree as ET
import xmltodict
import json
from argparse import ArgumentParser
from lib.ExportFormat import JsonFormat

__author__ = "yfujieda"
__version__ = "0.1"
__date__ = "2019_7_2"


class Summary:
    def __init__(self):
        self.total_record = 0
        self.start_time = time.time()
        self.end_time = None

    def add_record(self):
        self.total_record += 1
        return self.total_record

    def print_time(self):
        self.end_time = time.time()
        ms = self.elapsed_time()
        print("Analysing finished [time:{}m {}s]".format(ms[0], ms[1]))

    def elapsed_time(self):
        elapsed = round(self.end_time - self.start_time)
        ms = [elapsed // 60, elapsed % 60]
        return ms


class EvtxAnalyser:
    def __init__(self, key, process):
        self.key = key
        self.process = process
        self.value = ""
        self.summary = {}

    def record_analysis(self, record):
        self.value = record["Event"]["System"]["EventID"]["#text"]
        if self.value in self.summary:
            self.summary[self.value] += 1
        else:
            self.summary[self.value] = 1

    def serch_process(self, record):
        print()


def export(out, data):
    if out.split(".")[-1] == "json":
        JsonFormat(args.out, data, "a")
    elif out.split(".")[-1] == "xml":
        print("xml")
    else:
        print("\"{}\" is invalid format".format(out.split("/")[-1]))
        sys.exit()


def serchvalue(record, key, val):
    print("Searching start {}".format(val))


def get_args():
    parser = ArgumentParser(description="Analyse and Convert Evtx File.")

    parser.add_argument("evtx", type=str, help="Path to the Windows Evtx. (event log file[.evtx])")
    parser.add_argument("-o", "--out", type=str, help="export file format. (.json, .xml)")
    parser.add_argument("--search", type=str, help="search value.")
    parser.add_argument("--summary", action="store_true", help="Calculate statistical information based on Event ID.")
    parser.add_argument("-a", "--analysis" ,type=str, help="Select analysis type. (Event ID, Application)")

    args = parser.parse_args()

    return args


def dump_evtx(args):
    summary = Summary()
    event_summary = EvtxAnalyser("EventID", "d")

    with evtx.Evtx(args.evtx) as log:
        record_buf = e_views.XML_HEADER
        record_buf += "<Events>"
        for record in log.records():
            record_num = summary.add_record()

            sys.stdout.write("\rAnalysing %d record now..." % record_num)
            sys.stdout.flush()
            time.sleep(0.001)

            evtx_dict = xmltodict.parse(record.xml())
            event_summary.record_analysis(evtx_dict)
            if args.out is not None:
                export(args.out, evtx_dict)

    return summary, event_summary


def main(args):
    (summary, event_summary) = dump_evtx(args)
    sys.stdout.write("\n")

    summary.print_time()
    print("total record is {}".format(summary.total_record))
    print(event_summary.summary)


if __name__ == "__main__":
    args = get_args()

    main(args)
