attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Gill"])
optional_invitees = ["Ben J.", "Dave"]
potential_attendees = attendees + optional_invitees
print("There are", len(potential_attendees), "potential attendess currently")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)

print("To: " + to_line)
print("Cc: " + cc_line)
