#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Strategy, Question, Prequestionnaire, PackageComparison, PackagePair, \
    Postquestionnaire, QuestionEvent
from .forms import StrategyForm, QuestionForm, PrequestionnaireForm, PackagePairForm, \
    PackageComparisonForm, PostquestionnaireForm
from .concerns import CONCERNS


# This single function is going to handle the assignment
# of participants to conditions
def get_concern(user, concern_index):
    offset = user.id % len(CONCERNS)  # for counterbalancing
    adjusted_concern_index = (offset + concern_index) % len(CONCERNS)
    return CONCERNS[adjusted_concern_index]['question']


def save_event(user, question_index, event_type):
    QuestionEvent.objects.create(
        user=user,
        question_index=question_index,
        event_type=event_type
    )


@login_required
def strategy(request, question_index):

    question_index = int(question_index)
    concern = get_concern(request.user, question_index)

    # Either get this question from and existing response,
    # or initialize a new question
    try:
        strategy = Strategy.objects.get(
            user=request.user,
            question_index=question_index,
        )
    except Strategy.DoesNotExist:
        strategy = Strategy(
            user=request.user,
            question_index=question_index,
        )

    # In case some small things have changed in the concern's wording,
    # only add it after the question has been retrieved
    strategy.concern = concern

    # If the user posted, then save the responses and redirect them
    # to the next post (or send them to the previous one).
    if request.method == 'POST':
        save_event(request.user, question_index, 'post strategy')
        form = StrategyForm(
            request.POST,
            instance=strategy,
            label_suffix='',
        )
        if form.is_valid():
            form.save()
            next_index = question_index if request.POST.get('next') \
                else question_index - 1
            if next_index == 0:
                return HttpResponseRedirect(reverse('precomparison'))
            elif next_index > 0:
                if request.POST.get('next'):
                    return HttpResponseRedirect(reverse('task', args=(next_index,),))
                elif request.POST.get('previous'):
                    return HttpResponseRedirect(reverse('question', args=(next_index,),))

    # If the user is fetching a post, then just send it to them
    else:
        save_event(request.user, question_index, 'get strategy')
        form = StrategyForm(
            instance=strategy,
            label_suffix='',
        )

    return render(request, 'strategy.html', {
        'form': form,
        'question_index': question_index,
        'concern': concern,
    })


@login_required
def task(request, question_index):

    question_index = int(question_index)
    concern = get_concern(request.user, question_index)

    # If the user posted, then save the responses and redirect them
    # to the next post (or send them to the previous one).
    if request.method == 'POST':
        save_event(request.user, question_index, 'post task')
        if request.POST.get('next'):
            return HttpResponseRedirect(reverse('question', args=(question_index,),))
        elif request.POST.get('previous'):
            return HttpResponseRedirect(reverse('strategy', args=(question_index,),))
    else:
        save_event(request.user, question_index, 'get task')

    return render(request, 'task.html', {
        'question_index': question_index,
        'concern': concern,
    })


@login_required
def question(request, question_index):

    question_index = int(question_index)
    concern = get_concern(request.user, question_index)

    package_pair = PackagePair.objects.get(user=request.user)

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
    question.concern = "Based on the evidence you have seen, " + concern

    # If the user posted, then save the responses and redirect them
    # to the next post (or send them to the previous one).
    if request.method == 'POST':
        save_event(request.user, question_index, 'post responses')
        form = QuestionForm(
            request.POST,
            instance=question,
            label_suffix='',
        )
        if form.is_valid():
            form.save()
            next_index = question_index + 1 if request.POST.get('next') \
                else question_index
            if next_index > len(CONCERNS):
                return HttpResponseRedirect(reverse('postcomparison'))
            elif next_index > 0:
                if request.POST.get('previous'):
                    return HttpResponseRedirect(reverse('task', args=(next_index,),))
                elif request.POST.get('next'):
                    return HttpResponseRedirect(reverse('strategy', args=(next_index,),))

    # If the user is fetching a post, then just send it to them
    else:
        save_event(request.user, question_index, 'get responses')
        form = QuestionForm(
            instance=question,
            label_suffix='',
        )

    return render(request, 'question.html', {
        'form': form,
        'question_index': question_index,
        'package1': package_pair.package1,
        'package2': package_pair.package2,
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
            return HttpResponseRedirect(reverse('preinstructions'))

    else:
        form = PrequestionnaireForm(
            instance=prequestionnaire,
            label_suffix='',
        )

    return render(request, 'prequestionnaire.html', {
        'form': form,
    })


@login_required
def preinstructions(request):

    try:
        package_pair = PackagePair.objects.get(user=request.user)
    except PackagePair.DoesNotExist:
        package_pair = PackagePair(user=request.user)

    if request.method == 'POST':
        form = PackagePairForm(
            request.POST,
            instance=package_pair,
            label_suffix='',
        )
        if form.is_valid():
            form.save()
            if request.POST.get('previous') is not None:
                return HttpResponseRedirect(reverse('prequestionnaire'))
            else:
                return HttpResponseRedirect(reverse('pretask'))

    else:
        form = PackagePairForm(
            instance=package_pair,
            label_suffix='',
        )

    return render(request, 'preinstructions.html', {
        'form': form
    })


@login_required
def pretask(request):

    package_pair = PackagePair.objects.get(user=request.user)

    if request.method == 'POST':
        if request.POST.get('previous') is not None:
            return HttpResponseRedirect(reverse('preinstructions'))
        elif request.POST.get('next') is not None:
            return HttpResponseRedirect(reverse('precomparison'))

    return render(request, 'pretask.html', {
        'package1': package_pair.package1,
        'package2': package_pair.package2,
    })


@login_required
def precomparison(request):

    try:
        precomparison = PackageComparison.objects.get(user=request.user, stage='before')
    except PackageComparison.DoesNotExist:
        precomparison = PackageComparison(user=request.user, stage='before')

    package_pair = PackagePair.objects.get(user=request.user)

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
                return HttpResponseRedirect(reverse('strategy', args=(1,),))

    else:
        form = PackageComparisonForm(
            instance=precomparison,
            label_suffix='',
        )

    return render(request, 'precomparison.html', {
        'form': form,
        'package1': package_pair.package1,
        'package2': package_pair.package2,
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

    package_pair = PackagePair.objects.get(user=request.user)

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
        'package1': package_pair.package1,
        'package2': package_pair.package2,
    })


@login_required
def thanks(request):
    return render(request, 'thanks.html', {})
