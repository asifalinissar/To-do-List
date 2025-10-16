import json
import os
from datetime import datetime ,date

class ToDolist:

    def __init__(self , filename = "task.json"):
        self.filename  = filename
        self.task = []
        self.load_task ()
    

    def load_task(self):
        """Load tasks from the json file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename , 'r') as file:
                    data = json.load(file)
                    # coverting the string date to date time format
                    for task in data:
                        if task.get('due_date'):
                            task['due_date'] = datetime.strptime(task["due_date"] , "%Y-%m-%d").date()
                    self.task = data 
        except (json.JSONDecodeError , KeyError , ValueError) as e:
            print(f"⚠️  Error loading tasks: {e}. Starting with empty list.")
            self.task= []


    def save_task(self):
        print("start saving")
        save_task = []
        #change the datetime format to string format for saving in the json
        for task in self.task:
            task_copy = task.copy()
            if task_copy.get("due_date") and isinstance(task_copy["due_date"] , date):
                task_copy["due_date"] = task_copy["due_date"].isoformat()
            save_task.append(task_copy)
        with open(self.filename , 'w') as file :
            json.dump(save_task ,file , indent= 2)

        print("saved sucessfully")


    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("🎯 TO-DO LIST APPLICATION")
        print("="*50)
        print("1. 📝 Add Task")
        print("2. 👀 View Tasks")
        print("3. ✅ Mark Task as Done")
        print("4. 🔄 Mark Task as Not Done")
        print("5. 🗑️  Delete Task")
        print("6. 📅 View Tasks by Priority")
        print("7. 📋 View Tasks by Status")
        print("8. 🚪 Exit")
        print("-"*50)

    

    def add_task(self):
        """Add a new task to the list"""
        print('/n ADD NEW TASK')
        heading = input("enter the heading : ")
        description = input("enter the description")
        while True:
            try :
                priority = input("select Priority 1 : [high] , 2 : [medium] , 3 : [low] , default = 2").strip()
                if not priority:
                    print("you are not selected the priority : it will taken as default")
                    priority = 2
                else:
                    priority = int(priority)

                if priority not in [1, 2, 3]:
                    print("❌ Please enter 1, 2, or 3")
                    continue
                break
            except ValueError:
                print("please enter a valid number")

        due_date = None

        while True:
            date_input = input("Enter the due date (yyyy-mm-dd) or press Enter for Today date due date :").strip()
            if not date_input:
                due_date = datetime.utcnow().date()
                break
            try :
                due_date = datetime.strptime(date_input , '%Y-%m-%d').date()
                if due_date < date.today() :
                    print("you cannot enter a past date")
                    continue
                break

            except ValueError:
                print("enter the date incorrect format")


        task = {
            "id" : len(self.task) + 1,
            "heading" : heading,
            "description" : description,
            "done": False,
            "priority" : priority,
            "create_at" : datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            "due_date" : due_date
        }

        self.task.append(task)
        print("DEBUG: Calling save_task method")
        self.save_task()
        print(f"✅ Task '{heading}' added successfully!")
        print("DEBUG: After save_task call")


    def view_task(self  , tasks = None):
        if tasks is None:
            tasks = self.task
        if not tasks:
            print("No tasks found")
            return
        
        print(f"\n📋 TASKS ({len(tasks)} total)")
        print("-"*80)

        for i , task in enumerate(tasks , 1):
            status = "✅" if task['done'] else "⏳"
            priority_map = {1: "🔥 HIGH", 2: "🔶 MEDIUM", 3: "💤 LOW"}
            priority = priority_map.get(task["priority"] , "unknown")

            due_info = ""

            if task.get("due_date"):
                due_date = task['due_date']
                if isinstance(due_date , str):
                    due_date= datetime.strptime(task["due_date"] , '%Y-%m-%d').date()
                days_until = (due_date - date.today()).days

                if days_until < 0:
                    due_info = f"( overdue by {abs(days_until)})"
                elif days_until == 0:
                    due_info = " (⚠️ Due today!)"
                else:
                    due_info =  f" (Due: {due_date})"

            print(f"{i}. {status} {task['description']} [{priority}]{due_info}")

    def mark_task_done(self , done = True):
        """Mark a task as done or not """
        print("debug : reached up to here")
        action = "done" if done else "not done"
        status_icon = "✅" if done else "⏳"

        if not self.task:
            print("📭 No tasks to mark!")
            return
        print("debug : work up to here")
        self.view_task()

        try :
            task_num = int(input(f"\n Enter the task number to mark as {action} :"))
            if 1 <= task_num <= len(self.task):
                self.task[task_num -1]["done"] = done
                self.save_task()
                print(f"{status_icon} Task {task_num} marked as {action}!")
            else:
                print("❌ Invalid task number!")
        except ValueError:
            print("❌ Please enter a valid number!")


    def delete_task(self):
        """Delete a task from the list"""
        if not self.task:
            print("📭 No tasks to delete!")
            return
        self.view_task()

        try:
            task_num = int(input("\nEnter task number to delete: "))
            if 1 <= task_num <= len(self.task):
                deleted_task = self.task.pop(task_num - 1)
                # Update IDs for remaining tasks
                for i, task in enumerate(self.task, 1):
                    task['id'] = i
                self.save_task()
                print(f"🗑️  Task '{deleted_task['description']}' deleted successfully!")
            else:
                print("❌ Invalid task number!")
        except ValueError:
            print("❌ Please enter a valid number!")
    # this is the supporting function used for the view_tasks_by_priority

    def get_priority(self , task):
        return task["priority"]

    def view_tasks_by_priority(self):
        """view tasks sorted by priority"""
        if not self.task:
            print("📭 No tasks found!")
            return
        sorted_tasks = sorted(self.task, key=self.get_priority)
        print("\n📋 TASKS SORTED BY PRIORITY")
        self.view_task(sorted_tasks)

    def view_tasks_by_status(self):
        """view tasks grouped by completion status"""
        if not self.task:
            print("📭 No tasks found!")
            return
        
        # for task in self.task:
        #     completed_tasks = []
        #     if task['done']:
        #         completed_tasks.append(task)

        """for the above code we use the list comprehension"""

        completed_tasks = [task for task in self.task if task['done']]
        pending_tasks = [task for task in self.task if not task['done']]

        print("\n✅ COMPLETED TASKS")
        self.view_task(completed_tasks)

        print("\n⏳ PENDING TASKS")
        self.view_task(pending_tasks)

        total = len(self.task)
        completed = len(completed_tasks)
        pending = len(pending_tasks)
        completion_rate = (completed / total * 100) if total > 0 else 0
        
        print(f"\n📊 STATISTICS: {completed}/{total} completed ({completion_rate:.1f}%)")



def main():
    """Main funciton to run the To-Do List Applicaton"""

    todo_app = ToDolist()

    while True:
        todo_app.display_menu()

        try:
            choice  = input("\nEnter your choice (1-8): ").strip()

            if choice == '1':
                todo_app.add_task()
            elif choice == '2':
                todo_app.view_task()
            elif choice == '3':
                print("debug : calling the function")
                try:
                    todo_app.mark_task_done(done=True)
                except Exception as e:
                    print(f"some error occured {e}")
            elif choice == '4':
                todo_app.mark_task_done(done=False)
            elif choice == '5':
                todo_app.delete_task()
            elif choice == '6':
                todo_app.view_tasks_by_priority()
            elif choice == '7':
                todo_app.view_tasks_by_status()
            elif choice == '8':
                print("\n👋 Thank you for using the To-Do List App! Goodbye!")
                break
            else:
                print("❌ Invalid choice! Please enter a number between 1-8.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()



