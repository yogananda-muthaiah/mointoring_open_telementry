# mointoring_open_telementry

#### Architecture Overview
To implement monitoring effectively, a common stack combines several components working together:

* Inference API (FastAPI): The model is deployed behind an API that exposes two key endpoints—/predict (for serving predictions) and /metrics (for exposing performance and system metrics in a Prometheus-compatible format).
* Prometheus: A time-series database designed for monitoring. Prometheus periodically scrapes the /metrics endpoint, storing metrics over time so you can analyze trends and set up alert rules.
* Grafana: A visualization layer on top of Prometheus. It allows you to build dashboards to monitor accuracy, latency, drift, and business KPIs in real time. Grafana also supports alerting and integration with Slack, PagerDuty, and other tools.
* Docker Compose: To tie everything together, Docker Compose orchestrates the services (FastAPI, Prometheus, Grafana) in one environment. This makes it easy to spin up the full monitoring stack locally or in staging before moving to production.


#### Create a Python Monitoring Script
Let’s start with a simple monitoring script that logs model accuracy. For demonstration, we’ll simulate predictions and true labels instead of using a real dataset.



```
pip install -r requirements.txt
```

```
python app.py
```


```
docker build -t model-monitor .
docker run -p 8000:8000 model-monitor
```
