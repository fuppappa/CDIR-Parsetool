import json


def JsonFormat(path, data, flag):
    with open(path, flag) as fd:
        fd.write(json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': ')))

    print("s")