from django.shortcuts import render

# Create your views here.
def lord_of_rings(request):
    return render(
        request,
        'lord_of_rings/index.html',
    )