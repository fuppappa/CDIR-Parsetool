#!/usr/bin/env python3
from argparse import ArgumentParser
from lib import jsondeco
import json
import sys

__author__ = "yfujieda"
__version__ = "0.1"
__date__ = "2019_10_24"






def get_args():
    parser = ArgumentParser(description="Parse Program CDIR logs after Plaso conversion")

    parser.add_argument("CDIR_Logs", type=str, help="Path to a CDIR logs after Plaso conversion")
    parser.add_argument("-o", "--out", type=str, help="Path to export file")
    parser.add_argument("-i", "--interactive", action="store_true", help="switch interactive mode")
    parser.add_argument("-p", type=str, help="grep target program name")
    parser.add_argument("-t", "--timerange", type=str, help="time range in analysis(StartTime-EndTime)")
    parser.add_argument("--total_record", action="store_true", help="analysis only total record")

    args = parser.parse_args()

    return args


def main():
    args = get_args()
    pparser = PlasoLogpPrser(args)
    pparser.analysis_log()

    pparser.sum.display_time()


if __name__ == '__main__':
    main()
