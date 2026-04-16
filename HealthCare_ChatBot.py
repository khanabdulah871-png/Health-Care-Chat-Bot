from groq import Groq
import streamlit as st 
import os 
from dotenv import load_dotenv 


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY") 
client = Groq(api_key=GROQ_API_KEY)

def healthcare_bot(user_input):
    # Messages list
    messages = [
        {
            "role": "system", 
            "content": "You are a health care assistant trained to provide information about medical conditions, treatment options, and prevention strategies. You should also offer lifestyle tips related to health living, nutrition, and exercise when appropriate, while reminding users that consultations with healthcare professionals are essential for personalized advice."
        },
        {"role": "user", "content": user_input}
    ]

    # 2. Groq Model Request
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", 
        messages=messages,
        max_tokens=150,
        temperature=0.7 
    )

    # Response goes to model
    bot_response = response.choices[0].message.content.strip()
    return bot_response

def main():
    st.title("HealthCare Chat Bot")

    user_input = st.text_input("Hi! Whats on your mind? ")

    if user_input: 
        bot_response = healthcare_bot(user_input)

        st.write("**Bot's Response:**")
        st.write(bot_response)

if __name__ == "__main__":

    main()

    #user_input = input("What help do you want? : ")
    #if user_input:
       # output = healthcare_bot(user_input)
      #  print("\nBot:", output)