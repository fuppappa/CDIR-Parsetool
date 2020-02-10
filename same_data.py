import json


def same_data_report(base, target):
    same = []
    diff = []
    for base_i in base:
        for target_i in target:
            if base_i != target_i:
                continue
            same.append(base_i)
    print(same)

