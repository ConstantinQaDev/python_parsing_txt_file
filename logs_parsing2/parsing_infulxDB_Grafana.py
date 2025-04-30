# from influxdb_client import InfluxDBClient, Point
# from datetime import datetime
# import re, time
#
# # InfluxDB connection parameters
# url = "http://localhost:8086"
# token = "5LFw_xeyuRsNHv4OGTZD9M1MLrhxOm8LLjdk8WzgaJ_-JHGLDABcTKjDHx3AnPUfZnA9xToc-765zvn4623Rvw=="
# org = "jmeter-org"
# bucket = "parsing_bucket"
#
# # Connect to InfluxDB
# client = InfluxDBClient(url=url, token=token, org=org)
# write_api = client.write_api()
#
# # Dictionary to store requests per timestamp
# requests_by_timestamp = {}
#
# # Parse the log file
# with open("logs.txt", "r", encoding='utf8') as file:
#     for line in file:
#         match_time = re.search(r"\[(.*?)\]", line)
#         match_action = re.search(r": (.*?) -", line)
#
#         if match_time and match_action:
#             full_timestamp = match_time.group(1)  # e.g. 2025-03-29 00:03:54.939
#             action = match_action.group(1)
#
#             if full_timestamp not in requests_by_timestamp:
#                 requests_by_timestamp[full_timestamp] = {}
#
#             if action not in requests_by_timestamp[full_timestamp]:
#                 requests_by_timestamp[full_timestamp][action] = 1
#             else:
#                 requests_by_timestamp[full_timestamp][action] += 1
#
# # Write points to InfluxDB
# for timestamp, actions in requests_by_timestamp.items():
#     for action, count in actions.items():
#         point = Point("user_action") \
#             .tag("action", action) \
#             .field("count", count) \
#             .time(datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f"))
#
#         write_api.write(bucket=bucket, record=point)
#
# write_api.flush()
# time.sleep(2)
# client.close()
#
# print("✅ Data has been written to InfluxDB with full timestamps.")


# from influxdb_client import InfluxDBClient, Point
# from datetime import datetime, timezone
# import time
#
# # InfluxDB connection parameters
# url = "http://localhost:8086"
# token = "5LFw_xeyuRsNHv4OGTZD9M1MLrhxOm8LLjdk8WzgaJ_-JHGLDABcTKjDHx3AnPUfZnA9xToc-765zvn4623Rvw=="
# org = "jmeter-org"
# bucket = "parsing_bucket"  # your bucket name
#
# # Create client and write API
# client = InfluxDBClient(url=url, token=token, org=org)
# write_api = client.write_api()
#
# # Replacing utcnow() with a timezone-aware UTC datetime object
# point = Point("test_measurement") \
#     .tag("tag_name", "test_value") \
#     .field("test_field", 1) \
#     .time(datetime.now(timezone.utc))
#
# # Write test point to InfluxDB
# write_api.write(bucket=bucket, record=point)
#
# write_api.flush()
# time.sleep(2)
# client.close()
#
# print("Test data written to InfluxDB!")


from influxdb_client import InfluxDBClient, Point
from datetime import datetime, timezone
import re
import time

# InfluxDB connection parameters
url = "http://localhost:8086"
token = "5LFw_xeyuRsNHv4OGTZD9M1MLrhxOm8LLjdk8WzgaJ_-JHGLDABcTKjDHx3AnPUfZnA9xToc-765zvn4623Rvw=="
org = "jmeter-org"
bucket = "parsing_bucket"

# Connect to InfluxDB
client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api()

# Dictionary to store requests per timestamp
requests_by_timestamp = {}

# Parse the log file
with open("logs.txt", "r", encoding='utf8') as file:
    for line in file:
        match_time = re.search(r"\[(.*?)\]", line)
        match_action = re.search(r": (.*?) -", line)

        if match_time and match_action:
            full_timestamp_str = match_time.group(1)  # e.g. 2025-03-29 00:03:54.939
            action = match_action.group(1)

            # Initialize timestamp bucket if needed
            if full_timestamp_str not in requests_by_timestamp:
                requests_by_timestamp[full_timestamp_str] = {}

            # Count the action per timestamp
            if action not in requests_by_timestamp[full_timestamp_str]:
                requests_by_timestamp[full_timestamp_str][action] = 1
            else:
                requests_by_timestamp[full_timestamp_str][action] += 1

# Write points to InfluxDB
for timestamp_str, actions in requests_by_timestamp.items():
    try:
        timestamp_dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=timezone.utc)
    except ValueError:
        # If there's any formatting issue, fallback to current UTC time
        timestamp_dt = datetime.now(timezone.utc)

    for action, count in actions.items():
        point = Point("user_action") \
            .tag("action", action) \
            .field("count", count) \
            .time(timestamp_dt)

        write_api.write(bucket=bucket, record=point)

write_api.flush()
time.sleep(2)
client.close()

print("✅ Data has been written to InfluxDB with full timestamps.")
