from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range


class FeedbackDemographics(Page):
    def vars_for_template(self):
        return {'num_sm_visited': len(self.player.participant.vars['slotMachinesPrev']),
                'total_payoff': self.player.participant.payoff,
                'statusActive': self.player.participant.vars['statusActive'],
                }

    form_model = models.Player
    form_fields = ['email',
                   'satisfaction',
                   'age',
                   'gender',
                   'education',
                   'geographic',
                   'previous_mturk',
                   'reasoning_stay',
                   'reasoning_quit',
                   'reasoning_switch'
                   ]

page_sequence = [
    FeedbackDemographics
]
