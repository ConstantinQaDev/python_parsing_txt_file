import re
from collections import defaultdict
from datetime import datetime

actions_total = defaultdict(int)
actions_users = defaultdict(set)
actions_times = []

time_format = "%Y-%m-%d %H:%M:%S.%f"

with open("logs.txt", "r", encoding='utf8') as file:
    for line in file:
        # Match only "начато" events
        match = re.search(r"\[(.*?)\] Пользователь (\S+): (.+?) - начато", line)
        if match:
            dt_str = match.group(1)
            user_name = match.group(2)
            action = match.group(3)
            dt = datetime.strptime(dt_str, time_format)
            actions_total[action] += 1
            actions_users[action].add(user_name)
            actions_times.append(dt)

if actions_times:
    min_time = min(actions_times)
    max_time = max(actions_times)
    total_minutes = max((max_time - min_time).total_seconds() / 60, 1)
else:
    total_minutes = 1

print(f"{'Операция':20} {'Запусков':10} {'Уникальных пользователей':25} {'Частота (раз/мин)':18}")
for action in actions_total:
    freq = actions_total[action] / total_minutes
    print(f"{action:20} {actions_total[action]:<10} {len(actions_users[action]):<25} {freq:.2f}")





