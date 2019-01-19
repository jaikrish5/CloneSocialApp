from django.shortcuts import render
from .models import Tweet
from django.db.models import Q
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from django.urls import reverse_lazy
from .forms import TweetModelForm



# Create your views here.
def index(request):
    return render(request,'tweets/home.html',{})




class Home(TemplateView):
    template_name="tweets/home.html"



class tweet_create_view(CreateView):
    model = Tweet
    template_name = "tweets/tweet_form.html"
    fields = ['content']

    # success_url = "tweets/tweet_list.html"


class tweet_update_view(UpdateView):
    model = Tweet
    template_name = "tweets/tweet_form.html"
    fields = ['content']

class tweet_delete_view(DeleteView):
    model = Tweet
    template_name = "tweets/tweet_delete.html"
    success_url = reverse_lazy("tweet:list")





class tweet_detail_view(DetailView):
    model = Tweet
    context_object_name = 'tweet_detail'
    template_name="tweets/detail_view.html"



class tweet_list_view(ListView):
    model =Tweet
    template_name="tweets/tweet_list.html"
    def get_queryset(self,*args,**kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(
                        Q(content__icontains = query) |
                        Q(user__username__icontains=query)
                        )

        return qs

    def get_context_data(self,*args,**kwargs):
        context = super(tweet_list_view,self).get_context_data(*args,**kwargs)
        # formclass = TweetModelForm
        context['create_form'] = TweetModelForm()
        context['create_url']=reverse_lazy('tweet:create')
        return context

# def tweet_detail_view(request,id=1):
#     obj = Tweet.objects.get(id=id)
#     context = {
#         "object":obj
#
#     }
#     return render(request,"tweets/detail_view.html",context)

# def tweet_list_view(request):
#
#     queryset = Tweet.objects.all()
#     context = {
#         "object_list":queryset
#         }
#     return render(request,'tweets/list_view.html',context)
