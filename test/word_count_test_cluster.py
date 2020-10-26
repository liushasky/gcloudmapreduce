from mapreduce.applications.word_count import *
from mapreduce.api import *
import sys
import operator
### Input/Output file path
input_files = "/gcloud_mapreduce/test/input/*.txt"
output_location = "/gcloud_mapreduce/test/output/word_count_cluster_result.txt"

### Start testing
cluster_id = init_cluster(sys.argv[1])
result = run_mapred(input_files, map_words, count_words, output_location)
# destroy_cluster(cluster_id)

result.sort(key=operator.itemgetter(1))
result.reverse()
## Report
print('\nTOP 20 WORDS BY FREQUENCY\n')
top20 = result[:20]
for word, count in top20:
    print('{}: {}'.format(word, count))