## Date : 2026-11-11
## Author : imminhwa
## Description : 
## 구현 기능 :          

from quiz import Quiz


# 퀴즈 게임 진행을 관리하는 클래스
class QuizGame:

    # 게임 객체를 생성할 때 실행
    def __init__(self):
        self.score = 0
        self.quizzes = []

    # 게임에 퀴즈 문제 추가
    def add_quiz(self, question, options, answer):
        quiz = Quiz(question, options, answer)
        # append 리스트 맨 뒤에 데이터 하나 추가
        self.quizzes.append(quiz)

    # 현재 점수 출력
    def show_score(self):
        print(f"현재 점수: {self.score}")
