class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # მეთოდი, რომელიც ეძებს გადაცემულ ელემენტს და შლის მას
    def search(self, target):
        if not self.head:
            print("სია ცარიელია!")
            return False

        # თუ საძიებო ელემენტი პირველია (head)
        if self.head.data == target:
            self.head = self.head.next
            print(f"ელემენტი '{target}' მოიძებნა და წაიშალა!")
            return True

        # სიის გავლა და ელემენტის მოძებნა/წაშლა
        curr = self.head
        while curr.next and curr.next.data != target:
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next
            print(f"ელემენტი '{target}' მოიძებნა და წაიშალა!")
            return True
        else:
            print(f"ელემენტი '{target}' ვერ მოიძებნა!")
            return False

    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elements) if elements else "სია ცარიელია")


# დემონსტრაცია
if __name__ == "__main__":
    ll = LinkedList()
    for val in [10, 20, 30, 40, 50]:
        ll.append(val)

    print("საწყისი სია:")
    ll.display()

    print("\n30-ის მოძებნა და წაშლა:")
    ll.search(30)
    ll.display()

    print("\n10-ის მოძებნა და წაშლა:")
    ll.search(10)
    ll.display()

    print("\n99-ის ძებნა (არარსებული):")
    ll.search(99)
    ll.display()
