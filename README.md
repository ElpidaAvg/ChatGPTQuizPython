# ChatGPTQuiz 🧠

A simple GUI quiz application built with Python using Tkinter and
OpenAI's API.\
The app generates yes/no questions about world traditions and tracks
your score interactively.

## 🖼️ Application Preview

<p align="center">
<img width="642" height="867" alt="Print screen (1)" src="https://github.com/user-attachments/assets/af15479f-f0ac-45fd-a336-e579bc1014e3" />
</p>

## 🚀 Features

-   Dynamic question generation using OpenAI API
-   Simple YES / NO interface
-   Score tracking system
-   Progress bar visualization
-   Restart functionality after 5 questions
-   Clean themed UI using `ttkthemes`

## 🛠️ Technologies Used

-   Python
-   Tkinter
-   ttk / ttkthemes
-   OpenAI API

## 📦 Installation

1.  Clone the repository:

```{=html}
<!-- -->
```
    git clone https://github.com/yourusername/ChatGPTQuiz.git
    cd ChatGPTQuiz

2.  Install dependencies:

```{=html}
<!-- -->
```
    pip install openai ttkthemes

3.  Add your OpenAI API key: Replace:

```{=html}
<!-- -->
```
    client = openai.OpenAI(api_key="your API KEY")

with your actual API key.

## ▶️ Run the App

    python main.py

## 🎮 How It Works

-   The app generates a yes/no question about global traditions.
-   Click YES or NO to answer.
-   Your score updates after each question.
-   After 5 questions, you can restart the quiz.

## ⚠️ Notes

-   Requires internet connection for API calls
-   Make sure your API key is valid

## 📄 License

This project is open-source and free to use.
