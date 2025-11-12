# answers = ["Kannada","Maths","Darshan","Lawyer","kannada","maths","darshan","lawyer"]
# print("It's A small quiz, like confirming your Information are right")


# ques1 = "What is your Mother Tounge?\nA)English     B)Telugu\nC)Kannada     D)Tamil"
# print(ques1)
# answer = input("Enter your Answer:")
# if answer in answers:
#     print("Let's go to 2nd question")
# else:
#     print("No you'r quite wrong")

# ques2 = "What is your Favourite Subject?\nA)Maths              B)Science\nC)Social Science     D)Hindi"
# print(ques2)
# answer = input("Enter your Answer:")
# if answer in answers:
#     print("Let's go to 3rd question")
# else:
#     print("No you'r quite wrong")

# ques3 = "What is your Name?\nA)Darshan       B)Puneeth\nC)Yashwanth     D)Priya"
# print(ques3)
# answer = input("Enter your Answer:")
# if answer in answers:
#     print("Let's go to 4th question")
# else:
#     print("No you'r quite wrong")

# ques4 = "Which Job are you doing?\nA)Doctor          B)Engineer\nC)Teacher     D)Lawyer"
# print(ques4)
# answer = input("Enter your Answer:")
# if answer in answers:
#     print("Verification is Complete, Thank You...")
# else:
#     print("No you'r quite wrong")


questions = [
    ["What is the capital of India?","Bengalore","Hyberabad","Dehli","Sri Lanka",3],
    ["Who Invented Python?","Guido van Rossum","James Cameron","Putin","Trump",1],
    ["Which is largest animal in these?","cat","dog","rat","elephant",4],
    ["What is sqaure of 12?","1212","24","144","114",3],
    ["Which element has the symbol of O","Nitrogen","Oxygen","Oil","Osmiun",2],
    ["Which exam is consider for MBBS","NEET","KCET","DCET","JEE",1],
    ["Which language is used to create Facebook","Php","Python","C#","C++",1],
    ["What is Mother Tounge in karnataka","Tamil","Tamil","Kannada","Marati",3],
    ["Who is CEO of Google","Mark Zukerberg","Jeff Bezos","Elon Musk","Sundar Pichai",4],
    ["Which of the following is Elon's Company","Meta","Tesla","Mahindra","Threads",2],

]

levels = [1000,2000,3000,5000,10000,20000,50000,80000,150000,300000]
money = 0

for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs.{levels[i]}")
    print(question[0])
    print(f"1. {question[1]}          2. {question[2]}")
    print(f"3. {question[3]}          4. {question[4]}")

    # try:
    #     reply = int(input("Enter your answer (1-4) or 0 to quit:"))
    reply = int(input("Enter your answer (1-4) or 0 to quit:"))
    if(reply<0 or reply>4):
        raise ValueError("Options should be 1 to 4")
    
    if reply == 0:
        money = levels[i-1]if i > 0 else 0
        break
    if reply == question[-1]:
        print(f"Correct! You have won Rs. {levels[i]}")

    else:
        print("Wrong Anwser")
        break
    
print(f"Your take-home money is Rs. {money}")
       
    
