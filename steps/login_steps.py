from behave import *


@given('I am on the jules login page')

def step_impl(context):
    """
        CONTEXT este in primul rand un parametru pe care toate functiile/
        implementarile de scenario steps il vor avea.
        El reprezinta o cutiuta in care pot sa stochez toate obiectele
        instantiate in fisierul environment.py
        """
    #Voi avea nevoie de: o instanta/un obiect al clasei LoginPage
    #si sa apelez metoda navigate_to_login_page

    context.login_page_object.navigate_to_login_page()


@when('I insert correct email and correct password')
def step_impl(context):

    context.login_page_object.insert_correct_email()
    context.login_page_object.insert_correct_password()


@when('I insert correct email and incorrect password')
def step_impl(context):

    context.login_page_object.insert_correct_email()
    context.login_page_object.insert_incorrect_password()

@when('I insert incorrect email and correct password')
def step_impl(context):

    context.login_page_object.insert_incorrect_email()
    context.login_page_object.insert_correct_password()


@when('I click login button')
def step_impl(context):
    context.login_page_object.click_login_button()


@when('I insert correct email and no password')
def step_impl(context):
    context.login_page_object.insert_correct_email()
    context.login_page_object.insert_no_password()


@then('I can login into the jules app')
def step_impl(context):
    context.main_page_object.check_current_url()


@then('I cannot login into the jules app')
def step_impl(context):
    context.login_page_object.check_error_message()


@then('I cannot login into the jules app because no valid email was introduced')
def step_impl(context):
    context.login_page_object.wrong_email_message()


@then('I can logout')
def step_impl(context):
    context.login_page_object.click_logout_button()


@then('I cannot login into the jules app because no valid password was introduced')
def step_impl(context):
    context.login_page_object.no_password_message()
