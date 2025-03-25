



# Object-Oriented Programming
# البرمجة الكائنية 
# مفهوم الوراثة بين الكلاسات 
# هنا أنشءنا كلاسين 
# الكلاس الآول بأسم bakr
# والكلاس الثاني بأسم ahmed
# وأنشءنا دالة في الكلاس الآول وهو كلاس الأب 
# هذه الدالة بأسم GetFullInfo
# class bakr():
#     def __init__(self):
#         print('هذه رسالة من class الأب!')

#     def GetFullInfo(self):
#         print('اسمي هو: بكر محمد، وعمري هو: 60 عاما؛ وهذه رسالة من class الأب')

# class ahmed():
#     def __init__(self):
#         print('هذه رسالة من class الإبن!')

# name1 = bakr()
# name2 = ahmed()



# Object-Oriented Programming
# البرمجة الكائنية 
# مفهوم الوراثة بين الكلاسات 
# هنا أنشءنا كلاسين 
# الكلاس الآول بأسم bakr
# والكلاس الثاني بأسم ahmed
# وأنشءنا دالة في الكلاس الآول وهو كلاس الأب 
# هذه الدالة بأسم GetFullInfo
# هنا قمنا بطباعة معلومات الدالة GetFullInfo في الكلاس الأب 
# class bakr():
#     def __init__(self):
#         print('هذه رسالة من class الأب!')

#     def GetFullInfo(self):
#         print('اسمي هو: بكر محمد، وعمري هو: 60 عاما؛ وهذه رسالة من class الأب')

# class ahmed():
#     def __init__(self):
#         print('هذه رسالة من class الإبن!')

# name1 = bakr()
# name2 = ahmed()
# name1.GetFullInfo()


# Object-Oriented Programming
# البرمجة الكائنية 
# مفهوم الوراثة بين الكلاسات 
# هنا أنشءنا كلاسين 
# الكلاس الآول بأسم bakr
# والكلاس الثاني بأسم ahmed
# وأنشءنا دالة في الكلاس الآول وهو كلاس الأب 
# هذه الدالة بأسم GetFullInfo
# هنا قمنا بطباعة معلومات الدالة GetFullInfo في الكلاس الأب 
# هنا سوف يحدث خطء اذا اردنا ان نطبع الدالة  GetFullInfo  في الكلاس الإبن 
# لانها ليست موجودة أصلا الخطء هو 
# AttributeError: 'ahmed' object has no attribute 'GetFullInfo'
# class bakr():
#     def __init__(self):
#         print('هذه رسالة من class الأب!')

#     def GetFullInfo(self):
#         print('اسمي هو: بكر محمد، وعمري هو: 60 عاما؛ وهذه رسالة من class الأب')

# class ahmed():
#     def __init__(self):
#         print('هذه رسالة من class الإبن!')

# name1 = bakr()
# name2 = ahmed()
# name1.GetFullInfo()
# name2.GetFullInfo()



# Object-Oriented Programming
# البرمجة الكائنية 
# مفهوم الوراثة بين الكلاسات 
# هنا أنشءنا كلاسين 
# الكلاس الآول بأسم bakr
# والكلاس الثاني بأسم ahmed
# وأنشءنا دالة في الكلاس الآول وهو كلاس الأب 
# هذه الدالة بأسم GetFullInfo
# هنا قمنا بنجاح بطباعة الدالة GetFullInfo في الكلاس الأبن ahmed 
# بحيث وضعنا اسم الكلاس الأب bakr في قوسين الكلاس الإبن ahmed 
# class bakr():
#     def __init__(self):
#         print('هذه رسالة من class الأب!')

#     def GetFullInfo(self):
#         print('اسمي هو: بكر محمد، وعمري هو: 60 عاما؛ وهذه رسالة من class الأب')

# class ahmed(bakr):
#     def __init__(self):
#         print('هذه رسالة من class الإبن!')

# name1 = bakr()
# name2 = ahmed()
# name1.GetFullInfo()
# name2.GetFullInfo()



