class UnknownCategoryError(Exception):
    """Exception raised when an unknown category is encountered during prediction."""
    status_code = 422

class ModelLoadError(Exception):
    """Exception raised when the model fails to load from S3."""
    status_code = 503

class PredictionError(Exception):
    """Exception raised when a prediction fails."""
    status_code = 500

class InvalidInputError(Exception):
    """Exception raised when the input data is invalid."""
    status_code = 400

