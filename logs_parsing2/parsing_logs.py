import re

users_actions = {}

with open("logs.txt", "r", encoding='utf8') as file:
    logs = file.readlines()

    for line in logs:
        match = re.search(r"Пользователь (\S+): ([\S\s]+?) -", line)
        if match:
            user_name = match.group(1)
            action = match.group(2)
            if user_name not in users_actions:
                users_actions[user_name] = {}
            if action not in users_actions[user_name]:
                users_actions[user_name][action] = 1
            else:
                users_actions[user_name][action] += 1

print(f"Total unique users: {len(users_actions)}")

for user, actions in users_actions.items():
    print(f"\n{user}:")  # Changed from 'users' to 'user'
    for action, count in actions.items():
        print(f"  {action}: {count} times")

