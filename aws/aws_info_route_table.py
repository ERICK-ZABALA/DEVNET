#!/home/devnet/devnet/DEVNET/aws/venv/bin/python

import json
import boto3

region = 'us-east-1'
vpc_name = 'networking_demo'

ec2 = boto3.resource('ec2', region_name=region)
client = boto3.client('ec2')
response = client.describe_route_tables()

print(json.dumps(response['RouteTables'][0], sort_keys=True, indent=4))
