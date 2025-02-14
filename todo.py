Todo app
user can add,remove and mark todo ad completed
tasks=[]
def show_task():
    print("here are the task")
    for i,task in enumerate(tasks,1):

        print(f"the task are {i}.{task}")
def addtask(task):
     tasks.append(task)
def removetask(index):
      if 1<=index<= len(tasks):
        removed=tasks.pop(index-1)
        print(f'Here is the todo removed: {removed}')
     
def todo_app():
  while True:
       show_task()
       action=input("Type which action you want A[add],R[move] or Q[uit] :").strip().lower()
       if action == 'a':
          inputstuff=input("Enter todo").strip()
          addtask(inputstuff)
       elif action == 'r':
            indexinputed=int(input('Enter the index of  todo you want to remove'))
            removetask(indexinputed)
       elif action == 'q':
            print("Goobye forks")
            break
todo_app()
