from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import CodeForm 
from .models import Code
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from django.shortcuts import redirect

class code_list(ListView):
    template_name = 'coder/programs/list.html'
    queryset = Code.objects.all() 

class code_detail(DetailView):
    template_name = 'coder/programs/detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Code, id=id_)

class CodeCreate(CreateView):
    template_name = 'coder/add_code.html'
    form_class = CodeForm
    success_url = 'coder:code_list'

    def get_initial(self):
        initial = super().get_initial()
        initial['author'] = self.request.user.id
        return initial

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        code_list_url = reverse('coder:code_list')
        return redirect(
                to=code_list_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CodeCreate, self).get_form_kwargs(*args, **kwargs)
        kwargs['author'] = self.request.user
        return kwargs

class CodeUpdate(UpdateView):
    template_name = 'coder/add_code.html'
    form_class = CodeForm
    success_url = 'coder:code_list'

    def get_initial(self):
        initial = super().get_initial()
        initial['author'] = self.request.user.id
        return initial

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Code, id=id_)

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        code_list_url = reverse('coder:code_list')
        return redirect(
                to=code_list_url)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CodeUpdate, self).get_form_kwargs(*args, **kwargs)
        kwargs['author'] = self.request.user
        return kwargs

class CodeDelete(DeleteView):
    template_name = 'coder/delete_code.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['author'] = self.request.user.id
        return initial

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Code, id=id_)

    def get_success_url(self):
        return reverse('coder:code_list')
