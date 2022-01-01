import streamlit as st
from create_notes import *
from gramma import *
from gtp3 import *
from Notes_summary import *

full_message_temp ="""
    <div style="background-color:grey;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
    <p style="text-align:justify;color:white;padding:10px">{}</p>
    </div>
    """

st.header(' Natural Language Processor App')
a = st.sidebar.selectbox("",['Summarize Text','Create Notes', 'Gramma Correction','Notes to Summary','About App'])
if a == 'Summarize Text':
    text  = 'Translates difficult text into simpler concepts'
    st.sidebar.markdown(full_message_temp.format(text),unsafe_allow_html=True)
    summary()
elif a == "Create Notes":
    text = 'Provide a topic and get study notes.'
    st.sidebar.markdown(full_message_temp.format(text),unsafe_allow_html=True)
    Create_notes()
elif a == "Gramma Correction":
    text = 'Corrects sentences into standard English.'
    st.sidebar.markdown(full_message_temp.format(text),unsafe_allow_html=True)
    correct_gramma()
elif a == 'Notes to Summary':
    text = 'Turn meeting notes into a summary.'
    st.sidebar.markdown(full_message_temp.format(text),unsafe_allow_html=True)
    notes_summary()
elif a == "About App":
    st.image("index.png",width = 500)
    st.header("About")
    st.markdown("Official documentation of **[Openai GTP3](https://openai.com/api/)**")
    st.markdown("Official documentation of **[Streamlit](https://docs.streamlit.io/en/stable/getting_started.html)**")
    st.write("")
    st.write("Author:")
    st.markdown(""" **[Prince Ngema](https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile&lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_self_edit_contact_info%3BjZsKf1G2TyCk%2Bbr6GKw0KA%3D%3D)**""")
    st.write("Created on 01/01/2022")
    #st.write("Last updated: **29/04/2021**")
    
 
   
