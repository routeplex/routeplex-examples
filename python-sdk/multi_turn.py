"""
RoutePlex Python SDK — Multi-turn Conversation

pip install routeplex
"""

import os
from routeplex import RoutePlex, Message

client = RoutePlex(api_key=os.environ["ROUTEPLEX_API_KEY"])

# Multi-turn with message history
response = client.chat([
    Message.system("You are a helpful Python tutor. Keep answers concise."),
    Message.user("What are list comprehensions?"),
    Message.assistant("List comprehensions are a concise way to create lists: [x**2 for x in range(10)]"),
    Message.user("Can I add conditions to them?"),
])

print(response.output)
