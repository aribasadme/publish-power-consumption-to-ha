import logging
import json

from utils import publish_to_ha


log = logging.getLogger()
log.setLevel(logging.INFO)


def run(event, _):
    log.info(f"Received input event: {json.dumps(event, default=str)}")
    response = None
    for record in event["Records"]:
        if "s3" in record:
            bucket = record["s3"]["bucket"]["name"]
            key = record["s3"]["object"]["key"]
            response = publish_to_ha(bucket=bucket, key=key)
    if response:
        log.info("SUCCESS")
    else:
        log.info("ERROR. Could not connect to Home Assistant")
