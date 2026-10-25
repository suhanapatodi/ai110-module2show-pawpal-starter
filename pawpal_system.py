from dataclasses import dataclass, field
from typing import List, Optional, Tuple

@dataclass
class Task:
    """Represents a single pet care activity."""
    description: str
    time: str  # Format "HH:MM"
    frequency: str = "once"  # "once", "daily", "weekly"
    completed: bool = False

    def mark_complete(self):
        """Marks the task as complete."""
        self.completed = True

@dataclass
class Pet:
    """Stores pet details and a list of assigned tasks."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Adds a new task to the pet's schedule."""
        self.tasks.append(task)

    def get_task_count(self) -> int:
        """Returns the total number of tasks for the pet."""
        return len(self.tasks)

@dataclass
class Owner:
    """Manages multiple pets and provides access to all their tasks."""
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Adds a pet to the owner's household."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Tuple[str, Task]]:
        """Retrieves every pet's tasks together with their associated pet names."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet.name, task))
        return all_tasks

class Scheduler:
    """The central 'Brain' that retrieves, organizes, and manages tasks across pets."""
    
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_all_tasks(self) -> List[Tuple[str, Task]]:
        """Retrieves all tasks via the Owner model."""
        return self.owner.get_all_tasks()

    def sort_by_time(self) -> List[Tuple[str, Task]]:
        """Sorts all tasks chronologically by their time attribute."""
        tasks = self.get_all_tasks()
        return sorted(tasks, key=lambda item: item[1].time)

    def filter_tasks(self, completed: Optional[bool] = None, pet_name: Optional[str] = None) -> List[Tuple[str, Task]]:
        """Filters tasks by completion status and/or specific pet name."""
        tasks = self.get_all_tasks()
        filtered = []
        for p_name, task in tasks:
            if completed is not None and task.completed != completed:
                continue
            if pet_name is not None and p_name.lower() != pet_name.lower():
                continue
            filtered.append((p_name, task))
        return filtered

    def detect_conflicts(self) -> List[str]:
        """Detects if two or more tasks are scheduled at the exact same time."""
        tasks = self.get_all_tasks()
        time_map = {}
        warnings = []

        for p_name, task in tasks:
            if task.time in time_map:
                existing_pet, existing_desc = time_map[task.time]
                warnings.append(
                    f"⚠️ Conflict Warning: Task '{task.description}' ({p_name}) is scheduled at {task.time}, "
                    f"which conflicts with '{existing_desc}' ({existing_pet})."
                )
            else:
                time_map[task.time] = (p_name, task.description)
        return warnings

    def complete_task_with_recurrence(self, pet_name: str, task_description: str):
        """Marks a task complete and automatically schedules recurring instances."""
        for pet in self.owner.pets:
            if pet.name.lower() == pet_name.lower():
                for task in pet.tasks:
                    if task.description.lower() == task_description.lower():
                        task.mark_complete()
                        if task.frequency in ["daily", "weekly"]:
                            new_task = Task(
                                description=f"{task.description} (Next Occurrence)",
                                time=task.time,
                                frequency=task.frequency,
                                completed=False
                            )
                            pet.add_task(new_task)
                        return