import logging

import pandas as pd

from src.models.predict import PredictRequest, PredictResponse
from src.services.inference.model_loader import get_model
from src.utils.errors import UnknownCategoryError

logger = logging.getLogger(__name__)

def predict(payload: PredictRequest) -> PredictResponse:
    """
    Perform prediction using the loaded model.

    Args:
        payload (PredictRequest): Input data for prediction.

    Returns:
        PredictResponse: The predicted MPG and the input data.
    """
    model = get_model()

    # Convert input data to a DataFrame
    # input_df = pd.DataFrame([payload.model_dump()])
    input_df = pd.DataFrame([payload.dict()])

    try:
        # Perform prediction
        predicted_mpg = model.predict(input_df)[0]
    except ValueError as e:
        logger.error(f"Prediction failed due to unknown category: {e}")
        raise UnknownCategoryError("Prediction failed due to unknown category") from e

    return PredictResponse(predicted_mpg=predicted_mpg, input=payload)