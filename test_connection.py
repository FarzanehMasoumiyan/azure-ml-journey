from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient(
    credential=DefaultAzureCredential(),
    subscription_id="e",
    resource_group_name="rg-ml-journey",
    workspace_name="mlw-ml-journey",
)

print("Connected to workspace:", ml_client.workspace_name)
for compute in ml_client.compute.list():
    print("Existing compute:", compute.name)
