from scripts.ec2_audit_report import get_name_tag, has_iam_profile, build_findings

def test_get_name_tag_present():
    tags = [{"Key": "Name", "Value": "web"}]
    assert get_name_tag(tags) == "web"

def test_get_name_tag_missing():
    tags = []
    assert get_name_tag(tags) is None

def test_has_iam_profile_true():
    instance = {"IamInstanceProfile": {"Arn": "test"}}
    assert has_iam_profile(instance) is True

def test_has_iam_profile_false():
    instance = {}
    assert has_iam_profile(instance) is False

def test_build_findings_missing_both():
    result = build_findings(None, False)
    assert "missing_name_tag" in result
    assert "missing_instance_profile" in result


def test_build_findings_ok():
    result = build_findings("web", True)
    assert result == ["ok"]
