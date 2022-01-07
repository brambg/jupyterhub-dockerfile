#jupyterhub.Dockerfile
FROM jupyterhub/jupyterhub:1.5

COPY jupyterhub_config.py /srv/jupyterhub

RUN pip install dockerspawner

RUN adduser --quiet --disabled-password guest && \
	echo guest:guest | chpasswd
