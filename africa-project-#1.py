import PySimpleGUI as sg
#Please include comments!! 

quiz = {
    1: {
        "question": "What is the capital of Madagascar?",
        "answer": "Antananarivo"
    },
    2: {
        "question": "What is the capital of Algeria?",
        "answer": "Algiers" or "Algers"
    },
    3: {
        "question": "What is the capital of Angola?",
        "answer": "Luanda"
    },
    4: {
        "question": "What is the capital of Benin?",
        "answer": "Porto-Novo" or "Porto Novo"
    },
    5: {
        "question": "What is the capital of Botswana?",
        "answer": "Gaborone"
    },
    6: {
        "question": "What is the capital of Burkina Faso?",
        "answer": "Ouagadougou"
    },
    7: {
        "question": "What is the capital of Burundi?",
        "answer": "Gitega"
    },
    8: {
        "question": "What is the capital of Cabo Verde?",
        "answer": "Praia"
    },
    9: {
        "question": "What is the capital of Cameroon?",
        "answer": "Yaounde"
    },
    10: {
        "question": "What is the capital of Central African Republic?",
        "answer": "Bangui"
    },
    11: {
        "question": "What is the capital of Chad?",
        "answer": "N'Djamena"
    },
    12: {
        "question": "What is the capital of Comoros?",
        "answer": "Moroni"
    },
    13: {
        "question": "What is the capital of the Republic of the Congo?",
        "answer": "Brazzaville"
    },
    14: {
        "question": "What is the capital of the Democratic Republic of the Congo?",
        "answer": "Kinshasa"
    },
    15: {
        "question": "What is the capital of Djibouti?",
        "answer": "Djibouti city"
    },
    16: {
        "question": "What is the capital of Egypt?",
        "answer": "Cairo"
    },
    17: {
        "question": "What is the capital of Equatorial Guinea?",
        "answer": "Malabo" or "Oyala"
    },
    18: {
        "question": "What is the capital of Eritrea?",
        "answer": "Asmara"
    },
    19: {
        "question": "What is the capital of Eswatini?",
        "answer": "Mbabane" or "Lobamba"
    },
    20: {
        "question": "What is the capital of Ethiopia?",
        "answer": "Addis Ababa"
    },
    21: {
        "question": "What is the capital of Gabon?",
        "answer": "Libreville"
    },
    22: {
        "question": "What is the capital of Gambia?",
        "answer": "Banjul"
    },
    23: {
        "question": "What is the capital of Ghana?",
        "answer": "Accra"
    },
    24: {
        "question": "What is the capital of Guinea?",
        "answer": "Conakry"
    },
    25: {
        "question": "What is the capital of Guinea-Bissau?",
        "answer": "Bissau"
    },
    26: {
        "question": "What is the capital of Ivory Coast?",
        "answer": "Yamoussoukro"
    },
    27: {
        "question": "What is the capital of Kenya?",
        "answer": "Nairobi"
    },
    28: {
        "question": "What is the capital of Lesotho?",
        "answer": "Maseru"
    },
    29: {
        "question": "What is the capital of Liberia?",
        "answer": "Monrovia"
    },
    30: {
        "question": "What is the capital of Libya?",
        "answer": "Tripoli"
    },
    31: {
        "question": "What is the capital of Malawi?",
        "answer": "Lilongwe"
    },
    32: {
        "question": "What is the capital of Mali?",
        "answer": "Bamako"
    },
    33: {
        "question": "What is the capital of Mauritania?",
        "answer": "Nouakchott"
    },
    34: {
        "question": "What is the capital of Mauritius?",
        "answer": "Port Louis"
    },
    35: {
        "question": "What is the capital of Morocco?",
        "answer": "Rabat"
    },
    36: {
        "question": "What is the capital of Mozambique?",
        "answer": "Maputo"
    },
    37: {
        "question": "What is the capital of Namibia?",
        "answer": "Windhoek"
    },
    38: {
        "question": "What is the capital of Niger?",
        "answer": "Niamey"
    },
    39: {
        "question": "What is the capital of Nigeria?",
        "answer": "Abuja"
    },
    40: {
        "question": "What is the capital of Rwanda?",
        "answer": "Kigali"
    },
    41: {
        "question": "What is the capital of Sao Tome and Principe?",
        "answer": "Sao Tome"
    },
    42: {
        "question": "What is the capital of Senegal?",
        "answer": "Dakar"
    },
    43: {
        "question": "What is the capital of Seychelles?",
        "answer": "Victoria"
    },
    44: {
        "question": "What is the capital of Sierra Leone?",
        "answer": "Freetown"
    },
    45: {
        "question": "What is the capital of Somalia?",
        "answer": "Mogadishu"
    },
    46: {
        "question": "What is the capital of South Africa?",
        "answer": "Pretoria" or "Cape Town" or "Cape-Town" or "Bloemfontein"
    },
    47: {
        "question": "What is the capital of South Sudan?",
        "answer": "Juba"
    },
    48: {
        "question": "What is the capital of Sudan?",
        "answer": "Khartoum"
    },
    49: {
        "question": "What is the capital of Tanzania?",
        "answer": "Dodoma"
    },
    50: {
        "question": "What is the capital of Togo?",
        "answer": "Lomé" or "Lome"
    },
    51: {
        "question": "What is the capital of Tunisia?",
        "answer": "Tunis"
    },
    52: {
        "question": "What is the capital of Uganda?",
        "answer": "Kampala"
    },
    53: {
        "question": "What is the capital of Zambia?",
        "answer": "Lusaka"
    },
    54: {
        "question": "What is the capital of Zimbabwe?",
        "answer": "Harare"
    }
}


