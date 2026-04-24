import boto3

ec2 = boto3.client("ec2", region_name="us-east-1")

response = ec2.describe_instances()

instances = []
for reservation in response["Reservations"]:
    instancea.extend(reservation["Instances"])

if not instances:
    print("No EC2 instances found in this region.")
else:
    for instance in instances:

        instance_id = instance.get("InstanceID, N/A")
        state = instance.get("State", {}).get("Name", "unknown")
        instance_type = instance.get("InstanceType", "unknown")
        private_ip = instance.get("PrivateIpAddress", "N/A")
        public_ip = instance.get("PublicIpAddress", "N/A")

        print(f"Instance ID: {instance_id}")
        print(f"State: {state}")
        print(f"Type: {instance_type}")
        print(f"Private IP: {private_ip}")
        print(f"Public IP: {public_ip}")
        print("-" * 40)
