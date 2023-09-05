import queueADT
q = queueADT.Queue()
while(True):
    print("1:Insert,2:Delete,3:Display,4:length,5:Exit")
    choice = int(input("Enter the choice:"))
    if choice == 1:
        item = input("Enter the item to insert")
        q.enqueue(item)
    elif choice == 2:
        del_item = q.dequeue()
        print("Deleted item is ",del_item)
    elif choice == 3:
        q.display()
    elif choice == 4:
        n = q.length()
        print("Length of the queue is ",n)
    elif choice == 5:
        break
