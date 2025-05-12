#!/bin/sh
response=$(exec 3<>/dev/tcp/localhost/9000; echo -e "GET /health/ready HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n" >&3; cat <&3)
if echo "$response" | grep -q "200 OK"; then
  exit 0
else
  exit 1
fi
