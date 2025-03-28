from string import Template

# Usual string formatting with f-strings
str1 = "Hemant"
str2 = "Singh"
outputstr = f"You're watching {str1} by {str2}"
print(outputstr)

# Create a template with placeholders
template = Template("You're watching ${title} by ${author}")

# Use the substitute method with keyword arguments
outputstr2 = template.substitute(title="Advanced Python: Language Features", author="Joe Marini")
print(outputstr2)

# Use the substitute method with a dictionary
data = {"title": "Advanced Python: Language Features", "author": "Joe Marini"}
outputstr3 = template.substitute(data)
print(outputstr3)
