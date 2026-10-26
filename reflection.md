# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
The system is anchored by four primary classes:
- **`Task`**: Represents individual activities with descriptions, timestamps, frequencies, and completion flags.
- **`Pet`**: Holds pet metadata and a collection of assigned tasks.
- **`Owner`**: Manages multiple pets and aggregates all household tasks via `get_all_tasks()`.
- **`Scheduler`**: Acts as the algorithmic layer, querying the owner to process sorting, filtering, conflict checks, and recurring tasks.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
During implementation, the initial design was refined to ensure the `Scheduler` queries the `Owner` model directly rather than iterating over isolated pets. This decoupled the UI from data structures and simplified multi-pet task aggregation.
---

## 2. Scheduling Logic and Tradeoffs

### a. Smarter Scheduling
Algorithms were implemented to handle chronological sorting via Python's built-in `sorted()` function with lambda keys, multi-parameter filtering, recurrence generation using task duplication logic, and dictionary-based exact-time conflict detection.

### b. Tradeoffs
The conflict detection algorithm checks for exact string matches on the `time` attribute ("HH:MM"). While lightweight and efficient for a CLI/Streamlit app, this tradeoff means tasks spanning variable durations or overlapping intervals (e.g., a 1-hour groom starting at 10:00 vs. a 10:30 medication) are not flagged unless their start times are identical.

---

## 3. AI Collaboration

- **Effective AI Features**: Agent mode and structural code scaffolding were particularly useful for establishing clean Python dataclasses and writing initial test stubs.
- **Human Oversight**: An AI suggestion to handle recurrence by mutating global state was rejected in favor of an encapsulated method that appends new task instances directly to the respective pet's task list.
- **Workflow**: Maintaining separate chat sessions for design, implementation, and testing kept context windows focused and prevented architectural drift. As the lead architect, human oversight was essential for validating edge cases and ensuring cohesive class integration.

---

## 4. Testing and Verification

**a. What you tested**

We tested four core behaviors:
1. **Task Completion**: Verified that calling `mark_complete()` successfully changes a task's completion status.
2. **Task Addition**: Verified that adding a task correctly increments a pet's task count.
3. **Chronological Sorting**: Verified that tasks are returned in correct chronological order regardless of insertion order.
4. **Conflict Detection**: Verified that the scheduler correctly flags tasks scheduled at duplicate times.
======================== test session starts ========================
platform darwin -- Python 3.13.15, pytest-9.1.1, pluggy-1.7.0
rootdir: /Users/suhanapatodi/Documents/GitHub/ai110-module2show-pawpal-starter
plugins: anyio-4.15.1
collected 4 items                                                   

test_pawpal.py ....                                           [100%]

========================= 4 passed in 0.03s =========================

**b. Confidence**

We have 5/5 stars confidence in the system's reliability because all automated unit tests pass cleanly with green checkmarks, and the CLI/Streamlit workflows have been manually verified. If we had more time, we would test edge cases such as invalid time format strings (e.g., "25:61") and overlapping task duration intervals.

---

## 5. Reflection

a. What went well

We are most satisfied with the clean object-oriented encapsulation and how seamlessly the backend logic layer integrated with Streamlit's st.session_state to provide persistent state management across page reloads.

b. What you would improve

If we had another iteration, we would implement robust data persistence (e.g., saving pets and tasks to a data.json file) and upgrade conflict detection to support overlapping time intervals and task durations.

c. Key takeaway

The most important takeaway is that AI is an incredible accelerator for scaffolding and syntax generation, but rigorous human architectural oversight as the "lead architect" is mandatory to ensure correct class relationships, data encapsulation, and boundary handling.
