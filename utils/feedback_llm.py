import openai  # or use HuggingFace

def generate_feedback(resume, jd):
    prompt = f"Compare this resume:\n{resume}\n\nwith this job description:\n{jd}\n\nGive actionable feedback to improve resume for this job:"
    
    openai.api_key = "your-key"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
