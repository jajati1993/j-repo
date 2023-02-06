import boto3

def lambda_handler(event, context):
    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Identify the instance you want to stop by using its instance ID
    instance_id = 'your_instance_id'

    # Stop the instance
    ec2.stop_instances(InstanceIds=[instance_id])

    return "Instance stopped successfully"