# Object-Oriented Programming
# البرمجة الكائنية 
# مفهوم الوراثة بين الكلاسات 
# هنا طبعنا هذا الصطر 
# print(f'أسمي هو : {self.name} , وعمري هو : {self.age} عامأ , وهذه رسالة من class الأب')
# من دون الدالة GetFullInfo
# class bakr():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('هذه رسالة من class الأب!')
#         print(f'أسمي هو : {self.name} , وعمري هو : {self.age} عامأ , وهذه رسالة من class الأب')


# class ahmed(bakr):
#     def __init__(self):
#         print('هذه رسالة من class الإبن!')

# name1 = bakr('بكر', '61')



# Object-Oriented Programming
# البرمجة الكائنية 
# مفهوم الوراثة بين الكلاسات 
# اذا اردنا ان نورث البيانات من الكلاس الأب الى الكلاس الإبن
# نقوم بتعريف البيانات مرة أخرى في كلاس ahmed 
# في دالة  __init__(
# في كلاس الإبن 
# class bakr():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('هذه رسالة من class الأب!')        
#         print(f'أسمي هو : {self.name} , وعمري هو : {self.age} عامأ , وهذه رسالة من class الأب')


# class ahmed(bakr):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         print('هذه رسالة من class الإبن!')

# name1 = bakr('بكر', '61')
# name2 = ahmed('ahmed', '25')



# Object-Oriented Programming
# البرمجة الكائنية 
# مفهوم الوراثة بين الكلاسات 
# اذا اردنا ان نورث البيانات من الكلاس الأب الى الكلاس الإبن
# نقوم بتعريف البيانات مرة أخرى في كلاس ahmed 
# في دالة  __init__(
# في كلاس الإبن 
# هنا أنشءنا اتربيوت في كلاس الإبن ahmed 
# class bakr():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('هذه رسالة من class الأب!')
#         print(f'أسمي هو : {self.name} , وعمري هو : {self.age} عامأ , وهذه رسالة من class الأب')

# class ahmed(bakr):
#     def __init__(self , name, age, website):
#         self.web = website
#         super().__init__(name, age)
#         print('هذه رسالة من class الإبن!')
#         print(f'أسمي هو : {self.name} , وعمري هو : {self.age} عامأ , وموقعي الشخصي هو {self.web}')


# name2 = ahmed('ahmed', '25', 'https://tecwindow.net')



# Object-Oriented Programming
# البرمجة الكائنية 
# مفهوم الوراثة بين الكلاسات 
# هنا سوف يحدث خطء لأنه لا يمكننا أستخدام الورااثة العكسية بين الكلاسات 
# الخطء هو:
# TypeError: bakr.__init__() takes 3 positional arguments but 4 were given
# class bakr():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('هذه رسالة من class الأب!')
#         print(f'أسمي هو : {self.name} , وعمري هو : {self.age} عامأ , وهذه رسالة من class الأب')

# class ahmed(bakr):
#     def __init__(self , name, age, website):
#         self.web = website
#         super().__init__(name, age)
#         print('هذه رسالة من class الإبن!')
#         print(f'أسمي هو : {self.name} , وعمري هو : {self.age} عامأ , وموقعي الشخصي هو {self.web}')


# name1 = bakr('بكر', '61', 'https://tecwindow.net')



# Object-Oriented Programming
# البرمجة الكائنية 
# مفهوم الوراثة بين الكلاسات 
# هنا عملنا over ride بين الكلاسات 
# class bakr():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age    
#     def fullName(self):
#         print('أهلا بكم في دالة الكلاس الأول')

# class ahmed(bakr):
#     def __init__(self , name, age, website):
#         self.web = website
#         super().__init__(name, age)
#         print('هذه رسالة من class الإبن!')
#         print(f'أسمي هو : {self.name} , وعمري هو : {self.age} عامأ , وموقعي الشخصي هو {self.web}')

# name1 = bakr('بكر', '61')
# name2 = ahmed('ahmed', '25', 'https://tecwindow.net')
# name1.fullName()
# name2.fullName()


# Object-Oriented Programming
# البرمجة الكائنية 
# مفهوم الوراثة بين الكلاسات 
# هنا عملنا over ride بين الكلاسات 
# هنا حدثنا البيانات في الكلاس الإبن بحيث نسخنا الدالة  fullName الموجودة في الكلاس الأب
# الى الكلاس الثاني كلاس الإبن 
# class bakr():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age    
#     def fullName(self):
#         print('أهلا بكم في دالة الكلاس الأول')

