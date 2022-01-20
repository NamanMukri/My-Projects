def get_fullname(firstname, lastname):
    return "{}, {}".format(lastname, firstname)

def capitalize_names(func):
    def func_wrapper(fname, lname):
	      return func(fname, lname).upper()
    return func_wrapper

get_fullname = capitalize_names(get_fullname)
print(get_fullname("Tom" , "Holland"))

#Output: HOLLAND, TOM