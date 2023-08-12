import streamlit as st
import Dumsharas

st.title("Dumsharas Name Generator")

LanguageName = st.sidebar.selectbox("pick a Language",("Hindi","Bengali","Kannada","Marathi","konkani","tulu","assameese","Telugu","Tamil"))
print(LanguageName)

if(LanguageName):
    response = Dumsharas.AI_MOVIE_NAME_GENERATIR(LanguageName)
    st.write(response)