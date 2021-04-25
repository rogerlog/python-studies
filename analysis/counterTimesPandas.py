import pandas as pd
from pandas import DataFrame, Series
import json

import matplotlib
import matplotlib.pyplot as plt

path = 'analysis/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]

frame = DataFrame(records)
print (frame)
print (frame['tz'][:10])

tz_counts = frame['tz'].value_counts()
print (tz_counts[:10])

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])
tz_counts[:10].plot(kind='barh', rot=0)

frame['a'][1]
frame['a'][50]
frame['a'][51]

plt.show()

results = Series([x.split()[0] for x in frame.a.dropna()])
print(results[:5])
print(results.value_counts()[:8])

results.value_counts()[:8]
cframe = frame[frame.a.notnull()]

operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows', 'Not Windows')
operating_system[:5]

by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
agg_counts[:10]

indexer = agg_counts.sum(1).argsort()
indexer[:10]

count_subset = agg_counts.take(indexer)[-10:]
count_subset

#pg26
count_subset.plot(kind='barh', stacked=True)
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)


