from django.shortcuts import render, redirect


def homepage(request):
    return render(request, "home.html")


def words_listpage(request):
    with open("/home/artorias/Documents/django_task1/proj/mydict/dictionary.txt", "r") as rfile:
        strings = rfile.readlines()
        strongs = []
        for string in strings:
            spacein = string.find(" ")
            strongs.append([string[:spacein], string[spacein + 2:]])
    return render(request, "words_list.html", {"strings": strongs})


def add_wordpage(request):
    if request.method == "GET":
        return render(request, "add_word.html")
    else:
        print(request.POST)
        with open("/home/artorias/Documents/django_task1/proj/mydict/dictionary.txt", "a") as wfile:
            wfile.write("\n")
            wfile.writelines(request.POST['word1'] + " - " + request.POST['word2'])
        return redirect(homepage)
