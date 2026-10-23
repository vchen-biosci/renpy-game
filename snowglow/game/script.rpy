# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define o = Character("Osric", color="#5d4d2f")
define w = Character("Wynfled", color="#406197")
default wynn_affec = 100
default os_affec = 50


label start:

    scene bg room with dissolve
    show wynfled normal at right
    show osric normal at left

    "You and your friends, Wynnfled and Osric, have been sent out for the monthly ice haul, marking the rare ocassion
    of being permitted to leave Seolforstan, your orphanage to carve ice in outer Ismere."
    "Your fingers burn and begin to stiffen as you pull your handmitts off."
    show wynfled happy at right
    w "Osriccc! Come get it!"
    "Wynfled waves Os's shovel around, giggling."
    show osric happy at left
    o "...Give it here."
    w "No, no, I've got it."
    "Your fingers start freezing as they continue joking around."
    show wynfled laughing at left 
    show osric laughing at right
    w "Maren, catch! Oh nooo, where'd your shovel go, Os?"
    "You catch the shovel."
    menu:
        "'Can you get back on task?'":
            jump annoyed
        "*Laugh along and put your handmitts back on*":
            jump fun
        "Start carving the ice before your fingers freeze off":
            jump carve_alone

label annoyed:

    $ wynn_affec -= 1
    $ os_affec += 5
    show wynfled thinking at right
    show osric normal at left
    w "Mare, what's gotten into you?"
    o "It's one of her moods again..."
    show wynfled normal at right
    w "Well, at these times it's better to leave her alone anyways!"
    o "..."
    o "Wynn, she's right. Let's finish carving first."
    jump work

label fun:

    $ wynn_affec += 1
    $ os_affec -= 3
    show osric normal at right
    "Os glances at you briefly. He looks slightly annoyed."
    show osric happy at right
    w "Hey, you guys wanna go explore 'round Ismere?"
    menu: 
        "Yes!":
            jump explore
        "Hey, actually, let's finish carving the ice first.":
            jump annoyed


label explore:
    pass


label carve_alone:
    "Wynn and Os continue to mess around as you twist open the powder capsule. You use your pin to gently tip the melting reagent around the target region."
    "You adjust your holster, blowing at your fingers to keep them warm"
    show wynfled surprised at right
    show osric happy at left
    w "Oh! Mare's at it already!"
    show osric surprised at left
    o "Yeah, let's get back to work. Mare, pass me my shovel, eh?"
    show wynfled laughing 
    w "Os! Not yet! You wanna go explore 'round Ismere?"
    show osric sad
    o "But Mare'll be alone…"
    "Os looks at you, confused."
    show wynfled thinking
    w "You're right. Mare, do you want to come with?"
    menu:
        "'We genuinely need to work. Come on, guys.'":
            jump annoyed
        "'Yeah, I'll come.'":
            jump explore
        "'Look up and shake your head'":
            jump continue_alone

label work:
    show wynfled normal
    w "How'd I get roped into this again?"
    show osric laughing
    o "We've got to finish our quota or we'll get in trouble."
    show wynfled thinking
    w "Come to think of it, I haven't seen Heda and Wren since they left to Eolyusion."
    show osric normal
    menu:
        "I don't think they're meant to come back, you know.":
            pass
    show wynfled sad
    w "But that's just terrible!"
    show osric happy
    o "So put your head down and work, Wynn."
    show wynfled surprised
    show osric surprised
    "You take out the reducing agent and step back. You all watch as the ice falls away in a perfect circle."



label continue_alone:
    pass