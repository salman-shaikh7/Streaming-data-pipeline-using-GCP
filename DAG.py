import datetime
from airflow import models

from airflow.operators import BashOperator
from airflow.operators import PythonOperator

default_dag_args={
    "start_date": datetime.datetime(2022,1,1)
}

with models.DAG (
    dag_id = "composer_for_streaming_orchestration" ,
    schedule_interval = "@daily",
    default_args=default_dag_args,

) as dag:
    
    def gretting():

        import logging
        logging.info("Hello from gretting function")

    
    hello_from_python = PythonOperator(
                                        task_id="hello",
                                        python_callable=gretting
                                        )
    # Bash operator
    bye_from_bash = BashOperator(
                                task_id="hello",
                                bash_command="echo Goodbye."
                                        
                                )
    
    hello_from_python >> bye_from_bash
    


