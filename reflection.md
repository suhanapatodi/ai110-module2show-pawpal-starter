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

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
