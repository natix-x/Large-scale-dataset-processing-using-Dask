from dask.distributed import Client, LocalCluster 

def get_local_cluster(n_workers=4, threads_per_worker=2, memory_limit='4GB'):
    try:
        client = Client.current()
        close_local_cluster(client)
    except ValueError:
        pass

    cluster = LocalCluster(
        n_workers=n_workers,
        threads_per_worker=threads_per_worker,
        memory_limit=memory_limit
    )
    client = Client(cluster)

    print(f"Local cluster created with {n_workers} workers, "
          f"{threads_per_worker} threads per worker, and {memory_limit} memory limit.")
    print(f"Dashboard link: {client.dashboard_link}")
    return client


def close_local_cluster(client):
    if client:
      cluster = client.cluster
      client.close()
      if cluster:
            cluster.close()