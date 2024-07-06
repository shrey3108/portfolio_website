import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]


genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1,col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am shukla shrey")

with col2:
    st.image("image/shrey.jpeg")

persona = """
          You are Shrey AI bot. You help people answer questions about yourself (i.e., Shrey). Answer as if you are responding.
Don't answer in the second or third person.
If you don't know the answer, simply say "That's a secret."
Here is more info about Shrey:

- **Background**: Shrey Shukla is a student at ADIT. He is interested in machine learning, computer vision, and NLP.
- **Skills**: Shrey knows C, C++, Java, Python,machin larning,nlp,computer vision and is constantly learning new technologies.
- **Location**: He lives in Nadiad, Gujarat.
- **Education**: Shrey is pursuing a degree in computer science.
- **Projects**:
  - **Plant Detection System**: Developed a solution for early detection of plant diseases using deep learning and computer vision, integrated with Flask and Telebot for notifications.
  - **Mental Health Detection**: Created a text classification model to detect mental health disorders using NLP, Flask, and Dialogflow.
- **Interests**: Shrey enjoys working on AI projects, participating in hackathons, and exploring new advancements in technology.
- **Personality**: Shrey is curious, passionate about technology, and loves to solve complex problems. He enjoys helping others and sharing knowledge.
- **Contact Information**: You can reach out to Shrey via email at shreyshukla318@gmail.com.

Remember, if you don't know the answer to a question, just say, "That's a secret.

"""




st.title("shrey's AI  Bot")

user_question = st.text_input("Ask me anything about me")

st.write("")


if st.button("ASK" , use_container_width=400):
    prompt = persona +"Here is the question that the user asked: "+ user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")
st.title("My project's ")

st.title(" ")
col1,col2 = st.columns(2)
with col1:
    st.subheader("plant detection system Project:")
    st.write("- a solution of early detection of plant diseases")
    st.write("- if disease is detected send a message about it to user's bot")
    st.write("- use deeplarning , computervision ,flask,telebot")

with col2:
    st.video("https://youtu.be/UdWHBsCqZc0?si=9eJ-3EwGR98RjQV-")

st.title(" ")

col1, col2 = st.columns(2)
with col1:
    st.subheader("mental health detection project:")
    st.write("- Developed a text classification model for mental health disorders")
    st.write("- Implemented the model to provide insights into mental health based on user-inputted text.")
    st.write("- use nlp ,flask,Dialogflow")

with col2:
    st.video("https://youtu.be/K1DkpADCjrc?si=66S2WgYhsvUovuAR")

st.write("")
st.title("My Skills")
st.slider("Programmig",0,100,65)
st.slider("nlp",0,100,75)
st.slider("deep larning",0,100, 70)
st.slider("devlop ment",0,100, 50)


# st.file_uploader("upload a file")

st.write(" ")
st.write("CONTACT")
st.title("for any inquiries please email me")
st.write("shreyshukla318@gmail.com")


col3, col4 = st.columns(2)

col3, col4 = st.columns(2)



with col3:
    st.markdown("[![GitHub Logo](https://th.bing.com/th?q=GitHub+Logo+Font&w=36&h=36&c=7&rs=1&p=0&o=5&dpr=1.3&pid=1.7&mkt=en-IN&cc=IN&setlang=en&adlt=strict&t=1)](https://github.com/shrey3108/)")

with col4:
    st.markdown("[![LinkedIn Logo](https://th.bing.com/th?q=LinkedIn+Signature+Logo&w=36&h=36&c=7&rs=1&p=0&o=5&dpr=1.3&pid=1.7&mkt=en-IN&cc=IN&setlang=en&adlt=strict&t=1)](https://www.linkedin.com/in/shrey-shukla-38410024b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")

