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

    # 기본 퀴즈 5문항 등록
    def load_default_quizzes(self):
        self.add_quiz(
            "대한민국의 수도는?",
            ["부산", "서울", "대구", "인천"],
            2
        )

        self.add_quiz(
            "일본의 수도는?",
            ["오사카", "교토", "도쿄", "후쿠오카"],
            3
        )

        self.add_quiz(
            "프랑스의 수도는?",
            ["파리", "런던", "로마", "베를린"],
            1
        )

        self.add_quiz(
            "브라질이 위치한 대륙은?",
            ["유럽", "아시아", "남아메리카", "아프리카"],
            3
        )

        self.add_quiz(
            "이집트의 수도는?",
            ["카이로", "나이로비", "아테네", "마드리드"],
            1
        )

    # 퀴즈 풀기
    def play(self):
        self.score = 0

        for quiz in self.quizzes:
            quiz.show_question()

            # 사용자 정답 입력
            user_input = input("정답 번호를 입력하세요 (1~4): ").strip()

            # 숫자 입력 확인
            if user_input not in ("1", "2", "3", "4"):
                print("잘못된 입력입니다. 오답 처리합니다.")
                continue

            # 정답 확인
            if quiz.check_answer(int(user_input)):
                print("정답입니다!")
                self.score += 20
            else:
                print("오답입니다.")

        # 최종 점수 출력
        print(f"\n퀴즈 종료! 최종 점수: {self.score}점")

    # 사용자가 직접 퀴즈를 추가하는 메서드
    def input_quiz(self):
        print("\n===== 퀴즈 추가 =====")

        # 문제 입력
        question = input("문제를 입력하세요: ").strip()

        # 보기 4개 입력
        options = []

        for i in range(1, 5):
            option = input(f"{i}번 보기를 입력하세요: ").strip()
            options.append(option)

        # 정답 번호 입력
        while True:
            answer = input("정답 번호를 입력하세요 (1~4): ").strip()

            if answer in ("1", "2", "3", "4"):
                break

            print("잘못된 입력입니다. 1~4 중에서 선택하세요.")

        # 퀴즈 등록
        self.add_quiz(question, options, int(answer))

        print("퀴즈가 추가되었습니다!")
    