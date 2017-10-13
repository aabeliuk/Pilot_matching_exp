from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import random


class FirstWait(WaitPage):
    template_name = 'giveConsentExit/FirstWait.html'
    group_by_arrival_time = True

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {'num_others': self.num_waiting, 'num_needed': Constants.num_players}

    def get_players_for_group(self, waiting_players):
        self.num_waiting = len(waiting_players)
        if len(waiting_players) >= Constants.num_players:
            random.shuffle(waiting_players)
            '''
            # add more integers to the condition_ids list, as vary players and outside payout
            condition_ids = [1, 2]
            # 1: 4 players/group, 2: 8 players/group
            selection = random.choice(condition_ids)

            for p in waiting_players:
                p.participant.vars["condition"] = selection
            '''
            return waiting_players


class MyPage(Page):
    """Description of the game: How to play and potential returns"""
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {'main_image_path': "consented_sort\main1.jpg"}

page_sequence = [
    FirstWait,
    MyPage
]
