import boto3

ec2 = boto3.client("ec2", region_name="us-east-1")

response = ec2.describe_instances()

found = False

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        found = True
        instance_id = instance["InstanceID"]
        state = instance["State"]["Name"]
        instance_type = instance["InstanceType"]

        print(instance["InstanceID"], instance["State"]["Name"])

if not found:
    print("No EC2 instances found in this region.")
