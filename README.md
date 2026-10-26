# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

=== PawPal+ CLI Demo ===

--- Sorted Schedule (Chronological) ---
 Max - Morning Walk (daily) | Status: ⏳ Pending
 Max - Breakfast Feeding (daily) | Status: ⏳ Pending
 Luna - Veterinarian Checkup (once) | Status: ⏳ Pending
 Max - Evening Medication (daily) | Status: ⏳ Pending

--- Conflict Detection Check ---
⚠️ Conflict Warning: Task 'Breakfast Feeding' (Max) is scheduled at 07:30, which conflicts with 'Morning Walk' (Max).

--- Filtered View: Pending Tasks Only ---
 Max: Morning Walk
 Max: Breakfast Feeding
 Luna: Veterinarian Checkup
 Max: Evening Medication

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
`(.venv) suhanapatodi@Mac ai110-module2show-pawpal-starter % python -m pytest test_pawpal.py
======================== test session starts ========================
platform darwin -- Python 3.13.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /Users/suhanapatodi/Documents/GitHub/ai110-module2show-pawpal-starter
plugins: anyio-4.15.1
collected 4 items                                                   

test_pawpal.py ....                                           [100%]

========================= 4 passed in 0.03s =========================``

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | Schedule.sort_by_time()| Organizes all household tasks chronologically by "HH:MM" timestamps using a lambda sorting key.|
| Filtering | Scheduler.filter_tasks()| Filters tasks by completion status (completed=True/False) and/or specific pet name. |
| Conflict handling | Scheduler.detect_conflicts()| Uses a dictionary hash map to identify and flag tasks scheduled at the exact same timestamp. |
| Recurring tasks | Scheduler.complete_task_with_recurrence()| Automatically provisions a new task instance for the next occurrence when daily or weekly tasks are completed.|

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

Launch the Web App: Run streamlit run app.py in your terminal to open the interactive user interface in your browser.

Register a Pet: Navigate to the "Add Pet" page via the sidebar, enter your pet's name and species (e.g., Max the Dog), and submit the form.

Schedule Care Tasks: Go to the "Add Task" page, select your pet, provide a task description (e.g., Morning Walk), specify a time in "HH:MM" format, and choose a frequency (once, daily, weekly).

View Today's Schedule & Conflicts: Return to the "Dashboard & Schedule" view to see all household tasks sorted chronologically. If any tasks share identical timestamps, warning banners will immediately alert you.

Manage & Complete Tasks: Go to "Manage Tasks" to mark items as complete, which updates their status and automatically triggers recurring task generation.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
