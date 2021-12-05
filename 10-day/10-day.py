def format_name(f_name, l_name):
    """FORMAT NAME : first argument and second argument will create capilize letter"""
    if f_name == "" or l_name == "":
        return "Empty input"

    # firstName = f_name[0].upper() + f_name[1:].lower()
    # lastName = l_name[0].upper() + l_name[1:].lower()

    firstName = f_name.title()
    lastName = l_name.title()

    return f"Result : {firstName} {lastName}"

output = format_name("arunesh","kUMAr")
print(output)

print(format_name("sOhAn","DaS"))

print(format_name("",""))

