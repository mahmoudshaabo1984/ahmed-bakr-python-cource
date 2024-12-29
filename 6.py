 # A text that include spaces in the start and in the end
# print "I love python with spaces "
# text = "          I love python          "
# print(text)


# remove spaces from the txt
# This line will print the text without spaces
# text = "          I love python          "
# print(text.strip())


# other method to remove spaces from the txt
# Here we will create a variable called  full 
# text = "          I love python          "
# full = text.strip()
# print(full)


# remove sspaces from the left  of the txt 
# text = "          I love python          "
# print(text.lstrip())


# remove sspaces from the right  of the txt 
# text = "          I love python          "
# print(text.rstrip())

# A text that include a special characters
# text = "@@@@@@@@@@@@I love python######@@@@@@"
# print(text.strip())

# rmove the special characters from the text 
# text = "@@@@@@@@@@@@I love python######@@@@@@"
# print(text.strip("@#"))

# use the method center 
# name = "ahmed"
# print(name.center(25))

# Remove the spaces and put $instead of spaces
# name = "ahmed"
# print(name.center(25, "$"))


# using the method "Replace"
# This method replace the original word in the text to New word
# msg = "I love python , python is very easy "
# print(msg.replace("python", "php"))


# Replace "python two times"
# msg = "I love python , python is very easy python python python python "
# print(msg.replace("python", "php", 2))


# Replace "python 4  times"
# msg = "I love python , python is very easy python python python python "
# print(msg.replace("python", "php", 4))


# Replace "python 1  times"
# msg = "I love python , python is very easy python python python python "
# print(msg.replace("python", "php", 1))



# remove the word "python " from the text
# هنا سوف يتم حذف كلمة python من النص نهائيا 
# msg = "I love python , python is very easy python python python python "
# print(msg.replace("python", " "))


# using the method  index
# searching for the word "python " in the text 
# msg = "I love python , python is very easy python python python python "
# print(msg.index("python "))


# using the method  index
# searching for the character  "y" in the text 
# msg = "I love python , python is very easy python python python python "
# print(msg.index("y"))


# searching for the character  "y"  between the index 5 , 10
# msg = "I love python , python is very easy python python python python "
# print(msg.index("y", 5, 10))


# searching for the character  "y"  between the index 3, 6
# Here we will cause error because the string is not found in this area
# msg = "I love python , python is very easy python python python python "
# print(msg.index("y", 3, 6))



# using the method find
# It prints -1  no error
# msg = "I love python , python is very easy python python python python "
# print(msg.find("y", 3, 6))


# using the method find
# searching  between the index 3, 10  I will print 8
# msg = "I love python , python is very easy python python python python "
# print(msg.find("y", 3, 10))


# searching  between the index 3,  200 It will print 8
# msg = "I love python , python is very easy python python python python "
# print(msg.find("y", 3, 200))


# using the method start with 
# searching  between the index  3, 200  It will print False 
# this means that "y" does not find in these indexes 3 , 200
# msg = "I love python , python is very easy python python python python "
# print(msg.startswith("y", 3, 200))


# using the method start with 
# searching  between the index  8, 200  It will print True
# msg = "I love python , python is very easy python python python python "
# print(msg.startswith("y", 8, 200))


# using the method end with
# searching  between the index  8, 200  It will print False
# the text does not end of "y" now I  is going to print False 
# msg = "I love python , python is very easy python python python python "
# print(msg.endswith("y", 8, 200))


# using the method end with
# searching  between the index  5, 13  It will print True
# msg = "I love python , python is very easy python python python python "
# print(msg.endswith("n", 5, 13))



# using the method count 
# Count of the characters ofthe word python 6
# msg = "I love python , python is very easy python python python python "
# print(msg.count("python "))


# using the method count 
# searching  between the indexes  1 ,10 It will print 0
# Hear the interpreter could not able to count anything it’s returned0
# msg = "I love python , python is very easy python python python python "
# print(msg.count("python ", 1, 10))



# using the method count 
# searching  between the indexes  1 ,20 It will print 1
# msg = "I love python , python is very easy python python python python "
# print(msg.count("python ", 1, 20))


# using the method split 
# هذه الطريقة تقوم بتقسيم النصوص كقوائم lists 
# msg = "I love python , python is very easy python python python python "
# print(msg.split())
# print the type of split 
# print(type(msg.split()))


# using the method split 
# تقسيم النص بناءا على علامة -
# msg = "I love python , python is very easy python python python python "
# print(msg.split("-"))


# using the method split 
# تقسيم النص بناءا على علامة -
# msg = "I love -python , python is -very easy python python python -python "
# print(msg.split("-"))


# using the method maxsplit 
# مهمة هذه الطريقة تقسيم النص الى عدة قطع 
#  هنا قمنا بتقسيم النص الى 3 قطع 
# msg = "I love python , python is very easy python python python python "
# print(msg.split(maxsplit=3))



# strings formatting  the old method 
# هذه الطريقة القديمة ل strings formatting  
# name = "ahmed"
# age = 25
# rank = 10
#  TypeError: can only concatenate str (not "int") to str
#  هنا الخطء لا يمكن دمج int to str في دالة print 
# print("hi my name is"+name+"and my age is" +age)

# strings formatting  the old method 
# هنا سوف يعمل الكود لأني جعلت المتغير الثالث rank  "string
# # فيكون الكود على الشكل التالي "
# name = "ahmed"
# age = "25"
# rank = 10
# print("hi my name is"+name+"and my age is" +age)


# using strings formatting  the old method 
# هنا سوف نستخدم strings formatting  the old method  لتحويل int to string 
# name = "ahmed"
# age = 25
# rank = 10
# print("hi my name is %s and my age is%d"%(name,age))



# using strings formatting  the old method 
# اضافة المتغير rank الى الكود 
# name = "ahmed"
# age = 25
# rank = 10
# print("hi my name is %s and my age is%d and my rank is: %f"%(name,age,rank))



# التحكم بقيمة المتغير  rank (float) في الكود 
# على سبيل المثال التحكم بعدد الأصفار للمتغير rank 
# name = "ahmed bakr"
# age = 25
# rank = 10
# print("hi my name is %s and my age is%d and my rank is: %.1f"%(name,age,rank))




# التحكم في string في الكود 
# هنا سوفنتحكم في طريقة طباعة string عن طريقة strings formatting  the old method 
name = "ahmed bakr"
age = 25
rank = 10
print("hi my name is %.5s and my age is%d and my rank is: %.1f"%(name,age,rank))
