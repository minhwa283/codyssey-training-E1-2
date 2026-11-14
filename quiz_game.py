## Date : 2026-11-11
## Author : imminhwa
## Description : 퀴즈 추가, 목록 조회, 게임 실행, 점수 및 데이터 저장 등 게임 전체 기능을 관리하는 클래스

import json
from pathlib import Path

from quiz import Quiz


# 퀴즈 게임 진행을 관리하는 클래스
class QuizGame:

    # 게임 객체를 생성할 때 실행
    def __init__(self):
        self.score = 0
        self.high_score = 0  # 최고 점수
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
                # 브랜치 테스트
                print(f"정답은 {quiz.answer}번입니다.")

        # 최종 점수 출력
        print(f"\n퀴즈 종료! 최종 점수: {self.score}점")

          # 최고 점수 갱신
        if self.score > self.high_score:
           self.high_score = self.score
           print("새로운 최고 점수입니다!")


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

    # 등록된 퀴즈 목록 출력
    def show_quiz_list(self):
        print("\n===== 퀴즈 목록 =====")

        # 등록된 퀴즈가 없는 경우
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        # 등록된 퀴즈를 순서대로 출력
        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n{index}번 문제")
            quiz.show_question()
            print(f"정답 번호: {quiz.answer}")

    # 최고 점수 조회
    def show_high_score(self):
        print(f"\n최고 점수: {self.high_score}점")

    # 게임 데이터를 JSON 파일에 저장
    def save_state(self):
        data = {
            "high_score": self.high_score,
            "quizzes": []
        }

        # 퀴즈 객체를 저장 가능한 데이터로 변환
        for quiz in self.quizzes:
            data["quizzes"].append({
                "question": quiz.question,
                "options": quiz.options,
                "answer": quiz.answer
            })

        # 프로젝트 폴더의 state.json에 저장
        file_path = Path(__file__).resolve().parent / "state.json"

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("게임 데이터가 저장되었습니다.")


    # JSON 파일에서 게임 데이터 불러오기
    def load_state(self):
        file_path = Path(__file__).resolve().parent / "state.json"

        # 저장된 파일이 없으면 기본 문제 등록
        if not file_path.exists():
            self.load_default_quizzes()
            return

        # JSON 파일 읽기
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            # 저장된 최고 점수 복원
            self.high_score = data["high_score"]

            # 저장된 퀴즈 문제 복원
            self.quizzes = []

            for item in data["quizzes"]:
                self.add_quiz(
                    item["question"],
                    item["options"],
                    item["answer"]
                )

            print("저장된 게임 데이터를 불러왔습니다.")

        except (OSError, ValueError, KeyError, TypeError):
            print("저장된 데이터를 읽을 수 없어 기본 문제를 불러옵니다.")
            self.high_score = 0
            self.quizzes = []
            self.load_default_quizzes()    