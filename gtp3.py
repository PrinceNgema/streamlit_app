from io import StringIO
import streamlit as st
import pandas as pd
import numpy as np
import openai
import pdfplumber

def summary():
    openai.api_key = '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'

    def get_summary(text):
        response = openai.Completion.create(
        engine="davinci",
        prompt= text,
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0,
        stop=["\"\"\""]
        )
        return response

    def displayPaperContent(paperContent, page_start=1, page_end=1):
        for page in paperContent[page_start:page_end]:
            print(page.extract_text())
    full_message_temp ="""
    <div style="background-color:white;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
    <p style="text-align:justify;color:black;padding:10px">{}</p>
    </div>
    """
    method = st.selectbox("Please select Input method", ["Input Text","Upload Document"])
    if method == "Input Text":
        with st.form("Summaries from Text"):
            text = st.text_area("Add Text to Summarize here",height=200)
            t = "My twelfth grader asked me what this passage means:\n\"\"\"\n {}.\n\"\"\"\nI rephrased it for him, in plain language a twelfth grader can understand:\n\"\"\"\n"
            text = t.format(text)
            generate = st.form_submit_button("Summarize")
            if generate:
                summary = get_summary(text)
                summary_text = summary["choices"][0]["text"]
                st.markdown(full_message_temp.format(summary_text),unsafe_allow_html=True)
    elif method == "Upload Document":
        with st.form("Summaries from Document"):
            uploaded_file = st.file_uploader("Choose a file", "pdf")
            if uploaded_file is not None:
                paperContent = pdfplumber.open(uploaded_file).pages
            else:
                st.write("Please upload a supported file format")
            generate = st.form_submit_button("Summarize")
            if generate:
                paperContent = pdfplumber.open(uploaded_file).pages
                for page in paperContent[1:2]:
                    text = page.extract_text()
                summary = get_summary(text)
                summary_text = summary["choices"][0]["text"]
                st.markdown(full_message_temp.format(summary_text),unsafe_allow_html=True)
                #st.markdown(summary_text)

def get_tips():
    pass
                



