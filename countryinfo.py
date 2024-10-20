from countryinfo import *
import countryinfo
count = input ("Enter your country: ")
country = countryinfo(count)
print("Capital is: ",country.capital())
print("Currencies is: ",country.currencies())
print("Languge is: ",country.languges())
print("Borders are: ",country.borders())
print("Others names: ",country.alt_spellings())
print("Tortal state: ",country.states())