📝 To-Do List Application
A simple yet powerful command-line To-Do List application built with Python that helps you manage your tasks efficiently.

✨ Features
✅ Add Tasks - Create tasks with descriptions, priorities, and due dates

👀 View Tasks - Display all tasks with visual status indicators

✅ Mark Tasks - Mark tasks as done or not done

🗑️ Delete Tasks - Remove tasks from your list

📅 Smart Sorting - View tasks by priority or completion status

💾 Auto-Save - Tasks are automatically saved to a JSON file

⚡ Priority Levels - High, Medium, and Low priority support

🔔 Due Date Alerts - Visual warnings for overdue and upcoming tasks

🚀 Installation
Clone or download the Python script

Ensure you have Python 3.6+ installed

No additional dependencies required - uses only built-in Python modules

🎯 Usage
Run the application:

bash
python todo_app.py
Main Menu Options:
text
1. 📝 Add Task      - Create a new task
2. 👀 View Tasks    - Show all tasks
3. ✅ Mark Done     - Mark task as completed
4. 🔄 Mark Not Done - Mark task as pending
5. 🗑️ Delete Task   - Remove a task
6. 📅 By Priority   - View tasks sorted by priority
7. 📋 By Status     - View completed vs pending tasks
8. 🚪 Exit         - Quit the application
📋 Task Structure
Each task contains:

ID: Unique identifier

Heading: Task title

Description: Detailed task information

Priority: 1 (High), 2 (Medium), 3 (Low)

Status: Done or Not Done

Due Date: Optional deadline with smart alerts

Created At: Automatic timestamp

🎨 Visual Indicators
✅ Green Check - Completed tasks

⏳ Hourglass - Pending tasks

🔥 Fire - High priority

🔶 Orange Diamond - Medium priority

💤 Sleeping - Low priority

⚠️ Warning - Due today or overdue

💾 Data Storage
Tasks are automatically saved to tasks.json

Data persists between application sessions

JSON format for easy readability and backup

🛠️ Technical Details
Built with: Python 3.6+

Storage: JSON file format

Dependencies: Only standard library modules

Error Handling: Comprehensive input validation and error messages

📁 File Structure
text
todo_app.py          # Main application file
tasks.json           # Auto-generated task storage (created on first run)
🎮 Example Usage
text
🎯 TO-DO LIST APPLICATION
==================================================
1. 📝 Add Task
2. 👀 View Tasks
3. ✅ Mark Task as Done
4. 🔄 Mark Task as Not Done
5. 🗑️ Delete Task
6. 📅 View Tasks by Priority
7. 📋 View Tasks by Status
8. 🚪 Exit
--------------------------------------------------

Enter your choice (1-8): 1

ADD NEW TASK
enter the heading: Complete Project
enter the description: Finish the Python To-Do app
Select priority - 1: High, 2: Medium, 3: Low [default: 2]: 1
Enter due date (YYYY-MM-DD) or press Enter for today: 2024-12-25

✅ Task 'Complete Project' added successfully!
