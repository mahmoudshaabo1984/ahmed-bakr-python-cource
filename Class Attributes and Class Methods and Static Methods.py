class SiteMembers:
    # قائمة تحتوي على أسماء غير مسموح بها
    not_allowed_users = ['hell', 'shit', 'hi', 'nacer', 'perfect', 'mester', 'zozo']
    
    # متغير لتتبع عدد المستخدمين
    users_num = 0

    @staticmethod
    def HiUser():
        """ دالة ثابتة ترحب بالمستخدم """
        return 'أهلا بك في موقعنا'

    @classmethod
    def ShowUsersCount(cls):
        """ دالة فصلية تعرض عدد المستخدمين الحاليين """
        print(f'عدد المستخدمين في موقعك هو {cls.users_num} من المستخدمين')

    def __init__(self, fname, mname, lname, gender="unknown"):
        """
        دالة المُهيّئ (Constructor) لإنشاء كائن جديد للمستخدم.
        :param fname: الاسم الأول
        :param mname: الاسم الأوسط
        :param lname: اللقب (الاسم الأخير)
        :param gender: الجنس (افتراضي: غير معروف)
        """
        self.firstName = fname
        self.middleName = mname
        self.lastName = lname
        self.gender = gender.lower()  # تحويل الجنس إلى حروف صغيرة لتجنب الأخطاء
        SiteMembers.users_num += 1  # زيادة عدد المستخدمين عند إنشاء كائن جديد

    def FullName(self):
        """ دالة تُرجع الاسم الثلاثي للمستخدم """
        return f"{self.firstName} {self.middleName} {self.lastName}"

    def HelloUser(self):
        """ دالة ترحب بالمستخدم مع تحديد الصياغة حسب الجنس """
        if self.gender == "male":
            return f"أهلا بك يا أستاذ: {self.firstName}"
        elif self.gender == "female":
            return f"أهلا بكِ يا أستاذة: {self.firstName}"
        else:
            return f"Hello {self.firstName}"

    def GetFullInfo(self):
        """ 
        دالة تُرجع معلومات المستخدم بالكامل، مع التحقق مما إذا كان الاسم ممنوعًا.
        """
        if any(name.lower() in SiteMembers.not_allowed_users for name in [self.firstName, self.middleName, self.lastName]):
            return f'هذا الاسم {self.FullName()} غير مسموح به'
        else:
            return f'{self.HelloUser()} اسمك الثلاثي هو {self.FullName()}'

    def del_user(self):
        """ دالة تحذف المستخدم وتقلل العدد الإجمالي للمستخدمين """
        if SiteMembers.users_num > 0:
            SiteMembers.users_num -= 1  # تقليل عدد المستخدمين فقط إذا كان العدد أكبر من 0
        return f'المستخدم {self.firstName} قد تم حذفه'


# إنشاء بعض المستخدمين لاختبار الكود
member1 = SiteMembers('أحمد', 'بكر', 'محمد', 'male')
member2 = SiteMembers('زينب', 'محمد', 'بهاء', 'female')
member3 = SiteMembers('zozot', 'محمد', 'بهاء', 'female')

# طباعة معلومات المستخدمين
print(member1.GetFullInfo())
print(member2.GetFullInfo())

# حذف عضو
print(member3.del_user())

# عرض عدد المستخدمين الحالي
SiteMembers.ShowUsersCount()

# تجربة استخدام دالة الترحيب الثابتة
print(SiteMembers.HiUser())

# تجربة تحويل النصوص إلى أحرف كبيرة باستخدام upper()
MyName = 'ahmed'
print(MyName.upper())  # إخراج: AHMED

MyName = 'Perfect'
print(MyName.upper())  # إخراج: PERFECT
