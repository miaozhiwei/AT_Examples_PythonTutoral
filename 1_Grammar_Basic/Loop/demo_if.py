i = int(input("Enter a score(0~100): "))

if i >= 100:
    print("the score is %d. mark : S " % i)
elif i >= 90:
    print("the score is %d. mark : A " % i)
elif i >= 80:
    print("the score is %d. mark : B " % i)
elif i >= 70:
    print("the score is %d. mark : C " % i)
elif i >= 60:
    print("the score is %d. mark : D " % i)
else:
    print("the score is %d. NO MARK " % i)
