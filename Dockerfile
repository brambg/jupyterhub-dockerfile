#jupyterhub.Dockerfile
FROM jupyterhub/jupyterhub:2.3.0

COPY jupyterhub_config.py /srv/jupyterhub

RUN pip install dockerspawner

RUN adduser --quiet --disabled-password guest && \
	echo guest:guest | chpasswd
