# Configuration file for JupyterHub
# see https://github.com/jupyterhub/jupyterhub-deploy-docker/blob/master/jupyterhub_config.py
import os

c = get_config()

# Spawn single-user servers as Docker containers
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# Spawn containers from this image
c.DockerSpawner.image = 'brambdocker/jupyter-julia:0.1'

c.DockerSpawner.extra_create_kwargs.update({ 'command': 'start-singleuser.sh' })

# Remove containers once they are stopped
c.DockerSpawner.remove_containers = True

# network_name = 'mynetwork'
# c.DockerSpawner.use_internal_ip = True
# c.DockerSpawner.network_name = network_name

# # User containers will access hub by container name on the Docker network
# c.JupyterHub.hub_ip = 'jupyterhub'
# c.JupyterHub.hub_port = 8080