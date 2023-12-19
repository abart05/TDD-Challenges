def make_Snippet(test):
    words = test.split(" ")
    if len(words) > 5:
        first_five = words[:5]
        snippet = " ".join(first_five)
        return snippet + "..."
    else:
        return test