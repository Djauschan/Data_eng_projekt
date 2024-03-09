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




HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "webapp.py", "--server.port=8501", "--server.address=0.0.0.0"]