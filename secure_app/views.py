from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Object

def can_view(user):
    return user.groups.filter(name='Viewers').exists()

def can_change(user):
    return user.groups.filter(name='Changers').exists()

def can_delete(user):
    return user.groups.filter(name='Deleters').exists()

@login_required
def object_list(request):
    objects = Object.objects.all()
    return render(request, "object_list.html", {"objects": objects})

@login_required
@user_passes_test(can_view)
def object_detail(request, object_id):
    obj = get_object_or_404(Object, id=object_id)
    return render(request, "object_detail.html", {"object": obj})

@login_required
def object_change(request, object_id):
    obj = get_object_or_404(Object, id=object_id)

    if request.method == "POST":
        obj.name = request.POST.get("name")
        obj.save()
        return redirect("object_list")

    return render(request, "object_change.html", {"object": obj})

@login_required
def object_delete(request, object_id):
    obj = get_object_or_404(Object, id=object_id)

    if request.method == "POST":
        obj.delete()
        return redirect("object_list")

    return render(request, "object_delete.html", {"object": obj})
