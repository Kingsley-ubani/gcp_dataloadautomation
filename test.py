"parameters": {
        "inputFilePattern": "gs://ubani_project2/user.csv",
        "JSONPath": "gs://bkt_dataflow_proj/bq.json",
        "outputTable": "future-cat-426023-k3:user_data.users",
        "bigQueryLoadingTemporaryDirectory": "gs://bkt_dataflow_proj",
        "javascriptTextTransformGcsPath": "gs://bkt_dataflow_proj/udf.js",
        "javascriptTextTransformFunctionName": "transform"
    }