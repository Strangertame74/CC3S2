class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer
    def is_correct(self, answer):
        return self.correct_answer == answer

class Quiz:
    def __init__(self):
        self.questions=[]
        self.current_question_index=0
    def add_question(self,question):
        self.questions.append(question)
    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None
    def run_quiz():
        quiz = Quiz()
        while quiz.current_question_index < 10:
            question = quiz.get_next_question()
            if question:
                print(question.description)
                for idx, option in enumerate(question.options):
                    print(f"{idx + 1}) {option}")
                answer = input("Tu respuesta: ")
                if quiz.answer_question(question, answer):
                    print("¡Correcto!")
                else:
                    print("Incorrecto.")
            else:
                break
        print(f"Juego terminado. Respuestas correctas: {quiz.correct_answers}, incorrectas:{quiz.incorrect_answers}")
    