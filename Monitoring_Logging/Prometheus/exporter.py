from prometheus_client import start_http_server, Counter
import time

prediction_counter = Counter(
    "prediction_total",
    "Total prediction"
)

start_http_server(8000)

while True:
    prediction_counter.inc()
    time.sleep(5)