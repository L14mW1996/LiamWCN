# pets = { #defining dictionary in class then value
#     "species":"Dog",
#     "breed":"Border Collie",
#     "name":"taz",
#     "colour":"black",
#     "barks?":"yes"
# }

# # print(pets["name"]) #prints value of name

# # pets["name"] = "Molly" #changing name key to have the value Molly
# # print(pets["name"])

# # for j in pets.keys(): #prints dictionary keys
# #     print(j)

# # for v in pets.values(): #prints dictionary values
# #     print(v)

# # for i in pets.items(): #prints dictionary with both keys and values
# #     print(i)

# pets.pop("colour") #removes colour key from dictionary
# print(pets)

countries = {
    "United Kingdom":"London",
    "Spain":"Madrid",
    "Italy":"Rome",
    "France":"Paris",
    "Germany":"Berlin"
}

countries.setdefault("Sweden","Stockholm")
countries.setdefault("Portugal","Lisbon")

print(countries)

