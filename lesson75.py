#Write  a program to return the country code for various countrie's. Here is the dictionary of different country codes  {'India' : '0091','Australia' : '0025','Nepal' : '00977'}  


country_code={'India' : '0091','Australia' : '0025','Nepal' : '00977'} 

print("Country code of India is :")
print(country_code.get('India','Not Found'))

print("Country code of Australia is:")
print(country_code.get('Australia','Not found'))

print("Country_code of Nepal is:")
print(country_code.get('Nepal','Not found'))

