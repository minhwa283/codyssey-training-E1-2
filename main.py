def show_menu():
    print("\n===== 세계 여러 나라 퀴즈 게임 =====")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 최고 점수")
    print("0. 종료")


def main():
    show_menu()



#__name__ : Python이 자동으로 만들어 주는 특별한 변수 Python 파일을 실행하는 방식에 따라 값이 달라진다.
#__main__ : python3 main.py로 직접 실행 / main 다른 Python 파일에서 import main

#이 파일을 직접 실행했을 때만 main() 함수를 실행해라
#다른 Python 파일에서 이 파일을 import하면 main()까지 자동으로 실행되지 않도록 처리
#(Python은 다른 파일을 처음 import할 때 그 파일의 최상위 코드도 실행하기 때문)

# 파이썬은 위에서 아래로 로드 후 실행 이 로직이 위로 올라가면 main 메서드 못찾아서 NameError: name 'main' is not defined 오류 발생
if __name__ == "__main__":
    main()
