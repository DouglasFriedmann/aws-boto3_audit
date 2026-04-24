import boto3

REGION = "us-east-1"

def get_name_tag(tags):
    for tag in tags or []:
        if tag.get("Key") == "Name":
            return tag.get("Value")
    return None


def has_iam_profile(instance):
    return instance.get("IamInstanceProfile") is not None


def build_findings(name_tag, has_profile):
    findings = []

    if not name_tag:
        findings.append("missing_name_tag")

    if not has_profile:
        findings.append("missing_instance_profile")

    return findings if findings else ["ok"]

ec2 = boto3.client("ec2", region_name=REGION)
response = ec2.describe_instances()

instances = []

for reservation in response["Reservations"]:
    instances.extend(reservation["Instances"])

if not instances:
    print(f"No EC2 instances found in region: {REGION}.")
else:
    print(f"EC2 Audit Report - {REGION}")
    print("-" * 80)

    for instance in instances:
        instance_id = instance.get("InstanceId", "N/A")
        state = instance.get("State", {}).get("Name", "unknown")
        instance_type = instance.get("InstanceType", "unknown")

        name_tag = get_name_tag(instance.get("Tags"))
        has_profile = has_iam_profile(instance)
        findings = build_findings(name_tag, has_profile)
        
        print(f"Instance_ID: {instance_id}")
        print(f"Name: {name_tag if name_tag else '<missing>'}")
        print(f"State: {state}")
        print(f"Type: {instance_type}")
        print(f"IAM_Instance_Profile: {'yes' if has_profile else 'no'}")
        print(f"Findings: {', '.join(findings)}")
        print("-" * 80)
