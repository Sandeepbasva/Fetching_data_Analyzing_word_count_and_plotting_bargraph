'''
This program is to read data from .txt file and analyzing the top 10 words
'''

import re

with open('data.txt','rb') as data:
    Fetched_data = data.readlines()

# print Fetched_data[0].lower()
# print type(Fetched_data)


# Cleaning the dataset
with open('stopwords.txt','rb') as stop:
    stopwords = stop.readlines()


stop_new_words = [word.rstrip() for word in stopwords]

String = ""
for line in Fetched_data:
    String+= re.sub('[^a-zA-Z0-9-_*.]', ' ', line.lower())


# Fetched_data =re.sub('[^a-zA-Z0-9-_*.]', ' ',Fetched_data[0].lower())
Fetched_data = ''.join([i for i in String if not i.isdigit()])

# Spliting into words
Split_words = [word for word in Fetched_data.split() if word not in stop_new_words ]


# Getting frequency of words
dist = {}
for word in Split_words:
    if word in dist:
        dist[word]+=1
    else:
        dist[word]=1

# print dist
# print dict(sorted(dist.iteritems(), key=operator.itemgetter(1), reverse=True)[:10])

from collections import Counter
new_data_set = dict(Counter(dist).most_common(10))




titles = [titles for titles,_ in new_data_set.items()]
weights = [weights for _,weights in new_data_set.items()]
import matplotlib.pyplot as plt
import numpy as np
y_pos = np.arange(len(titles))
plt.bar(y_pos,weights, align="center", alpha=0.5)
plt.xticks(y_pos,titles)
plt.tick_params(axis='x', which='major', pad=20)
plt.ylabel("Word frequency")
plt.title("Final Results")
plt.show()







'''
import pickle
with open('filename.pickle', 'wb') as handle:
    pickle.dump(dist, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('filename.pickle', 'rb') as handle:
    b = pickle.load(handle)
print  b
'''
