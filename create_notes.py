import os
import openai
import streamlit as st

full_message_temp ="""
    <div style="background-color:white;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
    <p style="text-align:justify;color:black;padding:10px">{}</p>
    </div>
    """
def Create_notes():


  def get_notes(text):
    openai.api_key = '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'
    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt= text,
        temperature=1,
        max_tokens= 140,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
      )
    return response["choices"][0]["text"]


  with st.form("Summaries from Text"):
    st.subheader("Create study notes")
    text = st.text_area("Provide a topic and get study notes.",height=200)
    generate = st.form_submit_button("Get Notes")
    if generate:
      summary = get_notes(text)
      #st.markdown(full_message_temp.format(summary),unsafe_allow_html=True)
      st.markdown(summary)
    
  