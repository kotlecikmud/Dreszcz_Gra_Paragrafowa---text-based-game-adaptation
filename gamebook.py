import entities as ent
import functions as fun
import constants as cnst

gameboook = {
    'en':
        {
            "xxx": "",

            "eatables": "Would you like to eat provisions? (+4 Stamina) (Y/N)",

            "combat_init": "Begin the fight!",

            "combat_dead_info": "You have been killed by",

            "esc_choice": f"{cnst.def_txt_clr}Do you escape or stay and continue fighting? {cnst.special_txt_clr}/Stamina - 2/{cnst.def_txt_clr}:\
              \nescape          = <enter>\
              \ncontinue fighting = type anything",

            "combat_win_info": "You have defeated",

            "door": "door",

            "are": "are",

            "opened": "opened",

            "closed": "closed",

            "elxr_chc": "Choose elixir:\
                \n1. Dexterity\
                \n2. Endurance\
                \n3. Luck",

            "wrong_input": "Wrong input",

            "00a": f"\r{cnst.def_txt_clr}While wandering through the underground, you will find different types of weapons and items.\
                \nRemember that - except for the sword - each weapon can be used only once.\
                \nSimilarly, the found items are for single use.\
                \nYou can take one bottle of elixir with you.",

            "00b": "Hey, Brave One!\
                \n\
                \nThey say about you that icy water flows in your veins instead of blood,\
                \nand your muscles are made of the noblest steel?\
                \nIf so, look towards the setting sun.\
                \nThere, at the borders of the kingdom of Almanhagor, the uncharted Underground begins.\
                \nOnly you can unveil its Great Secret. Go forth!",

            "01": "The entrance to the underground is wide, overgrown with grass and lush bushes.\
                \nYou adjust your clothing and equipment.\
                \nLight your lantern! You enter the corridor. It is tall, and you don't have to stoop.\
                \nIt leads straight to the north. Soon, you reach a crossroads.\
                \nIt has the shape of the letter T. The branches lead west, east, and south (where you came from).",

            "02": "Kick the door. They swing open and hit the rock.\
                \nYou step inside with your sword ready to strike.\
                \nThe monster is definitely not hiding anywhere. It feels too powerful.\
                \nYes, you see it in front of you. It stands with its legs wide apart.\
                \nIt also has a sword. The tip is buried in the sand. It rests its hands on the hilt.\
                \nIt's waiting. Don't wait! If you have a helmet, put it on without fail.\
                \nIt will provide you with +3T throughout this battle.",

            "03": "Your patience - and especially your gold reserves - are running out.\
                \nOr maybe differently? The old residents of the underground say that the Dragon has its weaknesses.\
                \nEspecially weak is its left side, where it carries a bag of money and gold.\
                \nPerhaps you could try again, paying more than the fare (13 gold pieces)?",

            "04": "The DWARVES lead you to the table. They bring clean, green salad on plates.\
                \nThey place goblets. You pour the drink. Out of the corner of your eye,\
                \nyou notice that two DWARVES leave the room through the eastern door.\
                \nYou unbuckle your belt, discreetly draw out your sword, and place it in front of you on the table.\
                \nSilence ensues. The DWARVES observe you attentively.\
                \nYou look them straight in the eyes. The silence lingers.",

            "05": "Do you like fighting? Yes? That's great. Take a good look then.\
                \nFrom the left stand: SKELETON, ZOMBIE, and CANNIBAL. Is that enough?",

            "06": "You can look around the chamber. Oh, it's a true armory of earth dwarves.\
                \nShields hang on the walls, some heavy, with sharp spikes at the top and bottom,\
                \nothers decorative, covered in red-gold tiles. There are also light leather shields.\
                \nSwords gleam on a stand. The longest, thin ones are the only effective weapons against witches.\
                \nStone swords with a smooth blade and a needle-sharp tip are designed for fighting reptiles.\
                \nYou don't swing them, but rather drop them from above to pierce the bodies of those monsters.\
                \nRight by the ground, you see a row of tiny swords of goblins, earth dwarves.\
                \nIf only you knew what they can do with them!\
                \nOn the eastern wall, there are wooden shelves filled with a whole collection of helmets.\
                \nThere are helmets for tournament duels, lined with yellow grass, and heavy helmets with a raised visor.\
                \nOn the top shelf, there are three - probably - pots. No, those are helmets\
                \nfor fighting in rooms or corridors filled with corrosive gas.\
                \nYou flick some leather scraps with the tip of your sword.\
                \nIt's a cap that cruel monsters put on the heads of their tortured victims.\
                \nYou look around further. There are, or lie, plenty of weapons along the walls.\
                \nYou don't even know who they belong to or what they're used for. You see a heavy hammer on a wooden handle,\
                \nprobably acquired from goblins at some point, and a bone-hilted dagger in a leather sheath.\
                \nYou can take two things.",

            "07": "'Do you have something in stock that I could offer as a gift?' - you ask.\
                \n'How could I not have? I'm always prepared for such whims.\
                \nI have a lovely wooden stake and a jar of corrosive dust. Shall I pack them with a ribbon?'.",

            "08": "You peek into the chamber. The doors open slightly. What do you see?\
                \nSome kind of odd creature runs frantically from wall to wall. It doesn't look threatening.\
                \nAround its waist, sticking out of pockets, it has bones of various lengths and species.\
                \nYou enter. 'Why are you running like that, poor thing?' you ask.\
                \n-'Oh, sir, what have I done? Such a fuss over these few dice! My brothers, the goblins, caught some giant moles.'\
                \nAs you probably know, giant moles are goblins' favorite delicacy. I couldn't resist.\
                \nI sneaked up and snatched a few dice. I sat down here to eat them,\
                \nand those beasts tracked me down and will soon arrive. Oh, here they come.'\
                \nThe goblin starts going crazy again. You grab him by the arm and stand in the middle of the chamber.\
                \nIn a moment, a horde of goblins appears at the door.",

            "09": "You prepare to strike the DWARF with a wooden pole. He notices it.\
                \n'Oh, what a beautiful pole,' he says, 'Sell it to me for 20 gold pieces.'",

            "10": "DWARVES invite you to sit at the table. They smile.\
                \n'Finally, a cultured creature,' they say. 'Everyone just comes in here, snatches heads\
                \nof lettuce, and runs off. But we don't blame them. At least someone will make use of\
                \nour little vegetable, hehe.' You ponder for a moment about that 'hehe,' and already\
                \nthe DWARVES start spinning tales. Few of them have ventured\
                \ninto the deeper regions of the underground. Those who returned say\
                \nthat the scariest thing one can encounter is fire. A fat Dragon also wanders around\
                \nin the labyrinth. Apparently, it is very dangerous, although some say\
                \nit can be bribed.\
                \n\
                \nYou listen to these stories, but something still troubles you.\
                \n /// If you followed the path through the center of the chamber /../../../",

            "11": "The passage stands wide open. There are no doors to this chamber.\
                \nSo you enter boldly.\
                \n'Hello' - one word and you freeze.\
                \n'Hello, Brave One, hehe' - in the corner of the chamber sits a small, wrinkled creature.\
                \n'Are you thirsty? Take some water. Good, cool water. Finger-licking good'.\
                \nIn the middle of the chamber stands a stone fountain. Water surrounds the figure of some extraordinary being.\
                \nA small stream of water flows from its snout. '...There are real treasures. Do you want to taste the water?\
                \nIt's good, cool water.' You stand frozen. That little funny creature killed your wits.\
                \nYou've completely lost your composure. Well, make up your mind:",

            "12": "You extract the enchanted emerald. Pain tears through your back, your leather jacket cracks.\
                \nWide, bluish-gray wings sprout from your back. You ascend. You land on a dreamlike edge of a precipice.\
                \nThe spell is broken.",

            "13": "You don't have to look around. I'll tell you everything right away. In this chamber, a WEREWOLF lurks.\
                \nIt knows you're here. You take a few steps into the darkness and notice a glowing point beyond a rocky gap.\
                \nStealthily, you reach for your sword. You take further steps. Now there are two points. Clatter.\
                \nIt jumps out from behind the rock. In the streak of light, which falls through the partially open door to the cave,\
                \nyou only see white fangs and green eyes. Swiftly, you grip your sword with both hands.\
                \nYou swing... and freeze in place. The green eyes paralyze your body.",

            "14": "You can exit through the northern door - see 197, or the eastern door - see 39.",

            "15": "If you give up swimming across the lake - see 241. However, if you decide to attempt swimming across the lake,\
                \nmake a note of this paragraph number and see 113.",

            "16a": "You step out into the corridor. After a while, it turns south.\
                \nAt the same spot, you can sit down and eat your Provisions.",

            "16b": "You continue onwards. You walk south until the tunnel turns west again.\
                \nTwenty steps ahead, you see the entrance to a chamber.",

            "17": "If you want to see what's behind them - see 265, if you prefer to retreat - see 50.",

            "18": "You enter a small cave attached to the room. Behind you, three EVIL creatures.\
                \nThe old man stayed in the room. Through the rocky breach, you see a gremlin chained to the rock.\
                \nThe poor thing is barely breathing. The EVIL one takes you by the arm and leads you\
                \nten steps away from the gremlin. He hands you six arrows. The EVIL one also\
                \nhas six. He points his finger towards the chained gremlin. You should aim at him!\
                \nDo you want to play?",

            "19": "The DWARVES bid you farewell warmly and give you two lettuce heads\
                \nfor your journey. They escort you to the eastern door.",

            "20": "After a long march, you arrive at a large cave.\
                \nNo, it's more like an endless plain. Probably the famous Mad Fields.\
                \nYou hear some noise. You run west with all your might.\
                \nHowever, the monsters catch up with you.",

            "21": "If you want to see what's behind the doors - see 332, if not - turn back and see 212.",

            "22": "This might be the end of your journey. You've never seen such a lovely chamber before.\
                \nIt's bright everywhere, and a greenish mist floats in the air. The floor is even smoother than over the abyss.\
                \nThere's a little person sitting on the floor. Ah, it's a real DWARF playing with a toy dragon,\
                \nwound up with moving legs and a red tongue that sticks out every now and then.\
                \nIf you have a tin butterfly, you can rest and play with the DWARF - see 321.\
                \nIf you have an emerald, you can show it to the DWARF - see 187. But only if\
                \nyou have a wooden stick, you can try to scare or even attack the DWARF - see 9.\
                \nIf you have more than one of the mentioned items, you must choose only one possibility.",

            "23": "The door to the treasure chamber stands before you... open? Oh no! It's closed.\
                \nYou see two locks. If you have at least two numbered keys,\
                \nyou can open the door with them - see 185. If you don't have at least two keys,\
                \nyour Adventure ends here. You were so close!",

            "24": "Roll the die once. If you roll 1, 2, 3 - your weapon\
                \nproves to be effective in fighting the BUGS - see 58.\
                \nIf you roll 4, 5, 6, it's of no use - see 168.",

            "25": "An old man is sitting on a rock. He advises you to go west,\
                \nand then turn right at the next few intersections.",

            "26": "For each accurate hit on the fatso, you receive 5 gold pieces. See 171.",

            "27": "The corridor leads straight north. Along the way, you can eat Provisions.\
                \nIt starts to widen, expand until you reach an endless plain. It's the Mad Fields.\
                \nIt's better not to venture there. But... do you hear that rumbling? It must be the monsters.\
                \nSee 238. If you defeat them or retreat during the battle - see 316.\
                \nRemember this number, as you might lose your way.",

            "28": "Lift the large stone lying against the wall.",

            "29": f"You stumble upon a pebble. The sword clangs against the rock. {ent.entity_116.name} raises its head.\
                \nIt has spotted you. It rushes into a fight.",

            "30": "SSS. If you have an S - see 159. If you don't have an S - see 342.",

            "31": "Shine the lantern down. Sweep away the remains with your sword. And look - you've found 5 gold pieces!",

            "32": f"Exhausted, you sit down under a rock. You can eat something from the Provisions.\
                \nHardly finishing your meal, WEREWOLF enters the cave, significantly weaker\
                \nthan the WOLFLORD, but there are three of them. Treat them as a single creature and fight.\
                \n{ent.entity_032.name}\
                \nIf you emerge victorious - see 275.",

            "33": "Just a little more and you will be at the intersection.\
                \nYou're heading: north - see 293, east - see 188, south - see 247",

            "34": "You reveal your discovery: a door in the northern wall. It doesn't impress them.\
                \nYou say you want to see what's behind it. They don't protest.. You get up from the table and along the wall\
                \nyou reach the secret door. One of the DWARVES turns the hidden knob in the ground.\
                \nThe door opens. You enter - see 128",

            "35": "You pay according to the tariff (10 gold pieces). He bends over the chasm. He offers you his tail.\
                \nYou enter. It will probably transport you to the other side of the gorge soon. But... The dragon has its moods. They often change.\
                \nRight now, you grab its tail while hanging over the red abyss. SSS. If you have an S, you cross to the other side - see 186.\
                \nIf you don't have an S, the dragon throws you back onto the rocky ledge - see 158",

            "36": "SSS. If you have an S - see 152. If you don't have an S - see 176",

            "37":
                "Which shield do you choose: metal, ornate, or leather? Write your choice on the inventory list - see 324.",

            "38": "The corridor leads north at first, then gently curves east.\
                \nIt widens a bit and ends with stairs going down. You stand in front of the doors adorned with exquisite decorations.\
                \nHave you been beyond these doors before? If yes - see 167, if no - see 328.",

            "39": "You reach the intersection. Its branches lead to:",

            "40":
                "Will you rely only on the cards? - see 334, or will you use your LUCK? - see 62",

            "41": "You managed to take only a few steps when the corridor is completely blocked by a mass of stones and sand.\
                \nTry stomping your foot. Old gremlins say it's a way to deal with such blockages. SSS. If you have an S - the top of the rocks\
                \nfalls into the abyss, and you can continue - see 348. If you don't have an S - you have to go back - see 221.",

            "42": "They call him the BARBARIAN. Is it right? Who knows? When he sits on a bench with his legs stretched out and arms folded\
                \nacross his chest, he doesn't look threatening. He snores quietly. You hit the wall with your sword. What's the matter? He wakes up.\
                \nNow you enter the chamber and point to the door on the opposite, western side. Open those doors quickly - you show him with the tip of your sword.\
                \nOpen them yourself - he chuckles - The key is in the lock: Indeed. You approach the door, fearing an ambush,\
                \nyou don't touch the key with your hand, but you insert the tip of your sword into the keyhole and try to turn it. Nothing happens.\
                \nNothing at all... - the BARBARIAN growls - Do you know the spell? If you don't know, it's better to leave!\
                \nWell, do you remember the spell from the old gremlin book? Wait, maybe you didn't even see that book.\
                \nEither way, if you don't know the spell, it's the end for you, buddy. Try again, from the very beginning.\
                \nIf you think you remember the spell, repeat it. Now turn to paragraph 122. If you remembered correctly - see 376.\
                \nIf you made even the slightest mistake, your adventure ends. Continuing it in such a situation is not worthy of a true Adventurer.",

            "43": "You have to go back the way you came until you reach the other end of the chasm. Along the way, you don't fight anyone,\
                \nyou don't buy anything, you don't take anything. You have to try a different way. The options are listed in paragraph 186.",

            "44": "You go east. You see solid doors ahead.\
                \nYou try to open them. They don't give way...",

            "45": "You head towards the fountain. You collect water. It's enchanted.\
                \nYou put the container in your backpack. You notice that the fountain is already empty.",

            "46":
                "You look for a way out of the northern edge of the cave. You see a small opening. You move towards it and squeeze through with difficulty. See 53",

            "47": "You have only taken a few steps and the corridor turns right, and shortly after, it ends. You can sit down and calmly eat your Provisions.\
                \nThen return to the intersection and go north - see 191",

            "48": "You open your backpack and reach for the vial to transfer the treasure. At that moment, the gold scatters in all directions,\
                \nand the vials transform into two powerful, winged DEMONS, which rise and sit on the sunny ledge. You can attack them - see 169,\
                \nor start collecting the scattered gold - see 33.",

            "49": "You can take this book with you (write it on the inventory list) or leave it. See 286.",

            "50": "You approach the intersection.\
                \nYou can go:",

            "51":
                "You can exit through the south door - see 134, or through the north door - see 33. Leave both doors open.",

            "52": "A stream of biting gas shoots out of the hole in the wall. If you have a pot helmet, nothing happens to you.\
                \nAlthough the helmet gets destroyed. If you don't have such a helmet - see 315 first, and then 274 (record this number).",

            "53": "You land in a spacious corridor. It leads north, and after a while, it sharply turns east.\
                \nYou take several steps and stand in front of heavy doors. - Have you been here before? If yes - see 322, if no - see 299",

            "54": "You throw the dagger. You hit the target accurately. The GUARD loses 2 W, but still stands like a pillar. See 107.",

            "55": "You give the gold, take the shovel, the jar, or both - see 196.",

            "56": "You try to force the doors open again. Once again, without success.",

            "57": "After landing, the rascal demands all your gold. You can say that you will give only what he asked for - see 335,\
                \nor that - in that case - you won't give anything - see 91",

            "58": "You use your secret weapon. You completely paralyze the WORMS. If you want to dive into their bodies and\
                \nsearch the pool again - see 142, if not - see 320.",

            "59": "You enter, but you don't find anything here. Do you know any other way out of this room than the one you just entered through?",

            "60": "The DWARF offers 20 pieces of gold. Do you accept? Yes - see 262, no - see 338.",

            "61": "You walk along the corridor. Along the way, you can eat Provisions. After some time, there is a fork to the north, but you stubbornly continue west. A few steps past that fork, you see a door. You open it - see 42.",

            "62": "SSS. If you have S - see 201. If you don't have S - see 145.",

            "63": "The sword is not an effective weapon against WEREWOLVES. If you have any of the following items, you can use them in combat:\
                \nbone from the skeleton of an ancient monster - see 157,\
                \ngoblins' hammer - see 346,\
                \nmetaphorical shield - see 216,\
                \nnet - see 377,\
                \nbunch of keys - see 181.\
                \nIf you don't have any of these items, your only option is to Escape - see 275.",

            "64": "You approach the intersection. You can go in any of the four directions. Choose a direction:",

            "65": "Are you done with this place? If yes - see 195, if no - see 283.",

            "66": "You roll two dice. It shows you how many pieces of gold you win. Do you want to continue playing? - see 229. Don't want to? - see 19.",

            "67": "You have to retreat - see 50.",

            "68": "You leave the armory. The only door leads north. You follow the corridor until the next intersection. Along the way, you can sit down and eat Provisions. See 212.",

            "69a": "You asked for it. Two gruesome specters sit against the wall of the room.\
                \nSuch a meeting can only end in a fight, first with one, and then with the other monster.",

            "69b": "You've barely defeated the first specter and you're already going after the second one.",

            "69c": "You can search the room.",

            "70": "",

            "71": "",

            "72": "",

            "73": "",

            "74": "",

            "75": "You retreat. You return towards the intersection. You pass an old man.",

            "76": "",

            "77": "",

            "78": "",

            "79": "",

            "80": "",

            "81": "",

            "82": "",

            "83": "",

            "84": "",

            "85": "",

            "86": "",

            "87": "",

            "88": "",

            "89a": "Using the tip of your sword, you pry open the lid of the box. Inside, there are 3 pieces of gold.\
            \nYou can take them.",

            "89b": "You look around the corners. Suddenly, you hear some noise.\
            \nYou quickly gather your belongings and rush out, leaving the door open.",

            "90": "",

            "91": "",

            "92": "",

            "93": "",

            "94": "",

            "95": "",

            "96": "",

            "97": "",

            "98": "",

            "99": "",

            "100": "",

            "101": "",

            "102": "You reach the intersection. The corridors diverge in all directions.\
            \nChoose a direction:",

            "103": "You turn back. You pass the intersection. You go west. After some time, you see\
            \nanother intersection ahead of you.",

            "104": "You give the butterfly, take the gold and the pacifier.",

            "105": "You try to force the door. You gather momentum and hit it with all your strength.\
            \nThe door doesn't budge.",

            "106": "Just behind the door, you see wooden, chipped stairs leading downwards.\
            \nIn the central part of the cave, there is a square recess, like a pool,\
            \nbut empty. The stairs lead precisely to the bottom of the pool. The floor is covered in fine sand.\
            \nSand everywhere, no equipment, stones, or creatures... Hey,\
            \nwhat's that bent stick sticking out in the corner of the pool? Probably a root. You can't resist\
            \nthe temptation: you give it a solid kick. What happens next\
            \nexceeds imagination. If you survive and tell someone about your\
            \nadventure, they will surely not believe you. The pool now resembles a pot\
            \nwhere someone is stirring thick noodles. You are a small speck tossed in all directions.\
            \nThose are the WORMS, the most disgusting creatures of the underground world. They want to grind you\
            \nto dust. They wriggle their slippery bodies. They throw you to the surface,\
            \nthen push you to the bottom again. You can defend yourself with a sword. You can also\
            \nuse another weapon, namely... Well, that's the question: some say that an acidic liquid is an effective weapon\
            \nagainst WORMS, others say it's omnivorous (eternally hungry crustaceans).",

            "107": "",

            "108": "",

            "109": "",

            "110": "",

            "111": "",

            "112": "",

            "113": "",

            "114": "",

            "115": "Choose items:",

            "116a": f"You deviate into a corner of the cave. Stones crackle under your feet.\
            \n{ent.entity_116.name} looks at you attentively and growls. You must fight.",

            "116b": "\nYou can search the room.",

            "117": "",

            "118": "",

            "119":
                f"What was this beast blocking so much? You touch the wall where the hairy {ent.entity_317.name} leaned.\
            \nSuddenly, a part of the wall moves. It's a hiding place! Inside, there's a long, fire-resistant rope with a hook, an empty, moldy flask, and a WEREWOLF scalp.\
            \nYou can take up to two of these items.",

            "120": "You go west. The corridor gently turns right and now leads north.\
            \nYou see an intersection ahead of you.",

            "121": "",

            "122": "",

            "123": "The corridor runs west and turns south.\
            \nYou see an intersection ahead of you.",

            "124": "",

            "125": "",

            "126": "",

            "127": "",

            "128": "",

            "129": "",

            "130": "The corridor is now almost five steps wide.\
            \nYou walk comfortably. You straighten your bones.\
            \nYou've only walked a hundred steps, and here's another intersection.",

            "131": "",

            "132": "Did you go for water?",

            "133": "",

            "134": "",

            "135": "",

            "136": "The dragon politely invites you to its tail, which is swinging a bit\
            \nover the abyss, but soon you land on the other side.",

            "137": "",

            "138": "",

            "139": "",

            "140": "",

            "141": "",

            "142": "",

            "143": "",

            "144": "",

            "145": "",

            "146": "The corridor runs south and turns east.\
            \nYou see an intersection ahead of you.",

            "147": "",

            "148": "",

            "149": "",

            "150": "",

            "151": "",

            "152": "",

            "153": "A rat is a good sign. Your sword is enchanted. In every fight you engage in from now on,\
            \nyou can add 1 to your attack strength.",

            "154": "",

            "155": "",

            "156": "",

            "157": "",

            "158": "Had enough?",

            "159": "",

            "160": "You cautiously take steps. Your legs brush against the leaves of a large lettuce.\
            \nAs you pass through the center of the room, you notice a stream of light falling from above.\
            \nYou don't reveal your discovery. You reach the table.",

            "161": "",

            "162": "",

            "163": "",

            "164": "",

            "165": "",

            "166": "",

            "167": "",

            "168": "",

            "169": "",

            "170": "You reach an intersection. It has the shape of the letter T.\
            \nYou can go:",

            "171": "",

            "172": "",

            "173": "",

            "174": "",

            "175": "",

            "176": "You approach an intersection.\
            \nYou can go:",

            "177": "Under the stone, there was a fiery ball. You can take it.\
            \nYou exit.",

            "178": "It's increasingly difficult to pull your feet out of the muddy muck. The air becomes\
            \nmore and more humid. The corridor gradually widens until you finally reach the edge\
            \nof an underground lake. The shores are overgrown with vegetation with thick, wide\
            \nleaves. The ceiling is high above. In a few places, thin streams of light seep through.\
            \nYou look around carefully. Is this a dead end?\
            \nYou don't see any other exit than the one you came from.",

            "179": "",

            "180": f"You search the room again. In the {ent.entity_116.name} bag, which you didn't have time to look through, you find a key. The number 45 is engraved on it. You can take it with you.",

            "181": "You throw a bunch of keys at the monster that you found in one of the visited chambers. The throw is accurate but harmless. The WEREWOLF catches the bunch and escapes. You start chasing after it. The WEREWOLF falls into a narrow but deep crevice in the corner of the cave. It falls to the bottom and dies. You shine your lantern. You see the massive body of the monster in the depths, and next to it, the keys gleam.",

            "182": "Do you want to search for any secret passages?",

            "183": "",

            "184": "You wipe your bloody sword on the skins lying beneath your feet. You sharpen it",

            "185": "You enter a narrow corridor. It leads to a large room.",

            "186": "You managed to reach the other side. You have three exits: one leads west (A), and two lead north, one of which is located more to the west (B) than the other (C). Which one do you choose?",

            "187": "",

            "188": "",

            "189": "",

            "190": "You can choose any sword.",

            "191": "",

            "192": "'Maybe it's time to squeeze something out of this clown?' you think. You reach for your sword. Oh, why a sword? Just a punch will do.\
            \nYou approach the creature and prepare to strike. The creature disappears. Moreover, with a bang, the grate in the passage through which you entered this room falls.\
            \nYou look around. You don't see any other exit. You approach the fountain. Indeed, at the bottom, you see various mysterious objects: a monster's bone,\
            \na jar with omnivores (perpetually hungry crustaceans), a tin butterfly, a spear, and a shiny key. So, do you want water or one of these things?\
            \nRemember, you can only take one thing.",

            "193": "",

            "194": "",

            "195": "",

            "196": "",

            "197": "",

            "198": "",

            "199": "",

            "200": "After some time, you spot a door in the southern wall.",

            "201": "",

            "202": "",

            "203": "",

            "204": "",

            "205": "",

            "206": "",

            "207": "",

            "208": "",

            "209": "",

            "210": "",

            "211": "",

            "212": "You reach a spacious square, and the paths diverge in four directions. Which one do you choose?",

            "213": "",

            "214": "",

            "215": "",

            "216": "",

            "217": "",

            "218": "",

            "219": "",

            "220": "If you chose the monster's bone, the jar with omnivores, the tin butterfly, or the spear - see 109. If the key, see 366.",

            "221": "You reach a crossroad where you can go: north - see 339, east - see 41, south - see 173.",

            "222": "",

            "223": "",

            "224": "After a few steps, the corridor turns east. You continue walking. In the southern wall of the corridor, you see a door.",

            "225": "",

            "226": "The battle continues. After the second round, you can Escape again. Are you sure you want to continue fighting?",

            "227": "",

            "228": "The corridor runs north and turns east. Ahead, you see a crossroad.",

            "229": "",

            "230": "",

            "231": "",

            "232": "",

            "233": "",

            "234": "You finish the fight with the DEMON. Do you want to look inside the stone box on the altar?",

            "301": "You can try to open the door",

            "349": "Gently, you slide your foot into a narrow gap. With your hips, you push the door open.\
                \nThey swing aside. This is the method! You catch a faint scent of dried herbs.\
                \nOn the left wall, there are two smooth columns.\
                \nBetween them, at eye level, there is a granite shelf stretched out.\
                \nTwo lamps are standing there, with a stone box in the middle.\
                \n\
                \nThe floor is covered with hairy animal and monster skins.\
                \nThis must be an underground chapel! Against the wall, opposite the altar, you see a low table carved into the rock.\
                \nThere's something on it. You raise the lantern higher. Oh, King Almanhagor, they are two vases full of gold.\
                \nEach has the same exquisite shape. On one side, it's adorned with the head of a creature,\
                \non the other side, two shimmering wings are attached. Do you want to take the gold?",

            "364": f"You push the door, it gives way. A dark abyss opens up.\
                \nYou enter, illuminating the path with a lantern. You feel pebbles beneath your feet.\
                \nFrom the opposite end of the room, you hear a faint snoring.\
                \n{ent.entity_116.name} is sleeping on the floor. There is a box lying next to him."

        },
    'pl':
        {
            "xxx": "",

            "eatables": "Czy chcesz zjeść prowiant? (+4 Wytrzymałość) (Y/N)",

            "combat_init": "Rozpocznij walkę!",

            "combat_dead_info": "Zostałeś zabity przez",

            "esc_choice": f"{cnst.def_txt_clr}Uciekasz czy zostajesz i walczczysz dalej? {cnst.special_txt_clr}/Wytrzymałość - 2/{cnst.def_txt_clr}:\
              \nuciekasz        = <enter>\
              \nwalczysz dalej  = wpisz cokolwiek",

            "combat_win_info": "Pokonałeś",

            "door": "drzwi",

            "are": "są",

            "opened": "otwarte",

            "closed": "zamknięte",

            "elxr_chc": "Wybierz eliksir:\
                \n1. Zręczności\
                \n2. Wytrzymałości\
                \n3. Szczęścia",

            "wrong_input": "Niepoprawny wybór",

            "00a": f"\r{cnst.def_txt_clr}Wędrując po podziemiach będziesz znajdował inne rodzaje broni i przedmioty.\
                \nPamiętaj, że - poza mieczem - każda broń może być wykorzystana tylko raz.\
                \nPodobnie, znajdowane przedmioty są jednorazowego użytku.\
                \nMożesz zabrać ze sobą jedną butelkę eliksiru.",

            "00b": "Hej, Śmiałku!\
                \n\
                \nTo o Tobie mówią, że w Twoich żyłach zamiast krwi płynie lodowata woda,\
                \na twoje mięśnie są z najszlachetniejszej stali?\
                \nJeśli tak, spójrz w stronę zachodzącego słońca.\
                \nTam, na rubieżach królestwa Almanhagor, rozpoczynają się niezbadane Podziemia.\
                \nTylko Ty możesz wydrzeć ich Wielką Tajemnicę. Ruszaj!",

            "01": 'Wejście do podziemi jest szerokie, obrośnięte trawą i bujnymi krzewami.\
                \nPoprawiasz ubranie i ekwipunek.\
                \nZapal latarnię! Wchodzisz do korytarza. Jest wysoki, nie musisz się schylać.\
                \nProwadzi prosto na północ. Wkrótce dochodzisz do skrzyżowania.\
                \nMa ono kształt litery T. Odnogi prowadzą na zachód, wschód i południe (skąd przyszedłeś).',

            "02": "Kopnij drzwi. Otwierają się i uderzają o skałę.\
                \nWchodzisz do środka z mieczem gotowym do zadania ciosu.\
                \nNa pewno potwór nigdzie się nie ukrywa. Czuje się zbyt potężny.\
                \nTak, widzisz go przed sobą. Stoi na szeroko rozstawionych nogach.\
                \nOn też ma miecz. Czub wbił się w piasek. Opiera dłonie na rękojeści.\
                \nCzeka. Ty nie czekaj! Jeśli masz hełm, załóż go koniecznie, zapewni ci +3W na czas trwania tej walki.",

            "03": "Twoja cierpliwość - a szczególnie zapasy złota - są na wyczerpaniu.\
                \nA może inaczej? Starzy mieszkańcy podziemi mówią, że Smok ma swoje słabe strony.\
                \nSzczególnie słaba jest jego lewa strona, gdzie nosi wór na pieniądze i złoto.\
                \nMoże by tak spróbować jeszcze raz, płacąc ponad taryfę (13 sztuk złota)?",

            "04": "KRASNOLUDY prowadzą cię do stołu. Przynoszą na półmiskach czystą, zieloną sałatę.\
                \nStawiają pucharki. Rozlewasz napój. Kątem oka spostrzegasz,\
                \nże dwa KRASNOLUDY wychodzą z pokoju wschodnimi drzwiami.\
                \nRozpinasz rzemień, ukradkiem wyciągasz miecz i kładziesz go przed sobą na stole.\
                \nZapada cisza. KRASNOLUDY bacznie cię obserwują.\
                \nTy patrzysz im prosto w oczy. Milczenie przeciąga się",

            "05": "Lubisz walkę? Tak? To wspaniale. Przyjrzyj się więc dokładnie.\
                \nOd lewej stoją: SZKIELET, ZOMBI i LUDOJAD. Wystarczy?",

            "06": "Możesz rozejrzeć się po komnacie. Ech, toż to prawdziwa zbrojownia krasnali ziemnych.\
                \nNa ścianach wiszą tarcze, niektóre ciężkie, u góry i u dołu zakończone ostrymi szpicami,\
                \ninne ozdobne, obite czerwono-złotymi płytkami: są też lekkie tarcze skórzane.\
                \nNa stojaku błyszczą miecze. Te najdłuższe, cienkie, to jedyna skuteczna broń przeciw wiedźmom.\
                \nMiecze kamienne o gładkim brzeszczocie i ostrym jak igła czubie przeznaczone są do walki z płazurami.\
                \nNie wykonuje się nimi zamachów, lecz spuszcza z góry, by przeszywały cielska tych potworów.\
                \nPrzy samej ziemi widzisz poustawiane w rzędzie malutkie mieczyki gremlinów, krasnali ziemnych.\
                \nGdybyś widział jaki potrafią robić z nich użytek!\
                \nNa wschodniej ścianie wiszą drewniane półki zastawione całą kolekcją hełmów.\
                \nSą hełmy do pojedynków turniejowych, wyściełane żółtą trawą, są ciężkie hełmy z podnoszoną przyłbicą.\
                \nNa najwyższej półce stoją trzy - chyba - garnki. Nie, to są hełmy\
                \ndo walki w pomieszczeniach albo korytarzach wypełnionych żrącym gazem.\
                \nCzubkiem miecza podrzucasz jakieś skórzane płaty.\
                \nTo czapa, którą okrutne potwory zakładają na łeb torturowanym przez siebie istotom.\
                \nRozglądasz się dalej. Pod ścianami stoi, albo leży mnóstwo broni.\
                \nNawet nie wiesz komu i do czego służy. Widzisz ciężki młot na drewnianym stylisku,\
                \nzapewne zdobyty kiedyś na goblinach, a także kościany kordelas w skórzanym futerale.\
                \nMożesz zabrać dwie rzeczy.",

            "07": "'Może ma Pan na składzie coś, co mógłbym ofiarować w prezencie?' - mówisz.\
                \n'Jak mógłbym nie mieć? Jestem zawsze przygotowany na takie zachcianki.\
                \nMam uroczy drewniany pal i słój żrącego pyłu. Zapakować ze wstążeczką?'.",

            "08": "Zaglądasz do komnaty. Drzwi lekko się uchylają. Co widzisz?\
                \nJakiś dziwnystwór biega jak oszalały od ściany do ściany. Nie wygląda groźnie.\
                \nZa pas, wkieszenie, do cholew powtykane ma rozmaitej długości i różnego gatunku kości.\
                \nWchodzisz do środka. 'Czemu tak biegasz, biedaku?' - pytasz.\
                \n-'O, panie, co jaim zrobiłem? Taki raban o tych parę kostek! Moi bracia, gobliny upolowali kilkakocmołuchów.'\
                \nJak pewnie wiesz, kocmołuchy to największy przysmak goblinów. Niemogłem sobie odmówić.\
                \nPodkradłem się i gwizdnąłem kilka kostek. Siadłem tu, byje sobie zjeść,\
                \na te bestie wyśledziły mnie i zaraz tu wpadną. O, już biegną.'\
                \nIgoblin znów zaczyna szaleć. Bierzesz go za ramię i stajesz na środku komnaty.\
                \nZa chwilę w drzwiach pojawia się stado goblinów.",

            "09": "Przygotowujesz się, by walnąć KRASNALA drewnianym palem. On spostrzega to.\
                \n'Och, co za piękny pal' - mówi - 'Sprzedaj mi go za 20 sztuk złota.",

            "10": "KRASNOLUDY zapraszają cię, byś usiadł przy stole. Uśmiechają się.\
                \n'Nareszcie jakiś kulturalny potwór' - mówią. 'Wszyscy tylko wpadają tu, wyrywają główki\
                \nsałaty i zwiewają. Ale nie mamy im tego za złe. Przynajmniej komuś przyda się\
                \nnasze warzywko, he, he'. Zamyśliłeś się chwilę nad tym 'he, he', a tu już\
                \nKRASNOLUDY zaczynają snuć opowieści. Niewielu z nich zapuszczało się\
                \nkiedykolwiek w dalsze rejony podziemi. Ci, którzy wrócili, mówią,\
                \nże najstraszniejszą rzeczą którą można spotkać jest ogień. Błąka się też po\
                \nlabiryncie tłusty Smok. Podobno jest bardzo groźny, choć niektórzy powiadają,\
                \nże jest przekupny.\
                \n\
                \nSłuchasz tych opowieści, ale ciągle coś nie daje ci spokoju.\
                \n   ///   Jeśli szedłeś ścieżką przez środek komnaty /../../../",

            "11": "Przejście stoi otworem. Do tej komnaty nie ma żadnych drzwi.\
                \nWchodzisz więc śmiało.\
                \n'Cześć' - jedno słowo a ty nieruchomiejesz.\
                \n'Cześć, Śmiałku, he, he' - w rogu komnaty siedzi mały, pomarszczony stwór.\
                \n'Pić ci się chce? Weź sobie wody. Dobra, chłodna woda. Palce lizać i obgryzać'.\
                \nNa środku komnaty stoi kamienna fontanna. Woda otacza figurkę jakiejś niezwykłej istoty.\
                \nZ pyszczka wycieka jej mały strumyk wody. '...Są prawdziwe skarby. Chcesz skosztować wody?\
                \nTo dobra chłodna woda'. Stoisz jak wryty. Ten mały śmieszny stwór zabił ci ćwieka.\
                \nCałkiem straciłeś rezon. No, decyduj się:",

            "12": "Wyjmujesz zaczarowany szmaragd. Ból rozrywa ci plecy, pęka skórzana kurtka.\
                \nZ pleców wyrastają ci szerokie, sinoszare skrzydła. Unosisz się. Lądujesz na\
                \nwymarzonym brzegu przepaści. Czar pryska.",

            "13": "Nie musisz się rozglądać. Od razu powiem ci wszystko. W tej komnacie czai się\
                \nWILKOŁAK. Wie, że tu jesteś. Robisz kilka kroków w mrok Za wyłomem skalnym\
                \ndostrzegasz świecący punkt. Ukradkiem sięgasz po miecz. Robisz kolejne kroki.\
                \nTeraz już są dwa punkty. Łoskot. Zza skały wyskakuje on. W smudze światła,\
                \nktóra pada przez uchylone drzwi do pieczary, widzisz tylko białe kły i zielone oczy.\
                \nBłyskawicznie chwytasz oburącz swój miecz. Robisz zamach...\
                \ni zastygasz nieruchomo. Zielone ślepia paraliżują twe ciało",

            "14": "Możesz wyjść północnymi drzwiami - patrz 197, albo wschodnimi - patrz 39.",

            "15":
                "Jeśli rezygnuiesz z przepłynięcia jeziora - patrz 241, Natomiast jeżeli decydujesz się podjqć próbę przepłynięcia jeziora, zapisz numer niniejszego paragrafu i patrz 113.",

            "16a": "Wychodzisz na korytarz. Po pewnym czasie skręca on na południe. W tym samym\
                \nmiejscu możesz usiąść i zjeść Prowiant.",

            "16b": "Ruszasz dalej. Idziesz na południe do czasu, gdy tunel skręca na znowu zachód.\
                \nW odległości dwudziestu kroków widzisz przed sobą wejście do komnaty.",

            "17": "Jeśli chcesz zobaczyć co za nimi iest - patrz 265, jeśli wolisz się wycofać - patrz 50.",

            "18": "Wchodzisz do małej pieczary, przylegającej do komnaty. Za tobą trzy ZŁE.\
                \nStaruszek został w pokoju. Za wyłomem skalnym widzisz przykutego do skały\
                \ngremlina. Biedaczysko ledwie zipie. ZŁY bierze cię za ramię i odprowadza na\
                \nodległość dziesięciu kroków od gremlina. Daje ci w garść sześć strzałek. ZŁY też\
                \nma sześć. Pokazuje palcem w stronę zakutego gremlina. To w niego należy celować!\
                \nChcesz grać?",

            "19": "KRASNOLUDY żegnają cię serdecznie i wręczają na drogę dwie główki sałaty.\
                \nOdprowadzają cię do wschodnich drzwi.",

            "20": "Po długim marszu dochodzisz do jakiejś wielkiej jaskini.\
                \nNie, to raczej bezkresna równina. Zapewne sławetne Szalone Pola.\
                \nSłyszysz jakiś hałas. Co sił wnogach biegniesz na zachód.\
                \nJednak potwory dopadają cię.",

            "21": "Jeśli chcesz zobaczyć co jest za drzwiami - patrz 332, jeśli nie - zawracasz i patrz 212.",

            "22": "To chyba juz kres twej wędrówki. Tak ślicznej komnaty ieszcze nie widziałeŚ.\
                \nWszędzie jasno, unosi się zielonkawa mgiełka. Posadzka jeszcze gładsza niż nad przepaścią.\
                \nNa podłodze siedzi jakiś ludek. Ah, to prawdziwy KRASNAL bawi się smoczkiem, nakręcanym,\
                \nz ruchomymi nogami i czerwonym językiem, który mu się co chwilę wysuwa. JeŚli masz\
                \nblaszanego motyla, możesz odpocząć i pobawić się z KRASNALEM - patrz 321.\
                \nJeśli masz szmaragd, możesz pokazać go KRASNALOWI - patrz 187. Tylko wtedy,\
                \ngdy masz drewniany pal, możesz próbować postraszyć albo nawet zaatakowac KRASNALA -patrz 9.\
                \nJeżeli masz więcej niż,iedną z wymienionych rzeczy, musisz wybrac tylko jedną możliwość",

            "23": "Drzwi do skarbca stoia przed toba... otworem? o, nie! są zamknięte.\
                \nWidzisz dwa zamki. Jeśli masz przynaimniej dwa numerowane kluczyki,\
                \nmożesz otworzyć nimi drzwi - patrz 185. Jeśli nie masz choć dwóch kluczy,\
                \ntu kończy się twoja Wyprawa. A było tak blisko!",

            "24": "Rzuć raz kostką. Jeśli wy|osujesz 1, 2, 3 - twoja broń\
                \nokaże się skutecznym narzędziem w walce z ROBALAMI - patrz 58.\
                \nJeŚli wylosujesz 4, 5, 6, nic z tego - patrz 168.",

            "25": "Na kamieniu siedzi stary człowiek. Radzi ci iść na zachód,\
                \na później na kilku najbliższych skrzyżowaniach skręcać w prawo.",

            "26": "Za celne trafienie każdego grubasa dostajesz 5 sztuk złota. Patrz 171.",

            "27": "Korytarz prowadzi prosto na północ. Po drodze możesz zjeść Prowiant.\
                \nZaczyna się rozszerzać, powiększać, aż wychodzisz na bezkresną równinę, To szalone Pola.\
                \nLepiej się tam nie zapuszczaj. Ale... czy słyszysz to dudnienie? To na pewno potwory.\
                \nPatrz 238. JeŚli je pokonasz albo wycofasz się w trakcie walki - patrz 316.\
                \nZapisz ten numer, bo zgubisz drogę.",

            "28": "Podnieś wielki kamień leżący przy ścianie.",

            "29": f"Potykasz się na kamyku. Miecz brzęknął o skałę. {ent.entity_116.name} podnosi głowę.\
                \nZauważył cię. Rzuca się do walki.",

            "30": "SSS. Jeśli masz S - patrz 159. JeŚli nie masz S - patrz 342.",

            "31": "Poświeć latarnią niżej. Rozgarnij mieczem to padło. A widzisz - znalazteś 5 sztuk ztota!",

            "32": f"Wyczerpany siadasz pod skałą. Możesz zjeść coś z Prowiantu.\
                \nLedwie skończyłeś posiłek, gdy do pieczary wpadają WILKOLUDY, znacznie\
                \nsłabsze od WILKOŁAKA, ale za to są trzy. Traktujesz je jako jednego potwra i walczysz.\
                \n{ent.entity_032.name}\
                \nJeśli zwyciężyłeś - patrz 275.",

            "33": "Jeszcze trochę i będziesz na skrzyżowaniu.\
                \nIdziesz na: . północ - patrz 293, na wschód - patrz 188, na południe - patrz 247",

            "34": "Ujawniasz swe odkrycie: drzwi w północnej ścianie. Nie robi to na nich wrażenia.\
                \nMówisz. że chcesz zobaczyć, co za nimi jest. Nie protestują.. Wstajesz od stołu i wzdłuż ściany\
                \ndochodzisz do sekretnych drzwi. Jeden z KRASNOLUDÓW przekręca ukrytą w ziemi gałkę.\
                \nDrzwi otwierają się. Wchodzisz - patrz 128",

            "35": "Płacisz wedtug taryfy (10 sztuk ztota). On rozkracza się nad rozpadliną. Podstawia ci ogon.\
                \nWchodzisz. Zapewne zaraz przeniesie cię na druga stronę wąwozu. Ale... Smok ma swoie humory. Często mu się zmieniają.\
                \nWłaśnie teraz obłapiasz jego ogon Wiszac nad czerwoną otchłanią. SSS. Jeśli masz S, przechodzisz na drugi brzeg - patrz 186.\
                \nJeśli nie masz S, Smok zrzuca cię z powrotem na krawędz skalną - patrz 158",

            "36": "SSS. Jeśli masz S - patrz 152. .jeśli nie masz S - patrz 176",

            "37":
                "Jaka tarczę wybierasz: metalową, paradną, czy skórzaną? Wpisz swój wybór na listę ekwipunku - patrz 324.",

            "38": "Korytarz prowadzi najpierw na północ, a pózniej łagodnym łukiem skręca ku wschodowi.\
                \nRozszerza się nieco i kończy schodami biegnącymi w dół. Stajesz przed drzwiami pokrytymi wyszukanymi ozdobami.\
                \nCzy byłeś iuż za tymi drzwiami? Jeśli tak - patrz 167, jeśli nie - patrz 328.",

            "39": "Dochodzisz do skrzyżowania. Jego odnogi prowadzą na:",

            "40":
                "Czy będziesz polegał tylko na kartach? - patrz 334, czy też będziesz korzystał ze swoiego SZCZĘŚCIA? - patrz 62",

            "41": "Udało ci się zrobić tylko parę kroków a tu korytarz zupełnie zatarasowany masą kamieni i piasku.\
                \nSpróbuj tupnac noga. Stare gremliny mówią, że to jest sposób na takie zawalidrogi. SSS. Jeśli masz S - góra skał\
                \nwpada gdzieŚ w przepaść, możesz iść da|ej - patrz 348. Jeśli nie masz S - musisz wrócić - oatrz 221,",

            "42": "Mówią o nim BARBARZYŃCA. czy słusznie? Kto wie? Gdy tak siedzi na ławie z wyciągniętymi nogami i rękami założonymi\
                \nna piersiach, nie wyglada groźnie. Cicho chrapie. Walisz mieczem w ścianę. Co jest? Ocknął się. Wchodzisz teraz do komnaty\
                \ni pokazujesz na drzwi po przeciwnej, zachodniej stronie. Otwieraj szybko tamte drzwi - pokazuiesz mu końcem miecza.\
                \nSam sobie otwórz - rechoce - Klucz jest w zamku: Istotnie. Podchodzisz do drzwi. obawiając się zasadzki,\
                \nnie dotykasz ręką klucza, lecz wsadzasz czub miecza w oko klucza i próbujesz przekręcic. Nic z tego. \
                \nNic z tego...- ryczy BARBARZYŃCA - Zaklęcie znasz? Jeśli nie znasz, to lepiej się stąd wynoś!\
                \nNo, właśnie, pamiętasz zaklęcie ze starej księgi gremlinów? Zaraz, a może ty wcale nie widziałeś tej księgi\
                \nTak czy owak, jeśli nie znasz zaklęcia, to koniec z tobą, bratku. spróbuj jeszcze raz, od samego początku.\
                \nJeśli wydaje ci się, że pamiętasz zaklęcie, powtórz je, Teraz zairzyj do paragrafu 122. Jeśli zapamiętałeś prawidłowo - patrz 376.\
                \nJeżeli zrobiłeś choćby najmniejszy błąd, kończysz przygodę. Jej dalsze prowadzenie w takiej sytuacji nie jest godne prawdziwego Śmiałka.",

            "43": "Musisz wrócić tędy, którędy przyszedłeś, aż znaidziesz się na drugim końcu przepaści. Po drodze z nikim nie walczysz,\
                \nniczego nie kupujesz, niczego nie zabierasz. Musisz spróbować innego wyjścia. Wymienione są w paragrafie 186.",

            "44": "Idziesz na wschód. Widzisz przed sobą solidne drzwi.\
                \nPróbujesz je otworzyć. Nie ustępują...",

            "45": "Kierujesz się w stronę fontanny. Nabierasz wody. Jest zaczarowana.\
                \nChowasz naczynie do plecaka. Spostrzegasz, że fontanna jest już pusta.",

            "46":
                "Wypatrujesz, jak wyjść z północnego brzegu pieczary. Widzisz niewielki otwór. Ruszasz w jego stronę i przeciskasz się z trudem. Patrz 53",

            "47": "Przeszedłeś zaledwie kilkanaście kroków i korytarz skręca w prawo, a zaraz potem kończy się. Możesz usiąść i sokojnie zjeść Prowiant.\
                \nPotem wracaj do skrzyźownia i idż na północ - patrz 191",

            "48": "Otwierasz plecak i sięgasz po naczvnie, by przesypać skarb. W tej samej chwili złoto rozpryskuje się we wszystkie strony,\
                \na wazy przemieniają się w dwa potężne, skrzydlate DEMONY, które wznoszą się i siadają na slnym występie. Możesz zaatakować je - patrz 169,\
                \nalbo wziąć się do zbierania rozsypanego złota - patrz - 33.",

            "49": "Możesz wziąc tę księgę ze sobą (wpisz na listę ekwipunku) albo ją zostawić. Patrz 286.",

            "50": "Zbliżasz się do skrzyżowania.\
                \nMożesz iść:",

            "51":
                "Możesz wyjść drzwiami południowi - patrz 134, albo północnymi - patrz 33. Jedne i drugie drzwi zostaw otwarte",

            "52": "Z otworu w ścianie wystrzeliwuje strumień gryzącego gazu. Jeśli masz hełm garnkowy, nie dzieje ci się krzywda.\
                \nChoć hełm ulega zniszczeniu. Jeśli nie masz takieqo hełmu - patrz najpierw 315, a potem 274 (zapisz ten numer).",

            "53": "Lądujesz w przestronnym chodniku. Wiedzie na północ, a po pewnym czasie skręca ostro na wschód.\
                \nRobisz kilkadziesiąt kroków i stajesz przed ciężkimi drzwiami, - Czy byłeś już tu? Jeśli tak - patrz 322, jeśli nie - patrz 299",

            "54": "Miotasz mtotem. Trafiłeś celnie. STRAŻNIK traci 2 W, ale nadal stoi jak słup. Patrz 107.",

            "55": "Dajesz złoto, bierzesz pal, słój albo jedno i drugie - patrz 196.",

            "56": "Ponownie próbujesz wyważyć drzwi. Znowu bezskutecznie.",

            "57": "Po wylądowaniu łajdak żqda całego twoiego zlota. Możesz powiedzieć, że dasz tylko tyle, ile żądał - patrz 335,\
                \nalbo że - w takim razie - nie dasz nic - patrz 91",

            "58": "Stosujesz swą tajemną broń. Całkowicie paralizue ROBALE. Jeśli chcesz zanurzyć się między ich cielska i\
                \nponownie przeszukać basen - patrz 142, jeśli nie . patrz 320.",

            "59": "Wchodzisz, ale niczego tu nie znajdujesz.\
            \nCzy znasz inne wyjście z tej komnaty niż to, którym właśnie wszedłeś?",

            "60": "KRASNAL proponuje 20 sztuk złota. Akceptujesz? Tak - patrz 262, nie - patrz 338.",

            "61": "Idziesz korytarzem. Po drodze możesz zieść Prowiant. Po pewnym czasie odchodzi od niego rozgałęzienie na północ,\
                \nale ty uparcie podążasz na zachód. Kilkanaście kroków za tym rozgałęzieniem widzisz drzwi. Otwierasz je - patrz 42.",

            "62": "SSS. Jeśli masz S - patrz 201, Jeśli nie masz S - patrz 145",

            "63": "Miecz nie jest skuteczną bronią przeciw WILKOŁAKOM. Jeśli masz któryś z wymienionych przedmiotów, możesz użyc go do walki:\
                \nkośc ze szkieletu przedwiecznego potwora - patrz 157\
                \nmłot goblinów - patz 346, metafowa tarcza - patrz 216,\
                \nsieć - patrz 377, pęk kluczy - patrz 181. Jeśli nie masz żadnego z tych przedmiotów, pozostaie ci tylko Ucieczka - patrz 275.",

            "64": "Zbliżasz się do skrzyżowania. Możesz iść w każdym z czterech kierunków.\
                \nWybierz kierunek:",

            "65": "Masz już dosyć tego miejsca? Jeśli tak - patrz 195,  jeśli nie - patrz 283.",

            "66":
                "Rzucasz dwiema kostkami. Pokaża ci ile sztuk złota wygrywasz. Chcesz grac dalej? - patrz 229. Nie chcesz? - patrz 19",

            "67": "Musisz się wycofać.",

            "68":
                "Wychodzisz ze zbrojowni. Jedyne drzwi prowadzą na północ. Podążasz korytarzem aż do najbliższego skrzyżowania. Po drodze możesz usiąść i zjeść Prowiant.",

            "69a": "Sam tego chciałeś. Pod ścianą komnaty siedzą dwa koszmarne upiory.\
                \nTakie spotkanie może zakończyć się tylko walką, najpierw z jednym, a później z drugim potworem.",

            "69b": "Ledwo pokonałeś pierwszego upiora a już zabierasz się za drugiego.",

            "69c": "Możesz przeszukać komnatę.",

            "70": "",

            "71": "",

            "72": "",

            "73": "",

            "74": "",

            "75": "Wycofujesz się. Wracasz w stronę skrzyżowania. Mijasz starca.",

            "76": "",

            "77": "",

            "78": "",

            "79": "",

            "80": "",

            "81": "",

            "82": "",

            "83": "",

            "84": "",

            "85": "",

            "86": "",

            "87": "",

            "88": "",

            "89a": "Czubem miecza podważasz wieko pudełka. Wewnątrz są 3 sztuki złota.\
                \nMożesz je wziąć.",

            "89b": "Rozglądasz się po kątach. Nagle słyszysz jakiś hałas.\
                \nZbierasz szybko swój ekwipunek i wybiegasz zostawiając drzwi otwarte.",

            "90": "",

            "91": "",

            "92": "",

            "93": "",

            "94": "",

            "95": "",

            "96": "",

            "97": "",

            "98": "",

            "99": "",

            "100": "",

            "101": "",

            "102": "Dochodzisz do skrzyżowania. Korytarze rozchodzą się we wszystkich kierunkach.\
                \nWybierz kierunek:",

            "103": "Wracasz. Mijasz skrzyżowanie. Idziesz na zachód. Po pewnym czasie widzisz\
                \nprzed sobą skrzyżowanie",

            "104": "Dajesz motyla, bierzesz złoto i smoczek",

            "105": "Próbujesz wyważyć drzwi. Rozpędzasz się i z całej siły uderzasz barkiem.\
                \nDrzwi ani drgnęły.",

            "106": "Tuż za drzwiami widzisz drewniane, wyszczerbione schody prowadzące w dół.\
                \nW centralnej części pieczary znajduje się kwadratowe zagłębienie, coś jakby basen,\
                \nale pusty. Schody prowadzą właśnie na dno basenu. Posadzka wysypana jest miałkim piaskiem.\
                \nWszędzie piasek, żadnych sprzętów, kamieni, ani istot... Hejże,\
                \na co to za zgięta pała sterczy w rogu basenu? Pewnie jakiś korzeń. Nie możesz odmówić\
                \nsobie tej przyjemności: dajesz mu solidnego kopa. To, co się teraz dzieje,\
                \nprzekracza wyobrażenia. Jeśli przetrwasz i będziesz komuś opowiadał o swojej\
                \nprzygodzie, na pewno nie uwierzy. Basen przypomina teraz garnek, w którymś ktoś\
                \nmiesza gruby makaron. Ty jesteś małym ziarnkiem miotanym we wszystkie strony.\
                \nTo ROBALE, najobrzydliwsze stwory podziemnego świata. Chcą rozetrzeć cię na\
                \nproszek. Wiją swe śliskie cielska. To wyrzucają cię na powierzchnię, to znowu\
                \nprzyciskają cię do dna. Możesz bronić się mieczem. Możesz też\
                \nzastosować inną broń, czyli.. No właśnie: niektórzy mówią, że skuteczną bronią\
                \nprzeciw ROBALOM jest żrący płyn, inni że wszystkożery (wieczne głodne skorupiaki).",

            "107": "",

            "108": "",

            "109": "",

            "110": "",

            "111": "",

            "112": "",

            "113": "",

            "114": "",

            "115": "Wybierz żeczy:",

            "116a": f"Odbiegasz w kąt pieczary. Kamienie pryskają spod stóp.\
                \n{ent.entity_116.name} przygląda się uważnie i naciera. Musisz walczyć.",

            "116b": "\nMożesz rozejrzeć się po pokoju.",

            "117": "",

            "118": "",

            "119":
                f"Co ta bestia tak zasłaniała? Dotykasz ściany w miejscu, o które opierał swe plecy włochaty {ent.entity_317.name}.\
                \nNagle cześć ściany uchyla się. To jest schowek! A w nim długa, ognioodporna lina z hakiem, pusta omszała flasza i skalp WILKOŁAKA.\
                \nMożesz wziąć najwyżej dwie z tych rzeczy.",

            "120": "Idziesz na zachód. Korytarz łagodnie skręca w prawo i teraz prowadzi już na północ.\
                \nWidzisz przed sobą skrzyżowanie.",

            "121": "",

            "122": "",

            "123": f"Korytarz biegnie na zachód i skręca na południe.\
                \nPrzed sobą widzisz skrzyżowanie.",

            "124": "",

            "125": "",

            "126": "",

            "127": "",

            "128": "",

            "129": "",

            "130": "Korytarz ma teraz prawie pięć kroków szerokości.\
                \nIdziesz więc wygodnie. Prostujesz kości.\
                \nPrzeszedłeść zaledwie sto kroków, a tu znowu skrzyżowanie.",

            "131": "",

            "132": "Czy poszedłeś po wodę?",

            "133": "",

            "134": "",

            "135": "",

            "136": "Smok uprzejmie zaprasza cię na swój ogon, którym trochę - co prawda - buja\
                \nnad jamą, ale zaraz potem lądujesz po drugiej stronie",

            "137": "",

            "138": "",

            "139": "",

            "140": "",

            "141": "",

            "142": "",

            "143": "",

            "144": "",

            "145": "",

            "146": "Korytarz biegnie na połódnie i skręca na wschód.\
                \nPrzed sobą widzisz skrzyżowanie.",

            "147": "",

            "148": "",

            "149": "",

            "150": "",

            "151": "",

            "152": "",

            "153": "Szczur to dobry znak. Twój miecz jest zaczarowany. W każdej walce, którą będziesz odtąd prowadził,\
                \nmożesz dodać 1 do siły ataku.",

            "154": "",

            "155": "",

            "156": "",

            "157": "",

            "158": "Nie masz dosyć?",

            "159": "",

            "160": "Ostrożnie stawiasz kroki. Nogi ocierają się o liście dorodnej sałaty.\
                \nMijając środek pokoju dostrzegasz padającą z góry strużkę światła.\
                \nNie zdradzasz swego odkrycia. Dochodzisz do stołu",

            "161": "",

            "162": "",

            "163": "",

            "164": "",

            "165": "",

            "166": "",

            "167": "",

            "168": "",

            "169": "",

            "170": "Dochodzisz do skrzyżowania. Ma kształt litery T.\
                \nMożesz iść na:",

            "171": "",

            "172": "",

            "173": "",

            "174": "",

            "175": "",

            "176": "Zbliżasz się do skrzyżowania.\
                \nMożesz pójść na:",

            "177": "Pod kamieniem schowana była ognista kula. Możesz ją zabrać.\
                \nWychodzisz.",

            "178": "Coraz trudniej wyciągnąć stopy z błotnistej mazi. Powietrze staje się coraz\
                \nwilgotniejsze. Korytarz stopniowo się rozszerza, aż w końcu wychodzisz na brzeg\
                \npodziemnego jeziora. Brzegi zarośnięte są roślinnością o grubych, szerokich\
                \nliściach. Sklepienie zawieszone jest wysoko. W kilku miejscach przesączają się\
                \nnie cienkie strugi światła. Rozglądasz się uważnie. Czy to ślepy zaułek?\
                \nNie dostrzegasz innego wyjścia niż to, którym przyszedłeś.",

            "179": "",

            "180": f"Ponownie przeszukujesz pokój. W torbie {ent.entity_116.name},\
                \nktórej nie zdążyłeś przejrzeć, znajdujesz klucz. Jest na nim wygrawerowana liczba 45.\
                \nMożesz go wziąść ze sobą.",

            "181": "Ciskasz w potwora pękiem kluczy, który znalazłeś w jednej z odwiedzonych\
                \nkomnat. Rzut jest celny, ale niegroźny. WILKOŁAK przechwytuje pęk i ucieka.\
                \nRuszasz w pogoń. WILKOŁAK wpada do wąskiej, ale głębokiej rozpadliny znajdującej\
                \nsię w rogu pieczary. Spada na dno i ginie. Przyświecasz sobie latarnią.\
                \nWidzisz w głębi zwaliste cielsko potwora, a obok niego pobłyskują klucze.",

            "182": "Czy chcesz szukać jakichś sekretnych przejść?",

            "183": "",

            "184": "Wycierasz zakrwawiony miecz o skóry leżące pod twoimi nogami.\
                \nNacierasz",

            "185": "Wchodzisz do wąskiego korytarzyka. Prowadzi on do dużego pomieszczenia",

            "186": "Udało ci się dotrzeć na drugi brzeg. Masz trzy wyjścia:\
                \njedno prowadzi na zachód (A), a dwa na północ,\
                \njedno z nich jest położone bardziej na zachód (B) niż drugie (C).\
                \nKtóre wybierasz?",

            "187": "",

            "188": "",

            "189": "",

            "190": "Możesz wybrać dowolny miecz.",

            "191": "",

            "192": "'A może by tak wycisnąć coś z tego pajaca?' - myślisz. Sięgasz po miecz. Ech, po co po miecz?\
                \nWystarczy zdzielić go pięścią. Podchodzisz do stwora i zamierzasz się. Istota znika.\
                \nNa dodatek z hukiem opada krata w przejściu, którym dostałeś się do tego pokoju. Rozglądasz się.\
                \nNie widzisz żadnego innego wyjścia. Podchodzisz do fontanny. Istotnie na jej dnie widzisz\
                \nróżne zagadkowe przedmioty: kość potwora, słój z wszystkożerami (wiecznie głodnymi skorupiakami), blaszanego motyla,\
                \nwłócznię i błyszczący kluczyk. To co: chcesz wodę, czy którąś z tych rzeczy. Pamiętaj, ze możesz wziąć tylko jedna rzecz.",

            "193": "",

            "194": "",

            "195": "",

            "196": "",

            "197": "",

            "198": "",

            "199": "",

            "200": "Po pewnym czasie dostrzegasz drzwi w południowej ścianie.",

            "201": "",

            "202": "",

            "203": "",

            "204": "",

            "205": "",

            "206": "",

            "207": "",

            "208": "",

            "209": "",

            "210": "",

            "211": "",

            "212": "Dochodzisz do sporego placyku, którego drogi rozchodzą się w czterech kierunkach.\
                \nKtóry wybierasz?",

            "213": "",

            "214": "",

            "215": "",

            "216": "",

            "217": "",

            "218": "",

            "219": "",

            "220":
                "Jeśli wybrałeś kość potwora, słój z wszystkożerami, blaszanego motyla lub włócznię - patrz 109, a jeśli klucz. patrz 366.",

            "221":
                "Dochodzisz do skrzyżowania, którym możesz przedostać się na: północ - patrz 339, - wschód - patrz 41, o południe - patrz 173.",

            "222": "",

            "223": "",

            "224": "Po kilkunastu krokach korytarz skręca na wschód. Idziesz dalej.\
                \nW połódniowej ścianie korytarza dostrzegasz drzwi.",

            "225": "",

            "226": "Walka trwa dalej. Po drugiej rundzie znów możesz Uciec.\
                \nNa pewno chcesz walczyć dalej?",

            "227": "",

            "228": "Korytarz biegnie na północ i skręca w na wschód. Przed sobą widzisz skrzyżowanie.",

            "229": "",

            "230": "",

            "231": "",

            "232": "",

            "233": "",

            "234": "Kończysz walkę z DEMONEM. Czy chcesz zajrzeć do kamiennej puszki stojącej na ołtarzyku?",

            "235": "",

            "236": "",

            "237": "",

            "238a": "Napotykasz grupę wędrujących Potworów. Są to: GREMLIN, LICHA, BRONGO, ORKONIK i SAMASKÓRA.\
                \nPo walce z każdym możesz ratować się Ucieczką.",

            "238b": "",

            "239": "",

            "240": "",

            "241": "Pamiętaj, że możesz nabrać wody z jeziora - patrz:",

            "242": "",

            "243": "",

            "244": "",

            "245": "",

            "246": "",

            "247": "",

            "248": "",

            "249": "",

            "250": "",

            "251": "Wychodzisz tędy, którędy wszedłeś.",

            "252": "",

            "253": "",

            "254": "",

            "255": "",

            "256": "",

            "257": "",

            "258": "",

            "259": "",

            "260": "",

            "261": "",

            "262": "",

            "263": "",

            "264": f"Trudno przejść przez to zwalisko kamieni.\
                \nNa szczęście korytarz nie wije się we wszystkie strony,\
                \nlecz prowadzi prosto na północ.",

            "265": "",

            "266": "",

            "267": "",

            "268": "Krótki tunel dochodzi do zbutwiałych, starych drzwi.",

            "269": "Wyciągasz z plecaka linę. Jest ognioodporna i zakończona hakiem.\
                \nPodchodzisz do krawędzi. Szerokim zamachem rzucasz hak między skały na przeciwnym brzegu.\
                \nZaczepił się. Przywiązujesz drugi koniec liny. Będziesz 'szedł' wisząc na rękach.\
                \nOpuszczasz się. Nagle... trach! Hak puścił. Wdrapujesz się z powrotem.",

            "270": "",

            "271a": "Zdejmujesz ze stojaka bogato zdobiony, błyszczący miecz. Obracasz rękojeść w dłoni.\
                \nNagle broń wypada ci z ręki i rani ramie.",

            "271b": "Wybierasz inny. Wygląda skromnie. Dobrze leży w dłoni.\
                \nOdrzucasz swój stary miecz. Ten z sykiem zamienia się w szczura. Dobry to, czy zły znak?\
                \nChcesz swój nowy miecz wymienić na inny?",

            "272": "",

            "273": "",

            "274": "",

            "275": "",

            "276": "",

            "277": "",

            "278": "",

            "279": "",

            "280": "",

            "281": "",

            "282": "",

            "283": "",

            "284": "Korytarz jest coraz węższy, Ze sklepienia zwisają długie, kamienne brody.\
                \nMogą lada chwila urwać się",

            "285": "",

            "286": "",

            "287": "",

            "288": "",

            "289": "",

            "290": "",

            "291": "Kierujesz się do wyjścia, gdy nagle nie wiadomo skąd\
                \ntrafia cię w brzuch mała, błękitna strzałka.",

            "292": "",

            "293": "",

            "294": "",

            "295": "",

            "296a": "Korytarz biegnie na zachód i skręca na północ.",

            "296b": "Idziesz dalej. Przed sobą widzisz skrzyżowanie.",

            "297": "",

            "298": "",

            "299": "",

            "300": "",

            "301": "Możesz spróbować otworzyć drzwi",

            "302": "",

            "303": "",

            "304": "",

            "305": "W tej komnacie ukryte jest coś bardzo wartościowego. Żeby to znaleźć musisz wybrać jedną z podanych metod:",

            "306": "Nabierasz wody. Jest zaczarowana. Chowasz naczynie do plecaka. Dostajesz +2s. Patrz - 109",

            "307": "",

            "308": "",

            "309": "",

            "310": "Tylko dziesięć kroków dzieli Cię od zmurszałych, drewnianych drzwi.",

            "311": "",

            "312": "",

            "313": "",

            "314": "",

            "315": "",

            "316": "Idziesz korytarzem na południe",

            "317a": "Drzwi ustępują. Bucha spoza nich przerażliwy smród.\
                \nW nikłym swietle oliwnej lampy widzisz porozrzucane na całym pomieszczeniu jakieś szczątki.\
                \nPrzyglądasz sie bliżej. To kości! odwracasz z obrzydzeniem twarz. A czego tu się spodziewałeś?\
                \nWojennych Kwiatów? Tańczących elfów? Melancholijnej muzyki? To są, bracie\
                \npodziemia - królestwo zła. I dlatego ...///...",

            "317b": f"{ent.entity_317.name} leży u twych stóp. Ciągle jeszcze się brzydzisz?",

            "318": "",

            "319": "",

            "320": "",

            "321": "",

            "322": "",

            "323": "",

            "324": "",

            "325": "",

            "326": "",

            "327": "",

            "328": "",

            "329": "",

            "330": "Ta komnata ma tylko jedno wyjście: to, którym się tu dostałeś. Wracasz do korytarza.",

            "331": "Króciutki tunel prowadzi cię do jakiegoś pomieszczenia.",

            "332a": "Wrota obite są grubą metalową blachą. Ukośnie przebiegają wąskie metalowe\
                \npasy, w miejscach przecięcia nabite żelaznymi guzami. Zapierasz się plecami.\
                \nStopy ślizgają się po grząskim gruncie. Wrota ustępują. Przeraźliwie skrzypią.\
                \nSłyszysz dobiegający z komnaty pospieszny szmer. Wciskasz się do szpary i\
                \nopierając się plecami o skałę z całą mocą odpychasz wrota. Opornie otwierają się\
                \nna całą szerokość. To był szalony wysiłek.",

            "332b": f"Podnosisz latarnię na wysokość\
                \noczu i... serce podchodzi ci do gardła. Schowany za ścianą stoi {ent.entity_332.name}. Ciało ma\
                \nwygięte w pałąk. Wysoko za głową oburącz trzyma miecz. Wypina do przodu\
                \nowłosiony brzuch. Szalone oczy nabiegły mu krwią. Szczerzy zaciśnięte zęby.\
                \nJeszcze chwila i ogromny miecz przetnie powietrze. Sięgasz po swój miecz. W\
                \nokamgnieniu {ent.entity_332.name} wyprowadza cios. Udaje ci się odskoczyć. To będzie walka na\
                \nśmierć i życie.",

            "333": "",

            "334": "",

            "335": "",

            "336": "W niewielkiej odległości dostrzegasz jakieś drzwi. Podchodzisz bliżej",

            "337": "",

            "338": "",

            "339": "",

            "340": "",

            "341": "",

            "342": "",

            "343": "",

            "344": f"Ognista kula jest znakomitą bronią przeciw STRAŻNIKOWI TAJEMNICY.\
                \nJest bardzo skuteczna i szybka. Wraca do twojej ręki po każdym rzucie.\
                \nDaje ci to następujące korzyści podczas walki:\
                \n*możesz dodać 2 do liczby uzyskanej na kostkach przy określaniu siły ataku,\
                \n*każdy atak powoduje nie 2 lecz 3 rany, *gdy STRAŻNIK zrani cię, rzuć kostką:\
                \njeśli uzyskasz liczbę nieparzystą, zadaje ci - jak normalnie - 2 rany;\
                \njeśli wyrzucisz 2 lub 4 otrzymujesz 1 ranę; jeśli masz 6, nie trafia cię w ogóle.",

            "345": "Idziesz w stronę skrzyżowania. Możesz pójść na:",

            "346": "",

            "347": "",

            "348": "",

            "349": "Delikatnie wsuwasz stopę w wąską szparę. Biodrami rozpychasz drzwi.\
                \nOdskakują na bok. To jest metoda! Wyczuwasz lekki zapach suszonych ziół.\
                \nPrzy lewej ścianie stoją dwie gładkie kolumienki.\
                \nMiedzy nimi na wysokości oczu rozciągnięta jest granitowa półka.\
                \nStoją tam dwie lampki, a na środku kamienne pudełko.\
                \n\
                \nPosadzka wyłożona jest włochatymi skórami zwierząt i potworów.\
                \nTo chyba podziemna kaplica! Pod ścianą, naprzeciw ołtarzyka widzisz niski, wykuty w skale stół.\
                \nCos tam na nim stoi. Podnosisz wyżej latarnię. Och, królu Almanhagorze, to dwie wazy pełne złota.\
                \nKażda ma taki sam wyszukany kształt. Z jednej strony ozdobiona jest łbem jakiegoś stwora,\
                \nz drugiej - przymocowane są dwa połyskujące skrzydła. Czy chcesz zabrać złoto?",

            "350": "",

            "351": "Przeciskasz się przez zawalony kamieniami korytarz.",

            "352": "",

            "353": "",

            "354": "",

            "355": "",

            "356": "",

            "357": "",

            "358": "Zaczepiłeś linę i już 'idziesz' po niej. Wtem z wnętrza rozpadliny bucha\
                \njęzor ognia. Jeśli masz przy sobie napój niewidzialności - wypij go.\
                \nOgień nieczyni ci krzywdy. Ale napój przestaje działać zanim docierasz do drugiego brzegu.",

            "359": "",

            "360": "",

            "361": "",

            "362": "",

            "363": "",

            "364": f"Popychasz drzwi, uchylają się. Otwiera się ciemna czeluść.\
                \nWchodzisz oświetlając drogę latarnią. Pod stopami czujesz kamyki.\
                \nZ przeciwległego końca pokoju dochodzi ciebie ciche chrapanie.\
                \nNa podłodze śpi {ent.entity_116.name}. Obok niego leży jakieś pudełko.",

            "365": "",

            "366": "",

            "367": "",

            "368": "",

            "369": "",

            "370": "",

            "371": "",

            "372": "",

            "373": "",

            "374": "To nie korytarz, raczej jakiś kanał. Nogi zapadają się w błotnistą maź.\
                \nTunel zmienia kierunek: najpierw skręca na południe, później na wschód, a w końcu na północ.",

            "375": "",

            "376": "",

            "377": "",

            "378": "",

            "379": "",

            "380": "",

            "381": "",

            "382":
                "Po pewnvm czasie korytarz skręca na północ. Na zakręcie mozesz zjeść Prowiant. Patrz - 134",

            "383": "Ogarnia cię wściekłość. Chwytasz za miecz i atakujesz - patrz 318.",

            "384":
                "Pięćdziesiąt kroków naprzód, a potem skręt W lewo (czyli na północ) i trzydzieści kroków. Patrz 221.",

            "385": "Możesz wydostać się z komnaty DEMONÓW albo przez wschodnie albo przez zachodnie drzwi.",

            "386":
                "Zbliżasz sie do skrzyżwania. Możesz iść albo na zachÓd - patrz 345, albo na wschÓd - patrz 273.",

            "387": "Wkładasz klucze do zamka. Najpierw pierwszy... stuk, później drugi... stuk i trzeci... stuk. Detikatnie podnosisz wieko skrzvni.\
                \nNa jej dnie leżą jakieś papiery. Nie, to złożony na 16 stron, ilustrowany druk. ostrożnie przewracasz kartki. Znajdujesz w nim dokładny opis wędrówki po podziemnym labiryncie. Zatrzymaj go, bo to papier niezwykle wartościowv"
        },
    'es':
        {
            "xxx": "",

            "elxr_chc": "Elige una poción:\
                \n1. Destreza\
                \n2. Resistencia\
                \n3. Suerte",

            "00a": "\rMientras caminas por los subterráneos, encontrarás diferentes tipos de armas y objetos.\
                \nRecuerda que, excepto la espada, cada arma solo se puede usar una vez.\
                \nDe igual manera, los objetos que encuentres son de un solo uso.\
                \nPuedes llevar una botella de elixir contigo.",

            "00b": "¡Hey, valiente!\
                \n\
                \nDicen que en tus venas fluye agua helada en lugar de sangre,\
                \ny que tus músculos están hechos del acero más noble.\
                \nSi es así, mira hacia el sol poniente.\
                \nAllá, en las fronteras del reino de Almanhagor, comienza el subterráneo inexplorado.\
                \nSolo tú puedes descubrir su Gran Secreto. ¡Adelante!",

            "01": "La entrada al subterráneo es amplia, invadida por hierba y arbustos exuberantes.\
                \nAjustas tu ropa y tu equipo.\
                \n¡Enciende tu linterna! Entras al pasillo. Es alto y no necesitas agacharte.\
                \nSe dirige directamente hacia el norte. Pronto llegas a una intersección.\
                \nTiene forma de la letra T. Los caminos conducen al oeste, este y sur (de donde vienes)."
        },
    'fr':
        {
            "xxx": "",

            "elxr_chc": "Choisissez une potion:\
                \n1. Dextérité\
                \n2. Endurance\
                \n3. Chance",

            "00a": "\rEn vous promenant dans les souterrains, vous trouverez différents types d'armes et d'objets.\
                \nSouvenez-vous que - à l'exception de l'épée - chaque arme ne peut être utilisée qu'une seule fois.\
                \nDe même, les objets trouvés sont à usage unique.\
                \nVous pouvez emporter une bouteille d'élixir avec vous.",

            "00b": "Hé, Brave !\
                \n\
                \nOn dit de vous que de l'eau glacée coule dans vos veines au lieu de sang,\
                \net que vos muscles sont faits de l'acier le plus noble ?\
                \nSi c'est le cas, regardez vers le soleil couchant.\
                \nLà-bas, aux frontières du royaume d'Almanhagor, commence le souterrain inexploré.\
                \nVous seul pouvez dévoiler son Grand Secret. Avancez !",

            "01": "L'entrée du souterrain est large, envahie par l'herbe et les buissons luxuriants.\
                \nVous ajustez vos vêtements et votre équipement.\
                \nAllumez votre lanterne ! Vous entrez dans le corridor. Il est haut, et vous n'avez pas besoin de vous baisser.\
                \nIl mène droit vers le nord. Bientôt, vous arrivez à un carrefour.\
                \nIl a la forme de la lettre T. Les branches mènent à l'ouest, à l'est et au sud (d'où vous venez)."
        },
    'it':
        {
            "xxx": "",

            "elxr_chc": "Scegli un'elisir:\
                \n1. Destrezza\
                \n2. Resistenza\
                \n3. Fortuna",

            "00a": f"\r{cnst.def_txt_clr}Mentre esplori i sotterranei, troverai diversi tipi di armi e oggetti.\
                \nRicorda che, a parte la spada, ogni arma può essere utilizzata solo una volta.\
                \nAllo stesso modo, gli oggetti trovati sono ad uso singolo.\
                \nPuoi portare con te una sola pozione dell'elisir.",

            "00b": "Ehi, coraggioso!\
                \n\
                \nDicono che nelle tue vene scorra acqua gelida invece di sangue,\
                \ne che i tuoi muscoli siano fatti del più nobile acciaio.\
                \nSe è così, guarda verso il tramonto.\
                \nLì, ai confini del regno di Almanhagor, iniziano i misteriosi Sotterranei.\
                \nSolo tu puoi svelarne il Grande Segreto. Avanti!",

            "01": "L'ingresso nei sotterranei è ampio, ricoperto d'erba e fitte siepi.\
                \nSistemati l'abbigliamento e l'equipaggiamento.\
                \nAccendi la lanterna! Entri nel corridoio. È alto, non devi chinarti.\
                \nProsegue dritto verso nord. Presto raggiungi un incrocio.\
                \nHa la forma della lettera T. Le diramazioni portano a ovest, est e sud (da dove sei venuto)."
        },
}

