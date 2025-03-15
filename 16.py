




# Object-Oriented Programming
# البرمجة الكائنية 
# هنا أنشءنا كلاس  بأسم SiteMembers
# وداخل هذه الكلاس أنشءنا دالة بأسم  __init__( تحتوي على معامل أجباري 
# يسمى self هذا المعامل أجباري لمنادات المتغيرات  attributes 
# هذا attributes self حمل بداخله other attributes يسمى name 
# ثم قمنا بمناداة الكلاس attributes جديد 
# وطبعناه 
# class SiteMembers():
#     def __init__(self):
#         self.name = 'ahmed'

# member_one = SiteMembers()
# print(member_one.name)



# Object-Oriented Programming
# البرمجة الكائنية 
# هنا أنشءنا كلاس  بأسم SiteMembers
# وداخل هذه الكلاس أنشءنا دالة بأسم  __init__( تحتوي على معامل أجباري 
# يسمى self هذا المعامل أجباري لمنادات المتغيرات  attributes 
# هذا attributes self حمل بداخله other attributes يسمى name 
# ثم قمنا بمناداة الكلاس attributes جديد 
# وطبعناه 
# هنا قمنا بمنادا الكلاس  SiteMembers 3 مرات بأنشاء 3  attributes  
# وكانت نفس النتيجة بطباعة ahmed 3مرات 
# class SiteMembers():
#     def __init__(self):
#         self.name = 'ahmed'

# member1 = SiteMembers()
# member2 = SiteMembers()
# member3 = SiteMembers()

# print(member1.name)
# print(member2.name)
# print(member3.name)



# Object-Oriented Programming
# البرمجة الكائنية 
# هنا أنشءنا كلاس  بأسم SiteMembers
# وداخل هذه الكلاس أنشءنا دالة بأسم  __init__( تحتوي على معامل أجباري 
# يسمى self هذا المعامل أجباري لمنادات المتغيرات  attributes 
# هنا في داخل الدالة __init__( وبعدما كانت تحتوي عىل معامل أجباري 
# يسمى self قمنا بتمرير  3 معاملين 
# fname, mname, lname 
# وقام المعامل الأجباري بحمل 3  attributes   
# self.frastName = fname
#self.frastName = fname
#  self.medlName = mname
#   self.LastName = lname
# class SiteMembers():
#     def __init__(self, fname, mname, lname):
#         self.frastName = fname
#         self.medlName = mname
#         self.LastName = lname

# member1 = SiteMembers('محمد', 'بكر', 'احمد')
# member2 = SiteMembers('يونس', 'بكر', 'محمد')
# member3 = SiteMembers('منذر', 'بكر', 'محمد')

# print(member1.frastName, member1.medlName, member1.LastName)
# print(member2.frastName, member2.LastName)
# print(member3.LastName)



# Object-Oriented Programming
# البرمجة الكائنية 
# هنا أنشءنا كلاس  بأسم SiteMembers
# وداخل هذه الكلاس أنشءنا دالة بأسم  __init__( تحتوي على معامل أجباري 
# يسمى self هذا المعامل أجباري لمنادات المتغيرات  attributes 
# وقمنا بأنشاء دالة  باسم FullName 
# وظيفة هذه الدالة طبعة الأسم كامل 
# class SiteMembers:
#     def __init__(self, fname, mname, lname):
#         self.firstName = fname
#         self.middleName = mname
#         self.lastName = lname

#     def FullName(self):
#         return f"{self.firstName} {self.middleName} {self.lastName}"

# member1 = SiteMembers('أحمد', 'بكر', 'محمد')
# member2 = SiteMembers('يوسف', 'بكر', 'محمد')
# member3 = SiteMembers('زينب', 'بكر', 'محمد')
# member4 = SiteMembers('بهاء', 'محمد', 'محمد')

# print(member1.FullName())
# print(member2.firstName, member2.lastName)
# print(member3.lastName)


# Object-Oriented Programming
# البرمجة الكائنية 
# هنا أنشءنا كلاس  بأسم SiteMembers
# وداخل هذه الكلاس أنشءنا دالة بأسم  __init__( تحتوي على معامل أجباري 
# يسمى self هذا المعامل أجباري لمنادات المتغيرات  attributes 
# وقمنا بأنشاء دالة  باسم FullName 
# وظيفة هذه الدالة طبعة الأسم كامل 
# وقمنا بأنشاء دالة باسم HelloUser
# وظيفة هذه الدالة طباعة Hello قبل الأسم 
# class SiteMembers:
#     def __init__(self, fname, mname, lname):
#         self.firstName = fname
#         self.middleName = mname
#         self.lastName = lname

