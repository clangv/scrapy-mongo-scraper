

# 📚 Book Scraper with Scrapy and MongoDB

This project is a web scraping application built using **Scrapy** to extract book data from websites and store it in **MongoDB**.

---

## 📁 Project Structure

```
books/
│
├── books/
│   ├── spiders/
│   │   └── __init__.py
│   │
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   └── settings.py
│
└── scrapy.cfg
```

---

## 🛠️ Prerequisites

Before running the project, ensure the following are installed:

- ✅ Python 3.x
- ✅ MongoDB
- ✅ Scrapy

---

## 🔧 Setup Instructions

### 1. Create a Virtual Environment

```powershell
py -m venv venv
```

### 2. Activate the Virtual Environment

```powershell
venv\Scripts\activate
```

### 3. Install Scrapy

```powershell
(venv) pip install scrapy
```

### 4. Set Up MongoDB

Connect to MongoDB and create the database and collection:

```javascript
use books_db
db.createCollection("books")
```

---

## 🕷️ Running the Project

### Generate a New Spider (Optional)

Replace `book` and `example.com` with your desired spider name and domain:

```powershell
(venv) scrapy genspider book example.com
```

### Run the Spider

```powershell
(venv) scrapy crawl book
```

### Check Spider Contracts (Testing)

```powershell
(venv) scrapy check book
```

---

## 🧰 Available Scrapy Commands

| Command       | Description                              |
|---------------|------------------------------------------|
| `bench`       | Run quick benchmark test                 |
| `fetch`       | Fetch a URL using the Scrapy downloader  |
| `genspider`   | Generate new spider                      |
| `runspider`   | Run a self-contained spider              |
| `settings`    | Get settings values                      |
| `shell`       | Interactive scraping console             |
| `startproject`| Create new project                       |
| `version`     | Print Scrapy version                     |
| `view`        | Open URL in browser as seen by Scrapy    |

---

## ⚙️ Configuration

- Database settings can be configured in `settings.py`.
- Define item pipelines in `pipelines.py`.
- Implement spiders inside the `spiders/` directory.

---

## 🧪 Testing

The project includes contract testing for spiders. To run tests:

```powershell
(venv) scrapy check book
```

---

## 💾 Data Storage

All scraped book data is stored in MongoDB under the `books_db.books` collection.

Make sure MongoDB is running and the connection string is properly set in `settings.py`.

---

## 📘 Notes

- Always respect website terms of service and robots.txt when scraping.
- Add appropriate middleware or delays if necessary to avoid overwhelming servers.

---

Happy scraping! 🕵️‍♂️📖

--- 
