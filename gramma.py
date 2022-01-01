import os
import openai
import streamlit as st


full_message_temp ="""
    <div style="background-color:white;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
    <p style="text-align:justify;color:black;padding:10px">{}</p>
    </div>
    """

def correct_gramma():

  def get_correct(text):
    response = openai.Completion.create(
      engine="davinci",
      prompt=text,
      temperature=0,
      max_tokens=60,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["\n"]
    )
    return response["choices"][0]["text"]

  with st.form("Summaries from Text"):
    st.subheader("Create study notes")
    text = st.text_area("Provide text .",height=200)
    t = "Original: {}.\nStandard American English:"
    text = t.format(text)
    generate = st.form_submit_button("Correct Gramma")
    if generate:
      summary = get_correct(text)
      st.markdown(full_message_temp.format(summary),unsafe_allow_html=True)