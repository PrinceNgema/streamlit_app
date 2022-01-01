import os
import openai
import streamlit as st


full_message_temp ="""
    <div style="background-color:white;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
    <p style="text-align:justify;color:black;padding:10px">{}</p>
    </div>
    """

def notes_summary():

  def get_notes_summary(text):
    response = openai.Completion.create(
    engine="davinci-instruct-beta",
    prompt=text,
    temperature=0.7,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response["choices"][0]["text"]

  with st.form("Summaries from Text"):
    st.subheader("Notes to Summary")
    text = st.text_area("Provide Notes to Convert",height=200)
    t = "Convert my short hand into a first-hand account of the meeting: {}\n\nSummary:"
    text = t.format(text)
    generate = st.form_submit_button("Generate Summary")
    if generate:
      summary = get_notes_summary(text)
      st.markdown(full_message_temp.format(summary),unsafe_allow_html=True)