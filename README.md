# Rick & Morty Characters Exporter

## 📌 Project Description
This project fetches characters from the public Rick and Morty API, filters only:
- Human characters
- Status: Alive
- Origin starting with "Earth"

The filtered data is exported into a CSV file for further analysis or processing.

---

## 🛠 Technologies Used
- Python 3.12
- requests
- Git & GitHub

---

## 📁 Project Structure
```text
rick-morty-devops/
├── app/
│   ├── __init__.py
│   └── fetcher.py        # Fetches and filters characters from the API
├── scripts/
│   ├── __init__.py
│   └── export_csv.py     # Exports the filtered data to CSV
├── data/
│   └── characters.csv   # Generated output file
├── requirements.txt
├── .gitignore
└── README.md

