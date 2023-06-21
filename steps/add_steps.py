from behave import *


@when('I click on Add button')
def impl_steps(context):
    context.add_page_object.access_add_page()


@then('I can add Airplane A380 item to one of my records')
def impl_steps(context):
    context.add_page_object.add_item_to_records()
