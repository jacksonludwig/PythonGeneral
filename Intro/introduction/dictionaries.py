# Essentially a Hashmap where all keys must be unique (K:V format)
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Dec": "December",
    0: "June"
    # etc...
}

print(monthConversions["Dec"])
print(monthConversions["Mar"])
print(monthConversions["Jan"])
print(monthConversions["Feb"])

print(monthConversions.get("Feb"))
print(monthConversions.get("NotHere", "Not a valid key"))
print(monthConversions.get("Feb", "Not a valid key"))

print(monthConversions.get(0))

