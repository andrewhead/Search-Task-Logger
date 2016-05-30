#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Question, Prequestionnaire, PackageComparison, Postquestionnaire, QuestionEvent
from .forms import QuestionForm, PrequestionnaireForm, PackageComparisonForm, PostquestionnaireForm


CONCERNS = [
    "You will be able to find How-To documentation for more tasks you want to do.",
    "The documentation (e.g., API docs and example code) will reflect the most recent code.",
    "Developers will be able to answer the questions you ask as fast as you need answers to them.",
    "The community will be welcoming when responding to questions that you ask.",
    "The developers that write documentation produce trustworthy documentation and example code.",
    "The typical users of this package share a common technical background with you.",
]


# This single function is going to handle the assignment
# of participants to conditions
def get_concern(user, concern_index):
    offset = user.id % len(CONCERNS)  # for counterbalancing
    adjusted_concern_index = (offset + concern_index) % len(CONCERNS)
    return CONCERNS[adjusted_concern_index]


@login_required
def question(request, question_index):

    question_index = int(question_index)
    concern = get_concern(request.user, question_index)

    # Either get this question from and existing response,
    # or initialize a new question
    try:
        question = Question.objects.get(
            user=request.user,
            question_index=question_index,
        )
    except Question.DoesNotExist:
        question = Question(
            user=request.user,
            question_index=question_index,
        )

    # In case some small things have changed in the concern's wording,
    # only add it after the question has been retrieved
    question.concern = concern

    # If the user posted, then save the responses and redirect them
    # to the next post (or send them to the previous one).
    if request.method == 'POST':
        QuestionEvent.objects.create(
            user=request.user,
            question_index=question_index,
            event_type="post"
        )
        form = QuestionForm(
            request.POST,
            instance=question,
            label_suffix='',
        )
        if form.is_valid():
            QuestionEvent.objects.create(
                user=request.user,
                question_index=question_index,
                event_type="saved"
            )
            form.save()
            next_index = question_index + 1 if request.POST.get('next') \
                else question_index - 1
            if next_index > len(CONCERNS):
                return HttpResponseRedirect(reverse('postcomparison'))
            elif next_index == 0:
                return HttpResponseRedirect(reverse('precomparison'))
            elif next_index > 0:
                return HttpResponseRedirect(reverse('question', args=(next_index,),))

    # If the user is fetching a post, then just send it to them
    else:
        QuestionEvent.objects.create(
            user=request.user,
            question_index=question_index,
            event_type="get"
        )
        form = QuestionForm(
            instance=question,
            label_suffix='',
        )

    return render(request, 'questions.html', {
        'form': form,
        'question_index': question_index
    })


@login_required
def welcome(request):

    if request.method == 'POST':
        if request.POST.get('next') is not None:
            return HttpResponseRedirect(reverse('prequestionnaire'))

    return render(request, 'welcome.html', {})


@login_required
def prequestionnaire(request):

    try:
        prequestionnaire = Prequestionnaire.objects.get(user=request.user)
    except Prequestionnaire.DoesNotExist:
        prequestionnaire = Prequestionnaire(user=request.user)

    if request.method == 'POST':
        form = PrequestionnaireForm(
            request.POST,
            instance=prequestionnaire,
            label_suffix='',
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pretask'))

    else:
        form = PrequestionnaireForm(
            instance=prequestionnaire,
            label_suffix='',
        )

    return render(request, 'prequestionnaire.html', {
        'form': form,
    })


def pretask(request):

    if request.method == 'POST':
        if request.POST.get('previous') is not None:
            return HttpResponseRedirect(reverse('prequestionnaire'))
        else:
            return HttpResponseRedirect(reverse('precomparison'))

    return render(request, 'pretask.html', {})


@login_required
def precomparison(request):

    try:
        precomparison = PackageComparison.objects.get(user=request.user, stage='before')
    except PackageComparison.DoesNotExist:
        precomparison = PackageComparison(user=request.user, stage='before')

    if request.method == 'POST':
        form = PackageComparisonForm(
            request.POST,
            instance=precomparison,
            label_suffix='',
        )
        if form.is_valid():
            form.save()
            if request.POST.get('previous') is not None:
                return HttpResponseRedirect(reverse('pretask'))
            else:
                return HttpResponseRedirect(reverse('question', args=(1,),))

    else:
        form = PackageComparisonForm(
            instance=precomparison,
            label_suffix='',
        )

    return render(request, 'precomparison.html', {
        'form': form,
    })


@login_required
def postcomparison(request):

    try:
        postcomparison = PackageComparison.objects.get(user=request.user, stage='after')
    except PackageComparison.DoesNotExist:
        postcomparison = PackageComparison(user=request.user, stage='after')

    try:
        postquestionnaire = Postquestionnaire.objects.get(user=request.user)
    except Postquestionnaire.DoesNotExist:
        postquestionnaire = Postquestionnaire(user=request.user)

    if request.method == 'POST':

        comparison_form = PackageComparisonForm(
            request.POST,
            instance=postcomparison,
            label_suffix='',
        )
        questionnaire_form = PostquestionnaireForm(
            request.POST,
            instance=postquestionnaire,
            label_suffix='',
        )

        if comparison_form.is_valid() and questionnaire_form.is_valid():
            comparison_form.save()
            questionnaire_form.save()
            if request.POST.get('previous') is not None:
                return HttpResponseRedirect(reverse('question', args=(len(CONCERNS),)))
            else:
                return HttpResponseRedirect(reverse('thanks'))

    else:
        comparison_form = PackageComparisonForm(
            instance=postcomparison,
            label_suffix='',
        )
        questionnaire_form = PostquestionnaireForm(
            instance=postquestionnaire,
            label_suffix='',
        )

    return render(request, 'postcomparison.html', {
        'comparison_form': comparison_form,
        'feedback_form': questionnaire_form,
    })


@login_required
def thanks(request):
    return render(request, 'thanks.html', {})
