# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # Write your code here.
    tortoise = head.next
    hare = head.next.next
    while tortoise is not hare:
        tortoise = tortoise.next
        hare = hare.next.next
    one_stepper2 = head
    while tortoise is not one_stepper2:
        tortoise = tortoise.next
        one_stepper2 = one_stepper2.next
    return tortoise
