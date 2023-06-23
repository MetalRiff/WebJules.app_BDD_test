from behave import *


@then('I can click on Add button')
def impl_steps(context):
    context.add_page_object.access_add_page()


@then('I can click the Close button')
def impl_steps(context):
    context.add_page_object.close_add()


@then('I can add Airbus airplane items to my records')
def impl_steps(context):
    context.add_page_object.add_item_to_records()
