#!/usr/bin/env python3
from argparse import ArgumentParser
from lib import parser, jsondeco
import json
import sys

__author__ = "yfujieda"
__version__ = "0.1"
__date__ = "2019_10_24"


class PlasoLogpPrser:
    def __init__(self, args):
        self.plaso_path = args.CDIR_Logs
        self.sum = lib.Summary()
        self.count_trecord = args.total_record
        self.export = args.out
        self.parser = ""
        if args.p or args.timerange:
            if None is not args.timerange:
                if "-" in args.timerange:
                    print("time range option invalid")
                    sys.exit(1)
            else:
                self.target = self.target_set(args)
        else:
            self.target = None

    def count_Trecord(self):
        count = 0
        for line in open(self.plaso_path, "r", encoding="utf-8"):
            try:
                jd = json.loads(line)
                if not jd:
                    continue
                count += 1
            except json.JSONDecodeError as e:
                print(sys.exc_info())
                print(e)
                return False
        return count

    def target_set(self, args):
        target = {}
        if args.p:
            target["program"] =[]
            target["program"].append(args.p)
        else:
            target["program"] = None
        if args.timerange:
            target["timerange"] = args.t.split("-")
        else:
            target["timerange"] = None
        return target

    def analysis_log(self):
        if self.count_trecord:
            print(self.count_Trecord())
            return False
        record = 0
        for jline in jsondeco.loadJson2(self.plaso_path):
            if not jline:
                continue
            if not self.target:
                print("not set analysis options")
                # ターゲットが設定されていない場合の処理追加
                return False

            if self.target["timerange"]:
                if not self.target["timerange"][0] <= jline["timestamp"] <= self.target["timerange"][1]:
                    continue

            if self.target["program"]:
                for t in self.target["program"]:
                    p = False
                    try:
                        for string in jline["strings"]:
                            try:
                                if not string:
                                    continue
                                if t == string:
                                    print(string)
                            except KeyError:
                                print("Keyerror")
                                continue
                        if not p:
                            continue
                    except KeyError:
                        pass

            if self.export:
                with open(self.export, "a") as fd:
                    json.dump(jline, fd, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
            else:
                pass
                # print(jline)

            if 0 == self.sum.total_record % 100:
                self.sum.display_halfway()
            else:
                self.sum.add_record()


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
