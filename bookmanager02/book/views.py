from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo,PeopleInfo
# Create your views here.


# def index(request):

    # books = BookInfo.objects.all()
    # print(books)
    # return HttpResponse('index')


###############增加数据###################

#方式1
book = BookInfo(
    name = 'Django',
    pub_date = '2020-1-1',
    readcount = 10
)

book.save()

#方式2
#object ---相当于代理，实现增删改查
BookInfo.objects.create(
    name = '测试开发',
    pub_date= '2020-1-2',
    readcount = 100
)

########################修改数据#####################

# 方式1
# select * from bookinfo where id=6
books = BookInfo.objects.get(id=8)

books.name = '运维开发'

books.save()

#方式2

BookInfo.objects.filter(id=8).update(name='爬虫入门',commentcount=666)

# BookInfo.objects.get(id=5).update(name='555',commentcount=999)

#################删除数据####################

#方式1
books_del=BookInfo.objects.get(id=5)
#物理删除（这条记录的数据删除） 和 逻辑删除（修改标记位 is_delete =False)
books_del.delete()

#方式2
BookInfo.objects.get(id=8).delete()
BookInfo.objects.filter(id=8).delete()

########################查询##########################
try:
    book_get = BookInfo.objects.get(id=1)
except BookInfo.DoesNotExist:
    print('查询结果不存在')

from book.models import PeopleInfo
PeopleInfo.objects.all().count()
PeopleInfo.objects.count()

####################过滤查询####################

#实现SQL中的where功能
#filter过滤多个结果
#exclude排除符合条件剩下的结果
#get过滤一个结果

#模型类名.objects.filter(属性名__运算符=值)
#模型类名.objects.exclude(属性名__运算符=值)
#模型类名.objects.get(属性名__运算符=值)

# 查询编号为1的图书
BookInfo.objects.get(id=1)
BookInfo.objects.filter(id=1)
BookInfo.objects.get(pk=1)  #primary_key=1

# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='传')

# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')

# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)

# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1,3,5])

# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)

#查询编号不等于3的图书
book_ex=BookInfo.objects.exclude(id=3)

# 查询1980年发表的图书
book_year = BookInfo.objects.filter(pub_date__year=1986)
book_year

# 查询1990年1月1日后发表的图书
book_gt=BookInfo.objects.filter(pub_date__lt='1990-1-1')
book_gt

# 查询阅读量大于等于评论量的图书。
from django.db.models import F,Q

F_book = BookInfo.objects.filter(readcount__gt=F('commentcount'))

# 查询阅读量大于2倍评论量的图书。
F2_book = BookInfo.objects.filter(readcount__gt=F('commentcount')*2)
F2_book

# 查询阅读量大于20，并且编号小于3的图书。
# 多个过滤器逐个调用表示逻辑与关系，同sql语句中where部分的and关键字。
b1 = BookInfo.objects.filter(readcount__gt=20,id__lt=3)
b2 = BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)

# 如果需要实现逻辑或or的查询，需要使用Q()对象结合|运算符，Q对象被义在django.db.models中。

#Q(属性名__运算符=值）

# 查询阅读量大于20的图书，改写为Q对象

BookInfo.objects.filter(Q(readcount__gt=20))

# Q对象可以使用&、|连接，&表示逻辑与，|表示逻辑或。

# 查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
b3= BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))

# Q对象前可以使用~操作符，表示非not。
# 查询编号不等于2的图书。
b4 = BookInfo.objects.filter(~Q(id=2))

# 使用aggregate()过滤器调用聚合函数。聚合函数包括：Avg平均，Count数量，Max最大，Min最小，Sum求和，被定义在django.db.models中。

# 查询图书的总阅读量。
from django.db.models import Sum
b5 = BookInfo.objects.aggregate(Sum('readcount'))


# 使用order_by对结果进行排序

#默认升序
b6 = BookInfo.objects.all().order_by('readcount')

#降序
b7 = BookInfo.objects.all().order_by('-readcount')

# 查询书籍为1的所有人物信息
b8 = BookInfo.objects.get(id=1)

# 由一到多的访问语法：
# 一对应的模型类对象.多对应的模型类名小写_set 例：
b8.peopleinfo_set.all()

# 由多到一的访问语法:

# 多对应的模型类对象.多对应的模型类中的关系类属性名 例：
from book.models import PeopleInfo
person = PeopleInfo.objects.get(id=18)
person.book

# 访问一对应的模型类关联对象的id语法:
#
# 多对应的模型类对象.关联类属性_id
person = PeopleInfo.objects.get(id=18)
person.book_id

# 由多模型类条件查询一模型类数据:
# 关联模型类名小写__属性名__条件运算符=值
# 查询图书，要求图书人物为"郭靖"
b9 = BookInfo.objects.filter(peopleinfo__name='郭靖')
b9

# 查询图书，要求图书中人物的描述包含"八"
b10 = BookInfo.objects.filter(peopleinfo__description__contains='八')

# 查询书名为“天龙八部”的所有人物。
b11 = PeopleInfo.objects.filter(book__name='天龙八部')
b11

# 查询图书阅读量大于30的所有人物
b12 = PeopleInfo.objects.filter(book__readcount__gt=30)
b12

# 查询集，也称查询结果集、QuerySet，表示从数据库中获取的对象集合。
# 对查询集可以再次调用过滤器进行过滤
b13 = BookInfo.objects.filter(readcount__gt=30).order_by('pub_date')

b14 = BookInfo.objects.all()

for book in b14:
    print(book.name)

from book.models import BookInfo

[book.id for book in BookInfo.objects.all()]

b15 = BookInfo.objects.all()[0:4]
b15

#分页
b16 = BookInfo.objects.all()
from django.core.paginator import Paginator
paginator = Paginator(b16,2)
page_books = paginator.page(1)
#分页数据
page_books.object_list

##############################
#1对多的关系模型中
#                     PeopleInfo
#系统会为我们自动添加一个 关联模型类名小写_set
b17 = BookInfo.objects.get(id=1)
b17.peopleinfo_set.all()

#查询任务为1的书籍信息
person = PeopleInfo.objects.get(id=18)

person.book.name
person.book.readcount
