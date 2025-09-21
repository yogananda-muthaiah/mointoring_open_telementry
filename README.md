# mointoring_open_telementry

```
git clone <repo>
```

#### Architecture Overview
To implement monitoring effectively, a common stack combines several components working together:

* Inference API (FastAPI): The model is deployed behind an API that exposes two key endpoints—/predict (for serving predictions) and /metrics (for exposing performance and system metrics in a Prometheus-compatible format).
* Prometheus: A time-series database designed for monitoring. Prometheus periodically scrapes the /metrics endpoint, storing metrics over time so you can analyze trends and set up alert rules.
* Grafana: A visualization layer on top of Prometheus. It allows you to build dashboards to monitor accuracy, latency, drift, and business KPIs in real time. Grafana also supports alerting and integration with Slack, PagerDuty, and other tools.
* Docker Compose: To tie everything together, Docker Compose orchestrates the services (FastAPI, Prometheus, Grafana) in one environment. This makes it easy to spin up the full monitoring stack locally or in staging before moving to production.


#### Create a Python Monitoring Script
Let’s start with a simple monitoring script that logs model accuracy. For demonstration, we’ll simulate predictions and true labels instead of using a real dataset.



### Install
```
pip install -r requirements.txt
```

### Run the application
```
python app.py
```

### Docker Build
```
docker build -t model-monitor .
docker run -p 8000:8000 model-monitor
```

### Run the Docker Image
```
docker run -p 9090:9090 \
  -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus
```
Navigate to http://localhost:9090 to explore the metrics

### Run the Docker Build for Grafana
```
docker run -d -p 3000:3000 grafana/grafana
```

* Log in at http://localhost:3000 (default user: admin / admin).
* Add Prometheus as a data source (http://host.docker.internal:9090).
* Create panels for accuracy over time, latency histograms, or drift metrics.
