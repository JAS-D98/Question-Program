quiz = {
    "question1":{
        "question" : "What is the capital city of Kenya",
        "answer": "Nairobi"
    },
    "question2":{
        "question" : "What is the capital city of Uganda",
        "answer": "Kampala"
    },
    "question3":{
        "question" : "What is the capital city of Germany",
        "answer": "Berlin"
    },
    "question4":{
        "question" : "What is the capital city of Egypt",
        "answer": "Kairo"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer=input('Answer? ')

    if answer.lower() == value['answer'].lower():
        print('correct')
        score = score + 1
        print('Your score is: ', str(score))
    else:
        print('Wrong')
        print('The correct answer is ', value['answer'])
        print('Your score is: ', str(score))

print('Final Score is ', str(score), 'over four')
print('Total Percentage', str(int(score/4 * 100)), '%')