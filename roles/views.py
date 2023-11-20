from django.http import HttpResponseRedirect
from .temp_data import role_data
from django.shortcuts import render
from django.urls import reverse

def create_role(request):
    if request.method == 'POST':
        role_data.append({
            'name': request.POST['name'],
            'date': request.POST['date'],
            'address': request.POST['address'],
            'poster_url': request.POST['poster_url']
        })
        return HttpResponseRedirect(
            reverse('roles:detail', args=(len(role_data), )))
    else:
        return render(request, 'roles/create.html', {})

def search_roles(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "role_list": [
                m for m in role_data
                if request.GET['query'].lower() in m['name'].lower()
            ]
        }
    return render(request, 'roles/search.html', context)

def list_roles(request):
    context = {"role_list": role_data}
    return render(request, 'roles/index.html', context)

def detail_role(request, role_id):
    context = {'role': role_data[role_id - 1]}
    return render(request, 'roles/detail.html', context)

