#Each page has its own class where you always specify form_model = Player as we have players for each page
#and we have the form_fields in a list which indicate the variables we have on that page. There will be
#more functionality added here but this is a good start. 

class Welcome(Page):
    form_model = Player

    def before_next_page(self):
        #here we are increasing the counter for each player that goes past the Welcome Page
        self.group.counter += 1

class DemoPage(Page):
    form_model = Player
    form_fields = ['eligibility_question', 'age_question' 'gender', 'sunday_question', 'comment']

class Html_overview(Page):
    form_model = Player

class EndPage(Page):
    form_model = Player

#Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,
                DemoPage,
                Html_overview,
                EndPage]