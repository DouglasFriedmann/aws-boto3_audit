import boto3

REGION = "us-east-1"

ec2 = boto3.client("ec2", region_name=REGION)

response = ec2.describe_instances()

instances = []

for reservation in response["Reservations"]:
    instance.extend(reservation["Instances"])

if not instances:
    print(f"No EC2 instances found in region: {REGION}.")
else:
    print(f"EC2 Audit Report - {REGION}")
    print("-" * 80)

    for instance in instances:
        instance_id = instance.get("InstanceId", "N/A")
        state = instance.get("State", {}).get("Name", "unknown")
        instance_type = instance.get("InstanceType", "unknown")

        tags = instance.get("Tags", [])
        name_tag = None

        for tag in tags:
            if tag.get("Key") == "Name":
                name_tag = tag.get("Value")
                break

        iam_profile = instance.get("IamInstanceProfile")

        findings = []

        if not name_tag:
            findings.append("missing_name_tag")
        
        if not iam_profile:
            findings.append("missing_istance_profile")

        if not findings:
            findings.append("ok")

        print(f"Instance_ID: {instance_id}")
        print(f"Name: {name_tag if name_tag else '<missing>'}")
        print(f"State: {state}")
        print(f"Type: {instance_type}")
        print(f"IAM_Instance_Profile: {'yes' if iam_profile else 'no'}")
        print(f"Findings: {', '.join(findings)}")
        print("-" * 80)
