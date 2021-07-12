from django import forms
from django.shortcuts import render,HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Contact, Post, Subject, Class_in
from .forms import ContactForm,PostForm
from django.views import View
from django.views.generic import FormView
from django.db.models import Q
app_name='tuition'

def search(request):
    query=request.POST.get('search','')
    if query:
        queryset=(Q(title__icontains=query))|(Q(details__icontains=query))|(Q(medium__icontains=query))|\
        (Q(category__icontains=query))|(Q(subject__name__icontains=query))|\
        (Q(class__in__name__icontains=query))
        results=Post.objects.filter(queryset).distinct()
    else:
        resutls=[]
    context={
    'results':results
    }
    return render(request, 'tuition/search.html', context)
def filter(request):
    if request.method=="POST":
        subject=request.POST['subejcts']
        class_in=request.POST['class_in']
        if subject or class_in:
            queryset = (Q(subject__name__icontains=subject)) | (Q(class_in__name__icontainss=class_in))
            results = Post.objects.filter(queryset).distinct()
        else:
            resutls = []

        context = {
            'results': results
        }
        return render(request, 'tuition/search.html', context)
class ContactView(FormView):
    form_class=ContactForm
    template_name='contact.html'
    success_url='/'
    def form_valid(self, form):
        form.save
        messages.success(self.request,'Form Successfully Submited')
        return super().form_valid(form)
class ContactView(View):
    form_class=ContactForm
    template_name='contact.html'
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        return render(request, self.template_name,{'form':form})

from django.views.generic import DetailView
class PostDetailView(DetailView):
    model = Post
    template_name = 'tuition/postdetail.html'

def post(self,request,*args,**kwargs):
    form=self.form_class(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("Success")
    return render(request, self.template_name, {'form': form})

# Create your views here.
def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
          form.save()
    else:
        form=ContactForm()
    return render(request,'contact.html',{'form':form})


from django.views.generic import ListView
class PostListView(ListView):
    template_name= 'tuition/postlist.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'
    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['posts']=context.get('object_list')
        context['subjects']=Subject.objects.all()
        context['classes']=Class_in.objects.all()
        return context
def postview(request):
    post=Post.objects.all()
    return render(request,'tuition/postview.html',{'post':post})

def subview(request):
    sub=Subject.objects.all()
    return render(request,'tuition/subjectview.html',{'sub':sub})
from django.views.generic import CreateView
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'tuition/postcreate.html'
    success_url='/'
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        # id=self.object.id
        return reverse_lazy('tuition.subjects')

from django.views.generic import UpdateView, DeleteView
class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'tuition/postcreate.html'
    def get_success_url(self):
        id=self.object.id
        return reverse_lazy('tuition:postdetail', kwargs={'pk':id})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'tuition/delete.html'
    success_url = reverse_lazy('tuition:postlist')


def postcreate(request):
    if request.method=="POST":
        form =PostForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            sub=form.cleaned_data['subject']
            for i in sub:
                obj.subject.add(i)
                obj.save()
            class_in=form.cleaned_data['class_in']
            for i in class_in:
                obj.class_in.add(i)
                obj.save()
            return HttpResponse("Success")
    else:
        form=PostForm()
    return render(request,'tuition/postcreate.html',{'form':form})
