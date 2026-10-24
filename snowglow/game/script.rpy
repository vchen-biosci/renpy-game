# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define o = Character("Osric", color="#af8a45")
define w = Character("Wynfled", color="#4179d4")
default wynn_affec = 100
default os_affec = 50
default skip_ice = False
style my_text is text:
    size 40
    font "evelyne.regular.otf"


label start:

    scene bg room with dissolve
    show wynfled normal at right
    show osric normal at left

    "You and your friends, Wynnfled and Osric, have been sent out for the monthly ice haul, marking the rare ocassion
    of being permitted to leave Seolforstan, your orphanage to carve ice in outer Ismere."
    "Your fingers burn and begin to stiffen as you pull your handmitts off."
    define mc = Character("[name]")

    python:
        name = renpy.input("What is your name?", length=32, default="Maren Rime")
        name = name.strip()

        if not name:
            name = "Maren Rime"

        nickname = renpy.input("What nickname do you friends call you?", length=32, default="Mare")
        nickname = nickname.strip()
        if not nickname:
            nickname = "Mare"

    show wynfled happy at right
    w "Osriccc! Come get it! [nickname], quit scowling!"
    "Wynfled waves Os's shovel around, giggling."
    show osric happy at left
    o "...Give it here."
    w "No, no, I've got it."
    "Your fingers start freezing as they continue joking around."
    mc "Guys, I'm a bit cold..."
    show wynfled laughing at left 
    show osric laughing at right
    w "Then put your mitts back on! Wait, no! Ahhhh! [nickname], catch! Oh nooo, where'd your shovel go, Os?"
    "You catch the shovel."
    menu:
        "'Can you quit fooling around now?'":
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
    w "[nickname], what's gotten into you?"
    o "It's one of her moods again..."
    mc "So you just hate working, huh?"
    show wynfled normal 
    w "Well, at these times it's better to leave her alone anyways!"
    o "..."
    o "Wynn, she's right. Let's finish carving first."
    jump work

label fun:

    $ wynn_affec += 1
    $ os_affec -= 3
    show osric normal
    "Os glances at you briefly. He looks slightly annoyed."
    show osric happy
    w "Hey, you guys wanna go explore 'round Ismere?"
    menu: 
        "Yes!":
            jump explore
        "Hey, actually, let's finish carving the ice first.":
            jump annoyed


label explore:
    
    "The three of you mark the ice locus with a makeshift flag and set off to look around the landscape."

label carve_alone:
    "Wynn and Os continue to mess around as you twist open the powder capsule. You use your pin to gently tip the melting reagent around the target region."
    "You adjust your holster, blowing at your fingers to keep them warm"
    show wynfled surprised at right
    show osric happy at left
    w "Oh! [nickname]'s at it already!"
    show osric surprised 
    o "Yeah, let's get back to work. [nickname], pass me my shovel, eh?"
    show wynfled laughing 
    w "Os! Not yet! You wanna go explore 'round Ismere?"
    show osric sad
    o "But [nickname]'ll be alone…"
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
    show wynfled sad
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
    o "It's a punishment, Wynn. It's meant to set an example."
    o "So let's just focus on not becoming them and work hard."
    show wynfled surprised
    show osric surprised
    "You sprinkle the reducing agent on the red powder and step back. You all watch as the ice falls away in a perfect circle."
    mc "Yes!! We did it!"
    show wynfled happy
    show osric happy
    "You all do a group hi-five. You almost melt into your glove as you put it back on."
    w "Aaaaa!!! I can finally feel my fingers again!"
    w "But y'know, I kinda wanna stay out here just a little longer... can we go explore?"
    show osric normal
    "Osric doesn't respond, but looks at you cryptically."
    default ask_osric_count = 0
    jump decide_ice
    
label continue_alone:
    "Osric and Wynn leave without you, and now you're left alone."


label ask_osric:
    show osric angry
    "Osric looks angry."
    if ask_osric_count < 5:
        $ os_affec -= 2
        o "You decide."
        jump decide_ice
    else:
        o "You're really indecisive, huh? Let's just head back then, or we'll be here all day."
        show wynfled surprised
        w "Os, that's not like you!"
        show osric normal 
        o "Guess it's been a long day."
        "Wynfled looks hesitant, but nods."
        jump back_at_camp

label decide_ice:
    show osric normal
    menu:
        "I don't think so. We need energy to haul the ice back.":
            jump back_at_camp
        "Fine, we can stay a bit. We've collected enough ice anyways.":
            jump explore
        "Osric? What do you think?":
            $ ask_osric_count += 1
            jump ask_osric