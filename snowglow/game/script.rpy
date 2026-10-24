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
    show wynfled sad at right
    w "I'm... so tired."
    "You look down at the shoddy pile of ice you've gathered."
    menu: 
        "We're still short on ice.":
            jump branch_1
        "...let's take a break.":
            jump branch_2

label branch_1:
    w "How'd I get roped into this again?"
    show osric laughing
    o "We've got to finish our quota, Wynn. We signed up for this, remember?"
    show wynfled thinking
    w "Come to think of it, I haven't seen Heda and Wren since they left to Eolyusion."
    show osric normal
    menu:
        "They're never coming back. Don't you get it?":
            pass
        "Hey, I'm sure you're overthinking it...":
            jump con_branch_1
    show wynfled sad
    w "But that's just terrible!"
    show osric happy
    o "It's a punishment, Wynn. It's meant to set an example for all of us."
    o "So let's follow suit and work hard."
    show wynfled surprised
    show osric surprised
    jump branch_1_1

label branch_1_1:
    "The cold bites at your bare fingers, but none of you complain."
    "The faster you get this part done, the more likely you are to keep your digits."
    show wynfled thinking
    w "Os, some of that reducing agent please."
    show wynfled normal
    show osric happy
    o "Yes, one sec... you got the powder, [nickname]?"
    mc "Yes. Wynn?"
    show wynfled happy
    w "Here."
    "You hammer your rod-needle into the ice in the general shape of a circle."
    show wynfled thinking
    show osric normal
    "Meanwhile, Wynn and Os place the reducing agent and powder on opposite sides."
    show osric happy
    "You all nod at each other."
    show wynfled normal
    w "Kaboom!"
    "She uses her draw-pipe to blast the two substances at each other at high pressure."
    show wynfled sad
    show osric sad
    mc "Well... that was something."
    menu:
        "Come on, let's try again.":
            jump branch_1_2
        "The punishment doesn't sound so bad after all...":
            jump branch_2

label branch_1_2:
    show wynfled thinking
    show osric normal
    "Collection time is soon, and you can all feel it."
    "Wynn's gaze is clearer and she's making less jokes now."
    "None of you speak, but you nod at each other instead to communicate."
    "The shape is hammered in the ice, and Os spreads the reagents more carefully this time."
    "You all nod at each other."
    "BAM!"
    show wynfled happy
    show osric happy
    "The ice comes free."
    w "woo... WOAHHH!!!"
    o "..."
    mc "YES! Ugh, my hands are freezing."
    "You all put your mitts on."
    show wynfled laughing
    w "I know, right? Ahhhh, it feels like they're melting."
    o "Should we push for another one?"
    show wynfled angry
    w "I say no!"
    show osric happy
    show wynfled normal
    o "What do you say, [nickname]?"
    w "Come onnnn, let's just rest a bit, eh?"
    show wynfled sad
    w "I really think I'm about to get frostbite."
    menu:
        "I say we rest 'till Nightcumb comes!":
            jump branch_1_3_1
        "We're on a roll, let's do another one!":
            jump branch 1_3


label branch_2:
    pass

label con_branch_1:
    w "Ugh, you're right. Os, how bad can the punishment actually be?"
    show osric surprised
    o "..."
    show osric normal
    o "Nobody's ever come back, that's for sure."
    show wynfled happy
    "You and Wynn share a smile."
    w "Is getting to leave Seolforstan really that bad?"
    o "What?"
    w "Just saying, it's kinda like a prison..."
    "She's right. You're only ever allowed out under supervision."
    menu:
        "Let's take a break. What're they going to do, send us away?":
            jump branch_2
        "Better to be safe there than dying out here. Let's get back to work.":
            jump branch_1_1
    