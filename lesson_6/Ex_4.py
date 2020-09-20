import json
import datetime

with open("acdc.json") as f:
    ac_dc = json.load(f)


def find_duration(some_dict):
    tracks = ac_dc["album"]["tracks"]["track"]
    duration_of_all = 0
    for track in tracks:
        duration_of_all += int(track["duration"])
    return duration_of_all


print(datetime.timedelta(seconds=find_duration(ac_dc)))
