#!/usr/bin/env python3
import subprocess, sys

player_status = subprocess.run(["playerctl", "status"], stderr=subprocess.PIPE, stdout=subprocess.PIPE)

result = sys.argv[1]

if len(player_status.stderr) != 0:
  result = ""

print(result)