#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

from .concerns import CONCERNS


def verbatim_choices(list_):
    return zip(list_, list_)


def choice_range(min_, max_):
    return verbatim_choices(range(min_, max_))


class Prequestionnaire(models.Model):
    user = models.ForeignKey(User)
    programming_years = models.IntegerField(
        verbose_name="How many years of experience do you have programming?",
        choices=choice_range(0, 25),
    )
    python_years = models.IntegerField(
        verbose_name=(
            "How many years of experience do you have programming " +
            "with Python or Python packages?"),
        choices=choice_range(0, 25),
    )
    programming_profiency = models.CharField(
        verbose_name="How would you describe your proficiency as a programmer?",
        choices=verbatim_choices(["Novice", "Proficient", "Expert"]),
        max_length=100
    )
    python_proficiency = models.CharField(
        verbose_name="How would you describe your proficiency with Python?",
        choices=verbatim_choices(["Novice", "Proficient", "Expert"]),
        max_length=100
    )
    occupation = models.CharField(
        verbose_name="What is your job?",
        choices=verbatim_choices([
            "Software developer",
            "Graduate student",
            "Undergraduate student",
            "Project manager",
            "Quality assurance",
            "Systems administrator",
            "Other",
        ]),
        max_length=200
    )
    gender = models.CharField(
        verbose_name="Gender?",
        max_length=500,
        blank=True,
        null=True
    )


class Strategy(models.Model):
    user = models.ForeignKey(User)
    question_index = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    concern = models.CharField(
        verbose_name="Task: Find which package better satisfies this concern",
        max_length=1000,
    )
    strategy = models.CharField(
        verbose_name=(
            "What strategy will you use to find out which package " +
            "is better for this concern?"),
        help_text=(
            "Please answer in 1 or 2 sentences.  Feel free to take a minute " +
            "to think about a strategy."),
        max_length=10000
    )


class Question(models.Model):
    user = models.ForeignKey(User)
    question_index = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    concern = models.CharField(
        verbose_name="For this concern, which package is better?",
        max_length=1000
    )
    likert_comparison = models.IntegerField(
        verbose_name="For this concern, which package is better?",
        choices=choice_range(0, 5),
        default=-1  # this is to avoid showing bogus option
    )
    likert_confidence = models.IntegerField(
        verbose_name="How confident are you?",
        choices=choice_range(0, 5),
        default=-1  # this is to avoid showing bogus option
    )
    likert_comparison_evidence = models.IntegerField(
        verbose_name=(
            "Based only on the evidence you have seen, which package " +
            "is better for this concern?"
        ),
        choices=choice_range(0, 5),
        default=-1  # this is to avoid showing bogus option
    )
    evidence = models.CharField(
        verbose_name="What evidence informs your rating?",
        help_text="Refer to specific pages and content from the web.",
        max_length=10000,
        null=True,
        blank=True
    )
    likert_comparison_intuition = models.IntegerField(
        verbose_name=(
            "Based on your instinct, which package is better for this concern?"),
        choices=choice_range(0, 5),
        default=-1  # this is to avoid showing bogus option
    )
    likert_coverage = models.IntegerField(
        verbose_name="I found all the information that's relevant to this question.",
        choices=choice_range(0, 5),
        default=-1
    )
    scratch_work = models.CharField(
        verbose_name="Scratch work",
        max_length=10000,
        null=True,
        blank=True,
    )
    strategy = models.CharField(
        verbose_name="What was your strategy for answering this question?",
        help_text="What documents did you look at and why?",
        max_length=4000,
        null=True,
        blank=True
    )
    url1 = models.CharField(
        verbose_name="URL of indicator 1",
        max_length=1000,
        null=True,
        blank=True
    )
    url1_where = models.CharField(
        verbose_name="What web site does this URL point to?",
        max_length=1000,
        null=True,
        blank=True
    )
    url1_what = models.CharField(
        verbose_name="What information on that site helped you?",
        max_length=10000,
        null=True,
        blank=True
    )
    url1_why = models.CharField(
        verbose_name="Why was this helpful?",
        max_length=10000,
        null=True,
        blank=True
    )
    url2 = models.CharField(
        verbose_name="URL of indicator 2",
        max_length=1000,
        null=True,
        blank=True,
    )
    url2_where = models.CharField(
        verbose_name="What web site does this URL point to?",
        max_length=1000,
        null=True,
        blank=True,
    )
    url2_what = models.CharField(
        verbose_name="What information on that site helped you?",
        max_length=10000,
        null=True,
        blank=True,
    )
    url2_why = models.CharField(
        verbose_name="Why was this helpful?",
        max_length=10000,
        null=True,
        blank=True,
    )
    extra_information = models.CharField(
        verbose_name=(
            "What additional information do you want " +
            "to see to better answer this question?"),
        max_length=10000,
        null=True,
        blank=True,
    )
    comments = models.CharField(
        max_length=10000,
        null=True,
        blank=True,
    )


class QuestionEvent(models.Model):
    user = models.ForeignKey(User)
    question_index = models.IntegerField(db_index=True)
    time = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=300)


class PackageComparison(models.Model):
    user = models.ForeignKey(User)
    stage = models.CharField(
        choices=verbatim_choices(["before", "after"]),
        max_length=100
    )
    likert_quality = models.IntegerField(
        verbose_name="Which package has a better community and quality of documentation?",
        choices=choice_range(0, 5),
        default=-1,
    )
    likert_preference = models.IntegerField(
        verbose_name="Which package would you rather use?",
        choices=choice_range(0, 5),
        default=-1,
    )
    likert_community = models.IntegerField(
        verbose_name="Which package has a better community?",
        choices=choice_range(0, 5),
        default=-1,
    )
    likert_documentation = models.IntegerField(
        verbose_name="Which package has better documentation?",
        choices=choice_range(0, 5),
        default=-1,
    )


class Postquestionnaire(models.Model):
    user = models.ForeignKey(User)
    important_concern1 = models.CharField(
        verbose_name="To me, the most important question from this set when choosing a package is:",
        choices=verbatim_choices(CONCERNS),
        max_length=1000,
        blank=True,
        null=True,
    )
    important_concern2 = models.CharField(
        verbose_name="The second most important question is:",
        choices=verbatim_choices(CONCERNS),
        max_length=1000,
        blank=True,
        null=True,
    )
    likert_perception_change = models.IntegerField(
        verbose_name=(
            "My perception of the support and documentation for these packages changed " +
            "over the course of answering these questions."
        ),
        choices=choice_range(0, 5),
        default=-1,
    )
    change_justification = models.CharField(
        verbose_name=(
            "If you agree, how did your perception of the support and " +
            "documentation for these packages change over the course of answering " +
            "these questions?"
        ),
        max_length=10000,
        blank=True,
        null=True
    )


class PackagePair(models.Model):
    user = models.ForeignKey(User)
    package1 = models.CharField(
        verbose_name="What is the first package you will be learning about?",
        max_length=1000
    )
    package2 = models.CharField(
        verbose_name="What is the second one?",
        max_length=1000
    )
