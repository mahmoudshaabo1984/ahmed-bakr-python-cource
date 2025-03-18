

# Object-Oriented Programming
# البرمجة الكائنية 
# هنا سوف نقوم بأنشاء attribute داخل الكلاس  اسمه not_allowed_users 
# هذا ال attribute  عبارة عن قائمة  للكلمات التي لا يجوز للمستخدم التسجيل بها 
# هنا قمنا بالتحقق من هذا المتغير من الدالة GetFullInfo بأمر شرطي 
# وضضعنا في هذه الدالة  أمر شرطي وناديناه بأسم الكلاس  SiteMembers للتحقق 
# class SiteMembers:
#     not_allowed_users = ['hell', 'shit', 'hi', 'nacer', 'perfect', 'mester', 'zozo']

#     def __init__(self, fname, mname, lname, gender):
#         self.firstName = fname
#         self.middleName = mname
#         self.lastName = lname
#         self.gender = gender

#     def FullName(self):
#         return f"{self.firstName} {self.middleName} {self.lastName}"

#     def HelloUser(self):
#         if self.gender == "male":
#             return f"أهلا بك يا أستاذ {self.firstName}"
#         elif self.gender == "female":
#             return f"أهلا بكي يا أستاذة  {self.firstName}"
#         else:
#             return f"{self.firstName}"


#     def GetFullInfo(self):
#         if self.firstName in SiteMembers.not_allowed_users:
#             return f'هذا الأسم  {self.firstName} غير مسموح به'
#         else:
#             return f'{self.HelloUser()} و اسمك الثلاثي هو {self.FullName()}'

        

# member1 = SiteMembers('أحمد', 'بكر', 'محمد', 'male')
# member2 = SiteMembers('زينب', 'محمد', 'بهاء', 'female')
# member3 = SiteMembers('perfect', 'محمد', 'بها', 'female')

# print(member1.GetFullInfo())
# print(member2.GetFullInfo())
# print(member3.GetFullInfo())




# Object-Oriented Programming
# البرمجة الكائنية 
# هنا سوف نقوم بأنشاء attribute داخل الكلاس  اسمه not_allowed_users 
# هذا ال attribute  عبارة عن قائمة  للكلمات التي لا يجوز للمستخدم التسجيل بها 
# هنا قمنا بالتحقق من هذا المتغير من الدالة GetFullInfo بأمر شرطي 
# وضضعنا في هذه الدالة  أمر شرطي وناديناه بأسم الكلاس  SiteMembers للتحقق 
# هنا أنشءنا  attribute   بأسم attribute   
# وظيفة هذا attribute   معرفة عدد المستخدمين 
# وكانت النتيجة 0 , 3
# class SiteMembers:
#     not_allowed_users = ['hell', 'shit', 'hi', 'nacer', 'perfect', 'mester', 'zozo']
#     users_num = 0

#     def __init__(self, fname, mname, lname, gender):
#         self.firstName = fname
#         self.middleName = mname
#         self.lastName = lname
#         self.gender = gender
#         SiteMembers.users_num += 1

#     def FullName(self):
#         return f"{self.firstName} {self.middleName} {self.lastName}"

#     def HelloUser(self):
#         if self.gender == "male":
#             return f"أهلا بك يا أستاذ {self.firstName}"
#         elif self.gender == "female":
#             return f"أهلا بكي يا أستاذة  {self.firstName}"
#         else:
#             return f"{self.firstName}"


#     def GetFullInfo(self):
#         if self.firstName in SiteMembers.not_allowed_users:
#             return f'هذا الأسم  {self.firstName} غير مسموح به'
#         else:
#             return f'{self.HelloUser()} و اسمك الثلاثي هو {self.FullName()}'

# print(SiteMembers.users_num)

# member1 = SiteMembers('أحمد', 'بكر', 'محمد', 'male')
# member2 = SiteMembers('زينب', 'محمد', 'بهاء', 'female')
# member3 = SiteMembers('perfect', 'محمد', 'بها', 'female')

