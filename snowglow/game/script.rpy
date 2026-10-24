# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define o = Character("Osric", color="#af8a45")
define w = Character("Wynfled", color="#4179d4")
define n = Character("Nightcumb", color="#df28cd")
default wynn_affec = 100
default os_affec = 50
default skip_ice = False
define gui.text_font = "GlacialIndifference-Regular.otf"
define gui.text_instance = "light"
define gui.text_axis = {"width" : 125}
define gui.text_size = 35

#define audio.over_the_rise = 



label start:

    play music over_the_rise loop volume 0.75
    show mining site with dissolve
    with None
    "Before we begin, let's learn a bit more about you."
    define mc = Character("[name]")

    python:
        name = renpy.input("What's your name?", length=32, default="Maren Rime")
        name = name.strip()

        if not name:
            name = "Maren Rime"

        nickname = renpy.input("What nickname do you like to be called?", length=32, default="Mare")
        nickname = nickname.strip()
        if not nickname:
            nickname = "Mare"

    show wynfled normal at right
    "This is Wynn (Wynfled). She's your best friend."
    hide wynfled
    show osric normal at left
    "This is Os (Osric). He's your other team-member for ice expeditions."
    show wynfled normal at right
    "You've just finished hiking through the snowy tundra to reach outer Ismere (the ice-capped water body behind you)."
    "The quarterly ice haul is the only time you're ever permitted to leave Seolforstan, your orphanage."
    "Your fingers burn and begin to stiffen as you pull your handmitts off."
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
    "Wynn and Os continue to mess around as you twist open the powder capsule. You use your pin to gently tip the melting reagent around the target region."
    "You adjust your holster, blowing at your fingers to keep them warm."
    show wynfled surprised at right
    show osric happy at left
    w "Oh! [nickname]'s at it already!"
    show osric surprised 
    o "Yeah, let's get back to work. [nickname], pass me my shovel, eh?"
    show wynfled laughing 
    jump work
    

label work:
    show wynfled sad
    w "How'd I get roped into this again?"
    show osric laughing
    o "We've got to finish our quota or we'll get in trouble."
    show wynfled thinking
    w "Come to think of it, I haven't seen Heda and Wren since they left to Eolyusion."
    show osric normal
    menu:
        "I think they're not meant to come back.":
            pass
    show wynfled sad
    w "But that's just terrible!"
    show osric happy
    o "It's a punishment, Wynn. It's meant to set an example for all of us."
    o "So let's follow suit and work hard."
    show wynfled surprised
    show osric surprised
    "You sprinkle the reducing agent on the red powder and step back. You all watch as the ice falls away in a perfect circle."
    mc "...Isn't this the luckiest we've ever been?"
    show wynfled happy
    show osric happy
    "You all do a group hi-five. You almost melt into your glove as you put it back on."
    w "Aaaaa!!! I can finally feel my fingers again!"
    w "But y'know, I kinda wanna stay out here just a little longer... Can we go explore?"
    show osric normal
    "Osric doesn't respond, but looks at you cryptically."
    menu:
        "I don't think so. We need energy to haul the ice back. And we're not done yet.":
            pass
    o "That's right. I'm sure Nightcumb's coming for us soon."
    show wynfled scared
    "Wynn shivers. You giggle."
    show wynfled angry
    w "Hey! What's so funny?"
    mc "Nothing..."
    show wynfled normal
    "You all set to work lifting and hauling the ice."
    "It's taxing work, and by the end you're all glad you chose not to explore the tundra further."
    w "Just for the record, I'm not scared of-"
    show wynfled scared
    show nightcumb normal
    w "AAAAAAAA!!!!!"
    n "Hello, children."
    "He glances inscrutably at the ice pile."
    n "You did well to survive. Group 5 had some casualties this time around."
    show wynfled angry
    show osric angry
    n "Anyho! You can take this back to camp now!"
    menu:
        "...Understood.":
            pass
        "Think we could borrow any of that gear you have there?":
            pass
    n "See you!"
    hide nightcumb
    w "Tch."
    mc "If it helps, I find him disconcerting too."
    o "I just don't get why he can't show his marktag."
    show wynfled sad
    w "Right? He keeps it all tucked up behind his stupid purple hair."