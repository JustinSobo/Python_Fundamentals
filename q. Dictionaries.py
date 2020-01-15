monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
      123: "December",
}

print(monthConversions["Oct"])
print(monthConversions.get("Oct"))
print(monthConversions.get("Iqy", "Not a valid key"))
