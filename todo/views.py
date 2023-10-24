from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Todo


class TodoList(ListView):
    model = Todo

    def get_context_data(self, **kwargs):
        query = self.request.GET.get("q")
        if query:
            kwargs['query'] = query
            queryset = (Q(descricao__icontains=query))
            kwargs['object_list'] = Todo.objects.filter(queryset).distinct()
        return super(TodoList, self).get_context_data(**kwargs)



class TodoCreate(CreateView):
    model = Todo
    fields = ('descricao', 'prazo')
    success_url = reverse_lazy('todo-list')


class TodoEdit(UpdateView):
    model = Todo
    fields = ('descricao', 'prazo')
    success_url = reverse_lazy('todo-list')


class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo-list')
