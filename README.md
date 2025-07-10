# 🧠 Text2SQL Query Generator

A simple and powerful app that converts natural language into SQL queries using a local LLM model via [Ollama](https://ollama.com/) and [LangChain](https://www.langchain.com/) — all wrapped inside a beautiful [Streamlit](https://streamlit.io/) interface.

---

## 📌 Overview

This project allows you to input plain English queries like:

> "Get all users who signed up last month"

And automatically converts it to a syntactically correct SQL query:

```sql
SELECT * FROM users WHERE signup_date >= CURRENT_DATE - INTERVAL '1 month';
````

It uses a lightweight local language model through **Ollama** (e.g., `phi3`, `llama3`, `mistral`) to generate context-aware SQL queries, ensuring data privacy and low latency — no external API calls required.

---

## ⚙️ How It Works

1. You type your question in natural language.
2. A prompt template is applied: the model is asked to return only SQL.
3. The local model via Ollama processes your question.
4. The generated SQL is displayed in real-time via the Streamlit app.

---

## 🧱 Technologies Used

| Technology     | Role                                                 |
| -------------- | ---------------------------------------------------- |
| **Python**     | Base programming language                            |
| **Streamlit**  | For building the interactive UI                      |
| **LangChain**  | For chaining prompts and managing LLM inputs/outputs |
| **Ollama**     | For running local LLMs (like `phi3`, `llama3`, etc.) |
| **phi3 model** | Lightweight, open-source LLM optimized for local use |

---

## 🚀 Getting Started

### ✅ Prerequisites

* Python 3.9 or higher
* Ollama installed locally
* Git (optional, for cloning)

---

## 📥 Ollama Installation & Model Setup

### 1. Install Ollama

#### 🟢 For macOS:

```bash
brew install ollama
```

#### 🟢 For Linux:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### 🟢 For Windows:

Download the installer from: [https://ollama.com/download](https://ollama.com/download)

---

### 2. Start Ollama and Pull the Model

Choose a model like `phi3` (or `llama3`, `mistral`, etc.)

```bash
ollama pull phi3
```

Then make sure it's running:

```bash
ollama run phi3
```

This will launch the model locally and wait for input.

---

## 📦 Install Dependencies

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/text2sql-query.git
cd text2sql-query
```

### 2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install requirements:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

Once everything is installed:

```bash
streamlit run app.py
```

This will open the web app in your browser automatically.

---

