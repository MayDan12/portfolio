from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Hive, Membership
from .forms import HiveForm
from django.shortcuts import render, get_object_or_404, redirect

@login_required
def hive_detail(request, hive_id):
    hive = Hive.objects.get(id=hive_id)
    memberships = Membership.objects.filter(hive=hive)
    return render(request, 'hive_detail.html', {'hive': hive, 'memberships': memberships})

@login_required
def create_hive(request):
    if request.method == 'POST':
        form = HiveForm(request.POST)
        if form.is_valid():
            hive = form.save(commit=False)
            hive.queen_bee = request.user
            hive.save()

            # Create membership for the Queen Bee
            Membership.objects.create(user=request.user, hive=hive, role=Membership.QUEEN_BEE)
            return redirect('hive_detail', hive_id=hive.id)
    else:
        form = HiveForm()
    return render(request, 'create_hive.html', {'form': form})

def update_hive(request, hive_id):
    hive = get_object_or_404(Hive, id=hive_id)
    if request.method == 'POST':
        form = HiveForm(request.POST, instance=hive)
        if form.is_valid():
            form.save()
            return redirect('hive_detail', hive_id=hive_id)  # Redirect to Hive detail page
    else:
        form = HiveForm(instance=hive)
    return render(request, 'update_hive.html', {'form': form, 'hive': hive})

def delete_hive(request, hive_id):
    hive = get_object_or_404(Hive, id=hive_id)
    if request.method == 'POST':
        hive.delete()
        return redirect('hive_list')  # Redirect to Hive list page
    return render(request, 'delete_hive.html', {'hive': hive})

