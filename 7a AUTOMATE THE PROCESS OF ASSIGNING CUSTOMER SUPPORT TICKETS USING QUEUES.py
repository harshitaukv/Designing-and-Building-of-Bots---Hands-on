from collections import deque
# Step 1: Create a queue of customer support tickets
ticket_queue = deque([
    "TKT1001",
    "TKT1002",
    "TKT1003",
    "TKT1004",
    "TKT1005"
])
# Step 2: List of available support agents
agents = ["Agent A", "Agent B", "Agent C"]
agent_index = 0
print("Customer Support Ticket Assignment")
print("----------------------------------")
# Step 3: Process the queue
while ticket_queue:
    ticket = ticket_queue.popleft()   # remove ticket from queue
    assigned_agent = agents[agent_index]
    print(f"Ticket {ticket} assigned to {assigned_agent}")
    agent_index = (agent_index + 1) % len(agents)
print("----------------------------------")
print("All tickets have been assigned.")
