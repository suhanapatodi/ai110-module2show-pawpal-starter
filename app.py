import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+ Pet Care Manager", page_icon="🐾", layout="wide")

# Initialize session state so data persists across page refreshes
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Primary Owner")

owner = st.session_state.owner
scheduler = Scheduler(owner)

st.title("🐾 PawPal+ Smart Pet Care Management System")
st.sidebar.header("Navigation")
menu = st.sidebar.selectbox("Choose Action", ["Dashboard & Schedule", "Add Pet", "Add Task", "Manage Tasks"])

if menu == "Dashboard & Schedule":
    st.header("Today's Smart Schedule")
    
    # Conflict Warnings
    conflicts = scheduler.detect_conflicts()
    if conflicts:
        for warning in conflicts:
            st.warning(warning)
            
    # Sorted Schedule
    tasks = scheduler.sort_by_time()
    if tasks:
        st.subheader("Chronological Task List")
        for pet_name, task in tasks:
            status = "✅ Completed" if task.completed else "⏳ Pending"
            col1, col2, col3 = st.columns([2, 3, 2])
            with col1:
                st.write(f"**{pet_name}**")
            with col2:
                st.write(f"{task.time} - {task.description} *({task.frequency})*")
            with col3:
                st.write(status)
    else:
        st.info("No tasks scheduled yet. Use the sidebar to add a pet and schedule tasks!")

elif menu == "Add Pet":
    st.header("Register a New Pet")
    with st.form("add_pet_form"):
        pet_name = st.text_input("Pet Name")
        species = st.selectbox("Species", ["Dog", "Cat", "Bird", "Rabbit", "Other"])
        submitted = st.form_submit_button("Add Pet")
        if submitted and pet_name:
            new_pet = Pet(name=pet_name, species=species)
            owner.add_pet(new_pet)
            st.success(f"Successfully added {pet_name} the {species}!")

elif menu == "Add Task":
    st.header("Schedule a New Task")
    if not owner.pets:
        st.warning("Please add a pet first before scheduling tasks.")
    else:
        with st.form("add_task_form"):
            pet_names = [pet.name for pet in owner.pets]
            selected_pet = st.selectbox("Select Pet", pet_names)
            description = st.text_input("Task Description (e.g., Morning Walk, Medication)")
            time_str = st.text_input("Time (HH:MM format, e.g., 07:30)", value="08:00")
            frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])
            
            submitted = st.form_submit_button("Schedule Task")
            if submitted and description:
                for pet in owner.pets:
                    if pet.name == selected_pet:
                        pet.add_task(Task(description=description, time=time_str, frequency=frequency))
                        st.success(f"Added task '{description}' for {selected_pet} at {time_str}!")

elif menu == "Manage Tasks":
    st.header("Manage & Complete Tasks")
    tasks = scheduler.get_all_tasks()
    if not tasks:
        st.info("No tasks available to manage.")
    else:
        for pet_name, task in tasks:
            if not task.completed:
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"**{pet_name}**: {task.description} at {task.time} *({task.frequency})*")
                with col2:
                    if st.button("Complete", key=f"{pet_name}_{task.description}_{task.time}"):
                        scheduler.complete_task_with_recurrence(pet_name, task.description)
                        st.success(f"Marked '{task.description}' complete!")
                        st.rerun()