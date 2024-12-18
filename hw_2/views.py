from django.shortcuts import render

# Create your views here.

def hw_2(request):
    context = {
        'head_3': 'Geeks Online',
        'title_3': 'Добро пожаловать в Geeks',
        'description_3': 'Здесь вы можете посмотреть время уроков'
    }
    return render(request, 'hw_2.html', context=context)
