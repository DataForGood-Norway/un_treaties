FROM continuumio/miniconda3

RUN conda create -n env python=3.7
RUN echo "source activate env" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH

RUN pip install --upgrade pip

COPY . /app
WORKDIR /app

RUN  python -m pip install -e /app
RUN pip install connexion[swagger-ui]

#ENTRYPOINT [ "python" ]
#CMD [ "un_treaties/rest_api/api.py" ]
CMD [ "un_serve" ]