import webbrowser
import time

marks = [3,5,4,1,4,5,3,3,2,5,2,1,4,4,1,5,5,4,4,4,5,3,1,4,3,2,1,2,5,3,1,3,4,1,1,1,2,2,1,3,1,5,2,2,5,2,3,5,5,4]
i = 0
n = 0
T = 0
F = 0
N = 0
name = "Untitled Marks"

print("\n\t Sujested Answers For A/L ICT 2022(2023) MCQ paper\n\n")

print("HELP \n\tenter your marks 1-5 \n\tempty marks for enter 0")

name = input("\tEnter Your Name : ")
print("\n")
while True:
    n = n + 1
    ym = input(f"enter your marks of mcq quection number {n} : ")
    if str(marks[i]) == str(ym):
        T = T + 1
        print("Correct Mark is enterd! ")
    elif str(ym) == "0":
        print(str(marks[i]) + " is correct answer")
        N = N + 1
    else:
        print(str(marks[i]) + " is correct answer")
        F = F + 1

    if str(n) == "50":
        f = open(name + ".txt", "w")
        f.write(f"\nYour Correct Marks \t : {T} \nYour Wrone Marks \t : {N} \nYour Correct Marks \t : {N} \n\nDeveloped by : 2023 @ Alpha Ceph\nPlease protect the rights created!\nhttps://www.youtube.com/@BugAntProgrammer")
        f.close()

        print("\n_______________________________________________")
        print(f"Your Correct Marks count is \t: {T}")
        print(f"Your Wrong Marks count is \t: {F}")
        print(f"Your Empty Marks count is \t: {N}")
        print("_______________________________________________")
        input("Press Enter For The Exit \n")
        webbrowser.open('https://www.youtube.com/@BugAntProgrammer')
        print("Please protect the rights created!\nDeveloped by : 2023 ⓒ Alpha Ceph")
        
        time.sleep(5)
        break

    i = i + 1
