#!/home/devnet/devnet/DEVNET/aws/venv/bin/python

import json, boto3

region = 'us-east-1'
vpc_name = 'networking_demo'

ec2 = boto3.resource('ec2', region_name=region)
client = boto3.client('ec2')
filters = [{'Name':'tag:Name', 'Values':[vpc_name]}]
vpcs = list(ec2.vpcs.filter(Filters=filters))

for vpc in vpcs:
    response = client.describe_vpcs(
        VpcIds=[vpc.id,])
    print(json.dumps(response, sort_keys=True, indent=4))

"""
It is not so different in VPC, except it is an implicit router with a default routing
table of the local network, which in our example is 10.0.0.0/16. This implicit
router was created when we created our VPC. Any subnet that is not associated
with a custom routing table is associated with the main table.

"""