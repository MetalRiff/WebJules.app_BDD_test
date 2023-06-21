from page.login_page import LoginPage
from page.search_page import SearchPage
from page.add_page import AddPage
from browser import Browser



def before_all(context):
    """
        Vom defini toate instructiunile care trebuie executate
        sau pe care vrem sa le facem disponibile inaintea TUTUROR testelor/pasilor
        """

    context.browser = Browser()
    context.login_page_object = LoginPage()
    context.search_page_object = SearchPage()
    context.add_page_object = AddPage()

def after_all(context):
    """
       Vom defini toate instructiunile care trebuie executate
       sau pe care vrem sa le facem disponibile DUPA TOATE testele
       """
    context.browser.close()
