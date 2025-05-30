# Remote Job Aggregator

A Python-based command-line tool that fetches job postings from the [USAJOBS API](https://developer.usajobs.gov/) and prepares them for analysis or storage. This tool is designed for developers interested in automating the collection and processing of remote job data for further filtering, ranking, or visualization.

---

## 🚀 Features Implemented

- ✅ Fetches job postings from USAJOBS using authenticated API requests.
- ✅ Uses environment variables for secure credential management.
- ✅ Modular project structure with a clear separation between logic, utilities, and execution.
- ✅ Basic error handling for failed API requests.
- ✅ Functional unit test scaffold using `unittest`.
- ✅ Command-line executable via `main.py`.

---

## 📁 Project Structure

```
Remote_Job_Aggregator/
├── app/
│   ├── __init__.py
│   ├── fetcher.py         # Handles API requests to USAJOBS
│   ├── utils.py           # (Planned) Helper functions for parsing, saving, etc.
│   └── analyzer.py        # (Placeholder) To analyze/filter job data
├── test/
│   ├── __init__.py
│   └── test_fetcher.py    # Unit tests for fetcher module
├── main.py                # ✅ Entry point of the program
├── .env                   # API credentials (not committed)
└── README.md              # This file
```

---

## 🔐 Environment Variables

Credentials are stored in a `.env` file (never commit this). Required variables:

```env
USAJOBS_API_KEY=your-api-key
USAJOBS_USER_EMAIL=your-registered-email
```

---

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install requests python-dotenv
```

---

## 🧪 Running the Program

To fetch job data and print the results:

```bash
python main.py
```

---

## ✅ Running Unit Tests

From the root of the project:

```bash
python -m unittest discover -s test -p "test_*.py"
```

---

## 🛠️ In Progress / Planned Features

- [ ] Filter results by keyword, location, or pay grade
- [ ] Save jobs to JSON or CSV
- [ ] Detect job quality using keyword scoring
- [ ] Add logging and CLI options (e.g., output to file)
- [ ] Connect multiple APIs (e.g., Remotive, Adzuna)

---

## 📌 Notes

- The `fetcher.py` module is built for reuse — it can be tested independently or triggered via `main.py`.
- USAJOBS API requires proper headers (`User-Agent` and `Authorization-Key`) to authenticate requests.
- The project follows a testable and modular architecture to support future enhancements.

---

## 📄 License

MIT License.
