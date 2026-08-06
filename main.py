def main():
    tasks=[]

    while True:
        print("===== Todo App =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice=input("Choose: ")

        if choice=="1":
            task=input("Enter task: ")
            tasks.append(task)
            print("Task added!")

        elif choice=="2":
            print("\n====== Task List =====")

            if len(tasks)==0:
                print("No tasks yet")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice=="3":
            if len(tasks)==0:
                print("No tasks yet")
            else:
                delete_num=int(input("Delete number: "))
                tasks.pop(delete_num-1)
                print("Task deleted!")
                
        elif choice=="4":
            print("Goodbye!")
            break

        else:
            print("Please choose 1, 2, or 3.")
    
if __name__=="__main__":
    main()