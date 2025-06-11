from dask.distributed import Client, LocalCluster

def create_local_cluster(n_workers=4, threads_per_worker=2, memory_limit='4GB'):
    cluster = LocalCluster(
    n_workers=n_workers,
    threads_per_worker=threads_per_worker,
    memory_limit=memory_limit  
    )
    client = Client(cluster)
    print(f"Local cluster created with {n_workers} workers, \
          {threads_per_worker} threads per worker, and {memory_limit} memory limit.")
    print(f"Dashborad link: {client.dashborad_link}")
    return client