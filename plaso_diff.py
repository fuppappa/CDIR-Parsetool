#! /usr/bin/python3

from lib import json_interface, editgraph
from parsers import parser
import sys
from concurrent import futures


def seed_diff(logs):
    seed = []
    for log in json_interface.JsonloadLiner(logs):
        temp = parser.PlasoLogParser(log)
        try:
            temp.EventAnalysis()
        except AttributeError:
            print(temp.event["data_type"])
            continue
        temp.event = None
        seed.append(temp)
        del temp
    print(seed[0].event)
    print("end")
    return seed


if __name__ == "__main__":
    list1 = seed_diff(sys.argv[1])
    list2 = seed_diff(sys.argv[2])
    editgraph.diff(list1, list2,
                   editgraph.default_compare, editgraph.default_print_result)
