from singly_linked_list import SList

print("\n*------------- START -------------*\n")

print("Example 1:\n")

my_slist_message = SList()
my_slist_message.incert_front("are").incert_front("Linked lists").append("fun!").print_all() 

print("\nExample 2:\n")

my_slist = SList()

my_slist.append("1")
my_slist.append("3")
my_slist.append("5")
my_slist.append("7")
my_slist.print_all()
print(f"len: {my_slist.length}")

print("\n===\n")

my_slist.insert_at("2",1)
my_slist.insert_at("4",3)
my_slist.insert_at("6",5)
my_slist.print_all()
print(f"len: {my_slist.length}")

print("\nExample 3:\n")

my_slist.remove_back()
my_slist.remove_front()
my_slist.remove_val("3")
my_slist.remove_val("5")
my_slist.print_all()
print(f"len: {my_slist.length}")