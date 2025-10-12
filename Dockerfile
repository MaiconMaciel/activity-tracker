# Imagem base
FROM python:3.11-slim

# Variáveis de ambiente do Airflow
ENV AIRFLOW_HOME=/app/airflow
ENV PYTHONUNBUFFERED=1

# Atualiza o apt e instala dependências do sistema
RUN apt-get update && apt-get install -y \
    git \
    ssh \
    libfreetype6-dev \
    libpng-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Cria diretório de trabalho
WORKDIR /app

# Copia arquivos do projeto
COPY . .

# Instala requirements do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Instala Apache Airflow
# Usando constraint para compatibilidade com Python 3.12
RUN AIRFLOW_VERSION=2.8.3 \
    && PYTHON_VERSION=3.11 \
    && pip install "apache-airflow[postgres,celery,ssh]==${AIRFLOW_VERSION}" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"


# Cria diretórios para logs e gráficos
RUN mkdir -p ./logs ./graphs

# Comando padrão para iniciar o container (Airflow webserver + scheduler)
# Pode ajustar depois se quiser rodar só seu script
CMD ["airflow", "standalone"]
