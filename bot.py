import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["꽤나 흥미롭군요, 그거에 대해 계속 말해주세요.",
                    "알겠어요. 계속 해주세요",
                    "왜 그렇게 말하셨나요?",
                    "요즘 날씨가 참 특이해요. 그렇죠?",
                    "주제를 바꿔봐요.",
                    "어제 밤에 있던 경기 보셨나요?"]

print("안녕하세요, 저는 단순한 로봇 마빈이에요.")
print("언제든지 대화를 종료하고 싶으면 '안녕'을 입력하세요")
print("답변을 입력하시면 '엔터 키'를 눌러주세요")
print("오늘 기분 어떠신가요?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input == "안녕":
        # if they typed in '안녕', break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("즐거운 대화였어요, 안녕히 계세요!")
