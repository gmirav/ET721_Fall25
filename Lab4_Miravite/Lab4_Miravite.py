"""
Gabriel Miravite
Lab 3, Dictionary and Functions
Sep 10, 2025
"""

print("\n========= Example 1: Dictionary =========")
contacts = {
    "Bill" : "718-111-2222",
    "Martha" : "646-000-3333",
    "Peter" : "212-000-1111"
}
print(contacts)

user1 = contacts["Martha"]
print(f"Martha's phone number = {user1}")

contacts["Anna"] = "646-222-3333"
print(f"Added Anna")
print(contacts)

contacts["Peter"] = "800-000-0000"
print(f"Updated Peter")
print(contacts)

print("\n========= Example 2: Loop thru a Dictionary =========")
# print dictionary keys
for i in contacts:
    print(i)
print()

# print dictionary values
for i in contacts:
    print(contacts[i])
print()

# print dictionary key:value sets
for i in contacts:
    print(f"{i} = {contacts[i]}")

print("\n========= Example 3: Length of a Dictionary =========")
print(f"Dictionary has {len(contacts)} users")

print("\n========= Example 4: Copy of a Dictionary =========")
copy_contact1 = contacts.copy()
copy_contact2 = dict(contacts)
print(f"copy_contact1 = {copy_contact1}")
print(f"copy_contact2 = {copy_contact2}")

print("\n========= Example 5: Remove a key:value pair in a dictionary =========")
print(contacts)
contacts.pop("Peter")
print(contacts)

print("\n========= Example 6: Add a key:value pair in a dictionary =========")
contacts.update({"Lucas" : "212-111-1111"})
print(f"Added Lucas")
print(contacts)

print("\n========= Example 7: Add a key:value pair in a dictionary =========")
print(f"Return items = {contacts.items()}")
print(f"Return keys = {contacts.keys()}")
print(f"Return values = {contacts.values()}")

print("\n========= Example 8: Dictionary Application =========")
phrase = "to be or not to be"
list_phrase = phrase.split()
word_count_dict = {}
for word in list_phrase:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

for word in word_count_dict:
    print(f"\"{word}\" appears {word_count_dict[word]} times")

print("\n========= EXERCISE =========")
users = ["peterpan@yahoo.com","annie@hotmail.com","Carl@hotmail.com","martha@gmail.com","cassie@yahoo.com","Josue@hotmail.com","John@hotmail.com"]
print(users)
domains = {"gmail" : 0, "hotmail" : 0, "yahoo" : 0}
for user in users:
    x = user.find("@")
    if user[x+1:] == "gmail.com":
        domains["gmail"] += 1
    elif user[x+1:] == "hotmail.com":
        domains["hotmail"] += 1
    elif user[x+1:] == "yahoo.com":
        domains["yahoo"] += 1
print("The number of users that use 'gmail', 'hotmail' or 'yahoo' in the list above are saved in the dictionary below:")
print(domains)