# Build Docker images and push down to google cloud repository; 
docker build -t gcr.io/iu-e516-assignment3/mapreduce-kube-cluster . 

# Master pod pull Docker images from the google container repository
docker push gcr.io/iu-e516-assignment3/mapreduce-kube-cluster

# create master pod
kubectl create -f head.yml

# create workers pods
kubectl create -f worker.yml

# view logs of master pod to get the IP address of master pod
kubectl logs ray-head

# sshing into VMs.
kubectl exec -it ray-head bash

# test-cases for launching VMs: testing word count function and inverted index function in mapreduce 

python3 /gcloud_mapreduce/test/word_count_test_cluster.py 10.4.1.26:6379
python3 /gcloud_mapreduce/test/inverted_index_test_cluster.py 10.4.1.26:6379

# VMs must be launched dynamically when needed, and terminated when not required.
# all VMs are terminated at the end of each experiment.
kubectl delete service ray-head
kubectl delete pod ray-head
kubectl delete deploy ray-worker