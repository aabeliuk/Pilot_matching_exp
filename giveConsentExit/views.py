from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import random


class ConsentForm(Page):
    form_model = models.Player
    form_fields = ['consent']


class SorryBye(Page):
    def is_displayed(self):
        return not self.player.consent



page_sequence = [
    ConsentForm,
    SorryBye
]
