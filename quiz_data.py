import pandas as pd

# The list of questions provided
questions = [
    {
        "question": "Who developed Python Programming Language?",
        "options":["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which type of Programming does Python support?",
        "options": ["object-oriented programming", "structured programming", "functional programming", "all of the mentioned"],
        "answer": "all of the mentioned"
    },
    {
        "question": "Is Python case sensitive when dealing with identifiers?",
        "options": ["no", "yes", "machine dependent", "none of the mentioned"],
        "answer": "yes"
    },
    {
        "question": "Which of the following is the correct extension of the Python file?",
        "options": [".python",".pl", ".py", ".p"],
        "answer": ".py"
    },
    {
        "question": "Is Python code compiled or interpreted?",
        "options": ["Python code is both compiled and interpreted", "Python code is neither compiled nor interpreted", "Python code is only compiled", "Python code is only interpreted"],
        "answer": "Python code is both compiled and interpreted"
    },
    {
        "question": "All keywords in Python are in _________",
        "options": ["Capitalized", "lower case", "UPPER CASE", "None of the mentioned"],
        "answer": "None of the mentioned"
    },
    {
        "question": "What will be the value of the following Python expression?   4 + 3 % 5 ",
        "options": ["7", "2", "4", "1"],
        "answer": "7"
    },
    {
        "question": "Which of the following is used to define a block of code in Python language?",
        "options": ["Indentation", "Key", "Brackets", "All of the mentioned"],
        "answer": "Indentation"
    },
    {
        "question": "Which keyword is used for function in Python language?",
        "options": ["Function", "def", "Fun", "Define"],
        "answer": "def"
    },
    {
        "question": "Python supports the creation of anonymous functions at runtime, using a construct called __________",
        "options": ["pi", "anonymous", "lambda", "none of the mentioned"],
        "answer": "lambda"
    }
]

# Transform the questions list into a DataFrame
data = {
    "Question": [q["question"] for q in questions],
    "Option1": [q["options"][0] for q in questions],
    "Option2": [q["options"][1] for q in questions],
    "Option3": [q["options"][2] for q in questions],
    "Option4": [q["options"][3] for q in questions],
    "Answer": [q["answer"] for q in questions]
}

df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel("quiz_data.xlsx", index=False)

print("Excel file 'quiz_data.xlsx' has been created.")
