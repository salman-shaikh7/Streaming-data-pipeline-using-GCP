# Intial planned flow for streaming ETL pipeline

![alt text](Pipeline.png)



# Login 

Exceuting these command through wsl terminal

```bash
gcloud init
gcloud auth login
```

Set project id 

```bash

gcloud config set project myprojectid7028 
```

Enable cloud composer API

```bash
gcloud services enable composer.googleapis.com
```

Create Env

```bash
gcloud composer environments create my-composer-env \
    --location us-central1 \
    --image-version composer-3-airflow-2.9.1-build.7

```

To Deploy lets copy DAG.py file dags folder in composer enviornment.

```bash
gsutil cp DAG.py gs://us-central1-my-composer-env-844eed3e-bucket/dags
```