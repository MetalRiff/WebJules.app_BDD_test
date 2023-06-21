from behave import *


@then('I can logout')
def step_impl(context):
    context.search_page_object.click_logout_button()

