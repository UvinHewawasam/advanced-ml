import json
from src.models.predict import PredictRequest
from src.services.inference.inference_service import predict

def handler(event, context):

    event_body = event.get("body")
    predict_request = PredictRequest.model_validate(event_body)

    try:
        predict_response = predict(predict_request)
    except Exception as e:
        return {
            "statusCode": getattr(e, "status_code", 500),
            "body": json.dumps({"error": str(e)})
        }

    response = {
        "statusCode": 200,
        "body": json.dumps(predict_response),
    }

    return response
