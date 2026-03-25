import openai

client = openai.OpenAI(api_key = "your API KEY")

from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

window = ThemedTk(theme="Breeze")
window.configure(themebg="Breeze")
window.geometry("600x800")
window.title("ChatGPTQuiz")
window.resizable(False, False)

score = 0
allquestions = 0

def check(uanswer):
    global score, allquestions
    if answer == uanswer:
        score += 1
        allquestions += 1
        lblscore.configure(text = "Score: " + str(score) + "/" + str(allquestions))
        pb["value"] += 20
    else:
        allquestions += 1
        lblscore.configure(text="Score: " + str(score) + "/" + str(allquestions))

    if allquestions == 5:
        lblscore.configure(text="Total score: " + str(score) + "/" + str(allquestions))
        restartbtn = ttk.Button(window, text = "RESTART", command = generate_question)
        restartbtn.pack(pady = 50)
        score = 0
        allquestions = 0
        pb["value"] = 0
        yesbtn.configure(text="")
        nobtn.configure(text="")
        lbl.configure(text="")
    else:
        generate_question()

lbl = ttk.Label(window, text = "", font = 20)
lbl.pack(pady = 50)

framebuttons = ttk.Frame()
framebuttons.pack()

yesbtn = ttk.Button(framebuttons, text = "YES", command = lambda:check("yes"))
yesbtn.pack(side = "left")
nobtn = ttk.Button(framebuttons, text = "NO", command = lambda:check("no"))
nobtn.pack()

lblscore = ttk.Label(window, text = "", font = 20)
lblscore.pack(pady = 50)

pb = ttk.Progressbar(window, length = 400)
pb.pack()

def generate_question():

    global answer
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "Generate a simple yes/no question in English about traditions around the world with a clear correct answer." "Return the format: 'Question: <question> | Answer: <yes/no>' "},
            {"role": "user", "content": "Generate a simple yes/no question."}
        ]
    )
    #print(response)
    result = response.choices[0].message.content.strip()
    #print(result)
    question_part, answer_part = result.split(" | ")
    #print(question_part)
    #print(answer_part)

    question = question_part.replace("Question: ", "").strip()
    answer = answer_part.replace("Answer: ", "").strip().lower()
    print(question)
    print(answer)
    lbl.configure(text = question)

generate_question()

window.mainloop()