# print(SiteMembers.users_num)


# Object-Oriented Programming
# البرمجة الكائنية 
# هنا سوف نقوم بأنشاء attribute داخل الكلاس  اسمه not_allowed_users 
# هذا ال attribute  عبارة عن قائمة  للكلمات التي لا يجوز للمستخدم التسجيل بها 
# هنا قمنا بالتحقق من هذا المتغير من الدالة GetFullInfo بأمر شرطي 
# وضضعنا في هذه الدالة  أمر شرطي وناديناه بأسم الكلاس  SiteMembers للتحقق 
# هنا أنشءنا  attribute   بأسم attribute   
# وظيفة هذا attribute   معرفة عدد المستخدمين 
# وكانت النتيجة 0 , 3
# هنا أيضا طبعنا رسالة لمعرفة عدد المستخدمين 
# class SiteMembers:
#     not_allowed_users = ['hell', 'shit', 'hi', 'nacer', 'perfect', 'mester', 'zozo']
#     users_num = 0

#     def __init__(self, fname, mname, lname, gender):
#         self.firstName = fname
#         self.middleName = mname
#         self.lastName = lname
#         self.gender = gender
#         SiteMembers.users_num += 1

#     def FullName(self):
#         return f"{self.firstName} {self.middleName} {self.lastName}"

#     def HelloUser(self):
#         if self.gender == "male":
#             return f"أهلا بك يا أستاذ {self.firstName}"
#         elif self.gender == "female":
#             return f"أهلا بكي يا أستاذة  {self.firstName}"
#         else:
#             return f"{self.firstName}"


#     def GetFullInfo(self):
#         if self.firstName in SiteMembers.not_allowed_users:
#             return f'هذا الأسم  {self.firstName} غير مسموح به'
#         else:
#             return f'{self.HelloUser()} و اسمك الثلاثي هو {self.FullName()}'

# print(f'عدد المستخدمين هو {SiteMembers.users_num} مستخدمين')

# member1 = SiteMembers('أحمد', 'بكر', 'محمد', 'male')
# member2 = SiteMembers('زينب', 'محمد', 'بهاء', 'female')
# member3 = SiteMembers('perfect', 'محمد', 'بها', 'female')

# print(f'عدد المستخدمين هو {SiteMembers.users_num} مستخدمين')




# Object-Oriented Programming
# البرمجة الكائنية 
# هنا سوف نقوم بأنشاء attribute داخل الكلاس  اسمه not_allowed_users 
# هذا ال attribute  عبارة عن قائمة  للكلمات التي لا يجوز للمستخدم التسجيل بها 
# هنا قمنا بالتحقق من هذا المتغير من الدالة GetFullInfo بأمر شرطي 
# وضضعنا في هذه الدالة  أمر شرطي وناديناه بأسم الكلاس  SiteMembers للتحقق 
# هنا أنشءنا  attribute   بأسم attribute   
# وظيفة هذا attribute   معرفة عدد المستخدمين 
# وكانت النتيجة 0 , 3
# هنا أيضا طبعنا رسالة لمعرفة عدد المستخدمين 
# هنا أعدنا كتابة الكود مرة أخرى للتوضيح 
# وفككنا التهميش عن بعض الأكواد 
# class SiteMembers:
#     not_allowed_users = ['hell', 'shit', 'hi', 'nacer', 'perfect', 'mester', 'zozo']
#     users_num = 0

#     def __init__(self, fname, mname, lname, gender):
#         self.firstName = fname
#         self.middleName = mname
#         self.lastName = lname
#         self.gender = gender
#         SiteMembers.users_num += 1

#     def FullName(self):
#         return f"{self.firstName} {self.middleName} {self.lastName}"

#     def HelloUser(self):
#         if self.gender == "male":
#             return f"أهلا بك يا أستاذ {self.firstName}"
#         elif self.gender == "female":
#             return f"أهلا بكي يا أستاذة  {self.firstName}"
#         else:
#             return f"{self.firstName}"


