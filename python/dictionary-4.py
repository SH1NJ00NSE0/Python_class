from tkinter.font import families


dic={"위험":"설사 뭐시기",
     "경고":"조리도구뭐시기",
     "주의":"조리음식 뭐시기",
     "관심":"화장실 뭐시기"}

num=int(input())

if num>=86:
   print(dic.get("위험"))
elif num>=71:
   print(dic.get("경고"))
elif num>=55:
   print(dic.get("주의"))
else:
   print(dic.get("관심"))