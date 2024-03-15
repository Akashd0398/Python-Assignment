class Mulfuncs():
    def Subfields():
        print("Sub-fields in AI are:")
        lists = ["Machine Learning","Neural Networks","Vision,Robotics","Speech Processing","Natural Language Processing"]
        for subfieldsinAi in lists:
            print(subfieldsinAi)
            
    def OddEven():
        Number = int(input("Enter a number:"))
        if(Number%2==0):
            Message = print(Number,"is even number")
        else:
            Message = print(Number,"is odd number")
        return Message
        
    def Elegible():
        Gender = input("Your Gender : ")
        Age = int(input("Your Age : "))
        if(Gender == "Male"):
            if(Age > 21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif(Gender == "Female"):
            if(Age > 18):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
                
    def Percentage():
        Subject1 = int(input("Subject 1 : "))
        Subject2 = int(input("Subject 2 : "))
        Subject3 = int(input("Subject 3 : "))
        Subject4 = int(input("Subject 4 : "))
        Subject5 = int(input("Subject 5 : "))
        Total = Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total : ",Total)
        Percentage = (Total/500)*100
        print("Percentage = ",Percentage)
        return Percentage
        
    def Triangle():
        Height = int(input("Height : "))
        Breadth = int(input("Breadth : "))
        Area = (Height*Breadth)/2
        print("Area of triangle = (Height*Breadth)/2")
        print("Area of triange : ",Area)
        Height1 = int(input("Height1 : "))
        Height2 = int(input("Height2 : "))
        Breadth2 = int(input("Breadth2 : "))
        Perimeter = Height1+Height2+Breadth2
        print("Perimeter of triangle = Height1+Height2+Breadth2")
        print("Perimeter of Triangle : ",Perimeter)