#     def GetFullInfo(self):
#         if self.firstName in SiteMembers.not_allowed_users:
#             return f'هذا الأسم  {self.firstName} غير مسموح به'
#         else:
#             return f'{self.HelloUser()} و اسمك الثلاثي هو {self.FullName()}'



# print(f'عدد المستخدمين هو {SiteMembers.users_num} مستخدمين')

# member1 = SiteMembers('أحمد', 'بكر', 'محمد', 'male')
# member2 = SiteMembers('زينب', 'محمد', 'بهاء', 'female')
# member3 = SiteMembers('perfect', 'محمد', 'بها', 'female')

# print(member1.GetFullInfo())
# print(member2.GetFullInfo())
# print(member3.GetFullInfo())

# print(f'عدد المستخدمين هو {SiteMembers.users_num} مستخدمين')


# Object-Oriented Programming
# البرمجة الكائنية 
# هنا قد قمنا بأنشاء دالة method في الكلاس  SiteMembers وظيفة هذه الدالة حذف 
# مستخدمين اسم الدالة هو  del_user
# class SiteMembers:
#     not_allowed_users = ['hell', 'shit', 'hi', 'nacer', 'perfect', 'mester', 'zozo']
#     users_num = 0

#     def __init__(self, fname, mname, lname, gender):
#         self.firstName = fname
#         self.middleName = mname
#         self.lastName = lname
#         self.gender = gender
#         SiteMembers.users_num += 1

#     def FullName(self):
#         return f"{self.firstName} {self.middleName} {self.lastName}"

#     def HelloUser(self):
#         if self.gender == "male":
#             return f"أهلا بك يا أستاذ {self.firstName}"
#         elif self.gender == "female":
#             return f"أهلا بكي يا أستاذة  {self.firstName}"
#         else:
#             return f"{self.firstName}"


#     def GetFullInfo(self):
#         if self.firstName in SiteMembers.not_allowed_users:
#             return f'هذا الأسم  {self.firstName} غير مسموح به'
#         else:
#             return f'{self.HelloUser()} و اسمك الثلاثي هو {self.FullName()}'
#     def del_user(self):
#         SiteMembers.users_num -= 1
#         return f'المستخدم {self.firstName} قد تم حذفه'



# print(f'عدد المستخدمين هو {SiteMembers.users_num} مستخدمين')

# member1 = SiteMembers('أحمد', 'بكر', 'محمد', 'male')
# member2 = SiteMembers('زينب', 'محمد', 'بهاء', 'female')
# member3 = SiteMembers('zozo', 'محمد', 'بها', 'female')

# print(member1.GetFullInfo())
# print(member2.GetFullInfo())
# print(member3.del_user())

# print(f'عدد المستخدمين هو {SiteMembers.users_num} مستخدمين')



# Object-Oriented Programming
# البرمجة الكائنية 
# هنا قمنا بأنشاء method في الكلاس SiteMembers 
# اسم هذهال method : staticmethod
# class SiteMembers:
#     not_allowed_users = ['hell', 'shit', 'hi', 'nacer', 'perfect', 'mester', 'zozo']
#     users_num = 0
#     @staticmethod
#     def HiUser():
#         print(f'أهلا بك في موقعنا')


#     def __init__(self, fname, mname, lname, gender):
#         self.firstName = fname
#         self.middleName = mname
#         self.lastName = lname
#         self.gender = gender
#         SiteMembers.users_num += 1

#     def FullName(self):
#         return f"{self.firstName} {self.middleName} {self.lastName}"

#     def HelloUser(self):
#         if self.gender == "male":
#             return f"أهلا بك يا أستاذ {self.firstName}"
#         elif self.gender == "female":
#             return f"أهلا بكي يا أستاذة  {self.firstName}"
#         else:
#             return f"{self.firstName}"


