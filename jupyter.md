

podman run -it --rm -p 8888:8888 --user root -e GRANT_SUDO=yes -v "${PWD}":/home/jovyan/work quay.io/jeani/jupytergis-notebook

podman run -it --rm -p 8888:8888 --user root -e GRANT_SUDO=yes -v "${PWD}":/home/jovyan/work quay.io/jupyter/datascience-notebook

podman run -it --rm -p 8888:8888 --user root -e GRANT_SUDO=YES -v "${PWD}":/home/jovyan/work quay.io/bedata/jupyterlab/qgis/base
