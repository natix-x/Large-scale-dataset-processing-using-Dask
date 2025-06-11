from dask.distributed import Client
from dask_jobqueue import SLURMCluster
import json
import os

def get_slurm_cluster(config_file='slurm_config.json'):

    script_dir = os.path.dirname(os.path.abspath(__file__))  
    config_path = os.path.join(script_dir, config_file) 

    with open(config_path, 'r') as f:
        config = json.load(f)

    try:
        client = Client.current()
        close_slurm_cluster(client)
    except ValueError:
        pass

    cluster = SLURMCluster(
        queue=config.get("queue"),
        account=config.get("account"),
        cores=config.get("cores"),
        memory=config.get("memory"),
        walltime=config.get("walltime"))
    cluster.scale(n=100)
    client = Client(cluster)
    print(f"Dashboard: {client.dashboard_link}")
    return client



def close_slurm_cluster(client):
    if client:
      cluster = client.cluster
      client.close()
      if cluster:
            cluster.close()