again = 'yes'
while again == 'yes':
    right: int = 0
    wrong: int = 0

    question1 = input("year of birthday Alfred Hitchcock: ")  # 1899
    if question1 == "1899":
        print("bingo")
        right += 1
    else:
        print("no it not")
        wrong += 1

    question2 = input("year of birthday Dean Koontz: ")  # 1945
    if question2 == "1945":
        print("bingo")
        right += 1
    else:
        print("no it not")
        wrong += 1

    question3 = input("year of birthday Stephen King: ")  # 1947
    if question3 == "1947":
        print("bingo")
        right += 1
    else:
        print("no it not")
        wrong += 1

    question4 = input("year of birthday Howard Phillips Lovecraft: ")  # 1890
    if question4 == "1890":
        print("bingo")
        right += 1
    else:
        print("no it not")
        wrong += 1

    question5 = input("year of birthday James Herbert: ") # 1943
    if question5 == "1943":
        print("bingo")
        right += 1
    else:
        print("no it not")
        wrong += 1

    print("bingo", right)
    print("mistake", wrong)
    print("bingo", right * 100 / 5, "percent")
    print("mistake", wrong * 100 / 5, "percent")

    again = input("lets try again?")  # yes,no
