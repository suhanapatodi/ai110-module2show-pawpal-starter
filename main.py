from pawpal_system import Owner, Pet, Task, Scheduler

def main():
    print("=== PawPal+ CLI Demo ===")
    
    # 1. Create Owner and Pets
    owner = Owner(name="Sarah Jenkins")
    dog = Pet(name="Max", species="Dog")
    cat = Pet(name="Luna", species="Cat")
    
    owner.add_pet(dog)
    owner.add_pet(cat)
    
    # 2. Add Tasks (Including an intentional time conflict)
    dog.add_task(Task(description="Morning Walk", time="07:30", frequency="daily"))
    dog.add_task(Task(description="Breakfast Feeding", time="07:30", frequency="daily"))  # Conflict!
    cat.add_task(Task(description="Veterinarian Checkup", time="14:00", frequency="once"))
    dog.add_task(Task(description="Evening Medication", time="19:00", frequency="daily"))
    
    # 3. Initialize Scheduler
    scheduler = Scheduler(owner=owner)
    
    # 4. Display Sorted Schedule
    print("\n--- Sorted Schedule (Chronological) ---")
    sorted_tasks = scheduler.sort_by_time()
    for pet_name, task in sorted_tasks:
        status_str = "✅ Completed" if task.completed else "⏳ Pending"
        print(f"[{task.time}] {pet_name} - {task.description} ({task.frequency}) | Status: {status_str}")
        
    # 5. Conflict Detection
    print("\n--- Conflict Detection Check ---")
    conflicts = scheduler.detect_conflicts()
    if conflicts:
        for warning in conflicts:
            print(warning)
    else:
        print("No schedule conflicts detected.")
        
    # 6. Filter Pending Tasks
    print("\n--- Filtered View: Pending Tasks Only ---")
    pending_tasks = scheduler.filter_tasks(completed=False)
    for pet_name, task in pending_tasks:
        print(f"[{task.time}] {pet_name}: {task.description}")

if __name__ == "__main__":
    main()