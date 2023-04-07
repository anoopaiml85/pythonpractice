# Python program to implement the above approach
class Node:
	# constructor to initialize the node object
	def _init_(self, data):
		self.number = data
		self.next = None


def push(head, A):#push(0,1)
	n = Node(A) 
	n.number = A 
	n.next = head 
	head = n 
	return head


def deleteN(head, position):
	temp = head #head value = 4   temp variable for swap
	prev = head #head value = 4   previous variable to update the next property 
	print(f"Initial {temp.number},{prev.number}")
    # print(f"{temp},{prev}")
	for i in range(0, position): # range(0,5)
		print(f"{i}th iteration {temp.number}, {prev.number}")
		if i == 0 and position == 1:  # for 1st element of the linkedlist
			head = head.next    # 4,3,2,1,0 will be transformed into 3,2,1,0. head changes from 4 to 3 . 
		else:  #for any element in the middle or last
			if i == position-1 and temp is not None: # I = 5-1=4  and temp is not pointing to none.
				print(f"if prevfirst {prev.number}->{prev.next}")
				prev.next = temp.next # temp.next = none value 1 is now pointing to none as next element.
				print(f"if prevsecond {prev.number}->{prev.next}")
			else:
				prev = temp # prev value = 4 
				print(f"else prev {prev.number}->{prev.next}")
				# Position was greater than
				# number of nodes in the list
				if prev is None:
					break
				temp = temp.next #temp value = 4 to 3 
				print(f"else temp {temp.number}->{temp.next}")
	return head


def printList(head):
	while(head):
		if head.next == None:
			print("[", head.number, "] ", "[", hex(id(head)), "]->", "nil")
		else:
			print("[", head.number, "] ", "[", hex(
				id(head)), "]->", hex(id(head.next)))
		head = head.next
	print("")
	print("")


head = Node(0) #position =5 value=0                    -> 0 -> None
head = push(head, 1)#position = 4 value = 1            ->1->0 -> None
head = push(head, 2)#position = 3 value = 2            ->2 ->1 ->0 -> None
head = push(head, 3)#position = 2 value = 3            ->3->2->1->0 -> None
head = push(head, 4)#position = 1 value = 4            ->4->3->2->1->0 -> None

# printList(head)
# print(head)
# Delete any position from list
head = deleteN(head, 5)
# printList(head)