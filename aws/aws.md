# AWS

pip install awscli
(venv) devnet@PC1 ~/devnet/DEVNET/aws $ aws --version
aws-cli/1.29.40 Python/3.11.4 Linux/5.15.90.1-microsoft-standard-WSL2 botocore/1.31.40

+ Create an account AIM with programmatic access
you get:
user, account key, secret access key

$ aws configure 

AWS Access Key ID [None]: <key>
AWS Secret Access Key [None]: <secret>
Default region name [None]: us-east-1
Default output format [None]: json

$ pip install boto3

(venv) devnet@PC1 ~/devnet/DEVNET/aws $ python
Python 3.11.4 (main, Jun  7 2023, 10:13:09) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import boto3
>>> exit()

Regions available to you via SDK:

$ aws ec2 describe-regions

We can check the AZs in a Region in the AWS CLI:

$ aws ec2 describe-availability-zones --region us-east-1

+ The IAM service, https://aws.amazon.com/iam/, is the service that enables us to manage access to AWS services and resources securely.

+ Amazon Resource Names (ARNs), https://docs.aws.amazon.com/
general/latest/gr/aws-arns-and-namespaces.html, uniquely identify AWS resources across all of AWS. These resource names are important when we need to identify a service, such as DynamoDB and API Gateway, that needs access to our VPC resources.

+ Amazon Elastic Compute Cloud (EC2), https://aws.amazon.com/ec2/, is the service that enables us to obtain and provision compute capacities, such as Linux and Windows instances, via AWS interfaces. We will use EC2 instances throughout this chapter in our examples.

Virtual private cloud, AWS launch AWS resources in a virtual network dedicated to the customer's account. It is truly a customizable network that allows you to define your own IP address range, add and delete subnets, create routes, add
VPN gateways, associate security policies, connect EC2 instances to your own data center, and much more.

AWS:Region us-east-1
- VPC: 10.0.0.0/16 # when vpc is created exist an implicit GW
    Implicit GW
        - Private Subnet: 10.0.1.0/24
        AZ: us-east-1b
        - Private Subnet: 10.0.2.0/24
        AZ: us-east-1b
        - Public Subnet: 10.0.0.0/24    --- Internet Gateway
        AZ: us-east-1a

# Security Group

A security group is a stateful virtual firewall that controls inbound and outbound access to resources. Most of the time, we use a security group as a way to limit public access to our EC2 instance. The current limitation is 500 security groups in
each VPC. Each security group can contain up to 50 inbound and 50 outbound rules.

Network access control lists (ACLs) are an additional layer of security that is
stateless. Each subnet in the VPC is associated with a network ACL. Since an ACL
is stateless, you will need to specify both inbound and outbound rules.
The important differences between security groups and ACLs are as follows:
• Security groups operate at the network interface level, whereas ACLs
operate at the subnet level.
• For a security group, we can only specify allow rules and not deny rules,
whereas ACLs support both allow and deny rules.
• A security group is stateful so return traffic is automatically allowed; return
traffic in ACLs needs to be specifically allowed.

# Elastic IP

An Elastic IP (EIP) is a way to use a public IPv4 address that's reachable from the
internet.

An EIP can be dynamically assigned to an EC2 instance, network interface, or other
resources. A few characteristics of an EIP are as follows:
• An EIP is associated with the account and is region-specific. For example, an
EIP in us-east-1 can only be associated with resources in us-east-1.
• You can disassociate an EIP from a resource, and re-associate it with a
different resource. This flexibility can sometimes be used to ensure high
availability. For example, you can migrate from a smaller EC2 instance to a
larger EC2 instance by reassigning the same IP address from the small EC2
instance to the larger one.
• There is a small hourly charge associated with EIPs.
 # NAT Gateway 
 This is where a NAT gateway can help, by allowing the hosts in the private subnet
temporary outbound access by performing NAT. This operation is similar to port
address translation (PAT), which we normally perform on the corporate firewall. To
use an NAT gateway, we can perform the following steps:
1. Create an NAT gateway in a subnet with access to the internet gateway via
the AWS CLI, Boto3 library, or AWS console. The NAT gateway will need to
be assigned an EIP.
2. Point the default route in the private subnet to the NAT gateway.
3. The NAT gateway will follow the default route to the internet gateway for
external access.