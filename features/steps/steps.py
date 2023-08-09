from behave import given, when, then

to_do_list = []

@given('the to-do list contains tasks:')
def step_given_to_do_list_contains_tasks(context):
    for row in context.table:
        task = row['Task']
        status = row.get('Status', 'Pending')
        to_do_list.append({'task': task, 'status': status})

@when('the user marks task "{task}" as completed')
def step_when_user_marks_task_as_completed(context, task):
    for item in to_do_list:
        if item['task'] == task:
            item['status'] = 'Completed'
            break

@then('the to-do list should show task "{task}" as completed')
def step_then_to_do_list_should_show_task_as_completed(context, task):
    for item in to_do_list:
        if item['task'] == task:
            assert item['status'] == 'Completed'
            break

@when('the user clears the to-do list')
def step_when_user_clears_to_do_list(context):
    to_do_list.clear()

@then('the to-do list should be empty')
def step_then_to_do_list_should_be_empty(context):
    assert len(to_do_list) == 0
    

@when('the user edits the description of task "{task}" to "{new_description}"')
def step_when_user_edits_task_description(context, task, new_description):
    for item in to_do_list:
        if item['task'] == task:
            item['task'] = new_description
            break

@then('the to-do list should show task "{task}" as pending')
def step_then_to_do_list_should_show_task_as_pending(context, task):
    for item in to_do_list:
        if item['task'] == task:
            assert item['status'] == 'Pending'
            break