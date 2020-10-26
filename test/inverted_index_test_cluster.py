from mapreduce.applications.inverted_index import *
from mapreduce.api import *
import operator
import sys

### Input/Output file path
input_files = "/gcloud_mapreduce/test/input/*.txt"
output_location = "/gcloud_mapreduce/test/output/inverted_index_cluster_result.txt"

### Start testing
cluster_id = init_cluster(sys.argv[1])
result = run_mapred(input_files, map_words, inverted_index, output_location)
# destroy_cluster(cluster_id)

result.sort(key=operator.itemgetter(1))
result.reverse()
## Report
print('\nTOP 20 WORDS BY DOCUMENT LOCATION\n')
top20 = result[:20]
for word, count in top20:
    print('{}: {}'.format(word, count))