# class ahmed(bakr):
#     def __init__(self , name, age, website):
#         self.web = website
#         super().__init__(name, age)
#         print('هذه رسالة من class الإبن!')
#         print(f'أسمي هو : {self.name} , وعمري هو : {self.age} عامأ , وموقعي الشخصي هو {self.web}')
#     def fullName(self):
#         print('أهلا بكم في دالة الكلاس الثاني')

# name1 = bakr('بكر', '61')
# name2 = ahmed('ahmed', '25', 'https://tecwindow.net')
# name1.fullName()
# name2.fullName()



# Object-Oriented Programming
# البرمجة الكائنية 
# مفهوم الوراثة بين الكلاسات 
# هنا قمنا بأنشاء 3 كلاسات الكلاس الأول بأسم one 
# والكلاس الثاني بأسم two
# والكلاس الثالث بأسم ahmed
# الفكرة هنا نريد ان نجعل الكلاس ahmed يرث من الكلاسين one and  two
# هنا بدءت الوراثة من كلاس one وبعدها أنتهت الوراثة عند الكلاس two
# class one():
#     def __init__(self):
#         print('أهلا بك في class 1')

# class two():
#     def __init__(self):
#         print('أهلا بك في class 2')

# class ahmed(one, two):
#     pass

# name = ahmed() 


# Object-Oriented Programming
# البرمجة الكائنية 
# مفهوم الوراثة بين الكلاسات 
# هنا قمنا بأنشاء 3 كلاسات الكلاس الأول بأسم one 
# والكلاس الثاني بأسم two
# والكلاس الثالث بأسم ahmed
# الفكرة هنا نريد ان نجعل الكلاس ahmed يرث من الكلاسين one and  two
# هنا بدءت الوراثة عند الكلاس two 
# وأنتهت الوراثة عند الكلاس one 
# لأننا بدلنا أماكن المعاملين قصدي الكلاسات one and two في الكلاس الثالث ahmed
# class one():
#     def __init__(self):
#         print('أهلا بك في class 1')

# class two():
#     def __init__(self):
#         print('أهلا بك في class 2')

# class ahmed(two, one):
#     pass

# name = ahmed() 


# Object-Oriented Programming
# البرمجة الكائنية 
# مفهوم الوراثة بين الكلاسات 
# هناك method تعرفنا ترتيب الوراثة بين الكلاسات 
# اسم هذ الطريقة mro()
# class one():
#     def __init__(self):
#         print('أهلا بك في class 1')

# class two():
#     def __init__(self):
#         print('أهلا بك في class 2')

# class ahmed(two, one):
#     pass

# print(ahmed.mro())


# Object-Oriented Programming
# البرمجة الكائنية 
# مفهوم الوراثة بين الكلاسات 
# هناك طريقة  أيضا للوراثة بين الكلاسات 
# بحيث ننشء في كل كلاس one and two دالة 
# class one  اسم الدالة functionOne
# class two اسم الدالة functionTwo
# class one():
#     def __init__(self):
#         print('أهلا بك في class 1')
#     def functionOne(self):
#         print('hello one')

# class two():
#     def __init__(self):
#         print('أهلا بك في class 2')
#     def functionTwo(self):
#         print('hello two')

# class ahmed(two, one):
#     pass

# name = ahmed()
# name.functionTwo()



# Object-Oriented Programming
# البرمجة الكائنية 
# مفهوم الوراثة بين الكلاسات 
# نفس الطريقة للتوريث بين الكلاسات لكن كتبنا الكود مرة أخرى للتوضيح 
# class one():
#     def __init__(self):
#         print('أهلا بك في class 1')
#     def functionOne(self):
#         print('hello one من الكلاس الرئيسي')

# class two(one):
#     def __init__(self):
#         print('أهلا بك في class 2')
#     def functionTwo(self):
#         print('hello two بعد أن تم التوريث من الكلاس الأول')

# class ahmed(two):
#     pass

# name = ahmed()
# name.functionOne()
# name.functionTwo()


