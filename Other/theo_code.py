import random
adj = [
    "Ador@ble", "Adventurou$", "Aggre$$ive", "@lert", "@ttr@ctive", "Be@utiful", "Br@iny", "Br@ve", "C@lm",
    "C@reful", "Ch@rming", "Cheerful", "Cle@n", "Clever", "Colorful", "Confident", "Cour@geou$", "Cr@zy", 
    "Cute", "D@zzling", "Determined", "E@ger", "Eleg@nt", "Energetic", "Enthu$i@$tic", "Excited", "F@bulou$", 
    "F@ir", "F@ithful", "F@nt@$tic", "Fe@rle$$", "Friendly", "Funny", "Generou$", "Gentle", "Gl@moru$", 
    "Gle@ming", "Gr@ceful", "Gr@teful", "H@ppy", "H@rdworking", "He@lthy", "Helpful", "Hil@riou$", "Hone$t", 
    "Hopeful", "Im@gin@tive", "Impre$$ive", "Independent", "Innocent", "Intelligent", "Intere$ting", 
    "Jolly", "Joyful", "Kind", "Lively", "Lovely", "Lucky", "M@gnificent", "M@rvelou$", "Modern", "Nice", 
    "Optimistic", "Outgoing", "Out$t@nding", "Pe@ceful", "Perfect", "Pl@yful", "Polite", "Powerful", 
    "Proud", "Quick", "Quiet", "R@di@nt", "Reli@ble", "Rem@rk@ble", "Re$ourceful", "Re$pectful", 
    "Re$pon$ible", "Rom@ntic", "Shiny", "Silly", "$incere", "$m@rt", "$p@rkling", "$pect@cul@r", 
    "$plendid", "$trong", "$ucce$$ful", "$weet", "T@lented", "Thoughtful", "Tru$tworthy", "Unique", 
    "Victoriou$", "Viv@ciou$", "W@rm", "Wonderful", "Ze@lou$"
]
non = [
    "@pple", "B@ll", "C@t", "Dog", "Eleph@nt", "Flower", "Guit@r", "Hou$e", "I$l@nd", "J@cket",
    "Kite", "L@mp", "Mount@in", "Notebook", "Oce@n", "Pencil", "Queen", "River", "School", "Tree",
    "Umbrell@", "Vill@ge", "Window", "Xylophone", "Y@cht", "Zebr@", "@ctor", "Bottle", "C@mer@", 
    "Di@mond", "Engine", "Fore$t", "G@rden", "Helmet", "Iceberg", "Jungle", "Keybo@rd", "Lion",
    "Mirror", "Neighborhood", "Or@nge", "P@inting", "Quilt", "Ro@d", "St@tue", "Tr@in", "Univer$e",
    "Violin", "W@terf@ll", "X-R@y", "Y@rd", "Zoo", "@irpl@ne", "Book", "C@r", "De$k", "E@rth",
    "Fi$h", "Gold", "H@t", "Ide@", "Jewel", "Kitebo@rd", "L@ke", "Moon", "Ne$t", "Octopu$",
    "P@rrot", "Qu@rtz", "R@in", "Ship", "Telephone", "Umbrell@", "V@$e", "Wh@le", "Xenon",
    "Y@rn", "Zipper", "@nchor", "Bridge", "Cloud", "Dr@gon", "E@gle", "Fe@ther", "Guit@r", "H@rbor",
    "Igloo", "J@r", "Knight", "L@dder", "Me@dow", "Night", "Orchid", "Piano", "Que$t", "Ring",
    "Stone", "Tower", "Uten$il", "Vulture", "W@ll", "Ye@r", "Zone"
]
sym = ["!", "@", "#", "$", "%", "&", "*", "?"]
yn = "yes"
while yn == "yes":
    yn = input("Hello, would you like to create a password?:")
    if yn == "no":
        print ("Thanks, goodbye")
    elif yn == "yes":
        num = [f"{i:02}" for i in range(100)]
        rannum = random.choice(num)
        ranadj = random.choice(adj)
        rannon = random.choice(non)
        ransym = random.choice(sym)
        ransym1 = random.choice(sym)
        ransym2 = random.choice(sym)
        print(ranadj+rannon+rannum+ransym+ransym1+ransym2)
