from django.shortcuts import render, redirect
from app01 import models
import time
from django.views import View
from django.utils.decorators import method_decorator
from django.urls import reverse
# from django.http import HttpResponse


def timer(func):
    def inner(request, *args, **kwargs):
        start = time.time()
        ret = func(request, *args, **kwargs)
        print('执行的时间：{}'.format(time.time()-start))
        return ret
    return inner


@timer
# Create your views here.
def publisher_list(request):
    # 获取所有出版社的信息
    all_publisher = models.Publisher.objects.all().order_by('id')

    return render(request, 'publisher_list.html',
                  {'all_publisher': all_publisher})


def publisher_add(request):
    # post 请求
    # 获取用户提交的数据
    # 将数据加入数据库
    # 返回一个重定向展示出版社的页面

    if request.method == "POST":
        pub_name = request.POST.get('pub_name')
        if not pub_name:
            return render(request, 'publisher_add.html',
                          {'error': '出版社名称不能为空！'})
        if models.Publisher.objects.filter(name=pub_name):
            return render(request, 'publisher_add.html',
                          {'error': '出版社名称已经存在！'})
        ret = models.Publisher.objects.create(name=pub_name)

        return redirect('/publisher_list')
    # get 请求返回一个页面
    return render(request, 'publisher_add.html')

# create a new publisher  - cbv

# @method_decorator(timer, name="get")
# @method_decorator(timer, name="post")
@method_decorator(timer, name="dispatch")
class PublisherAdd(View):
    @method_decorator(timer)
    # 可以设定允许提交的方式
    # http_method_names=['get',]
    # def dispatch(request, *args, **kwargs):
    #     ret = super().dispatch(request, *args, **kwargs)  # 执行view中的dispatch
    #     return ret


    def get(self, request):
        # 处理get请求
        return render(request, 'publisher_add.html')

    def post(self, request):
        pub_name = request.POST.get('pub_name')
        if not pub_name:
            return render(request, 'publisher_add.html',
                          {'error': '出版社名称不能为空！'})
        if models.Publisher.objects.filter(name=pub_name):
            return render(request, 'publisher_add.html',
                          {'error': '出版社名称已经存在！'})
        models.Publisher.objects.create(name=pub_name)

        return redirect('/publisher_list')


def publisher_del(request):
    # 获取删除数据的id
    pub_id = request.GET.get('id')
    # 根据id到数据库进行删除

    # models.Publisher.objects.get(pk=pub_id).delete()
    models.Publisher.objects.filter(pk=pub_id).delete()  #查询到一个对象列表 并删除所有对象
    # 返回重定向
    return redirect('/publisher_list')


def publisher_edit(request, pk):
    # pub_id = request.GET.get('id')
    pub_id=pk
    pub_object = models.Publisher.objects.get(pk=pub_id)
    if request.method == 'GET':

        #get 返回一个页面，页面包含form表, input有原始数据
        return render(request, 'publisher_edit.html',
                      {'pub_object': pub_object})
    #post 修改数据库
    else:
        pub_name = request.POST.get('pub_name')
        pub_object.name = pub_name  #只是在内存中修改
        pub_object.save()  #修改操作提交到数据库
        #重定向
        return redirect('/publisher_list')


def book_list(request):
    all_book = models.Book.objects.all().order_by('id')

    return render(request, 'book_list.html', {'all_book': all_book})


def book_del(request):
    #获取删除数据的id
    book_id = request.GET.get('id')
    #根据id到数据库进行删除

    #models.Book.objects.get(pk=pub_id).delete()
    models.Book.objects.filter(pk=book_id).delete()  #查询到一个对象列表 并删除所有对象
    #返回重定向
    return redirect('/book_list')


def book_add(request):
    #post 请求
    #获取用户提交的数据
    #将数据加入数据库
    #返回一个重定向展示出版社的页面
    error = ''

    if request.method == "POST":
        book_name = request.POST.get('book_name')
        pub_id = request.POST.get('pub_id')
        if not book_name:
            error = '书籍名称不能为空！'
        elif models.Book.objects.filter(name=book_name):

            error = '书籍名称已经存在！'
        else:
            models.Book.objects.create(name=book_name, publisher_id=pub_id)
            return redirect('/book_list')

    all_publishers = models.Publisher.objects.all()
    #get 请求返回一个页面
    return render(request, 'book_add.html', {
        'all_publishers': all_publishers,
        'error': error
    })


def book_edit(request):
    book_id = request.GET.get('id')
    book_object = models.Book.objects.get(pk=book_id)
    all_publishers = models.Publisher.objects.all()
    if request.method == 'GET':

        #get 返回一个页面，页面包含form表, input有原始数据
        return render(request, 'book_edit.html', {
            'book_object': book_object,
            'all_publishers': all_publishers
        })
    #post 修改数据库
    else:
        book_name = request.POST.get('book_name')
        pub_id = request.POST.get('pub_id')
        book_object.name = book_name  #只是在内存中修改
        book_object.publisher_id = pub_id
        book_object.save()  #修改操作提交到数据库
        #重定向
        return redirect('/book_list')


def author_list(request):
    all_author = models.Author.objects.all().order_by('id')
    #author.book.all()#关系管理 所关联的所有对象
    return render(request, 'author_list.html', {'all_author': all_author})


def author_add(request):
    error = ''
    if request.method == "POST":
        author_name = request.POST.get('author_name')
        book_id = request.POST.getlist('book_id')  #获取多个数据
        if not author_name:
            error = '作者名称不能为空！'
        elif models.Author.objects.filter(name=author_name):
            error = '作者名称已经存在！'
        else:
            author_obj = models.Author.objects.create(name=author_name)
            author_obj.books.set(book_id)  #设置多对多关系
            return redirect('/author_list')
    all_book = models.Book.objects.all()
    all_author = models.Author.objects.all()
    return render(request, 'author_add.html', {
        'all_book': all_book,
        'all_author': all_author,
        'error': error
    })


def author_del(request):
    #获取删除数据的id
    author_id = request.GET.get('id')
    #根据id到数据库进行删除

    models.Author.objects.filter(pk=author_id).delete()  #查询到一个对象列表 并删除所有对象
    #返回重定向
    return redirect('/author_list')


def author_edit(request):
    author_id = request.GET.get('id')
    author_object = models.Author.objects.get(pk=author_id)
    all_books = models.Book.objects.all()
    if request.method == 'GET':

        #get 返回一个页面，页面包含form表, input有原始数据
        return render(request, 'author_edit.html', {
            'author_object': author_object,
            'all_books': all_books
        })
    #post 修改数据库
    else:
        author_name = request.POST.get('author_name')
        book_id = request.POST.getlist('book_id')
        author_object.name = author_name  #只是在内存中修改
        author_object.save()  #修改操作提交到数据库
        author_object.books.set(book_id)

        #重定向
        return redirect('/author_list')


def delete(request,name,pk):
    print(name,pk)
    # dic = {'publisher': model.Publisher,
    #         'book':model.Book}

    clr = getattr(models, name.capitalize())
    if not cls:
        return HttpResponse('检测表名')
    ret=clr.objects.filter(pk=pk)
    if ret：
        ret.delete()
    else:
        return HttpResponse("要删除的数据不存在")
    return redirect(reverse(name)) #直接使用捕获的