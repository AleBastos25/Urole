from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Role, Comment, List
from .forms import CommentForm


class ListListView(generic.ListView):
    model = List
    template_name = 'roles/lists.html'


class ListCreateView(generic.CreateView):
    model = List
    template_name = 'roles/create_list.html'
    fields = ['name', 'author', 'roles']
    success_url = reverse_lazy('roles:lists')



def create_comment(request, role_id):
    role = get_object_or_404(Role, pk=role_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            role=role)
            comment.save()
            return HttpResponseRedirect(
                reverse('roles:detail', args=(role_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'role': role}
    return render(request, 'roles/comment.html', context)

def update_role(request, role_id):
    role = get_object_or_404(Role, pk=role_id)

    if request.method == "POST":
        role.name = request.POST['name']
        role.dia = request.POST['dia']
        role.address = request.POST['address']
        role.poster_url = request.POST['poster_url']
        role.save()
        return HttpResponseRedirect(
            reverse('roles:detail', args=(role.id, )))

    context = {'role': role}

    return render(request, 'roles/update.html', context)


def delete_role(request, role_id):
    role = get_object_or_404(Role, pk=role_id)

    if request.method == "POST":
        role.delete()
        return HttpResponseRedirect(reverse('roles:index'))

    context = {'role': role}
    return render(request, 'roles/delete.html', context)

def create_role(request):
    if request.method == 'POST':
        role_name = request.POST['name']
        role_dia = request.POST['dia']
        role_address = request.POST['address']
        role_poster_url = request.POST['poster_url']
        role = Role(name=role_name,
                      dia=role_dia,
                      address=role_address,
                      poster_url=role_poster_url)
        role.save()
        return HttpResponseRedirect(
            reverse('roles:detail', args=(role.id, )))
    else:
        return render(request, 'roles/create.html', {})

def search_roles(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        role_list = Role.objects.filter(name__icontains=search_term)
        context = {"role_list": role_list}
    return render(request, 'roles/search.html', context)

def list_roles(request):
    role_list = Role.objects.all()
    context = {'role_list': role_list}
    return render(request, 'roles/index.html', context)

def detail_role(request, role_id):
    role = get_object_or_404(Role, pk=role_id)
    context = {'role': role}
    return render(request, 'roles/detail.html', context)