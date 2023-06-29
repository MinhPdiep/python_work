guest_list=['Hannah','Steven', 'Anthony', 'Krystal', 'Kamal']
print(f"{guest_list}, come to my dinner!\n")
print(f"Oops! {guest_list[2]} cant make it!\n")
guest_list[2]='Dean'
print(f"{guest_list} are invited to my dinner!\n")
guest_list.insert(0,'Jared')
guest_list.insert(3,'Bryce')
guest_list.append('Bob')
print(f"{guest_list}, come to my dinner!")
print("Only 2 of you can come!")
print(f"{guest_list.pop(0)}, you are no longer invited!")
print(f"{guest_list.pop(2)}, you are not invited either!")
print(f"{guest_list.pop(4)}, you are not invited!")
print(f"{guest_list.pop(3),guest_list.pop(2),guest_list.pop(1)}, you are removed from the list!")
print(f"Congratulation! {guest_list} get to stay!")
del guest_list[0]
del guest_list[0]
print(f"{guest_list}, party canceled, nobody invited!")