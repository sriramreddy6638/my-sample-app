import boto3
import time

# Initialize AWS clients
ecs_client = boto3.client('ecs', region_name='ap-south-1', aws_access_key_id='YOUR_AWS_ACCESS_KEY_ID', aws_secret_access_key='YOUR_AWS_SECRET_ACCESS_KEY')
ecr_client = boto3.client('ecr', region_name='ap-south-1')
 
# Create or Update ECS Service with Docker image
def deploy_to_ecs():
    cluster_name = 'sample-ecs'
    service_name = 'sample-ecs'
    task_definition_name = 'sample-ecs'

    try:
        # Register task definition
        response = ecs_client.register_task_definition(
            family=task_definition_name,
            containerDefinitions=[
                {
                    'name': 'my-app',
                    'image': '307546041091.dkr.ecr.ap-south-1.amazonaws.com/my-app',
                    'memory': 512,
                    'cpu': 256,
                    'essential': True,
                    'portMappings': [
                        {
                            'containerPort': 80,
                            'hostPort': 80
                        }
                    ]
                }
            ]
        )

        # Update ECS service
        ecs_client.update_service(
            cluster=cluster_name,
            service=service_name,
            taskDefinition=task_definition_name
        )
        
        print("Deployment to ECS succeeded!")
    except Exception as e:
        print(f"Error deploying to ECS: {e}")

if __name__ == "__main__":
    deploy_to_ecs()
