import re

requests_per_minute = {}

with open("logs.txt", "r", encoding='utf8') as file:
    logs = file.readlines()

    for line in logs:
        match_time = re.search(r"\[(.*?)\]", line)
        match_action = re.search(r": (.*?) -", line)

        if match_time and match_action:
            full_time = match_time.group(1)
            short_time = full_time[:16]
            action = match_action.group(1)

            if short_time not in requests_per_minute:
                requests_per_minute[short_time] = {}

            if action not in requests_per_minute[short_time]:
                requests_per_minute[short_time][action] = 1
            else:
                requests_per_minute[short_time][action] += 1

for minute, actions in requests_per_minute.items():
    print(f"\n{minute}:")
    for action, count in actions.items():
        print(f"  {action}: {count}")
