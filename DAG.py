import datetime
from airflow import models

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

import pandas as pd

from google.cloud import pubsub_v1


default_dag_args={
    "start_date": datetime.datetime(2022,1,1)
}

with models.DAG (
    dag_id = "Test_DAG_1" ,
    schedule_interval = None,

    default_args=default_dag_args,

) as dag:



    def pandas_test():

        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path("myprojectid7028", "stream_topic")

        data = "Hello, world!_NOWWW"
        data = data.encode("utf-8")
        future = publisher.publish(topic_path, data)
        print(f"Published message ID: {future.result()}")
        return "Message published successfully"


    hello_from_python = BashOperator(
                                task_id="Hi_task",
                                bash_command="python3 -m site"       
                                )

    test_pandas= PythonOperator(
                                task_id='pandas_test_task',
                                python_callable=pandas_test,
                                )

    bye_from_bash = BashOperator(
                                task_id="bye_task",
                                bash_command="pip3 list"       
                                )
    
    hello_from_python >> test_pandas>> bye_from_bash
    
