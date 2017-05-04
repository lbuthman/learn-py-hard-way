def scan(data):

    directions = ["north", "south", "east", "west"]
    verbs = ["go", "kill", "eat"]
    nouns = ["bear", "princess"]

    words = data.split(" ")
    result = []

    for word in words:
        if word.lower() in directions:
            result.append(("direction", word))
            continue
        if word.lower() in verbs:
            result.append(("verb", word))
            continue
        if word.lower() in nouns:
            result.append(("noun", word))
            continue
        try:
            result.append(("number", int(word)))
        except ValueError:
            result.append(("error", word))

    return result