# def check_answer(question, ans, attempts, score):
#     if quiz[question]['answer'].lower() == ans.lower():
#         return True
#     else:
#         return False


# def print_dictionary():
#     for question_id, ques_answer in quiz.items():
#         for key in ques_answer:
#             print(key + ':', ques_answer[key])


# def introduction_message():
#     print("Welcome to this geography quiz! \nAre you ready to test your knowledge about Africa?")
#     print("There are a total of 55 questions, you can skip a question anytime by typing 'skip'")
#     input("Press enter to start the challenge! ")
#     return True

sg.theme('BlueMono')
question_number = 1
score = 0

layout = [[sg.Text('Welcome to the Africa Quiz!\nThis is a quiz with 55 questions'), sg.Text('\t   Score: '), sg.Text('0', key='score')],
          [sg.Image('africa.png')], # this is where i put the image
          [sg.Text('Question #:', key='numberLabel'), sg.Text(question_number, key='QuestionNumber'), sg.Text(key='Result')],
          [sg.Text(quiz[1]['question'], key='Question')],
          [sg.Input(key='input')],
          [sg.Button('Submit'), sg.Button('Skip')],
          ]

window = sg.Window('Africa Quiz', layout)


def next():
    global question_number
    question_number += 1
    window['score'].update(score)
    window['QuestionNumber'].update(question_number)
    window['Question'].update(quiz[question_number]['question'])


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Skip':
        next()
    if event == 'Submit':
        window['input'].update('')
        if question_number < 54:
            if quiz[question_number]['answer'].lower() == values['input'].lower():
                #window['Result'].update('\tCorrect answer! +1 points')
                score += 1
                next()
            else:
                #window['Result'].update('\tWrong answer')
                next()
        elif question_number == 54:
            if quiz[question_number]['answer'].lower() == values['input'].lower():
                score += 1
                window['score'].update(score)
            window['Question'].update('')
            window['numberLabel'].update('')
            window['QuestionNumber'].update('End of quiz. Your final score is: ' + str(score) + '/55')

window.close()

# intro = introduction_message()
# while True:
#     score = 0
#     for question in quiz:
#         attempts = 2
#         while attempts > 0:
#             print(quiz[question]['question'])
#             answer = input("Enter Answer (To move to the next question, type 'skip') : ")
#             if answer == "skip":
#                 break
#             check = check_answer(question, answer, attempts, score)
#             if check:
#                 score += 1
#                 break
#             attempts -= 1
#
#     break
#
# print(f"Your final score is {score}!\n\n")
#
#
