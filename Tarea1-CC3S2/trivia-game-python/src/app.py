from Question import Question
from Quiz import Quiz
from questions_for_quiz import questions_for_quiz
def run_quiz():
    print("Bienvenido al Juego de Trivia!")
    print("Responde las siguientes preguntas seleccionando el número de la opción correcta.")
    quiz = Quiz() #Se inicia el quiz
    for q in questions_for_quiz:
        question = Question(q["description"], q["options"], q["correct_answer"]) 
        quiz.add_question(question) #Agregamos las preguntas a la lista
    while quiz.current_question_index < 10:
        question =  quiz.get_next_question()
        if question:
            print(question.description)
            for idx, option in enumerate (question.options):
                print(f"{idx+1}. {option}")
            answer = input("Tu respuesta: ")
            if (quiz.answer_question(question,answer)):
                print("¡Correcto!")
            else: print("Incorrecto.")
        else: 
            break

    print("Juego terminado.")
    print(f"Preguntas contestadas: {quiz.current_question_index}")
    print(f"Respuestas correctas: {quiz.correct_answers}")
    print(f"Respuestas incorrectas: {quiz.incorrect_answers}")
    
if __name__=="__main__":
    run_quiz()

    