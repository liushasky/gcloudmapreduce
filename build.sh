docker build . -t gcr.io/iu-e516-assignment3/mapreduce-kube-cluster
docker push gcr.io/iu-e516-assignment3/mapreduce-kube-cluster

kubectl create -f head.yml
kubectl create -f worker.yml

kubectl logs ray-head

kubectl exec -it ray-head bash
python3 /mapreduce/test/unit_test_cluster.py 10.4.0.22:6379

kubectl delete service ray-head
kubectl delete pod ray-head
kubectl delete deploy ray-worker