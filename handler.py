import logging
import json

from utils import publish_to_ha


log = logging.getLogger()
log.setLevel(logging.INFO)


def run(event, _):
    log.info(f"Received input event: {json.dumps(event, default=str)}")
    response = None
    for sqs_records in event["Records"]:
        s3_records = json.loads(sqs_records['body'])
        for s3_record in s3_records['Records']:
            bucket = s3_record["s3"]["bucket"]["name"]
            key = s3_record["s3"]["object"]["key"]
            log.info(f"Bucket {bucket} and Key {key} retrieved successfully")
            response = publish_to_ha(bucket=bucket, key=key)
    if response:
        log.info("Data successfully published to HA")
        log.info("SUCCESS")
    else:
        log.info("ERROR. Could not connect to Home Assistant")
