from django.shortcuts import render

from sample.utils import add_person, get_people


def index(request):
    if request.method == "POST":
        add_person(request.POST["name"], int(request.POST["age"]))

    context = {
        "age_choices": list(range(1, 101)),
        "people": get_people(),
    }

    return render(request, "sample/index.html", context)
