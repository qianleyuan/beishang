from django.shortcuts import render
from .models import Articles
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    '''
    文章列表页
    '''
    article = Articles.objects.all()
    nums = 2
    p = Paginator(article,nums)
    try:
        pIndex = request.GET.get('page',1)
    except PageNotFoundError:
        pIndex = 1
    articles = p.page(pIndex)
    context={
        'articles':article
    }
    return render(request,'index.html',context)
def detail(request,pk):
    '''
    文章详情页
    '''
    article = Articles.objects.get(pk=pk)
    return render(request,'single_article.html',locals())
def contact(request):
    '''
    联系我们
    '''
    return render(request,'contact.html')
def about(request):
    '''
    关于我们
    '''
    return render(request,"about.html")