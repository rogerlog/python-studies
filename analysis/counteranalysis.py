from collections import defaultdict
from collections import Counter
import json

path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
records[0]['tz']

print (records[0]['tz'])

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones[:10])

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts

counts = get_counts(time_zones)
print (counts['America/New_York'])

print (len(time_zones))

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

print (top_counts(counts))

counts = Counter(time_zones)
print (counts.most_common(10))
