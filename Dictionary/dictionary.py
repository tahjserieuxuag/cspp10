from pprint import pprint
#frpm the pprint module, import the pprint function
#dictionaries
d = {
#     key : value
    "name":"Tahj",
    "birthmonth":"April",
    "grade":16
    
}
schedule = {
    "A":"Global History",
    "B":"Global History",
    "C":"AP Chemistry/Hell",
    "D":"Algebra II"

}
x = input("period: ") 

pprint(schedule[x])