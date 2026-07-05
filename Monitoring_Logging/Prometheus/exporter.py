from prometheus_client import Counter, start_http_server
import time

prediction_counter = Counter(
    "prediction_total",
    "Total predictions processed by the model exporter"
)

if __name__ == "__main__":
    start_http_server(8000)
    while True:
        prediction_counter.inc()
        time.sleep(5)