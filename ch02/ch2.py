
path = "ch02/usagov_bitly_data2012-03-16-1331923249.txt"

import json

records = [json.loads(line) for line in open(path)]
records[3]["hh"]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
time_zones[:10]


def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
        return counts

counts = get_counts(time_zones)
