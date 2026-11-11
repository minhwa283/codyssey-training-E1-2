## Date : 2026-11-11
## Author : imminhwa
## Description : 세계 여러 나라 퀴즈 게임
## 구현 기능 : 메뉴 번호 입력 및 반복 출력, 잘못된 번호·문자·빈 입력 처리, 0 입력 시 종료, Ctrl+C/D 입력 시 정상 종료              
from quiz_game import QuizGame

def show_menu():
    print("\n===== 세계 여러 나라 퀴즈 게임 =====")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 최고 점수")
    print("0. 종료")


def main():
     # 게임 객체 생성
    game = QuizGame()

    # 기본 퀴즈 5문항 등록
    game.load_default_quizzes()
     
     #사용자가 종료를 선택하기 전까지 퀴즈 게임 메뉴를 계속 보여주기 위함
    while True:
        show_menu()

        try:
            #.strip() 앞뒤 공백제거
            choice = input("메뉴 번호를 선택하세요: ").strip()
       
            if choice == "0":
                print("게임을 종료합니다.")
                break

            elif choice == "1":
                game.play()

            elif choice == "2":
                game.input_quiz()

            elif choice == "3":
                game.show_quiz_list()

            elif choice == "4":
                game.show_high_score()

            else:
              print("잘못된 입력입니다. 다시 선택하세요.")
            
        #KeyboardInterrupt Ctrl+C로 실행을 중단할 때 발생하는 예외 
        #EOFError Ctrl+D 등으로 입력이 종료될 때 발생하는 예외
        except (KeyboardInterrupt, EOFError):
            print("\n게임을 종료합니다.")
            break


# JSON 저장 기능 테스트
from quiz_game import QuizGame

test_game = QuizGame()
test_game.load_default_quizzes()
test_game.high_score = 80

test_game.save_state()

#__name__ : Python이 자동으로 만들어 주는 특별한 변수 Python 파일을 실행하는 방식에 따라 값이 달라진다.
#__main__ : python3 main.py로 직접 실행 / main 다른 Python 파일에서 import main

#이 파일을 직접 실행했을 때만 main() 함수를 실행해라
#다른 Python 파일에서 이 파일을 import하면 main()까지 자동으로 실행되지 않도록 처리
#(Python은 다른 파일을 처음 import할 때 그 파일의 최상위 코드도 실행하기 때문)

# 파이썬은 위에서 아래로 로드 후 실행 이 로직이 위로 올라가면 main 메서드 못찾아서 NameError: name 'main' is not defined 오류 발생
if __name__ == "__main__":
    main()

    