#     def FullName(self):
#         return f"{self.firstName} {self.middleName} {self.lastName}"

#     def HelloUser(self):
#         return f"hello Mr: {self.firstName}"

# member1 = SiteMembers('أحمد', 'محمد', 'بكر')
# member2 = SiteMembers('يوسف', 'محمد', 'بكر')
# member3 = SiteMembers('محمد', 'أحمد', 'بكر')
# member4 = SiteMembers('زينب', 'محمد', 'بكر')

# print(member1.HelloUser())
# print(member4.HelloUser())





# Object-Oriented Programming
# البرمجة الكائنية 
# هنا أنشءنا كلاس  بأسم SiteMembers
# وداخل هذه الكلاس أنشءنا دالة بأسم  __init__( تحتوي على معامل أجباري 
# يسمى self هذا المعامل أجباري لمنادات المتغيرات  attributes 
# وقمنا بأنشاء دالة  باسم FullName 
# وظيفة هذه الدالة طبعة الأسم كامل 
# وقمنا بأنشاء دالة باسم HelloUser
# وظيفة هذه الدالة طباعة Hello قبل الأسم 
# في هذه الدالة HelloUser استخدمنا أمر شرطي للتحقق هل اسم 
# زينب ذكر أو أنثى 
# class SiteMembers:
#     def __init__(self, fname, mname, lname, gender):
#         self.firstName = fname
#         self.middleName = mname
#         self.lastName = lname
#         self.gender = gender

#     def FullName(self):
#         return f"{self.firstName} {self.middleName} {self.lastName}"

#     def HelloUser(self):
#         if self.gender == "male":
#             return f"hello Mr: {self.firstName}"
#         elif self.gender == "female":
#             return f"hello Ms: {self.firstName}"
#         else:
#             return f"{self.firstName}"

# member1 = SiteMembers('أحمد', 'محمد', 'بكر', 'male')
# member2 = SiteMembers('يوسف', 'محمد', 'بكر', 'male')
# member3 = SiteMembers('زينب', 'محمد', 'بكر', 'female')
# member4 = SiteMembers('زينب', 'بهاء', 'محمد', 'female')

# print(member1.HelloUser())
# print(member4.HelloUser())



# Object-Oriented Programming
# البرمجة الكائنية 
# هنا أنشءنا كلاس  بأسم SiteMembers
# وداخل هذه الكلاس أنشءنا دالة بأسم  __init__( تحتوي على معامل أجباري 
# يسمى self هذا المعامل أجباري لمنادات المتغيرات  attributes 
# وقمنا بأنشاء دالة  باسم FullName 
# وظيفة هذه الدالة طبعة الأسم كامل 
# وقمنا بأنشاء دالة باسم HelloUser
# وظيفة هذه الدالة طباعة Hello قبل الأسم 
# في هذه الدالة HelloUser استخدمنا أمر شرطي للتحقق هل اسم 
# زينب ذكر أو أنثى 
# هنا أنشءنا دالة بأسم GetFullInfo 
# وظيفة هذه الدالة ان تأخذ المعلومات كاملة من المستخدم 
# class SiteMembers:
#     def __init__(self, fname, mname, lname, gender):
#         self.firstName = fname
#         self.middleName = mname
#         self.lastName = lname
#         self.gender = gender

#     def FullName(self):
#         return f"{self.firstName} {self.middleName} {self.lastName}"

#     def HelloUser(self):
#         if self.gender == "male":
#             return f"hello Mr: {self.firstName}"
#         elif self.gender == "female":
#             return f"hello Ms: {self.firstName}"
#         else:
#             return f"{self.firstName}"


#     def GetFullInfo(self):
#         return f' {self.HelloUser()} اسمك الثلاثي هو {self.FullName()}'
        


# member1 = SiteMembers('أحمد', 'محمد', 'بكر', 'male')
# member2 = SiteMembers('يوسف', 'محمد', 'بكر', 'male')
# member3 = SiteMembers('زينب', 'محمد', 'بكر', 'female')
# member4 = SiteMembers('زينب', 'بهاء', 'محمد', 'female')


# print(member1.GetFullInfo())
# print(member4.GetFullInfo())

