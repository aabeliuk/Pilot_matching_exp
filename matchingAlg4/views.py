import json

from matchingAlg4 import models
from matchingAlg4.models import Constants
from ._builtin import Page, WaitPage


class MyPage(Page):
    """Description of the game: How to play and potential returns"""
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {'main_image_path': "matchingAlg4\main1.jpg"}





class ResultsWaitPage(WaitPage):
    template_name = 'matchingAlg4/ResultsWaitPage.html'

    def is_displayed(self):
        return self.round_number != 1 and self.player.participant.vars.get('statusActive')

    def vars_for_template(self):
        return {'status': self.player.in_round(self.round_number-1).offer_accepted,
                'image_path': 'matchingAlg4/play{}.jpg'.format(self.player.in_round(self.round_number-1).offer_accepted),
                }

    def after_all_players_arrive(self):
        self.group.before_next_round()


class ResultsOptions(Page):
    """Player: Choose whether to return, switch, or quit slot machines"""
    def vars_for_template(self):
        with open("matchingAlg4/static/matchingAlg4/image_credits.json") as source:
            credit_source = json.loads(source.read())
        return {
                'round_number': self.round_number,
                'balance': sum([p.payoff for p in self.player.in_all_rounds()]),
                'rounds_remaining': Constants.num_rounds - self.round_number,
                'image_path': 'matchingAlg4/{}.jpg'.format(self.player.current_slot_machine_id),
                'image_credit': credit_source[str(self.player.current_slot_machine_id)],
                'quit_pay': self.player.quit_payoff(),
                'quit_pay_per_round': self.player.quit_payoff()/(Constants.num_rounds - self.round_number),
                'average_pay_prev': self.player.group.average_pay_prev()
                }

    form_model = models.Player
    form_fields = ['offer_accepted']

    timeout_seconds = Constants.timeout_seconds
    timeout_submission = {'offer_accepted': 3}  # player quits if times out

    def is_displayed(self):
        return self.player.participant.vars.get('statusActive')


class SorryBye(Page):
    def is_displayed(self):
        return self.player.participant.vars['statusActive'] == 'Timeout'


page_sequence = [
    ResultsWaitPage,
    SorryBye,
    ResultsOptions,

]
