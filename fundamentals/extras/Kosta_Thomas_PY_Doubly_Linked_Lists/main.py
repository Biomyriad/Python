from dllist import Dllist

my_dllist = Dllist()

print(f"ln: {my_dllist.length}")
my_dllist.add("a")
print(f"ln: {my_dllist.length}")
my_dllist.add("b")
print(f"ln: {my_dllist.length}")
my_dllist.add("c")
print(f"ln: {my_dllist.length}")
my_dllist.add("d")
print(f"ln: {my_dllist.length}")
my_dllist.print_all()

print("\n------\n")

my_dllist.remove_val("d")
print(f"ln: {my_dllist.length}")
my_dllist.print_all()

print("\n------\n")

my_dllist.incert_val("head test",0)
my_dllist.incert_val("1",2)
my_dllist.incert_val("2",4)
# Not being able to place new node at tail is intended
# as learn platform specifies "before a given value, at a certain index"
my_dllist.incert_val("tail test", my_dllist.length - 1)
print(f"ln: {my_dllist.length}")
my_dllist.print_all()

