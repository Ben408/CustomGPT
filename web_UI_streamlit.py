import os
import streamlit as st
from dotenv import load_dotenv

def main():
    load_dotenv()
    st.set_page_config(page_title="Ask Your Own Documents")
    st.header("Ask your Own Documents")
    

    # show user input
   #  user_question = st.text_input("Ask a question about your Documents:")
   #  if user_question:
   #  docs = Chroma(persist_directory=persist_directory, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)(user_question)
        
   #  llm = ('MODEL_TYPE')
   #  chain = load_qa_chain(llm, chain_type="stuff")
    
   #  response = chain.run(input_documents=docs, question=user_question)
   #  print(cb)
           
   #  st.write(response)
