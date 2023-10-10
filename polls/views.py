# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question, Choice
from typing import List
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list
        }
    return render(request, "polls/index.html", context)

@login_required
def sobre(request):
    return HttpResponse('Este é um app de enquete!')
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    return HttpResponse(f"Resultados da pergunta de número {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Você vai votar na pergunta de número {question_id}")



class QuestionCreateView(CreateView):
    model = Question 
    fields = ('question_text',)
    success_url = reverse_lazy('question-list')
    template_name = 'polls/question_form.html'

class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'

class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'question'

from django.contrib import messages

class QuestionDeleteView(DeleteView):
    model = Question 
    success_url = reverse_lazy("question-list")
    success_message ="Enquete excluída com sucesso"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

class QuestionUpdateView(UpdateView):
    model = Question 
    template_name = 'polls/question_form.html'
    fields = ('question_text', 'pub_date', )
    success_url = reverse_lazy('question-list')
    success_message = 'Pergunta atualizada com sucesso'

    def get_context_data(self, **kwargs):
        context = super(QuestionUpdateView, self).get_context_data(**kwargs)
        context['form_tittle'] = 'Editando a pergunta'

        question_id = self.kwargs.get('pk')
        choices = Choice.objects.filter(question__pk=question_id)
        context['question_choices'] = choices

        return context

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(QuestionUpdateView, self).form_valid(request, *args, **kwargs)

class ChoiceCreateView(CreateView):
    model = Choice
    template_name = "polls/choice_form.html"
    fields = ('choice_text', )
    success_message = 'Opção de voto registrado com sucesso'

    def dispatch(self, request, *args, **kwards):
        self.question = get_object_or_404(Question, pk=self.kwargs.get('pk'))
        return super(ChoiceCreateView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwards): 
        question = get_object_or_404(Question, pk=self.kwargs.get('pk'))

        context = super(ChoiceCreateView, self).gett_context_data(**kwargs)
        context['form_tittle'] = f'Alternativa para: {question.question+text}'

        return context

    def def form_valid(self, form):
        form.instance.question = self.question
        message_success(self.request, self.success_message)
        return super(ChoiceCreateView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        question_id = self.kwargs.get('pk')
        return reverse_lazy('poll_edit', kwargs={'pk': question_id}) 
     