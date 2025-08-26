import boto3
import os
import pytest

# Lee las credenciales de las variables de entorno
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

@pytest.fixture
def s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )

def test_upload_file(s3_client, tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("Este es un test para S3")

    # Subir archivo
    s3_client.upload_file(str(test_file), BUCKET_NAME, "test.txt")

    # Verificar que existe
    response = s3_client.list_objects_v2(Bucket=BUCKET_NAME, Prefix="test.txt")
    assert "Contents" in response
