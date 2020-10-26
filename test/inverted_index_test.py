from mapreduce.applications.inverted_index import *
from mapreduce.api import *
import operator

### Input/Output file path
input_files = "/Users/shaliu/gcloud_mapreduce/test/input/*.txt"
output_location = "/Users/shaliu/gcloud_mapreduce/test/output/word_count_result.txt"

### Start testing
cluster_id = init_cluster('localhost:9008')
result = run_mapred(input_files, map_words, inverted_index, output_location)
destroy_cluster(cluster_id)

result.sort(key=operator.itemgetter(1))
result.reverse()
## Report
print('\nTOP 20 WORDS BY DOCUMENT LOCATION\n')
top20 = result[:20]
for word, count in top20:
    print('{}: {}'.format(word, count))