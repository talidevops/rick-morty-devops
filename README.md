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

---

## 🐞 Debugging & Fixes

During development, the following issue was encountered and resolved:

### Problem
When running the script directly:

```bash
py scripts/export_csv.py
ModuleNotFoundError: No module named 'app'
### Solution

The issue was caused by running the script directly, which prevented Python
from resolving the project package structure.

The fix was to run the script as a module from the project root:

```bash
py -m scripts.export_csv







