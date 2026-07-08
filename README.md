# Ai_learning_mentor
# 🎓 AI Learning Mentor

An **Agentic AI-powered Learning Mentor** built using **Streamlit, LangGraph, LangChain, Gemini AI, and MySQL**. The application helps students learn concepts, generate personalized study plans, and provides a secure login system with an interactive AI chatbot.

---

## 🚀 Features

### 🔐 User Authentication
- Student Registration
- Secure Login
- Password Hashing using bcrypt
- MySQL Database Integration

### 🤖 AI Learning Mentor
- Ask academic questions
- Get simple and detailed explanations
- Examples and code snippets where applicable
- Powered by Google Gemini

### 📅 AI Study Planner
- Personalized study schedules
- Day-wise preparation plans
- Revision strategy
- Exam preparation guidance

### 🧠 Agentic AI Architecture
The project uses **LangGraph** to route user requests intelligently.

- **Router Agent**
  - Determines user intent
  - Decides which AI agent should respond

- **Mentor Agent**
  - Answers academic questions
  - Explains concepts in simple language

- **Planner Agent**
  - Creates personalized study plans
  - Generates exam preparation schedules

### 📊 Dashboard
- Student Profile
- Course Information
- Year Information
- AI Learning Mentor
- Study Planner
- Progress Section *(Under Development)*

---

# 🏗️ Tech Stack

- Python
- Streamlit
- LangChain
- LangGraph
- Google Gemini API
- MySQL
- bcrypt
- Plotly
- Pandas
- FAISS *(Future RAG Implementation)*

---

# 📁 Project Structure

```
AI_Learning_Mentor/
│
├── agents/
│   ├── mentor_agent.py
│   ├── planner_agent.py
│   ├── router_agent.py
│   └── workflow.py
│
├── database/
│   ├── db.py
│   └── user_db.py
│
├── pages/
│   ├── login.py
│   ├── registration.py
│   ├── dashboard.py
│   ├── ai_chat.py
│   └── planner.py
│
├── prompts/
│   ├── mentor_prompt.py
│   ├── planner_prompt.py
│   └── router_prompt.py
│
├── utils/
│   └── auth.py
│
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/AI_Learning_Mentor.git
```

```bash
cd AI_Learning_Mentor
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

### 5️⃣ Configure MySQL Database

Create a database named

```sql
CREATE DATABASE ai_learning_mentor;
```

Use it

```sql
USE ai_learning_mentor;
```

Create the Students table

```sql
CREATE TABLE students(

student_id INT PRIMARY KEY AUTO_INCREMENT,

full_name VARCHAR(100),

email VARCHAR(100) UNIQUE,

password VARCHAR(255),

course VARCHAR(100),

year INT

);
```

---

### 6️⃣ Run the Application

```bash
streamlit run app.py
```

---

# 🧠 Agent Workflow

```
Student Question
        │
        ▼
  Router Agent
        │
 ┌──────┴──────┐
 │             │
 ▼             ▼
Mentor      Planner
 Agent        Agent
 │             │
 └──────┬──────┘
        ▼
     Response
```

---

# 📸 Screenshots

Add screenshots of:

- Home Page
- Login Page
- Registration Page
- Dashboard
- AI Chat
- Study Planner

---

# 🌟 Future Enhancements

- 📄 PDF Question Answering (RAG)
- 📊 Progress Analytics Dashboard
- 📈 Learning Statistics
- 🎯 Personalized Recommendations
- 🧠 Conversation Memory
- 👨‍🏫 Teacher Dashboard
- 📅 Calendar Integration
- 📝 Quiz Generation
- 📚 Notes Generator

---

# 📚 Learning Objectives

This project demonstrates:

- Agentic AI
- LangGraph Workflow
- Prompt Engineering
- LLM Routing
- Gemini API Integration
- Streamlit Development
- MySQL Integration
- Authentication
- AI-based Study Planning

---

# 👩‍💻 Author

**Nivedita Nilesh Bhoinwad**


## 📄 License

This project is intended for educational and learning purposes.
