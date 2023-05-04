# Data-engineering-Uber-rides-project
The final project for taxi rides dataset in New York city 2015-2022


Prequesits 
- conda
  - ``` wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh ```
  - ```bash Anaconda3-2023.03-1-Linux-x86_64.sh```
  - ```conda create -n zoomcamp python=3.9```
  - ```conda activate zoomcamp```
- Docker
  - ```sudo apt-get update && sudo apt-get install docker.io```
- Docker compose
  - ```wget https://github.com/docker/compose/releases/download/v2.17.3/docker-compose-linux-x86_64```
  - ```mv docker-compose-linux-x86_64 docker-compose```
  - ```chmod +x docker-compose```
- Postgres
  - ```conda install -c conda-forge pgcli```
- Google Cloud SDK
  - ```gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS```
- Terraform (IaC)
  - ```wget https://releases.hashicorp.com/terraform/1.4.6/terraform_1.4.6_linux_amd64.zip```
  - ```unzip terraform_1.4.6_linux_amd64.zip```
