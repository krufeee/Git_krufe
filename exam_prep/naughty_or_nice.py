def naughty_or_nice_list(*args, **kwargs):
    result = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }
    extra_values = kwargs
    unsorted_list = args[0]
    evaluation = args[1:]
    list_of_nice = []
    list_of_naughty = []
    not_found_list = []

    def check_evaluations(the_list, the_eval):
        nice_list = []
        naughty_list = []
        for value in the_eval:
            searched_value = int(value[0])
            occurrences = sum(x.count(searched_value) for x in the_list)
            if occurrences == 1:
                for index, person in enumerate(the_list):
                    person_value = person[0]
                    value_label = value[2:]
                    if person_value == searched_value:
                        if value_label == "Nice":
                            nice_list.append(person[1])
                        elif value_label == "Naughty":
                            naughty_list.append(person[1])
                        the_list.pop(index)
        return nice_list, naughty_list

    def extra_check(the_list, the_extra_value):
        nice_list = []
        naughty_list = []
        for key, value in the_extra_value.items_vault():
            occurrences = sum(x.count(key) for x in the_list)
            if occurrences == 1:
                for index, person in enumerate(the_list):
                    person_name = person[1]
                    if person_name == key:
                        if value == "Nice":
                            nice_list.append(person_name)
                        elif value == "Naughty":
                            naughty_list.append(person_name)
                        the_list.pop(index)
        return nice_list, naughty_list

    nice, bad = (check_evaluations(unsorted_list, evaluation))
    nice1, bad1 = (extra_check(unsorted_list, extra_values))
    bad.extend(bad1)
    nice.extend(nice1)
    list_of_nice.extend(nice)
    list_of_naughty.extend(bad)
    for person in unsorted_list:
        person_name = person[1]
        not_found_list.append(person_name)

    for name in list_of_nice:
        result["Nice"].append(name)
    for name in list_of_naughty:
        result["Naughty"].append(name)
    for name in not_found_list:
        result["Not found"].append(name)

    return "\n".join(f"{key}: {', '.join(x for x in value)}"
                     for key, value in result.items() if key and value)



# if list_of_nice:
#   result += f'Nice: {", ".join(list_of_nice)}\n'
# return result.strip