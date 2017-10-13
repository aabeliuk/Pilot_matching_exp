from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    email = models.CharField(
        verbose_name= "Please enter you email address, so we may send you a code to access the payment you earned"
    )

    age = models.PositiveIntegerField(
        verbose_name='What is your age?',
        min=18, max=125)

    gender = models.CharField(
        choices=['Male', 'Female'],
        verbose_name='What is your gender?',
        widget=widgets.RadioSelect())

    education = models.CharField(
        choices=['Less than a high school degree', 'High School Diploma', 'Vocational Training','Attended College','Bachelor’s Degree','Graduate Degree','Unknown' ],
        verbose_name='What is the highest level of education you have completed?',
        widget=widgets.RadioSelect()
    )

    geographic = models.CharField(
        verbose_name='In which city and country did you grow up? If you lived in more than one place, list the one in which you spent the most time. (If the United States, please also indicate the state)'
    )

    previous_mturk = models.IntegerField(
        min=0,
        verbose_name='Have you previously done any experiments on Mechanical Turk or other online sites? If you have not, please type 0 in the response box. If yes, please indicate how many experiments you have done in total.'
    )

    satisfaction = models.CharField(
        choices=['Very pleased', 'Pleased', 'Neutral', 'Displeased', 'Very displeased'],
        verbose_name='How satisfied are you with the outcome of this game?',
        widget=widgets.RadioSelectHorizontal())

    reasoning_stay = models.CharField(
        verbose_name='If/when you remained at the same planet(s), why did you stay at that/those planet(s)?'
    )

    reasoning_switch = models.CharField()

    reasoning_quit = models.CharField()
    # check that player is human rather than robot [like Recaptcha]

