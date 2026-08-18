from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient(
    credential=DefaultAzureCredential(),
    subscription_id="ed3cde43-f0b0-44b7-89b1-8e27bc2a1fc8",
    resource_group_name="rg-ml-journey",
    workspace_name="mlw-ml-journey",
)

print("Connected to workspace:", ml_client.workspace_name)
for compute in ml_client.compute.list():
    print("Existing compute:", compute.name)