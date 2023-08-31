from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import Movie
from .forms import ReviewForm


class MoviesView(View):
    def get(self, request):
        kino = Movie.objects.all()
        return render(request, "row/glav.html", {'kino': kino})


class MovieAbout(View):
    def get(self, request, slug):
        kinos = Movie.objects.get(url=slug)
        return render(request, "row/about.html", {'kinos': kinos})


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
        form.movie = movie
        form.save()
        return redirect("/")
