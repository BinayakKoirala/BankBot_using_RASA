import streamlit as st
import requests

def get_bot_response(user_input):
    url = "http://localhost:5005/webhooks/rest/webhook"
    payload = {"sender": "user", "message": user_input}
    response = requests.post(url, json=payload)
    bot_response = response.json()[0]['text']
    return bot_response

def main():
    st.title("BankBot by Binayak Koirala")
    user_input = st.text_input("User Input")

    if st.button("Send"):
        response = get_bot_response(user_input)
        st.text_area("Bot Response", value=response, height=200, max_chars=None, key=None)

if __name__ == "__main__":
    main()

