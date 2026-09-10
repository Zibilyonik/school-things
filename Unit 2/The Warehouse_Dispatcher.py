### Practice task  the software for an Amazon-style warehouse.

dispatch_queue = []
shipped_stack = []

while True:
    print("1. Place New Order")
    print("2. Ship Next Order")
    print("3. Cancel Last Shipment (Undo)")
    print("4. View Manifest")
    print("5. Exit System")
    choice = input("Select Option: ")


    # 1. PLACE ORDER (Enqueue)
    if choice == '1':
        item = input("Enter Order Details: ")
        dispatch_queue.append(item)
        print(f"Order received: '{item}'")


    # 2. SHIP NEXT (Dequeue -> Push)
    elif choice == '2':
        if len(dispatch_queue) == 0:
            print("No pending orders to ship.")
        else:
            # FIFO: Remove from index 0(front of line)(simulating dequeue)
            box = dispatch_queue.pop(0)
            # LIFO: Add to end (top of stack)(simulating push)
            shipped_stack.append(box)
            print(f"Shipped: '{box}' loaded onto truck.")


    # 3. CANCEL SHIPMENT (Pop -> Enqueue)
    elif choice == '3':
        if len(shipped_stack) == 0:
            print("No shipped orders to cancel.")
        else:
            # Remove the most recent item(top of stack)(simulating pop)
            returned_box = shipped_stack.pop()
            # Insert at index 0 (Front of line)(simulating enqueue)
            dispatch_queue.insert(0, returned_box)
            print(f"Canceled: '{returned_box}' returned to processing.")


    # 4. VIEW MANIFEST
    elif choice == '4':
        print("To Be Shipped (Queue):", dispatch_queue)
        print("On The Truck  (Stack):", shipped_stack)


    # 5. QUIT
    elif choice == '5':
        print("System shutting down...")
        break


    else:
        print("Invalid command.")



