# Adicionar um cálculo de média semanal/mensal.

# Gerar um ranking de “dias mais produtivos”.

# Enviar notificações (ex: via Telegram) com o resumo diário.

# Integrar com APIs de sistema (Windows/macOS/Linux) pra medir tempo real de sessão.

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from scripts.data_extract import get_data
from scripts.data_transform import create_log
from scripts.data_vis import create_graphs
from scripts.data_load import git_commit_push

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
}

with DAG(
    dag_id="activity_pipeline",
    default_args=default_args,
    description='Pipeline completo de Dados',
    start_date=datetime(2025, 10, 17),
    catchup=False,
    tags=['Pipeline', 'Portfolio']
) as dag:

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=get_data
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=create_log
    )

    visualize_task = PythonOperator(
        task_id="data_vis",
        python_callable=create_graphs
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=git_commit_push
    )

    extract_task >> transform_task >> visualize_task >> load_task

# test a f*cking commit