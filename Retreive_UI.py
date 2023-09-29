from tkinter import *
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import GPT4All, LlamaCpp
import os
import argparse

load_dotenv()

embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
persist_directory = os.environ.get('PERSIST_DIRECTORY')

model_type = os.environ.get('MODEL_TYPE')
model_path = os.environ.get('MODEL_PATH')
model_n_ctx = os.environ.get('MODEL_N_CTX')
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS', 4))

from constants import CHROMA_SETTINGS

# UI configuration
window = Tk()
window.title("Query the chatbot")
window.minsize(width=330, height=200)
window.maxsize(width=500, height=500)

l1 = Label(window, text='Query the bot', bg="gray")
l1.place(x=30, y=20)

q = StringVar()

e1 = Entry(window, width=40, textvariable=q)
e1.place(x=40, y=50)

# Initialize the LLM and QA components
embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
db = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})

def ask():
    question = q.get()
    l2.config(text=question, bg="green")

    # Prepare the LLM
    if model_type == "LlamaCpp":
        llm = LlamaCpp(model_path=model_path, n_ctx=model_n_ctx, verbose=False)
    elif model_type == "GPT4All":
        llm = GPT4All(model=model_path, n_ctx=model_n_ctx, backend='gptj', verbose=False)
    else:
        l2_answer.config(text="Model not supported", bg="red")
        return

    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

    # Get the answer from the chain
    res = qa(question)
    answer, docs = res['result'], res['source_documents']

    # Print the result
    l2_answer.config(text=answer, bg="blue")

    # Print the relevant sources used for the answer
    for document in docs:
        print("\n> " + document.metadata["source"] + ":")
        print(document.page_content)

l2 = Label(window, text="Nothing entered", bg="black", fg="white")
l2.place(x=40, y=100)

b1 = Button(window, text="Ask", bg="green", command=ask)
b1.place(x=40, y=70)

l2_answer = Label(window, text="", bg="white")
l2_answer.place(x=40, y=130)

b2 = Button(window, text="Exit", bg="red", command=window.destroy)
b2.pack(side=BOTTOM)

window.mainloop()
