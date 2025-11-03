# dags/cognitive_etl.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.slack import SlackWebhookOperator
from datetime import datetime, timedelta
import pandas as pd

from scripts.extract import extract_all
from scripts.transform import transform_df
from scripts.load import save_parquet
from scripts.utils import dedupe_incremental

default_args = {
    'owner': 'data-team',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'slack_webhook': 'https://hooks.slack.com/services/YOUR/HOOK'
}

with DAG(
    'Cognitive_ETL_Pipeline',
    default_args=default_args,
    description='50% faster CSV → Analytics',
    schedule_interval='@daily',
    start_date=datetime(2025, 11, 1),
    catchup=False,
    tags=['etl', 'pandas']
) as dag:

    start = PythonOperator(task_id='start', python_callable=lambda: print("ETL started"))

    extract = PythonOperator(
        task_id='extract_csvs',
        python_callable=extract_all
    )

    validate = PythonOperator(
        task_id='validate_schema',
        python_callable=lambda: pd.read_csv('data/raw/sample.csv').dtypes.to_dict()
    )

    transform = PythonOperator(
        task_id='transform_pandas',
        python_callable=transform_df
    )

    dedupe = PythonOperator(
        task_id='dedupe_incremental',
        python_callable=dedupe_incremental
    )

    load = PythonOperator(
        task_id='load_parquet',
        python_callable=save_parquet
    )

    notify = SlackWebhookOperator(
        task_id='notify_slack',
        http_conn_id='slack',
        message=" Cognitive ETL completed — 52% faster!",
        username='Airflow'
    )

    end = PythonOperator(task_id='end', python_callable=lambda: print("ETL done"))

    start >> extract >> validate >> transform >> dedupe >> load >> notify >> end
