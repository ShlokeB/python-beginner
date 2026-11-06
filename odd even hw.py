
def even():
    count=0
    for i in range(5):
        
        num= int(input("Enter a number: "))
        if num%2==0:
            count +=1
            print('The number is even')
        else:
            print('The number is odd')
    print(count)


even()
