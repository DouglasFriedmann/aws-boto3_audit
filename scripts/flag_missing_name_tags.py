import boto3

REGION = "us-east-1"

ec2 = boto3.client("ec2", region_name=REGION)

response = ec2.describe_instances()

instances = []
for reservation in response["Reservations"]:
    instances.extend(reservation["Instances"])

if not instances:
    print(f"No EC2 intances found in region: {REGION}.")
else:
    for instance in instances:
        instance_id = instance.get("InstanceId", "N/A")
        tags = instance.get("Tags", [])

        name_tag = None

        for tag in tags:
            if tag.get("Key") == "Name":
                name_tag = tag.get("Value")
                break

        if name_tag:
            print(f"{instance_id} has Name tag:{name_tag}")
        else:
            print(f"{instance_id} is missing a Name tag")