#     def GetFullInfo(self):
#         if self.firstName in SiteMembers.not_allowed_users:
#             return f'هذا الأسم  {self.firstName} غير مسموح به'
#         else:
#             return f'{self.HelloUser()} و اسمك الثلاثي هو {self.FullName()}'
#     def del_user(self):
#         SiteMembers.users_num -= 1
#         return f'المستخدم {self.firstName} قد تم حذفه'

# member1 = SiteMembers('أحمد', 'بكر', 'محمد', 'male')
# member2 = SiteMembers('زينب', 'محمد', 'بهاء', 'female')
# member3 = SiteMembers('zozo', 'محمد', 'بها', 'female')

# print(SiteMembers.HiUser())



#  Object-Oriented Programming
#  البرمجة الكائنية 
#  هنا انشءنا method في الكلاس SiteMembers اسمها classmethod
#  ههذه الطريقة تأخذ معامل أجباري اسمه cls 
# class SiteMembers:
#     not_allowed_users = ['hell', 'shit', 'hi', 'nacer', 'perfect', 'mester', 'zozo']
#     users_num = 0
#     @staticmethod
#     def HiUser():
#         print(f'أهلا بك في موقعنا')
#     @classmethod
#     def ShowUsersCount(cls):
#         print(f'عدد المستخدمين في موقعك هو {SiteMembers.users_num} من المستخدمين')



#     def __init__(self, fname, mname, lname, gender):
#         self.firstName = fname
#         self.middleName = mname
#         self.lastName = lname
#         self.gender = gender
#         SiteMembers.users_num += 1

#     def FullName(self):
#         return f"{self.firstName} {self.middleName} {self.lastName}"

#     def HelloUser(self):
#         if self.gender == "male":
#             return f"أهلا بك يا أستاذ {self.firstName}"
#         elif self.gender == "female":
#             return f"أهلا بكي يا أستاذة  {self.firstName}"
#         else:
#             return f"{self.firstName}"


#     def GetFullInfo(self):
#         if self.firstName in SiteMembers.not_allowed_users:
#             return f'هذا الأسم  {self.firstName} غير مسموح به'
#         else:
#             return f'{self.HelloUser()} و اسمك الثلاثي هو {self.FullName()}'
#     def del_user(self):
#         SiteMembers.users_num -= 1
#         return f'المستخدم {self.firstName} قد تم حذفه'




# member1 = SiteMembers('أحمد', 'بكر', 'محمد', 'male')
# member2 = SiteMembers('زينب', 'محمد', 'بهاء', 'female')
# member3 = SiteMembers('zozo', 'محمد', 'بها', 'female')

# print(SiteMembers.ShowUsersCount())



#  Object-Oriented Programming
# البرمجة الكائنية 
# هنا اردنا ان نعرف ما يحصل في لغة بيثون في الخلفية 
# بدءت بيثون في الكلاس ثم الطريقة method  GetFullInfo
# ثم المعامل وهو المتغير المثيل  الذي حمل الكلاس SiteMembersmember1
# class SiteMembers:
#     not_allowed_users = ['hell', 'shit', 'hi', 'nacer', 'perfect', 'mester', 'zozo']
#     users_num = 0
#     @staticmethod
#     def HiUser():
#         print(f'أهلا بك في موقعنا')
#     @classmethod
#     def ShowUsersCount(cls):
#         print(f'عدد المستخدمين في موقعك هو {SiteMembers.users_num} من المستخدمين')



#     def __init__(self, fname, mname, lname, gender):
#         self.firstName = fname
#         self.middleName = mname
#         self.lastName = lname
#         self.gender = gender
#         SiteMembers.users_num += 1

#     def FullName(self):
#         return f"{self.firstName} {self.middleName} {self.lastName}"

#     def HelloUser(self):
#         if self.gender == "male":
#             return f"أهلا بك يا أستاذ {self.firstName}"
#         elif self.gender == "female":
#             return f"أهلا بكي يا أستاذة  {self.firstName}"
#         else:
#             return f"{self.firstName}"


