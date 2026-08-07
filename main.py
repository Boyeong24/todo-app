def main():
    tasks=[]

    while True:
        print("===== Todo App =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Task")
        print("4. Edit Task")
        print("5. Complete Task")
        print("6. Exit")

        choice=input("Choose: ")

        if choice=="1":
            task_name=input("Enter task: ")
            task={
                "name": task_name,
                "completed":False
            }
            tasks.append(task)
            print("Task added!")

        elif choice=="2":
            print("\n====== Task List =====")

            if len(tasks)==0:
                print("No tasks yet")
            else:
                for number, task in enumerate(tasks, start=1):
                    if task["completed"]:
                        print(f"{number}. [✓] {task['name']}")
                    else:
                        print(f"{number}. [ ] {task['name']}")

        elif choice=="3":
            if len(tasks)==0:
                print("No tasks yet")
            else:
                delete_num=int(input("Delete number: "))
                tasks.pop(delete_num-1)
                print("Task deleted!")

        elif choice=="4":
            if len(tasks)==0:
               print("No tasks yet")
            else:
                edit_num=int(input("Edit number: "))
                if 1<=edit_num<=len(tasks):
                    new_task=input("New task: ")
                    tasks[edit_num-1]=new_task
                    print("Task edited!")
                else:
                    print("Invalid task number.")

        elif choice == "5":
            if len(tasks)==0:
                print("No tasks yet.")

            else:
                complete_num=int(input("Complete number: "))

                if 1<= complete_num <= len(tasks):
                    tasks[complete_num-1]["completed"]=True
                    print("Task completed!")
                else:
                    print("Invalid task number.")

        elif choice=="6":
            print("Goodbye!")
            break

        else:
            print("Please choose 1-6.")
    
if __name__=="__main__":
    main()
