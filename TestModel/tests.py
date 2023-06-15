from django.test import TestCase

# Create your tests here.

dict_test = {
    "inclination": 45.0,
    "argOfPerigee": 45.0,
    "raan": 45.0
}

new_dict ={
    "ic":dict_test.pop("inclination")
}

print(dict_test)
print(new_dict)