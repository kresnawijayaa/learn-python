# tipe data dictionary

# tipe data Dictionary (dict) untuk simpan data banyak dan terstruktur berbentuk key dan value

profile_1 = {
    "name": "Kresna",
    "is_male": True,
    "age": 24,
    "hobbies": ["running", "gaming"]
}

print("nama: %s" % (profile_1["name"]))
print("hobi: %s dan %s" % (profile_1["hobbies"][0], profile_1["hobbies"][1]))