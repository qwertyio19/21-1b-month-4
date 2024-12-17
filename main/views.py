from django.shortcuts import render

# Create your views here.
def main(request):
    context = {
        'head': "Geeks",
        'title': 'Привет Geeks',
        'description': 'Время'
    }
    return render(request, 'index.html', context=context)

def list(reqused):
    context_2 = {
        'head_2': "Geeks",
        'title_2': 'Студент 1',
        'description_2': 'Талантбек уулу Саидахмад',
        "title_3": 'Студент 2',
        'description_2': 'Матазимов Амирбек'
    }
    return render(reqused, 'list.html', context=context_2)