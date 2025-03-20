import mlflow
print("printing tracking URI scheme below")
print(mlflow.get_artifact_uri())
print("\n")

mlflow.set_tracking_uri("http://localhost:5000")
print("printing tracking URI scheme below")
print(mlflow.get_tracking_uri())
print("\n")