#     def GetFullInfo(self):
#         if self.firstName in SiteMembers.not_allowed_users:
#             return f'هذا الأسم  {self.firstName} غير مسموح به'
#         else:
#             return f'{self.HelloUser()} و اسمك الثلاثي هو {self.FullName()}'
#     def del_user(self):
#         SiteMembers.users_num -= 1
#         return f'المستخدم {self.firstName} قد تم حذفه'


# member1 = SiteMembers('أحمد', 'بكر', 'محمد', 'male')
# member2 = SiteMembers('زينب', 'محمد', 'بهاء', 'female')
# member3 = SiteMembers('zozo', 'محمد', 'بها', 'female')

# print(SiteMembers.GetFullInfo(member1))



#  Object-Oriented Programming
# البرمجة الكائنية 
# هنا اردنا ان نعرف ما يحصل في لغة بيثون في الخلفية 
# بدءت بيثون في الكلاس ثم الطريقة method  GetFullInfo
# ثم المعامل وهو المتغير المثيل  الذي حمل الكلاس SiteMembersmember1
# هنا كانت نفس النتيجة في الطباعة حتى ولو أستخدمنا هذا الصطر 
# print(member1.GetFullInfo())

# class SiteMembers:
#     not_allowed_users = ['hell', 'shit', 'hi', 'nacer', 'perfect', 'mester', 'zozo']
#     users_num = 0
#     @staticmethod
#     def HiUser():
#         print(f'أهلا بك في موقعنا')
#     @classmethod
#     def ShowUsersCount(cls):
#         print(f'عدد المستخدمين في موقعك هو {SiteMembers.users_num} من المستخدمين')



#     def __init__(self, fname, mname, lname, gender):
#         self.firstName = fname
#         self.middleName = mname
#         self.lastName = lname
#         self.gender = gender
#         SiteMembers.users_num += 1

#     def FullName(self):
#         return f"{self.firstName} {self.middleName} {self.lastName}"

#     def HelloUser(self):
#         if self.gender == "male":
#             return f"أهلا بك يا أستاذ {self.firstName}"
#         elif self.gender == "female":
#             return f"أهلا بكي يا أستاذة  {self.firstName}"
#         else:
#             return f"{self.firstName}"


#     def GetFullInfo(self):
#         if self.firstName in SiteMembers.not_allowed_users:
#             return f'هذا الأسم  {self.firstName} غير مسموح به'
#         else:
#             return f'{self.HelloUser()} و اسمك الثلاثي هو {self.FullName()}'
#     def del_user(self):
#         SiteMembers.users_num -= 1
#         return f'المستخدم {self.firstName} قد تم حذفه'


# member1 = SiteMembers('أحمد', 'بكر', 'محمد', 'male')
# member2 = SiteMembers('زينب', 'محمد', 'بهاء', 'female')
# member3 = SiteMembers('zozo', 'محمد', 'بها', 'female')

# print(member1.GetFullInfo())
# print(SiteMembers.GetFullInfo(member1))

# Object-Oriented Programming
# البرمجة الكائنية 
# وظيفة هذه ال function "dir" جلب كل العناصر في الكلاس 
# print(dir(str()))



# Object-Oriented Programming
# البرمجة الكائنية 
# MyName = 'ahmed'
# print(MyName.upper())



# Object-Oriented Programming
# البرمجة الكائنية 
# هنا نقوم بمعرفة ماذا يحصل في الخلفية في python 
# هذا الصطر يوضح ما ذا يحصل في الخلفية في أمر الطباعة 
# تكون نفس النتيجة 
# AHMED
# AHMED
# MyName = 'ahmed'
# print(MyName.upper())
# print(str.upper(MyName))



# Object-Oriented Programming
# البرمجة الكائنية 
# هنا نقوم بمعرفة ماذا يحصل في الخلفية في python 
# حيث تكون نفس النتيجة حتى ولو غيرنا تنسيق الكود 
# فتكون نتيجة الطباعة على الشكل التالي 
# AHMED
# PERFECT
# MyName = 'ahmed'
# print(MyName.upper())
# MyName = 'Perfect'
# print(str.upper(MyName))

