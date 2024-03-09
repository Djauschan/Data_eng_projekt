#Python Laufzeitumgebung
FROM python:3.11.8-bookworm

WORKDIR /app

#Git runterladen für Code aus Repo
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/Djauschan/Data_eng_projekt.git .

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "webapp.py", "--server.port=8501"]