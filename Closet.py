id = 0
tops = ["Helton Head", "UK", "Flowers","Red and black","grey shirt","black shirt"]
bottoms = ["jeans","jean shorts","sweatpants","yoga pants"]
shoes = ["Sneakers","Toms","Heels","Rainboots","None"]
headgear = ["None","Headbands"]
socks = ["None","cats","dogs","Hogwarts","fuzzy socks"]

pattern = "#{0}: Top={1}, Bottom={2}, Shoes={3}, Head={4}, Socks={5}"
for top in tops:
	for bottom in bottoms:
		for kicks in shoes:
			for headitem in headgear:
				for pair in socks:
					if kicks != "None" and pair == "None":
						continue

					id += 1
					print(pattern.format(id, top, bottom, kicks, headitem, pair))
