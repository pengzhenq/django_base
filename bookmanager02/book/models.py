from django.db import models

# Create your models here.

"""
1、模型类 需要继承自 models.Model类
2、定义属性
    属性名=models.类型（选项)
    2.1 属性名对应字段名
    
    2.2 类型 MYSQL的类型
    2.3 选项 是否有默认值 是否唯一 是否为Null
        Charfield 必须设置max_length
        Verbose_name 主要是admin

3、修改表的名称
    默认的表的名称是： 子应用名_类名 都是小写
    修改表的名字
    
        create table `qq_user` (
        id int
        name varchar(10) not null default ''
    )
"""

class BookInfo(models.Model):


    name= models.CharField(max_length=10,unique=True)
    pub_date=models.DateField(null=True)
    readcount=models.IntegerField(default=0)
    commentcount=models.IntegerField(default=0)
    is_delete=models.BooleanField(default=False)

    #peopleinfo_set=[PeopleInfo,...]

    def __str__(self):
        return self.name

    #修改表名字
    class Meta:
        db_table = 'bookinfo'
        verbose_name = '书籍管理'

class PeopleInfo(models.Model):

    # 定义一个有序字典
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )


    name = models.CharField(max_length=10,unique=True)
    gender=models.SmallIntegerField(choices=GENDER_CHOICE)
    description = models.CharField(max_length=100,null=True)
    is_delete=models.BooleanField(default=False)

    #外键
    #系统会自动为外键添加_id

    #外键的级联操作
    #主表和从表
    # 1对多
    # 书籍 对 人物


    #主表的数据删除了
    #从表有关联的数据，
    # SET_NULL
    #
    #CASCADE 主表数据删除从表数据也删除
    #
    #PROTECT 保护主表数据抛出删除异常
    #
    #DO_NOTHING 不进行任何操作并抛出异常


    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    #book = BookInfo()
    #实例对象

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物管理'

    def __str__(self):
        return self.name

