# product groups
'''
01-05  Animal & Animal Products
06-15  Vegetable Products
16-24  Foodstuffs
25-27  Mineral Products
28-38  Chemicals & Allied Industries
39-40  Plastics / Rubbers
41-43  Raw Hides, Skins, Leather, & Furs
44-49  Wood & Wood Products
50-63  Textiles
64-67  Footwear / Headgear
68-71  Stone / Glass
72-83  Metals
84-85  Machinery / Electrical
86-89  Transportation
90-97  Miscellaneous
'''
def def_2d(n):
    if n in range(1, 6):
        return 'Animals & animal prod'
    elif n in range(6, 16):
        return 'Vegetable products'
    elif n in range(16, 25):
        return 'Foodstuff'
    elif n in range(25, 28):
        return 'Mineral products'
    elif n in range(28, 39):
        return 'Chemicals & allied'
    elif n in range(39, 41):
        return 'Plastics & rubbers'
    elif n in range(41, 44):
        return 'Leather & hides'
    elif n in range(44, 50):
        return 'Wood & wood products'
    elif n in range(50, 64):
        return 'Textiles'
    elif n in range(64, 68):
        return 'Footwear & headgear'
    elif n in range(68, 72):
        return 'Stone & glass'
    elif n in range(72, 84):
        return 'Metals'
    elif n in range(84, 86):
        return 'Machinery & electrical'
    elif n in range(86, 90):
        return 'Transportation'
    elif n in range(90, 98):
        return 'Miscellaneous'
    else:
        return -1