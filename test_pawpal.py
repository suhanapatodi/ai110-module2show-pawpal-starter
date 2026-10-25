import pytest
from pawpal_system import Owner, Pet, Task, Scheduler

def test_task_completion():
    """Verify that marking a task complete updates its status."""
    task = Task(description="Grooming", time="11:00", completed=False)
    assert task.completed is False
    task.mark_complete()
    assert task.completed is True

def test_pet_task_addition():
    """Verify that adding a task increases the pet's task count."""
    pet = Pet(name="Rocky", species="Dog")
    assert pet.get_task_count() == 0
    task = Task(description="Fetch", time="09:00")
    pet.add_task(task)
    assert pet.get_task_count() == 1

def test_scheduler_sorting():
    """Verify tasks are correctly sorted chronologically by time."""
    owner = Owner(name="Alex")
    pet = Pet(name="Simba", species="Cat")
    owner.add_pet(pet)
    pet.add_task(Task(description="Dinner", time="18:30"))
    pet.add_task(Task(description="Breakfast", time="08:00"))
    
    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()
    
    assert sorted_tasks[0][1].time == "08:00"
    assert sorted_tasks[1][1].time == "18:30"

def test_conflict_detection():
    """Verify the scheduler flags tasks scheduled at the same time."""
    owner = Owner(name="Jordan")
    dog = Pet(name="Zeus", species="Dog")
    cat = Pet(name="Cleo", species="Cat")
    owner.add_pet(dog)
    owner.add_pet(cat)
    
    dog.add_task(Task(description="Medication", time="12:00"))
    cat.add_task(Task(description="Feeding", time="12:00"))
    
    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) == 1
    assert "Conflict Warning" in conflicts[0]