import boto3

REGION = "us-east-1"

ec2 = boto3.client("ec2", region_name=REGION)

response = ec2.describe_instances()

instances = []
for reservation in response["Reservations"]:
    instances.extend(reservation["Instances"])

if not instances:
    print(f"No EC2 instances found in region: {REGION}.")
else:
    for instance in instances:
        instance_id = instance.get("InstanceId", "N/A")

        iam_profile = instance.get("IamInstanceProfile")

        if iam_profile:
            print(f"{instance_id} has an IAM istance profile attached")
        else:
            print(f"{instance_id} is MISSING an IAM instance profile 🚨 ")
