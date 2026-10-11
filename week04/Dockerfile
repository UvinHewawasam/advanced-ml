FROM public.ecr.aws/lambda/python:3.12 AS builder

# Install Poetry
ENV POETRY_VERSION=2.1.1 POETRY_NO_INTERACTION=1 POETRY_VIRTUALENVS_CREATE=false
RUN pip install "poetry==$POETRY_VERSION"

# Copy the pyproject.toml and poetry.lock files to the container
WORKDIR ${LAMBDA_TASK_ROOT}
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry install --only main --no-root --no-interaction --no-ansi

FROM public.ecr.aws/lambda/python:3.12

COPY --from=builder /var/lang/lib/python3.12/site-packages/ /var/lang/lib/python3.12/site-packages/

# Copy the application code to the container
WORKDIR ${LAMBDA_TASK_ROOT}
COPY . .

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD ["handler.handler"]