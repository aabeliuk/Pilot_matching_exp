from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,

)
import random


class Constants(BaseConstants):
    name_in_url = 'giveConsentExit'
    num_players = 2*4
    players_per_group = None
    num_rounds = 1
    instructions_template = 'giveConsentExit/Instructions.html'

    mins_required = 10
    baseline = 50


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField()




