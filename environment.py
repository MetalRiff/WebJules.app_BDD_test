from page.login_page import LoginPage
from browser import Browser



def before_all(context):
    """
        Vom defini toate instructiunile care trebuie executate
        sau pe care vrem sa le facem disponibile inaintea TUTUROR testelor/pasilor
        """

    context.browser = Browser()
    context.login_page_object = LoginPage()

def after_all(context):
    """
       Vom defini toate instructiunile care trebuie executate
       sau pe care vrem sa le facem disponibile DUPA TOATE testele
       """
    context.browser.close()
