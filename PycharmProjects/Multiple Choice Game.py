# Create a multiple choice questionnaire and display the score

from Class import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
'''What color are kiwis?
(a) Brown
(b) Yellow
(c) Orange\n\n''',
'''What color are limes?
(a) Yellow
(b) Green
(c) Red\n\n''',
'''What color are Tangerines?
(a) Green
(b) Red
(c) Orange\n\n'''
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "c"),
]


def run_test(questions):
    score = 0
    for question in questions:
        user_answer = input(question.prompt)
        if user_answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(question_prompts)))


run_test(questions)