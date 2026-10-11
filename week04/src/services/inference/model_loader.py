import io
import logging

import boto3
import joblib
from botocore.exceptions import BotoCoreError, ClientError

from src.config import MODEL_BUCKET_NAME, MODEL_OBJECT_KEY
from src.utils.errors import ModelLoadError

logger = logging.getLogger(__name__)

_model = None
_s3_client = None

def get_model():
    global _model
    if _model is not None:
        return _model

    logger.info(
        "Cold start: Loading model from S3 bucket '%s' with key '%s'",
        MODEL_BUCKET_NAME, MODEL_OBJECT_KEY
    )

    if _model is None:
        try:
            s3_client = _get_s3_client()
            response = s3_client.get_object(Bucket=MODEL_BUCKET_NAME, Key=MODEL_OBJECT_KEY)
            model_data = response["Body"].read()
            buffer = io.BytesIO(model_data)
            _model = joblib.load(buffer)
        except (BotoCoreError, ClientError) as e:
            logger.error(f"Failed to load model from S3: {e}")
            raise ModelLoadError("Failed to load model from S3") from e
        except Exception as e:
            logger.error(f"Unexpected error while loading model: {e}")
            raise ModelLoadError("Unexpected error while loading model") from e

    logger.info("Model loaded successfully from S3 and cached for this execution environment") 
    return _model

def _get_s3_client():
    global _s3_client
    if _s3_client is None:
        _s3_client = boto3.client("s3")
    return _s3_client