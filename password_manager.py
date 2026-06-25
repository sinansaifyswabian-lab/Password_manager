import json
import random

questions = []

DEFINITIONS

def load_questions():
global questions
try:
with open("quiz.txt", "r") as file:
questions = json.load(file)
except FileNotFoundError:
questions = []

def save_questions():
try:
with open("quiz.txt", "w") as file:
json.dump(questions, file)
except:
print('Error Saving the questions!!!')

def add_questions():
question_text = input("Enter Question: ")
options = []
for i in range(4):
option = input(f"Enter option {i + 1}: ")
options.append(option)

answer = input("Enter Answer: ")  
question = {  
    "question": question_text,   
    "options": options,           
    "answer": answer  
}  
questions.append(question)  
print("Question Added!!")

def show_questions():
if len(questions) == 0:
print('No Questions Added yet')
else:
for question in questions:
print(question)

def delete_questions():
if len(questions) == 0:
print("No Questions Added Yet!!")
else:
del_q = input("Enter question to delete: ")
found = False
for question in questions:
if del_q == question["question"]:
questions.remove(question)
print("Question Deleted!!")
found = True
break
if not found:
print("Question not found!")

def take_quiz():
if len(questions) == 0:
print("No questions available!")
return
score = 0
random.shuffle(questions)
for question in questions:
print("\n" + question["question"])
for i, option in enumerate(question["options"]):
print(f"{i + 1}. {option}")
user_answer = input("Your answer: ")
if user_answer.strip().lower() == question["answer"].strip().lower():
print("Correct!")
score += 1
else:
print(f"Wrong! Correct answer: {question['answer']}")
print(f"\nYour Score: {score}/{len(questions)}")

def main():
load_questions()
while True:
print("\n===== Quiz App =====")
print("1. Add Question")
print("2. Show Questions")
print("3. Delete Question")
print("4. Take Quiz")
print("5. Exit")

choice = input("Enter choice: ")  

    if choice == "1":  
        add_questions()  
        save_questions()  
    elif choice == "2":  
        show_questions()  
    elif choice == "3":  
        delete_questions()  
        save_questions()  
    elif choice == "4":  
        take_quiz()  
    elif choice == "5":  
        print("Goodbye!")  
        break  
    else:  
        print("Invalid choice!")

main()

