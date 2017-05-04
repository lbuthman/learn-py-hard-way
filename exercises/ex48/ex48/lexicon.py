def scan(data):
    words = data.split()
    for word in words:
        if word == "north":
            return [("direction", "north")]
