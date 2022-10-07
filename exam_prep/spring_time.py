def start_spring(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if value not in result.keys():
            result[value] = []
            result[value].append(key)
        else:
            result[value].append(key)
    result = dict(sorted(result.items(), key=lambda x: (-len(x[1]), x[0])))
    for value in result.values():
        value.sort()
    nl = "\n-"
    return "\n".join(f"{key}:{nl}{nl.join(value)}" for key, value in result.items())
