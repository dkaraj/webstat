
def __format_error_response(errors):
    list_of_errors = []
    for x in errors.keys():
        val = str(x + ": " + str(errors[x][0]))
        list_of_errors.append(val)
    return list_of_errors


