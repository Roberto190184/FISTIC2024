import streamlit as st
import web_spacy_app
import spacy
nlp = spacy.load('it_core_news_md')
st.title('Token Identifier and Translator')
text_input = st.text_area('Enter text to tokenize and translate:')

if st.button('Tokenize'):  
    # Process the text with SpaCy
    doc = nlp(text_input)

    tokens = [token.text for token in doc]
    st.write('Tokens:', tokens)

    from  google import  Translator
    translator = Translator()

    st.title('Token Identifier and Translator')

    text_input = st.text_area('Enter text to tokenize and translate:')
    if st.button('Tokenize'):  
    # Process the text with SpaCy
    doc = nlp(text_input)
    tokens = [token.text for token in doc]
    st.write('Tokens:', tokens)







