from lib import json_interface
import sys

print("hogs")
data_types = {}
if __name__ == '__main__':

    for f in json_interface.JsonloadLiner(sys.argv[2]):
        data_type = f["data_type"]
        if data_type not in data_types:
            data_types[data_type] = 1
        else:
            data_types[data_type] += 1

    print(data_types)
