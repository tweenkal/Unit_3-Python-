# 👉Write a programe to show method overloading to find sum of two or
#   three numbers.


class myclass:
    def sum(self,a = None , b = None , c  = None):
        if a != None and b != None and c != None:
            print("Sum of three numbers:",(a+b+c))

        elif a != None and b != None:
            print("Sum of two numbers:",(a+b))

        else:
            print("Please enter 2 or 3 arguments")

m = myclass()
m.sum(10,15,20)
m.sum(30,50)
m.sum(100)

#output:-
# Sum of three numbers: 45
# Sum of two numbers: 80
# Please enter 2 or 3 arguments
