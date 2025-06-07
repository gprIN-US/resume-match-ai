import streamlit as st
from utils.resume_parser import extract_text_from_pdf
from utils.jd_parser import extract_text_from_jd
from utils.scorer import calculate_similarity
# from utils.feedback_llm import generate_feedback

st.title("📄 Resume Match AI")
st.write("Upload your resume and job description to see how well they match!")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_file = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])

if resume_file and jd_file:
    with open("temp_resume.pdf", "wb") as f:
        f.write(resume_file.read())
    with open("temp_jd.pdf", "wb") as f:
        f.write(jd_file.read())

    resume_text = extract_text_from_pdf("temp_resume.pdf")
    jd_text = extract_text_from_jd("temp_jd.pdf")

    match_score = calculate_similarity(resume_text, jd_text)
    st.metric("📊 Resume-JD Match Score", f"{match_score}%")

    # Uncomment below to add LLM feedback
    # feedback = generate_feedback(resume_text, jd_text)
    # st.subheader("💡 Feedback from LLM")
    # st.write(feedback)
