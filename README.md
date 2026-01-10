# Rick & Morty DevOps Project 🚀

## 📌 Project Overview
This project started as a **Python data exporter** that fetches characters from the public  
**Rick and Morty API**, filters them, and exports the results to a CSV file.

The project was later **extended into a full DevOps pipeline**, including:
- Flask web application
- Docker containerization
- Kubernetes deployment (Minikube)
- Helm chart for deployment management

---

## 🎯 Project Goals
- Practice Python API consumption and data processing
- Package an application using Docker
- Deploy the application to Kubernetes
- Manage Kubernetes resources using Helm
- Expose the service locally and verify functionality via browser

---

## 🛠 Technologies Used
- Python 3.12
- Flask
- requests
- Docker
- Kubernetes (Minikube)
- Helm
- Git & GitHub
- VS Code

---

## 📁 Project Structure
```text
rick-morty-devops/
├── app/
│   ├── api.py              # Flask application
│   ├── fetcher.py          # Fetches and filters characters from the API
│   ├── __init__.py
│   ├── templates/
│   │   └── index.html      # Frontend page
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── giphy.gif
│   └── Dockerfile
│
├── data/
│   └── characters.csv      # Generated output file
│
├── helm/
│   └── rick-morty/
│       ├── templates/
│       │   ├── deployment.yaml
│       │   └── service.yaml
│       ├── values.yaml
│       ├── Chart.yaml
│       └── _helpers.tpl
│
├── requirements.txt
├── .gitignore
└── README.md
