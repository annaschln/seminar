from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Anna Schleiter Nielsen'
doc = 'Homework1: Sunday Question'

class Constants(BaseConstants):
    name_in_url = 'survey-example-sonntagsfrage'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    counter = models.IntegerField(initial = 0)

class Player(BasePlayer):
    
#The Variables are structured on the base of pages
    eligibility_question = models.IntegerField(initial=-999)
    gender = models.IntegerField(initial=-999)
    sunday_question = models.IntegerField(initial=-999)
    age_question = models.IntegerField(max=110, min=1, label="Bitte geben Sie ihr Alter an:")
    comment = models.StringField(blank = True, label="Wollen Sie noch etwas hinzufügen?")

def age_question_error_message(player, value):
    if value < 18:
        return 'Sie sind zu jung. Sind Sie sich sicher, dass Sie wahlberechtigt sind?'
