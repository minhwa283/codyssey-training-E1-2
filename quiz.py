## Date : 2026-11-11
## Author : imminhwa
## Description : 개별 퀴즈의 문제, 선택지, 정답 데이터를 관리하는 클래스

       
# 퀴즈 문제 하나를 관리하는 클래스
class Quiz:

    # 퀴즈 객체가 생성될 때 실행되는 초기화 메서드
    def __init__(self, question, options, answer):
        self.question = question  # 문제
        self.options = options    # 보기 4개
        self.answer = answer      # 정답 번호

    # 문제와 보기 출력
    def show_question(self):
        print(f"\n문제: {self.question}")

        for index, option in enumerate(self.options, start=1):
            print(f"{index}. {option}")

    # 사용자의 답이 정답인지 확인
    def check_answer(self, user_answer):
        return user_answer == self.answer
