from fastapi import FastAPI
from prometheus_client import Counter, Histogram, CONTENT_TYPE_LATEST, generate_latest
from fastapi.responses import Response
import mlflow.pyfunc
import pandas as pd
import time

from fastapi import FastAPI
import mlflow.pyfunc
import pandas as pd
import time

from prometheus_client import Counter, Histogram

app = FastAPI()

model = mlflow.pyfunc.load_model(
    "runs:/5ba660299c6543919722377984e4102c/logistic_regression_model"
)

REQUEST_COUNT = Counter(
    "prediction_requests_total",
    "Total prediction requests"
)

REQUEST_LATENCY = Histogram(
    "prediction_latency_seconds",
    "Prediction latency"
)

@app.post("/predict")
def predict(data: dict):

    REQUEST_COUNT.inc()

    start = time.time()

    df = pd.DataFrame(data)

    prediction = model.predict(df)

    REQUEST_LATENCY.observe(time.time() - start)

    return {
        "prediction": prediction.tolist()
    }


@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )