# Data-engineering-taxi-rides-project
The final project for taxi rides dataset in New York city 2015-2022
## Description 
In this dataset there are taxi rides data in New York city. I tried to find out the distribution of average taxi type ( green/yellow ) used by the taxi passengers and then in the second step I wanted to figure out the diveristy of most pickup zones in the city. Below is the link for the dashboard report, it might stop working if my GCP free trial expires.

<img width="1168" alt="image" src="https://user-images.githubusercontent.com/21027044/236313809-c7d5cb18-1a75-49b5-a8bb-0783b5374413.png">


### Technologies & Prerequisite 
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
- Prefect ( pipelines )


### Workflow orchestration
 - I'm using Prefect deployment schedule via cli
  - ```prefect deployment build etl_web_to_gcs.py:etl_parent_flow -n " Paramterized ETL flow"  --cron “0 0 * * *” -a```
  
### Tranformation ( Dbt )
- Transform taxi data using `dbt` tool using SQL
  - inside dbt directory ```dbt init```
  - change `profile` that match your `profiles.yml` inside dbt_project.yml config file
  - Test the config by executing `dbt debug`
  - Run model ```dbt run --m <model-name>```
  - Add some tests using dbt schema that guarantees the data contraints
  ```dbt test --select <model-name>```
    - column_name : `tripid`
    - testing : `unique`, `not_null`
    - column_name : `Pickup_locationid`
    - testing : `relationships` with `taxi_zone_lookup` on field `locationid`
    - column_name : `Payment_type`
    - testing : only `accepted_values` defined in the project config var `payment_type_values`

### Visualization ( looker )
**DEMO**
- https://lookerstudio.google.com/u/0/reporting/6954ac54-0788-4f49-b02b-1e9cd9d86118/page/kBCPD
    
