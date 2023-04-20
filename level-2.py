Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

#Transform all names to uppercase using [normal list - list comprehension - functional programming]
names_uppercase = [name.upper() for name in Names]
#Get the names that contains ‘a’ in a list using [normal list - list comprehension - functional programming]
names_with_a = [name for name in Names if 'a' in name]
#Get the names that starts with ‘t’ in a list using [normal list - list comprehension - functional programming]
t_names = [name for name in Names if name.startswith('T')]
#Get the names that contains 2 or more ‘a’ letter using [normal list - list comprehension - functional programming]
aa_names = [name for name in Names if name.count('a') >= 2]
#Print a list contains the len of each word in the list using [normal list - list comprehension - functional programming]
lengths = [len(word) for word in Names]
#--------------------------------------------------------------
a, *b = Names
a, *_, b = Names
a, b, *_ = Names
#--------------------------------------------------------------





