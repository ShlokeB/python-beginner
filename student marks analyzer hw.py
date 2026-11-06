def check_grade():
    math = int(input("Enter math marks"))
    if math>=40 :
        print("Pass")
    else:
        print("Fail")
    science = int(input("Enter science marks"))
    if science>=40 :
        print("Pass")
    else:
        print("Fail")
    english = int(input("Enter englsih marks"))
    if english>=40 :
        print("Pass")
    else:
        print("Fail")
    social_science = int(input("Enter sst marks"))
    if social_science>=40 :
        print("Pass")
    else:
        print("Fail")
    hindi = int(input("Enter hindi marks"))
    if hindi>=40 :
        print("Pass")
    else:
        print("Fail")
    total=math+science+hindi+english+social_science
    average=total/5 
    print ("total = ", (total))
    print("average =", (average))



check_grade()

