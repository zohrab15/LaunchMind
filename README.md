# LaunchMind 🚀  
**Your idea’s first checkpoint.**  

LaunchMind is a lightweight MVP project that allows users to evaluate their business ideas using AI. The platform collects essential information about a startup idea through a simple form, and then gives a visual feedback on the potential success using OpenAI's language models.

## 🌟 MVP Purpose

This is the initial version of the project focused on:

- Simple and user-friendly input form (HTML)
- Flask backend to handle form submissions
- Integration with OpenAI API to analyze and score the idea
- Displaying the result visually without needing a full backend infrastructure

> ⚠️ Note: No database or user login system is included at this stage.

---

## 💻 Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python + Flask
- **AI Service:** OpenAI API
- **Deployment (Future):** Render / Vercel / Railway (optional)

---

## 🧠 Features

- Collects 5 key aspects of the user's business idea
- Evaluates and scores the idea using AI (0-100%)
- Prevents incomplete submissions
- Simple, elegant UI with no signup required
- MVP built without full backend database for rapid testing

---

## 🔧 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/zohrab15/launchmind.git
cd launchmind

2. Install dependencies
bash
Copy
Edit
pip install flask openai python-dotenv
3. Add your OpenAI API key
Create a .env file:

ini
Copy
Edit
OPENAI_API_KEY=your_api_key_here
4. Run the application
bash
Copy
Edit
python app.py
Then open your browser at:
http://127.0.0.1:5000

📥 User Input Fields
Business Idea – Short description

Problem & Uniqueness – What issue it solves and how it's different

Target Audience & Market – Who and where

Current Stage & Resources – Idea, prototype, or launched?

Goal & Concerns – What’s the aim? What worries you?

📊 Output
AI-generated success probability (%)

Feedback message based on your inputs

Button disables after result shown to avoid resubmission

🔮 Future Plans
Add a trained ML model for offline evaluation

Build user accounts & idea history

Multilingual form interface

Feedback explanation breakdown

Integration with other APIs and datasets

🪪 License
This project is licensed under the MIT License.

👤 Author
Zöhrab Mirzayev
Founder of LaunchMind
