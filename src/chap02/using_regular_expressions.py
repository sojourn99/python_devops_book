import re

line = '127.0.0.1 - rj [13/Nov/2019:14:34:30 -0000] "GET HTTP/1.0" 200'
m = re.search(r'(?P<IP>\d+\.\d+\.\d+\.\d+)', line)
print(m)

ip = m.group('IP')
print(ip)

m = re.search(r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})', line)
time = m.group('Time')
print(time)
