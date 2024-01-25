guest_list = ['mozart', 'turing', "shakespeare"]
invite1 = guest_list[0]
message = f"\nDearest {invite1.title()} you are cordially invited to dinner."
print(message)
invite2 = guest_list[1]
message = f"\nDearest {invite2.title()} you are cordially invited to dinner."
print(message)
invite3 = guest_list[2]
message = f"\nDearest {invite3.title()} you are cordially invited to dinner."
print(message)
decline = guest_list[2]
text = f"\nUnfortunately {decline.title()} will not be able to make it to dinner"
guest_list.append('Vonnegut')
print(text)
invite4 = guest_list[3]
message = f"\nDearest {invite4.title()} you are cordially invited to dinner."
print(message)
guest_list.insert(0, 'jesus')
guest_list.insert(2, 'harvard')
invite5 = guest_list[0]
message = f"\nDearest {invite5.title()} you are cordially invited to dinner."
print(message)
invite6 = guest_list[2]
message = f"\nDearest {invite6.title()} you are cordially invited to dinner."
print(message)
deny = guest_list.pop()
deny1 = guest_list.pop()
deny2 = guest_list.pop()
deny3 = guest_list.pop()
denial = f"\nUnfortunately the following will not be able to make dinner: {deny.title()}, {deny1.title()}, {deny2.title()}, and {deny3.title()}."
print(denial)
final_list = f"\nWhich means that the only two who will be available will be {guest_list[0].title()} and {guest_list[1].title()}"
print(final_list)
print(len(guest_list))