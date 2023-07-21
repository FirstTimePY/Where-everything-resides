# dictionary = a changeable, unordered, collection or unique key:value pairs
#               Fast because they use hashing, allow us to access a value quickly


capitals = {"USA":"Washington DC", 
            "United Kingdom":"London",
            "China":"Beijing",
            "Russia":"Moscow"}

#Adding Germany and its capital to the dictionary
capitals.update({"Germany":"Berlin"})
#Updating the USA's capital
capitals.update({"USA":"Las Vegas"})
#Removing "Germany" from the dictionary
capitals.pop("Germany")
#Clearing the whole dictionary
#capitals.clear()

#Prints the country "USA" and its capital (not safe)
#print(capitals["USA"])

#Prints the country "USA" and its capital (safer)
#print(capitals.get("USA"))

#Prints all the countries
#print(capitals.keys())

#Prints all the capitals of countries
#print(capitals.values())

#Prints both capitals and countries in the dictionary
#print(capitals.items())


#Listing all the countries and capitals but cooler
for key,value in capitals.items():
    print(key + ", " + value)

