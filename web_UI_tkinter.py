from tkinter import *
import subprocess

# Define the UI
window=Tk()
window.title("Ask the Chatbot")
window.minsize(width=330, height=200)
window.maxsize(width=1000, height=1000)

l1=Label(window,text='Query the bot', bg="gray")
l1.place(x=40, y=20)

l2_answer = Label(window, text="", bg="white")
l2_answer.place(x=40, y=130)

q=StringVar()

e1=Entry(window,width=40,textvariable=q)
e1.place(x=40, y=50)

# Define the asking function
def ask():
    question = q.get()
    l2.config(text=question, bg="green")

    # Call the customGPT.py script and pass the question as an argument
    process = subprocess.Popen(['python', 'customGPT.py', question], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if process.returncode == 0:
        answer = output.decode('utf-8')
        l2_answer.config(text=answer, bg="blue")
    else:
        error_message = error.decode('utf-8')
        l2_answer.config(text=error_message, bg="red") 

l2=Label(window,text="Nothing entered",bg="black",fg="white")
l2.place(x=40, y=100)

b1=Button(window, text="Ask",bg="green", command=ask)
b1.place(x=40, y=70)

l2_answer = Label(window, text="", bg="white")
l2_answer.place(x=40, y=130)

b2=Button(window, text="Exit",bg="red",command=window.destroy)
b2.pack(side=BOTTOM)

window.mainloop()