infoboook = {
    'en':
        {
            "return": "back",

            "Mmenu_headline": "MAIN MENU",

            "Mmenu_h": "Hello",

            "Mmenu0": "Continue",

            "Mmenu1": "New game",

            "Mmenu2": "Load game",

            "Mmenu3": "Game Rules",

            "Mmenu4": "Settings",

            "Mmenu4_sub1": "Language",

            "Mmenu4_sub1_1": "Choose language",

            "Mmenu4_sub1_2": "You chose",

            "Mmenu4_sub1_3": "easy",

            "Mmenu4_sub1_4": "medium",

            "Mmenu4_sub1_5": "hard",

            "Mmenu4_sub2": "Difficulty level",

            "Mmenu4_sub3": "Sound",

            "Mmenu4_sub3_1": "Dialogs",

            "Mmenu4_sub3_2": "Effects",

            "Mmenu4_sub3_3": "Music",

            "Mmenu4_sub4": "Character name",

            "Mmenu4_sub4_1": "Choose a character name (leave this field empty to generate a random name)",

            "Mmenu4_sub5": "Randomize character attributes",

            "Mmenu4_sub5_1": "Generating initial character statistics through randomization",

            "Mmenu5": "Exit the game",

            "Mmenu5_sub1_1": "Are you sure?",

            "Mmenu3_sub1": "Equipment and attributes",

            "Mmenu3_sub2": "Combat",

            "Mmenu3_sub3": "Escape",

            "Mmenu3_sub4": "Luck",

            "Mmenu3_sub5": "Leveling up attributes",

            "Mmenu3_sub6": "Provisions",

            "Mmenu3_sub7": "Purpose of the expedition",

            "Mmenu3_sub1_1a": "You are a daredevil.\
                \n\
                \nYour equipment consists of:",

            "Mmenu3_sub1_1b": f"While wandering through the dungeons, you will find different types of weapons and items.\
                \nRemember that - except for the sword - each weapon can only be used once.\
                \nSimilarly, the found items are single-use.\
                \nYou can take one bottle of elixir with you.\
                \nYou can choose among the elixirs: {cnst.special_txt_clr}AGILITY{cnst.def_txt_clr}, {cnst.special_txt_clr}ENDURANCE{cnst.def_txt_clr}, and {cnst.special_txt_clr}LUCK{cnst.def_txt_clr}.\
                \nYou can drink it at any time, but only twice during the adventure.\
                \n{cnst.def_txt_clr}Your attributes are: AGILITY, ENDURANCE, and LUCK.\
                \nBefore descending into the dungeons, the initial levels of these attributes are randomly determined.\
                \nTheir level will constantly change during your journey,\
                \nbut it cannot exceed the initial level.",

            "Mmenu3_sub1_2": "You will be fighting monsters. Their attributes (AGILITY and ENDURANCE) are unique to each enemy.\
                \nIn the current version of the game, battles are performed automatically. There is no possibility of interaction until the end of the fight,\
                \nunless the text allows for the option of escape.",

            "Mmenu3_sub1_3": "When in danger, you can save yourself by Escaping, if the text allows it.\
                \nIf you escape, the monster inflicts a wound: subtract 2 from your STAMINA.\
                \nDuring Escape (before or during combat), you can use SSS as described below.",

            "Mmenu3_sub1_4": "While traveling, you check if luck is on your side. You do it as follows:\
                \nRoll 2D. If the result is equal to or less than your current LUCK level, you have LUCK.\
                \nIf the result is greater, you don't have LUCK.\
                \nThis procedure is called Checking Your Luck (CYL).\
                \nAfter each CYL - regardless of the result - subtract 1 from your current LUCK level.\
                \nCYL must be done when the text predicts it, and can also be done during combat.\
                \nDuring combat, CYL is done at the appropriate moment in the round (see above), and its result only applies to that round.\
                \nHere's how CYL affects the course of combat:\
                \n\
                \n1. When you have wounded the monster\
                \n- if you have LUCK, subtract an additional 2 from the monster's STAMINA (total -4).\
                \n- if you don't have LUCK, subtract a total of 1.\
                \n2. When the monster has wounded you\
                \n- if you have LUCK, subtract a total of 1 from your STAMINA.\
                \n- if you don't have LUCK, subtract a total of 3.",

            "Mmenu3_sub1_5": f"While traveling, through adventures and combat, your characteristics change.\
                \n1. SKILL - changes very little\
                \n- enchanted weapon increases SKILL\
                \n- ELIXIR OF SKILL restores the initial level\
                \n2. STAMINA - constantly changing\
                \n- each meal (you have {cnst.eatables_count} of them at the start) adds {cnst.eatable_W_load} points\
                \n- ELIXIR OF STAMINA restores the initial level\
                \n3. LUCK\
                \n- successful adventures add points\
                \n- ELIXIR OF LUCK restores the initial level and even raises it by 1.\
                \nExcept for that case, SKILL, STAMINA, and LUCK cannot exceed the initial level.",

            "Mmenu3_sub1_6": f"In your backpack, you have Provisions, which are enough for {cnst.eatables_count} meals. You can only eat a meal when the text allows it.\
                \nYou can eat only one meal at a time. After consuming a meal, you gain {cnst.eatable_W_load} to your STAMINA.",

            "Mmenu3_sub1_7": "Your goal is to reach the treasure chamber. You will wander through a maze of corridors.\
                \nYou will visit many chambers inhabited by different creatures. You will encounter various surprises.\
                \nYou will probably fall into some traps.\
                \nFinding the right path and defeating the monsters will not be easy.\
                \nYou will probably have to undertake several expeditions before you reach your destination.\
                \nDraw a map of the dungeons each time. It will greatly help you.",
        },
    'pl':
        {
            "return": "wróć",

            "Mmenu_headline": "MENU GŁÓWNE",

            "Mmenu_h": "Witaj",

            "Mmenu0": "Kontynuuj",

            "Mmenu1": "Nowa gra",

            "Mmenu2": "Wczytaj grę",

            "Mmenu3": "Zasady Gry",

            "Mmenu4": "Ustawienia",

            "Mmenu4_sub1": "Język",

            "Mmenu4_sub1_1": "Wybierz język",

            "Mmenu4_sub1_2": "Wybrałeś",

            "Mmenu4_sub1_3": "łatwy",

            "Mmenu4_sub1_4": "średni",

            "Mmenu4_sub1_5": "trudny",

            "Mmenu4_sub2": "Poziom trudności",

            "Mmenu4_sub3": "Dźwięk",

            "Mmenu4_sub3_1": "Dialogi",

            "Mmenu4_sub3_2": "Efekty",

            "Mmenu4_sub3_3": "Muzyka",

            "Mmenu4_sub4": "Imię postaci",

            "Mmenu4_sub4_1": "Wybierz imię bohatera (zostaw puste aby wylosować imię)",

            "Mmenu4_sub5": "Losuj nowe atrybuty postaci",

            "Mmenu4_sub5_1": "Losowanie początkowych statystyk bohatera",

            "Mmenu5": "Wyjdź z gry",

            "Mmenu5_sub1_1": "Czy na pewno?",

            "Mmenu3_sub1": "Wyposażenie i cechy",

            "Mmenu3_sub2": "Walka",

            "Mmenu3_sub3": "Ucieczka",

            "Mmenu3_sub4": "Szczęście",

            "Mmenu3_sub5": "Podwyższanie poziomu cech",

            "Mmenu3_sub6": "Prowiant",

            "Mmenu3_sub7": "Cel wyprawy",

            "Mmenu3_sub1_1a": "Jesteś Śmiałkiem.\
                \n\
                \nTwój ekwipunek to:",

            "Mmenu3_sub1_1b": f"Wędrując po podziemiach będziesz znajdował inne rodzaje broni i przedmioty.\
                \nPamiętaj, że - poza mieczem - każda broń może być wykorzystana tylko raz.\
                \nPodobnie, znajdowane przedmioty są jednorazowego użytku.\
                \nMożesz zabrać ze sobą jedną butelkę eliksiru.\
                \nWybierasz spośród eliksirów: {cnst.special_txt_clr}ZRĘCZNOŚCI{cnst.def_txt_clr}, {cnst.special_txt_clr}WYTRZYMAŁOŚCI{cnst.def_txt_clr} i {cnst.special_txt_clr}SZCZĘŚCIA{cnst.def_txt_clr}.\
                \nMożna wypić go w dowolnym momencie, ale tylko dwukrotnie podczas przygody.\
                \n{cnst.def_txt_clr}Twoje cechy to: ZRĘCZNOŚĆ, WYTRZYMAŁOŚĆ i SZCZĘŚCIE.\
                \nPrzed zejściem do podziemi losowane są początkowe poziomy tych cech.\
                \nIch poziom będzie się nieustannie zmieniał podczas wędrówki,\
                \nale nie może przekroczyć poziomu początkowego.",

            "Mmenu3_sub1_2": f"Będziesz walczył z potworami. Ich cechy (ZRĘCZNOŚĆ i WYTRZYMAŁOŚĆ) są indywidualne dla każdego wroga.\
                \nW bieżącej wersji gry walki są wykonywane automatycznie. Do końca walki nie ma możliwości interackji,\
                \nchyba że tekst przewiduje możliwość ucieczki.",

            "Mmenu3_sub1_3": "Będąc w niebezpieczeństwie możesz ratować się Ucieczką, o ile tekst to przewiduje.\
                \nJeśli uciekasz, potwór zadaje ci ranę: odejmij 2 od swojej WYTRZYMAŁOŚCI.\
                \nPodczas Ucieczki (przed walką lub w jej trakcie) możesz zastosować SSS w opisany niżej sposób.",

            "Mmenu3_sub1_4": "Podczas wędrówki sprawdzasz, czy szczęście ci sprzyja. Robisz to w następujący sposób:\
                \nRzucasz 2K. Jeśli wynik jest równy lub mniejszy od aktualnego poziomu SZCZĘŚCIA, to masz SZCZĘŚCIE.\
                \nJeśli wynik jest większy, nie masz SZCZĘŚCIA.\
                \nTa procedura nazywa się Sprawdzanie Swojego Szczęścia (SSS).\
                \nPo każdym SSS - niezależnie od wyniku - należy odjąć 1 od aktualnego poziomu SZCZĘŚCIA.\
                \nSSS trzeba zrobić, gdy przewiduje to tekst, a także można zrobić podczas walki.\
                \nPodczas walki SSS robi się w odpowiednim momencie rundy (patrz wyżej), a jego wynik stosuje się tylko do tej rundy.\
                \nOto jakie znaczenie dla przebiegu walki ma SSS:\
                \n\
                \n1. Gdy zadałeś ranę potworowi\
                \n- jeśli masz SZCZĘŚCIE, to odejmujesz dodatkowo 2 od WYTRZYMAŁOŚCI potwora (łącznie -4).\
                \n- jeśli nie masz SZCZĘŚCIA, to odejmujesz łącznie 1.\
                \n2. Gdy potwór zadał ci ranę\
                \n- jeśli masz SZCZĘŚCIE, to odejmujesz łącznie 1 od swojej WYTRZYMAŁOŚCI\
                \n- jeśli nie masz SZCZĘŚCIA, to odejmujesz łącznie 3.",

            "Mmenu3_sub1_5": f"Podczas wędrówki, dzięki przygodom i walce, zmienia się poziom twoich cech.\
                \n1. ZRĘCZNOŚĆ - niewiele się zmienia\
                \n- zaczarowana broń podwyższa ZRĘCZNOŚĆ\
                \n- eliksir ZRĘCZNOŚCI przywraca poziom początkowy\
                \n2. WYTRZYMAŁOŚĆ - nieustannie się zmienia\
                \n- każdy posiłek (masz ich na starcie {cnst.eatables_count}) dodaje {cnst.eatable_W_load} punkty\
                \n- eliksir WYTRZYMAŁOŚCI przywraca poziom początkowy\
                \n3. SZCZĘŚCIE\
                \n- udane przygody dodają punkty\
                \n- eliksir SZCZĘŚCIA przywraca poziom początkowy, a nawet podnosi go o 1.\
                \nPoza tym przypadkiem, ZRĘCZNOŚĆ, WYTRZYMAŁOŚĆ i SZCZĘŚCIE nie mogą przekroczyć poziomu początkowego.",

            "Mmenu3_sub1_6": f"W plecaku masz Prowiant, który wystarcza na {cnst.eatables_count} posiłków. Posiłek można zjeść TYLKO wówczas, gdy przewiduje to tekst.\
                \nZa jednym razem można zjeść tylko jeden posiłek. Spożywszy posiłek, dostajesz {cnst.eatable_W_load} do swojej WYTRZYMAŁOŚCI.",

            "Mmenu3_sub1_7": "Twoim celem jest dotarcie do skarbca. Będziesz wędrował przez labirynt korytarzy.\
                \nOdwiedzisz wiele komnat, w których żyją różne istoty. Spotkają cię rozmaite niespodzianki.\
                \nZapewne wpadniesz w jakieś pułapki.\
                \nZnalezienie właściwej drogi i pokonanie potworów nie będzie łatwe.\
                \nZapewne będziesz musiał podjąć kilka wypraw, zanim uda ci się dotrzeć do celu.\
                \nZa każdym razem rysuj mapę podziemi. Bardzo ci pomoże.",
        },
    'es':
        {
            "return": "volver",

            "Mmenu_headline": "MENÚ PRINCIPAL",

            "Mmenu_h": "Bienvenido",

            "Mmenu0": "Continuar",

            "Mmenu1": "Nuevo juego",

            "Mmenu2": "Cargar juego",

            "Mmenu3": "Reglas del Juego",

            "Mmenu4": "Configuración",

            "Mmenu4_sub1": "Idioma",

            "Mmenu4_sub1_1": "Seleccionar idioma",

            "Mmenu4_sub1_2": "Has seleccionado",

            "Mmenu4_sub1_3": "fácil",

            "Mmenu4_sub1_4": "medio",

            "Mmenu4_sub1_5": "difícil",

            "Mmenu4_sub2": "Nivel de dificultad",

            "Mmenu4_sub3": "Sonido",

            "Mmenu4_sub3_1": "Diálogos",

            "Mmenu4_sub3_2": "Efectos",

            "Mmenu4_sub3_3": "Música",

            "Mmenu4_sub4": "Nombre del personaje",

            "Mmenu4_sub4_1": "Selecciona un nombre para el héroe (deja en blanco para generar uno al azar.)",

            "Mmenu4_sub5": "Generar nuevos atributos para el personaje",

            "Mmenu4_sub5_1": "Generando estadísticas iniciales del héroe",

            "Mmenu5": "Salir del juego",

            "Mmenu5_sub1_1": "¿Estás seguro?",

            "Mmenu3_sub1": "Equipamiento y habilidades",

            "Mmenu3_sub2": "Combate",

            "Mmenu3_sub3": "Huida",

            "Mmenu3_sub4": "Suerte",

            "Mmenu3_sub5": "Mejora de habilidades",

            "Mmenu3_sub6": "Provisiones",

            "Mmenu3_sub7": "Objetivo de la expedición",

            "Mmenu3_sub1_1a": "Eres un Valiente.\
                \n\
                \nTu equipamiento incluye:",

            "Mmenu3_sub1_1b": f"A medida que explores las mazmorras, encontrarás diferentes tipos de armas y objetos.\
                \nRecuerda que, excepto por la espada, cada arma solo se puede usar una vez.\
                \nDel mismo modo, los objetos encontrados son de un solo uso.\
                \nPuedes llevar contigo una botella de elixir.\
                \nPuedes elegir entre los elixires de {cnst.special_txt_clr}DESTREZA{cnst.def_txt_clr}, {cnst.special_txt_clr}RESISTENCIA{cnst.def_txt_clr} y {cnst.special_txt_clr}SUERTE{cnst.def_txt_clr}.\
                \nPuedes beberlo en cualquier momento, pero solo dos veces durante la aventura.\
                \n{cnst.def_txt_clr}Tus habilidades son: DESTREZA, RESISTENCIA y SUERTE.\
                \nAntes de descender a las mazmorras, se generan niveles iniciales aleatorios para estas habilidades.\
                \nSus niveles cambiarán constantemente durante tu viaje,\
                \npero no pueden superar el nivel inicial.",

            "Mmenu3_sub1_2": f"Te enfrentarás a monstruos. Sus habilidades (DESTREZA y RESISTENCIA) son individuales para cada enemigo.\
                \nEn la versión actual del juego, los combates se resuelven automáticamente. No hay posibilidad de interacción,\
                \na menos que el texto permita la opción de huir.",

            "Mmenu3_sub1_3": "Cuando te encuentres en peligro, puedes intentar huir si el texto lo permite.\
                \nSi escapas, el monstruo te infligirá una herida: resta 2 puntos de tu RESISTENCIA.\
                \nDurante la huida (antes o durante el combate), puedes utilizar la Prueba de Suerte de la siguiente manera.",

            "Mmenu3_sub1_4": "Durante tu viaje, verificarás si tienes suerte. Lo haces de la siguiente manera:\
                \nLanzas 2D. Si el resultado es igual o menor que tu nivel actual de SUERTE, entonces tienes suerte.\
                \nSi el resultado es mayor, no tienes suerte.\
                \nEste procedimiento se llama Prueba de Suerte Personal (PSP).\
                \nDespués de cada PSP, independientemente del resultado, debes restar 1 punto de tu nivel actual de SUERTE.\
                \nDebes realizar la PSP cuando el texto lo indique, y también puedes hacerlo durante el combate.\
                \nDurante el combate, la PSP se realiza en el momento adecuado de la ronda (ver arriba), y su resultado solo se aplica a esa ronda.\
                \nEsto es lo que significa la PSP para el desarrollo del combate:\
                \n\
                \n1. Cuando infliges una herida al monstruo\
                \n- si tienes SUERTE, resta adicionalmente 2 puntos de RESISTENCIA al monstruo (un total de -4).\
                \n- si no tienes SUERTE, resta un total de 1 punto.\
                \n2. Cuando el monstruo te inflige una herida\
                \n- si tienes SUERTE, resta un total de 1 punto de tu RESISTENCIA\
                \n- si no tienes SUERTE, resta un total de 3 puntos.",

            "Mmenu3_sub1_5": f"Durante tu viaje, a través de aventuras y combates, tus habilidades cambiarán de nivel.\
                \n1. DESTREZA: cambia poco\
                \n- las armas encantadas aumentan tu DESTREZA\
                \n- el elixir de DESTREZA restablece tu nivel inicial\
                \n2. RESISTENCIA: cambia constantemente\
                \n- cada comida (tienes {cnst.eatables_count} al comienzo) agrega {cnst.eatable_W_load} puntos\
                \n- el elixir de RESISTENCIA restablece tu nivel inicial\
                \n3. SUERTE\
                \n- las aventuras exitosas suman puntos\
                \n- el elixir de SUERTE restablece tu nivel inicial e incluso lo incrementa en 1.\
                \nExcepto en el caso mencionado, DESTREZA, RESISTENCIA y SUERTE no pueden superar el nivel inicial.",

            "Mmenu3_sub1_6": f"Tienes provisiones en tu mochila, suficientes para {cnst.eatables_count} comidas. Solo puedes comer una comida\
                \nen los momentos indicados por el texto.\
                \nSolo puedes comer una comida a la vez. Después de comer, se suman {cnst.eatable_W_load} puntos a tu RESISTENCIA.",

            "Mmenu3_sub1_7": "Tu objetivo es llegar a la cámara del tesoro. Viajarás a través de un laberinto de pasillos.\
                \nVisitarás muchas habitaciones donde habitan diferentes criaturas. Encontrarás diversas sorpresas.\
                \nProbablemente caerás en algunas trampas.\
                \nEncontrar el camino correcto y derrotar a los monstruos no será fácil.\
                \nProbablemente tendrás que emprender varias expediciones antes de llegar a tu destino.\
                \nDibuja un mapa de las mazmorras cada vez. Te será de gran ayuda.",

        },
    'fr':
        {
            "return": "retour",

            "Mmenu_headline": "MENU PRINCIPAL",

            "Mmenu_h": "Bonjour",

            "Mmenu0": "Continuer",

            "Mmenu1": "Nouveau jeu",

            "Mmenu2": "Chargement du jeu",

            "Mmenu3": "Règles du jeu",

            "Mmenu4": "Paramètres",

            "Mmenu4_sub1": "Langue",

            "Mmenu4_sub1_1": "Choisissez une langue",

            "Mmenu4_sub1_2": "Vous avez sélectionné",

            "Mmenu4_sub1_3": "facile",

            "Mmenu4_sub1_4": "moyen",

            "Mmenu4_sub1_5": "difficile",

            "Mmenu4_sub2": "Niveau de difficulté",

            "Mmenu4_sub3": "Son",

            "Mmenu4_sub3_1": "Dialogues",

            "Mmenu4_sub3_2": "Effets",

            "Mmenu4_sub3_3": "Musique",

            "Mmenu4_sub4": "Nom du personnage",

            "Mmenu4_sub4_1": "Choisissez le nom du héros (veuillez laisser le champ vide pour générer un nom aléatoire)",

            "Mmenu4_sub5": "Générer de nouvelles caractéristiques pour le personnage",

            "Mmenu4_sub5_1": "Génération des statistiques initiales du héros",

            "Mmenu5": "Quitter le jeu",

            "Mmenu5_sub1_1": "Êtes-vous sûre ?",

            "Mmenu3_sub1": "Équipement et caractéristiques",

            "Mmenu3_sub2": "Combat",

            "Mmenu3_sub3": "Fuite",

            "Mmenu3_sub4": "Chance",

            "Mmenu3_sub5": "Amélioration des caractéristiques",

            "Mmenu3_sub6": "Ravitaillement",

            "Mmenu3_sub7": "Objectif de l'expédition",

            "Mmenu3_sub1_1a": "Vous êtes un Intrépide.\
                \n\
                \nVotre équipement comprend :",

            "Mmenu3_sub1_1b": f"Lors de votre exploration des souterrains, vous trouverez différents types d'armes et d'objets.\
                \nVeuillez noter que, à l'exception de l'épée, chaque arme ne peut être utilisée qu'une seule fois.\
                \nDe même, les objets trouvés sont à usage unique.\
                \nVous pouvez emporter une seule fiole d'élixir avec vous.\
                \nVous pouvez choisir parmi les élixirs suivants : {cnst.special_txt_clr}AGILITÉ{cnst.def_txt_clr}, {cnst.special_txt_clr}ENDURANCE{cnst.def_txt_clr} et {cnst.special_txt_clr}CHANCE{cnst.def_txt_clr}.\
                \nVous pouvez le boire à tout moment, mais seulement deux fois au cours de l'aventure.\
                \n{cnst.def_txt_clr}Vos caractéristiques sont : AGILITÉ, ENDURANCE et CHANCE.\
                \nLes niveaux initiaux de ces caractéristiques sont générés aléatoirement avant d'entrer dans les souterrains,\
                \net ils peuvent évoluer tout au long de votre périple, mais ne peuvent pas dépasser le niveau initial.",

            "Mmenu3_sub1_2": f"Vous affronterez des monstres. Leurs caractéristiques (AGILITÉ et ENDURANCE) sont spécifiques à chaque ennemi.\
                \nDans la version actuelle du jeu, les combats sont automatisés. Il n'est pas possible d'interagir pendant le combat,\
                \nà moins que le texte ne vous donne la possibilité de fuir.",

            "Mmenu3_sub1_3": "En cas de danger, vous pouvez tenter de vous échapper si le texte le permet.\
                \nSi vous parvenez à vous échapper, le monstre vous infligera une blessure : retirez 2 points de votre ENDURANCE.\
                \nLors de la fuite (avant ou pendant le combat), vous pouvez utiliser la procédure SSS décrite ci-dessous.",

            "Mmenu3_sub1_4": "Lors de votre exploration, vous pouvez tester votre chance. Voici comment procéder :\
                \nLancez 2D. Si le résultat est inférieur ou égal à votre niveau actuel de CHANCE, vous avez de la chance.\
                \nSi le résultat est supérieur, vous n'avez pas de chance.\
                \nCette procédure est appelée Vérification de Votre Chance (VVC).\
                \nAprès chaque VVC, quel que soit le résultat, vous devez réduire de 1 votre niveau actuel de CHANCE.\
                \nLa VVC doit être effectuée lorsque le texte le prévoit, et peut également être effectuée pendant le combat.\
                \nPendant le combat, la VVC est effectuée à un moment précis du tour (voir ci-dessus), et le résultat n'est applicable qu'à ce tour.\
                \nVoici comment la VVC affecte le déroulement du combat :\
                \n\
                \n1. Si vous avez infligé une blessure au monstre\
                \n- si vous avez de la CHANCE, retirez 2 points supplémentaires de l'ENDURANCE du monstre (pour un total de -4).\
                \n- si vous n'avez pas de CHANCE, retirez un total de 1 point.\
                \n2. Si le monstre vous a infligé une blessure\
                \n- si vous avez de la CHANCE, retirez un total de 1 point de votre ENDURANCE\
                \n- si vous n'avez pas de CHANCE, retirez un total de 3 points.",

            "Mmenu3_sub1_5": f"Lors de votre exploration, grâce aux aventures et aux combats, vos niveaux de caractéristiques peuvent évoluer.\
                \n1. AGILITÉ - ne change que légèrement\
                \n- les armes enchantées augmentent l'AGILITÉ\
                \n- l'élixir d'AGILITÉ ramène le niveau à sa valeur initiale\
                \n2. ENDURANCE - change constamment\
                \n- chaque repas (vous en avez {cnst.eatables_count} au départ) ajoute {cnst.eatable_W_load} points\
                \n- l'élixir d'ENDURANCE ramène le niveau à sa valeur initiale\
                \n3. CHANCE\
                \n- les aventures réussies ajoutent des points\
                \n- l'élixir de CHANCE ramène le niveau à sa valeur initiale, voire l'augmente de 1.\
                \nEn dehors de cette situation, l'AGILITÉ, l'ENDURANCE et la CHANCE ne peuvent pas dépasser leur niveau initial.",

            "Mmenu3_sub1_6": f"Dans votre sac à dos, vous avez des provisions qui suffisent pour {cnst.eatables_count} repas.\
                \nVous ne pouvez manger un repas QUE si le texte le permet.\
                \nVous ne pouvez manger qu'un repas à la fois. En mangeant un repas, vous récupérez {cnst.eatable_W_load} points d'ENDURANCE.",

            "Mmenu3_sub1_7": "Votre objectif est d'atteindre le trésor. Vous vous aventurerez à travers le labyrinthe de couloirs.\
                \nVous visiterez de nombreuses pièces où vivent différentes créatures. Vous ferez face à diverses surprises.\
                \nVous tomberez probablement dans des pièges.\
                \nTrouver le bon chemin et vaincre les monstres ne sera pas facile.\
                \nVous devrez probablement entreprendre plusieurs expéditions avant de parvenir à votre objectif.\
                \nDessinez une carte des souterrains à chaque fois. Cela vous sera très utile.",
        },
    'it':
        {
            "return": "ritorna",

            "Mmenu_headline": "MENU PRINCIPALE",

            "Mmenu_h": "Benvenuto",

            "Mmenu0": "Continua",

            "Mmenu1": "Nuovo gioco",

            "Mmenu2": "Carica il gioco",

            "Mmenu3": "Regole del Gioco",

            "Mmenu4": "Impostazioni",

            "Mmenu4_sub1": "Lingua",

            "Mmenu4_sub1_1": "Seleziona lingua",

            "Mmenu4_sub1_2": "Hai selezionato",

            "Mmenu4_sub1_3": "facile",

            "Mmenu4_sub1_4": "medio",

            "Mmenu4_sub1_5": "difficile",

            "Mmenu4_sub2": "Livello di difficoltà",

            "Mmenu4_sub3": "Audio",

            "Mmenu4_sub3_1": "Dialoghi",

            "Mmenu4_sub3_2": "Effetti",

            "Mmenu4_sub3_3": "Musica",

            "Mmenu4_sub4": "Nome del personaggio",

            "Mmenu4_sub4_1": "Seleziona il nome del protagonista (lascia vuoto questo casella per scegliere un nome casuale)",

            "Mmenu4_sub5": "Genera nuove caratteristiche del personaggio",

            "Mmenu4_sub5_1": "Generazione iniziale delle statistiche del protagonista",

            "Mmenu5": "Esci dal gioco",

            "Mmenu5_sub1_1": "Sei sicuro?",

            "Mmenu3_sub1": "Equipaggiamento e attributi",

            "Mmenu3_sub2": "Combattimento",

            "Mmenu3_sub3": "Fuga",

            "Mmenu3_sub4": "Fortuna",

            "Mmenu3_sub5": "Aumentare il livello degli attributi",

            "Mmenu3_sub6": "Provvisioni",

            "Mmenu3_sub7": "Obiettivo dell'avventura",

            "Mmenu3_sub1_1a": "Sei un Coraggioso.\
                \n\
                \nIl tuo equipaggiamento include:",

            "Mmenu3_sub1_1b": f"Mentre esplori i sotterranei, troverai diversi tipi di armi e oggetti.\
                \nRicorda che - a parte la spada - ogni arma può essere utilizzata solo una volta.\
                \nAllo stesso modo, gli oggetti trovati possono essere utilizzati una sola volta.\
                \nPuoi portare con te una sola bottiglia di elisir.\
                \nPuoi scegliere tra gli elisir: {cnst.special_txt_clr}DESTREZZA{cnst.def_txt_clr}, {cnst.special_txt_clr}RESISTENZA{cnst.def_txt_clr} e {cnst.special_txt_clr}FORTUNA{cnst.def_txt_clr}.\
                \nPuoi berlo in qualsiasi momento, ma solo due volte durante l'avventura.\
                \n{cnst.def_txt_clr}I tuoi attributi sono: DESTREZZA, RESISTENZA e FORTUNA.\
                \nPrima di scendere nei sotterranei, vengono generate casualmente i livelli iniziali di questi attributi.\
                \nI loro livelli cambieranno costantemente durante il tuo viaggio,\
                \nma non possono superare il livello iniziale.",

            "Mmenu3_sub1_2": f"Ti scontrerai con mostri. Le loro caratteristiche (DESTREZZA e RESISTENZA) sono individuali per ogni nemico.\
                \nNella versione attuale del gioco, i combattimenti vengono eseguiti automaticamente. Non c'è interazione durante il combattimento,\
                \na meno che il testo non preveda la possibilità di fuggire.",

            "Mmenu3_sub1_3": "Quando sei in pericolo, puoi cercare di fuggire, a condizione che il testo lo preveda.\
                \nSe fuggi, il mostro ti infligge una ferita: sottrai 2 dalla tua RESISTENZA.\
                \nDurante la fuga (prima o durante il combattimento), puoi usare la Procedura di Salvataggio dalla Sfortuna (PSS) come descritto di seguito.",

            "Mmenu3_sub1_4": "Durante il tuo viaggio, puoi verificare se la fortuna ti sorride. Puoi farlo nel seguente modo:\
                \nLancia 2D. Se il risultato è uguale o inferiore al tuo livello attuale di FORTUNA, allora hai FORTUNA.\
                \nSe il risultato è maggiore, non hai FORTUNA.\
                \nQuesta procedura è chiamata Procedura di Salvataggio dalla Sfortuna (PSS).\
                \nDopo ogni PSS - indipendentemente dal risultato - sottrai 1 dal tuo livello attuale di FORTUNA.\
                \nIl PSS deve essere eseguito quando previsto dal testo e può essere eseguito anche durante il combattimento.\
                \nDurante il combattimento, il PSS viene eseguito nel momento appropriato del round (vedi sopra), e il suo risultato si applica solo a quel round.\
                \nEcco cosa significa per il corso del combattimento il PSS:\
                \n\
                \n1. Quando infliggi una ferita al mostro\
                \n- se hai FORTUNA, sottrai ulteriormente 2 dalla RESISTENZA del mostro (totale -4).\
                \n- se non hai FORTUNA, sottrai un totale di 1.\
                \n2. Quando il mostro ti infligge una ferita\
                \n- se hai FORTUNA, sottrai un totale di 1 dalla tua RESISTENZA\
                \n- se non hai FORTUNA, sottrai un totale di 3.",

            "Mmenu3_sub1_5": f"Durante il tuo viaggio, grazie alle avventure e ai combattimenti, il livello dei tuoi attributi cambierà.\
                \n1. DESTREZZA - cambia poco\
                \n- le armi incantate aumentano la DESTREZZA\
                \n- l'elisir di DESTREZZA ripristina il livello iniziale\
                \n2. RESISTENZA - cambia costantemente\
                \n- ogni pasto (hai {cnst.eatables_count} pasti all'inizio) aggiunge {cnst.eatable_W_load} punti\
                \n- l'elisir di RESISTENZA ripristina il livello iniziale\
                \n3. FORTUNA\
                \n- le avventure fortunate aggiungono punti\
                \n- l'elisir di FORTUNA ripristina il livello iniziale e può aumentarlo di 1.\
                \nOltre a questo caso, DESTREZZA, RESISTENZA e FORTUNA non possono superare il livello iniziale.",

            "Mmenu3_sub1_6": f"Nello zaino hai del Cibo, che è sufficiente per {cnst.eatables_count} pasti. Puoi mangiare il Cibo SOLO quando previsto dal testo.\
                \nPuoi mangiare solo un pasto alla volta. Dopo aver mangiato il pasto, ricevi {cnst.eatable_W_load} punti nella tua RESISTENZA.",

            "Mmenu3_sub1_7": "Il tuo obiettivo è raggiungere la camera del tesoro. Camminerai attraverso il labirinto dei corridoi.\
                \nVisiterai molte stanze in cui vivono diverse creature. Incontrerai molte sorprese.\
                \nProbabilmente incapperai in qualche trappola.\
                \nTrovare la strada giusta e sconfiggere i mostri non sarà facile.\
                \nProbabilmente dovrai intraprendere diverse spedizioni prima di riuscire a raggiungere l'obiettivo.\
                \nDisegna una mappa del sottosuolo ogni volta. Ti sarà molto utile.",
        },

}


def get_translation(translation):
    if not translation in gameboook:  # if not available, set to english
        fun.debug_message('not available, language defaulted to english')
        translation = 'en'
    cnst.translation = translation
    return gameboook[translation], infoboook[translation], cnst.translation
