#طباعة الكلمة hello python بأستخدام الدالة print
# print("hello python ")
# print('ahmed bakr')
#\ سوف  تقوم بتخطي الحرف الذي بعد هذه العلامة 
# سوف يحدث خطئ
# print('ahme\d bakr')

#استخدام Escape Sequence Characters
# مثال يطبع كلمتين باستخدام Escape Sequence Characters
# print('ahmed bkar \'hello\'' )

# تكرار نفس المثال لكن باستخدام علمات التنصيص ""
# نستخدم مرة أخرى  Escape Sequence Characters
# print("ahmed bakr \"helo\"")


#كتابة علامة \\ مرتين لكي يعمل الكود بشكل صحيح 
# print("I like \\")
#print many words each word on a line 
#using \n لفصل الصطور 
# print(" i like \nyoutube and \nfacebook and \ntelegram")

#تخطي الصطور بأستخدام علامة \
# print("I like\
#       youtube\
#       facebook\
#       ")


#استخدام 3 علامات تنصيص """  
# للطباعة على ثلاثة صطور 
# print(""")I like
#       "facebook"
#       "youtube"
#       "telgram"
#       """)



#مثال للأستخدام  Escape Sequence Characters
# print("helo\b pytho\nn")
 

 #انشاء متغير جديد  
# user = 'ahmed bakr'
# print(user)


# Slicing and Indexing
# الحصول على  أول حرف
# user = 'ahmed bakr'
# print(user[0])


#طباعة الحرف الرابع 
# user = 'ahmed bakr'
# print(user[4])

#طباعة الحرف السادس b
# user = 'ahmed bakr'
# print(user[6])

# الحصول على آخر حرف  r
# user = 'ahmed bakr'
# print(user[-1])



# الحصول على الحرف الثاني h
# user = 'ahmed bakr'
# print(user[1])


# الحصر 
# طباعة الأحرف من 0 الى 5
# باستخدام الحصر 
# سوف يطبع ahmed 
# user = 'ahmedbakr'
# print(user[0:5])


#طباعة الأحرف من 0 الى 6 
# سوف يطبع ahmedb
# user = 'ahmedbakr'
# print(user[0:6])


#طباعة من 0 الى -1
# سوف يطبع ahmedbak
# user = 'ahmedbakr'
# print(user[0:-1])


#طباعة من 0:يطبعة ahmedbakr
# user = 'ahmedbakr'
# print(user[0:])

# طباعة من أول خمسة احرف
# سوف يطبع bakr
# user = 'ahmedbakr'
# print(user[5:])


# طباعة من 0 :61:
#سوف يطبع ahmedb
# user = 'ahmedbakr'
# print(user[0:6:1])


# طباعة من  0:6:2
# سوف يطبع amd
# user = 'ahmedbakr'
# print(user[0:6:2])


# الحصول على النص بالكامل بالعكس (التقطيع بالعكس)
# user = 'ahmedbakr'
# print(user[::-1])

# Concatenation 
# تحويل النص إلى حروف صغيرة (lowercase)
# msg = "hello Qais, and AHMED, and mahmoud"
# print(msg.lower())


# تحويل النص إلى حروف كبيرة (uppercase)
# msg = "hello Qais, and AHMED, and mahmoud"
# print(msg.upper())


# حساب طول النص
# msg = "hello Qais, and AHMED, and mahmoud"
# print(len(msg))


# تعريف نصوص إضافية
# دمج النصوص وجمعها 
#هنا سوف  يطبع النص بدون مسافات ahmedbakr
# one = "ahmed"
# two = "bakr"
# age = 25 
# print("hello"+one+two)


# دمج النصوص مع إضافة مسافة واحدة بين hello و one
# one = "ahmed"
# two = "bakr"
# age = 25 
# print("hello "+one+two)


# دمج النصوص مع إضافة مسافات بين الكلمات
# هنا سوف يطبع hello ahmed bakr مع مسافات بين الكلمات 
# one = "ahmed"
# two = "bakr"
# age = 25 
# print("hello"+" "+one+" "+two)


# محاولة دمج نصوص مع عدد (متغير age)
# هذا السطر يحتوي على خطأ لأن المتغير age نوعه int، ولا يمكن دمجه مع نصوص مباشرة باستخدام علامة +
# هذا السطر يحتوي على خطأ لأن المتغير age نوعه int، ولا يمكن دمجه مع نصوص مباشرة باستخدام علامة +
# في هذا الصطر سوف يحدث خطء 
# one = "ahmed"
# two = "bakr"
# age = 25 
# print('hello'+' '+one+' '+two+' your age is: '+ age)  
    
