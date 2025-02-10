


# انشاء  دالة تحتوي على معامل واحد 
# def say_hello(name):
#     print(f'hello {name}')

# say_hello('ahmed')


# انشاء دالة بأسمة say_hello
# تحتوي على 4 معاملات وتحتوي على قائمة بأربع عناصر 
# ولوب for 
# هنا سوف يحدث خطء  لأننا وضعنا اتفيقتين 
# وهي تحتاج الى 4 اتفقيات لكي تعمل عند  أستدعاها 
# def say_hello(n1, n2, n3, n4):
#     users = ['ahmed', 'mahmoud', 'qais', 'hero']
#     for user in users:
#         print(f' hello {user}')

# say_hello('ahmed', 'qais')


# انشاء دالة بأسمة say_hello
# تحتوي على 4 معاملات وتحتوي على قائمة بأربع عناصر 
# ولوب for 
# هنا سوف يعمل الكود لأننا اضفنا 
# الأتفقيات الأربعة 
# def say_hello(n1, n2, n3, n4):
#     users = ['ahmed', 'mahmoud', 'qais', 'hero']
#     for user in users:
#         print(f' hello {user}')

# say_hello('ahmed', 'qais', 'hero', 'mahmoud')


# انشاء دالة بأسمة say_hello
# هنا نريد ان نضيف عناصر لكنن لا نعرف عددها 
# نستخدم * onpack  نضع متغير في الدالة 
# مع علامة * 
# def say_hello(*users):
#     for user in users:
#         print(f' hello {user}')

# say_hello('ahmed', 'qais', 'hero', 'mahmoud')


# هنا قمنا باضافة zozo 
# def say_hello(*users):
#     for user in users:
#         print(f' hello {user}')

# say_hello('ahmed', 'qais', 'hero', 'mahmoud', 'zozo')


# هنا قمنا بأضافة nacer
# def say_hello(*users):
#     for user in users:
#         print(f' hello {user}')

# say_hello('ahmed', 'qais', 'hero', 'mahmoud', 'zozo', 'nacer')


# هنا وضعنا اسم واحد ahmed 
# def say_hello(*users):
#     for user in users:
#         print(f' hello {user}')

# say_hello('ahmed')



# انشاء دالة بأسم show_skills
# مثال ثاني لأستخدام * inpack 
# هنا وضعنا المهرات للمستخدم ahmed
# def show_skills(name, *skills):
#     print(f'hello {name}, \nyour skills is: ')
#     for skill in skills:
#         print(skill)

# show_skills('ahmed', 'html', 'css', 'php')


# انشاء دالة بأسم show_skills
# هنا وضعنا المهارات للمستخدم qais
# وزودنا المهارات 
# def show_skills(name, *skills):
#     print(f'hello {name}, \nyour skills is: ')
#     for skill in skills:
#         print(skill)

# show_skills('qais', 'html', 'css', 'php', 'dart', 'java')


# انشاء دالة بأسم show_skills
# هنا وضعنا المهارات للمستخدم qais
# وزودنا المهارات 
#  هنا طبعنا نوع المعامل skills
# يكون نوعه مصفوفة tuple
# def show_skills(name, *skills):
#     print(type(skills))
#     print(f'hello {name}, \nyour skills is: ')
#     for skill in skills:
#         print(skills)

# show_skills('qais', 'html', 'css', 'php', 'dart')

# انشاء دالة بأسم show_skills
# هنا وضعنا المهارات للمستخدم ahmed
# وزودنا المهارات 
# def show_skills(name, *skills):
#     print(f"Hello {name} Your Skills Is: ")
#     for skill in skills:
#         print(skill)

# show_skills('ahmed', 'html', 'css', 'php', 'dart', 'flutter')


# انشاء دالة بأسم show_skills
# هنا اذا اردنا ان نمرر عناصر عن طريق القاموس 
# يجب علينا ان نضع علامة النجمة مرتين ** 
# قبل المعامل skills في الدالة 
# هنا سوف يحدث خطء لاننا مررنا 4 أتفقيات 
# عند أستدعاء الدالة مع انننها تحتاج الى 
# اتفاقية واحدة لكي يعمل الكود 
# def show_skills(name, **skills):
#     print(f"Hello {name} Your Skills Is: ")
#     for skill_k, skill_v in skills.items():
#         print(f'{skill_k} -> {skill_v}')

# show_skills('qais', 'html', 'css', 'php', 'dart')


# انشاء دالة بأسم show_skills
# هنا وضعنا المستخدم  qais 
# مع مهارته والمستوى الذي وصل اليه فيها 
# def show_skills(name, **skills):
#     print(f"Hello {name} Your Skills Is: ")
#     for skill_k, skill_v in skills.items():
#         print(f'{skill_k} -> {skill_v}')

# show_skills('qais', js='50%')


