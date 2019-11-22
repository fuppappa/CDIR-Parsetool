import json
import sys
from argparse import ArgumentParser

__author__ = "yfujieda"
__version__ = "0.1"
__date__ = "2019_7_2"


class JsonConverter:
    def __init__(self, jsn_path, export_path):
        self.jsn_path = jsn_path
        self.export_path = export_path

    def loadJson(self):
        try:
            with open(self.jsn_path, 'r') as fd:
                data = json.load(fd)
        except json.JSONDecodeError as e:
            print(sys.exc_info())
            print(e)
            return False
        return data

    def exportJson(self, data, flag):
        try:
            with open(self.export_path, flag) as fd:
                json.dump(data, fd, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
        except json.JSONDecodeError as e:
            print(sys.exc_info())
            print(e)
            return False


def JsonShaping(res, out):
    JsonConv = JsonConverter(res, out)
    data = JsonConv.loadJson()

    if not data:
        print("EROOR: failed imoprt json file [{}] ....".format(JsonConv.jsn_path))
        print("please try it to Shaping_Json2 method")

        return False

    if not JsonConv.exportJson(data, "w"):
        print("convert failed. File may be invalid")

        return False


def JsonShapingLiner(res, out):
    with open(out, "a") as fd:

        for line in open(res, "r", encoding="utf-8"):
            jd = json.loads(line)
            if jd == "null":
                continue
            json.dump(jd, fd, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))


def JsonloadLiner(res):
    for line in open(res, "r", encoding="utf-8"):
        try:
            jd = json.loads(line)
            if jd == "null":
                continue
        except json.JSONDecodeError as e:
            print("*****Error******")
            print(sys.exc_info())
            print(e)
            return False
        yield jd


def get_args():
    parser = ArgumentParser()

    parser.add_argument("arg1", help="[sourcefile.json]")
    parser.add_argument("arg2", help="outfile.json")

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = get_args()

    JsonShapingLiner(args.arg1, args.arg2)
