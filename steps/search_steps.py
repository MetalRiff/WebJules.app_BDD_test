from behave import *

@then('I can select Record filter')
def step_impl(context):
    context.search_page_object.click_filter_button()
    context.search_page_object.select_record_filter()

@then('I can select Type filter')
def step_impl(context):
    context.search_page_object.click_filter_button()
    context.search_page_object.select_type_filter()

@then('I can select Category filter')
def step_impl(context):
    context.search_page_object.click_filter_button()
    context.search_page_object.select_category_filter()

@then('I can select Tag filter')
def step_impl(context):
    context.search_page_object.click_filter_button()
    context.search_page_object.select_tag_filter()

@then('I can select Connection filter')
def step_impl(context):
    context.search_page_object.click_filter_button()
    context.search_page_object.select_connection_filter()

