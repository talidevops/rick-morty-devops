# Rick & Morty DevOps Project 🚀

## 📌 Project Overview
This project started as a **Python data exporter** that fetches characters from the public  
**Rick and Morty API**, applies filtering logic, and exports the results to a CSV file.

The project was later **extended into a full DevOps pipeline**, including:
- Flask web application
- Docker containerization
- Kubernetes deployment using Minikube
- Helm chart for deployment management
- Public exposure using ngrok

---

## 🎯 Project Goals
- Consume and process data from a public REST API
- Build a Flask-based web application
- Containerize the application using Docker
- Deploy and manage the application on Kubernetes
- Use Helm for Kubernetes configuration management
- Expose a local Kubernetes service to the public internet
- Demonstrate a complete DevOps workflow from code to production-like access

---

## 🛠 Technologies Used
- Python 3.12
- Flask
- requests
- Docker
- Kubernetes (Minikube)
- Helm
- ngrok
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
