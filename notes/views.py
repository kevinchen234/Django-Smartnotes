from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import NotesForm
from .models import Notes
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = '/login/'

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'
    login_url = '/login/'

class PopularNotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'popular_notes'
    template_name = 'notes/notes_list.html'
    queryset = Notes.objects.filter(likes__gt=0)
    login_url = '/login/'

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/smart/notes/'
    template_name = 'notes/notes_form.html'
    form_class = NotesForm
    login_url = '/login/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user  # Set the user to the current logged-in user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    success_url = '/smart/notes/'
    template_name = 'notes/notes_form.html'
    form_class = NotesForm
    login_url = '/login/'

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/smart/notes/'
    template_name = 'notes/notes_delete.html'
    login_url = '/login/'

def add_like_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.likes += 1
        note.save()
        return HttpResponseRedirect(reverse('notes.detail', args=(pk, )))
    raise Http404

def change_visibility_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.is_public = not note.is_public
        note.save()
        return HttpResponseRedirect(reverse('notes.detail', args=(pk, )))
    raise Http404

class NotesPublicDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    queryset = Notes.objects.filter(is_public=True)
