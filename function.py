from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "prj-poc-001"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
    "jobName": "bq-load",  # Provide a unique name for the job
   "parameters": {
        "inputFilePattern": "gs://ubani_project2/user.csv",
        "JSONPath": "gs://bkt_dataflow_proj/bq.json",
        "outputTable": "future-cat-426023-k3:user_data.users",
        "bigQueryLoadingTemporaryDirectory": "gs://bkt_dataflow_proj",
        "javascriptTextTransformGcsPath": "gs://bkt_dataflow_proj/udf.js",
        "javascriptTextTransformFunctionName": "transform"
    }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)
