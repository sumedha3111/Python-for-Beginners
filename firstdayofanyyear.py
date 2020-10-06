#Contributed by Mastermind.
#Check out his website : https://codexwithmastermind.wixsite.com/codex

def check_leap(year):
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

def main(year , dayg , yearc):          #Enter the given year(int) , first day of given year(str) , the year whose first day is required(int)
    n,diff=0,0
    for i in range(len(days)):
        if dayg.lower()==days[i]:
            n=i
    for i in range(year,yearc):
        if check_leap(i):
            diff+=2
        else:
            diff+=1

    n+=diff%7
    return(days[n%7])


print(main(2000,'saturday' , 3001))
