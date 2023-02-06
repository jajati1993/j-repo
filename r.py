 import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    ec2.stop_instances(InstanceIds=['<instance_id>'])
    print('Stopped instance: <instance_id>')