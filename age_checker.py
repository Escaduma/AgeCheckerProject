def check_age(age):
    if age <0:
        raise ValueError("Age cannot be negative")
    if age>18 and age<60:
        return "Regular"
    if age<18:
        return "Child"
    if age>60 and age<=100:
        return "Senior"
    else:
        return "You are from another centuary!!!! :o"
    
# 1. Because it needs to tell what is wrong
# 2. Becaue it is easy to find and to work with when mistakes are made.

if __name__ == "__main__":
    user_age=int(input("Enter your age: "))
    result = check_age(user_age)
    print(result)

# 1. it helps to run the program in a easy way
# 2. because you do not have to do double work