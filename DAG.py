import datetime
from airflow import models

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from google.cloud import pubsub_v1
import requests


default_dag_args={
    "start_date": datetime.datetime(2022,1,1)
}

with models.DAG (
    dag_id = "Test_DAG_1" ,
    schedule_interval = None,

    default_args=default_dag_args,

) as dag:



    def Fetch_and_publish():

        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path("myprojectid7028", "stream_topic")

        api_url="https://randomuser.me/api/"
        response = requests.get(api_url)
        if response.status_code == 200:
            data=response.json()
        else:
            data=response.status_code
        
        future = publisher.publish(topic_path, data)
        print(f"Published message ID: {future.result()}")
        return "Message published successfully"


    hello_from_bash = BashOperator(
                                task_id="Hi_task",
                                bash_command="echo HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo"       
                                )

    Fetch_and_publish_data= PythonOperator(
                                task_id='pandas_test_task',
                                python_callable=Fetch_and_publish,
                                )

    bye_from_bash = BashOperator(
                                task_id="bye_task",
                                bash_command="BYEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"       
                                )
    
    hello_from_bash >> Fetch_and_publish_data >> bye_from_bash
    