# انشاء دالة بأسم show_skills
# هنا وضعنا المستخدم  qais 
# مع مهارته والمستوى الذي وصل اليه فيها 
# هنا زودنا مهارة جديدة ل qais  html='99
# ووضعنا مستواه فيها 
# def show_skills(name, **skills):
#     print(f"Hello {name} Your Skills Is: ")
#     for skill_k, skill_v in skills.items():
#         print(f'{skill_k} -> {skill_v}')

# show_skills('qais', js='50%', html='99%')

# هنا وضعنا المستخدم mahmoud 
# مع 3 مهارات والمستوى الذي وصل اليه في كل مهارة 
# python='90%' php='80%' js='40%')
# def show_skills(name, **skills):
#     print(f"Hello {name} Your Skills Is: ")
#     for skill_k, skill_v in skills.items():
#         print(f'{skill_k} -> {skill_v}')

# show_skills('mahmoud', python='90%', php='80%', js='40%')




# انشاء قاموس خارج الدالة show_skills بأسم skills 
# هنا سوف يعمل القاموس بشكل صحيح 
# اذا وضعنا علامة ** مرتين قبل الأتفاقية  skills
# عند أستدعاء الدالة 
# skills = {
#     'html': '100%',
#     'python': '100%',
#     'css': '20%',
#     'dart': '40%',
#     'flutter': '30%',
#     'java': '1%',
# }
# def show_skills(name, **skills):
#     print(f"Hello {name} Your Skills Is: ")
#     for skill_k, skill_v in skills.items():
#         print(f'{skill_k} -> {skill_v}')

# show_skills('ahmed', **skills)



# انشاء قاموس خارج الدالة show_skills بأسم skills 
# هنا ولو حذفنا مفتحين وقيمتين من القاموس سوف يعمل 
# الكود بشكل صحيح 
# skills = {
#     'html': '100%',
#     'python': '100%',
#     'dart': '40%',
#     'flutter': '30%',
# }    
# def show_skills(name, **skills):
#     print(f"Hello {name} Your Skills Is: ")
#     for skill_k, skill_v in skills.items():
#         print(f'{skill_k} -> {skill_v}')

# show_skills('ahmed', **skills)



# scoop النطاق
# if name == 'ahmed':
#     print('hello ahmed')

# scoop النطاق
# x = 50
# print(x)

# scoop النطاق
# هنا عندما حاولنا طباعة المتغير 
#  x خارج نطاق الدالة 
# حدث خطء 
# NameError name 'x' is not defined
# هذا يعني لا ييمكن طباعة المتغير 
# خارج حدود الدالة 
# def num():
#     x = 20

# print(x)


# scoop النطاق
# هنا سوف يعمل الكود 
# لأننا طبعنا المتغير x داخل نطاق الدالة 
# def num():
#     x = 20
#     print(x)

# num()


# scoop النطاق
# هنا بدء بالطباعة من داخل الدالة ثم خارجها 
# x = 50

# def num():
#     x = 20
#     print(x)

# print(x)
# num()
# print(x)


# اذا اردنا ان نطبع المتغير خارج النطاق 
# نضع الدالة global 
# x = 50

# def num():
#     global x
#     x = 20

#     print(x)

# print(x)
# num()
# print(x)


# استخدام scoop مع النصوص 
# هنا طابع خارج الدالة اولا 
# ثم طبع داخل الدالة مرتين 
# بأستخدام المتغير  global 
# x = 'أنا خارج الدالة'
# def num():
#     global x
#     x = 'أنا داخل الدالة'
#     print(x)

# print(x)
# num()
# print(x)


# استخدام scoop مع النصوص 
# x = 'أنا خارج الدالة'
# def num():
#     global x
#     x = 'أنا داخل الدالة'
#     print(x)
# print(x)
# num()
# print(x)
# x = 'أنا خارج الدالة'
# print(x)


# استخدام lambda function 
# وظيفة هذه الدالة تنفيذ أمر على الطاير 
# ملاحظة في أمر الطباعة نطبع الدالة وليس المتغير 
# my_function = lambda: 'hello ahmed'
# print(my_function())

# استخدام lambda function 
# هنا سوف نطبع نوع الدالة my_function()
# فيكون نوعها  'str'>
# my_function = lambda: 'hello ahmed'
# print(my_function())
# print(type(my_function()))


# استخدام lambda function 
# هنا سوف نطبع نوع الدالة my_function()
# فيكون نوعها  'str'>
# هنا ايضا سوف نقوم بطباعة نوع الدالة all
#  الدالة all هي  من الدوال المبنية في بيثون 
# فيكون نوعها 
# 'builtin_function_or_method'
# my_function = lambda: 'hello ahmed'
# print(my_function())
# print(type(my_function()))
# print(type(all)) 

# استخدام lambda function 
# هنا سوف نقوم بطباعة نوع الدالة  my_function
# فيكون نوعها function
# my_function = lambda: 'hello ahmed'
# print(my_function())
# print(type(my_function))



