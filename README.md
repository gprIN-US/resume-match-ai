# 🧠 Resume Match AI

An AI-powered tool that compares your resume with a job description to:

-  Calculate a Match Score using TF-IDF + Cosine Similarity
-  Provide actionable resume improvement tips via GPT (optional)
- ️ Streamlit UI for easy interaction
-  PDF support for resumes and job descriptions

---

##  Project Structure

resume-match-ai/
├── app.py
├── examples/
│ ├── sample_resume.pdf
│ └── sample_jd.pdf
├── utils/
│ ├── resume_parser.py
│ ├── jd_parser.py
│ ├── scorer.py
│ └── feedback_llm.py
├── requirements.txt
└── README.md

---

## How to Run

1. Clone this repo  
2. Install dependencies  
   ```bash
   pip install -r requirements.txt
streamlit run app.py

Technologies Used

pdfplumber – to extract text from PDF resumes and JDs
scikit-learn – for TF-IDF vectorization and similarity scoring
Streamlit – to build a clean and interactive UI
OpenAI GPT (optional) – to generate improvement feedback