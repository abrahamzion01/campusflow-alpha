# CampusFlow Design Decisions

## 1. Ticket Representation

Each ticket will be represented as a Python dictionary.

All tickets will be stored in a list of dictionaries named `tickets`.

Each ticket will contain these fields:

* `id`
* `title`
* `category`
* `urgency`
* `affected_users`
* `priority`
* `status`
* `assigned_to`

## 2. Ticket Identification

Each ticket will have a unique ID, such as `T001`, `T002`, and `T003`.

Functions that operate on an existing ticket will identify it by its ID.

## 3. Initial Ticket Values

* New tickets will have the status `open`.
* New tickets will have `assigned_to` set to `None`.
* Priority will be calculated using the rules in the project guide.

## 4. Function Responsibilities

* `create_ticket()` creates a ticket.
* `assign_ticket()` assigns a ticket to a staff member.
* `update_status()` changes a ticket's status while enforcing workflow rules.
* `get_work_queue()` returns unresolved tickets in the required priority order.
* `generate_report()` summarizes ticket counts.
* `load_tickets()` loads tickets from JSON storage.
* `save_tickets()` saves tickets to JSON storage.

## 5. Persistence

The storage module will handle loading tickets from and saving tickets to a JSON file.

Missing storage files will allow the application to start with an empty ticket list. Malformed JSON must produce a clear error instead of silently discarding existing data.

## 6. Testing

We will use Python's built-in `unittest` module to test the application's business logic.

Tests should not depend on interactive terminal input.

## 7. Collaboration

Both team members will use the same ticket structure and agreed function contracts. We will review these decisions together before integrating our branches.

## 8. Function Contracts

- `create_ticket()` returns the newly created ticket dictionary.
- `assign_ticket()` modifies the existing ticket dictionary in the shared list.
- `update_status()` modifies the existing ticket dictionary after validating the requested transition.
- `get_work_queue()` returns a sorted list of unresolved tickets.
- `generate_report()` returns ticket counts grouped by status and priority.
- `load_tickets()` returns the loaded ticket list, or an empty list if the file is missing.
- `save_tickets()` saves the shared ticket list to JSON.

Invalid operations must produce clear errors rather than silently failing.
