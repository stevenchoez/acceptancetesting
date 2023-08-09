Feature: To-Do List Management

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task         | Status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task       |
      | Buy groceries |
      | Pay bills  |
    When the user clears the to-do list
    Then the to-do list should be empty
	
	Scenario: Edit task description
    Given the to-do list contains tasks:
      | Task          | Status  |
      | Buy groceries | Pending |
    When the user edits the description of task "Buy groceries" to "Buy fruits and vegetables"
    Then the to-do list should show task "Buy fruits and vegetables" as pending