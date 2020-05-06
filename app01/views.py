from django.shortcuts import render
from django.views.generic.base import View
from .models import Books
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


# Create your views here.
class BookListView(View):
    """
    获取图书列表
    """
    def get(self, request):
        list = Books.objects.all()
        return render(request, 'booklist.html', {'list': list})


class GetBookView(View):
    """
    获取单个图书
    """
    @method_decorator(cache_page(3))
    def get(self, request, id):
        book = Books.objects.filter(id=id).first()
        print(book.pv)
        book.pv += 1
        book.save()
        return render(request, 'book.html', {'t': book})
