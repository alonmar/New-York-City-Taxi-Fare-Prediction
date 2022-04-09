FROM continuumio/anaconda3
WORKDIR /app
RUN conda install \
    numpy \
    pandas \
    matplotlib \
    jupyterlab 

RUN conda install nodejs -c conda-forge --repodata-fn=repodata.json
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager keplergl-jupyter

COPY . /app/

CMD ["jupyter-lab","--ip=0.0.0.0","--no-browser","--allow-root"]