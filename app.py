from prometheus_client import start_http_server, Gauge
from sklearn.metrics import accuracy_score
import time
import random

# Define Prometheus metrics
accuracy_gauge = Gauge('model_accuracy', 'Accuracy of model predictions')

def get_mock_predictions():
    """Simulate predictions and labels for demo purposes."""
    y_true = [random.randint(0, 1) for _ in range(100)]
    y_pred = [random.randint(0, 1) for _ in range(100)]
    return y_true, y_pred

def monitor_model():
    while True:
        y_true, y_pred = get_mock_predictions()
        acc = accuracy_score(y_true, y_pred)
        accuracy_gauge.set(acc)
        print(f"Logged accuracy: {acc:.2f}")
        time.sleep(10)

if __name__ == "__main__":
    start_http_server(8000)  # Expose metrics at http://localhost:8000/metrics
    monitor_model()
