#!/usr/bin/env python3
import subprocess
import json

player_status = subprocess.run(["playerctl", "status"], stdout=subprocess.PIPE)
result = {
  "text": "",
  "class": "custom__player-status",
}

if player_status.stdout == b"Paused\n":
  result["text"] = ""
elif player_status.stdout == b"Playing\n":
  result["text"] = ""
elif player_status.stdout == b"Stopped\n":
  result["text"] = ""

print(json.dumps(result))