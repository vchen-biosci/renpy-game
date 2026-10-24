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
    show osric laughing
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
        "Wynn, one last push? We're on a roll!":
            jump branch_1_3

label branch_1_3:
    show osric sad
    "Wynn sniffs and casts you a sad glance, but doesn't resist."
    "You all know that it's for the better."
    show osric normal
    menu: 
        "Sorry, Wynn.":
            $ wynn_affec += 5
            show wynfled laughing
            w "I was just joking, but awwww!"
            "Your bond with Wynn seems to have grown stronger."
        "Good idea, Os!":
            $ os_affec += 5
            show osric laughing
            o "Wynn's the one being strong and pushing through."
            "Your bond with Os seems to have grown stronger."
    show wynfled happy
    show osric surprised
    w "Hey, let's all switch places. My legs are dyinggg!"
    show wynfled happy at left
    show osric happy at right
    o "Good idea. [nickname], it looks like we can do this one without Wynn."
    show osric normal 
    o "Should we let her rest?"
    menu:
        "I think we need her for this one.":
            o "Fair enough."
            $ wynn_affec += 1
            "Wynn seems to appreciate your self-confidence."
            jump branch_1_3_2
        "Yeah, she should rest.":
            $ os_affec += 2
            "Os seems to appreciate your gesture."
            jump branch_1_3_1


label branch_1_3_1:
    show wynfled sad
    w "I feel really bad to sit out like this..."
    mc "Your safety comes first, Wynn."
    show wynfled happy
    w "I really appreciate you guys."
    hide wynfled
    show osric happy
    o "Ok, [nickname] - can you try leaning over and pouring both sides at once?"
    menu:
        "Then it won't be evenly spread.":
            jump branch_1_3_1_1
        "Got it!":
            jump branch_1_3_1_2
    
label branch_1_3_1_1:
    show osric laughing at center
    o "Good point!"
    mc "Ok, just one more small tip, like this..."
    o "It's good we're avoiding punishment today, honestly."
    mc "Right? I'm all for adventure, but unnecessary disobedience is just bad for us."
    show osric happy 
    o "We got pretty lucky with the ice."
    "Out of the the corner of your eye, you spot Wynn walking away secretively."
    menu:
        "Where are you going, Wynn?":
            pass
        "*She must have her reasons for sneaking away, she knows what she's doing*":
            pass
    mc "Nah, it's all thanks to our hard work, definitely!"
    "You tip the red powder evenly and carefully."
    mc "Wynn does have a point though. Seolforstan really is a prison, hm?"
    show osric normal
    o "What would the alternative be? Dying out in the cold?"
    mc "I suppose. We're lucky, you're right."
    "Os sighs."
    o "I get what you mean. I've always wondered what's farther out there in the world."

    

label branch_1_3_1_2:
    "You lean over, trying to focus."
    "You accidentally tip out far too much reactant."
    "Out of the corner of your eye, you see Os drawing back the blast trigger of his pipe."
    "It's too late. You can feel it."
    mc "Wait! Os! Don't - !"


label branch_1_3_2:
    show wynfled sad
    "Wynn bites her lip as she takes her glove back off."
    mc "Wynn, hang in there!"
    show wynfled happy 
    w "O-oh, don't worry about me!!!"
    o "You sure we need her for this?"
    show wynfled laughing
    w "Really, I was just joking earlier."
    menu:
        "Wynn, you know what? Take a break. We can tell you're hurting.":
            $ os_affec += 2
            $ wynn_affec -= 1
            "Os seems to appreciate your considerosity, while Wynn seems to feel patronised."
            jump branch_1_3_1
        "*gloss over Os's question*":
            $ os_affec -= 20
            $ wynn_affec += 5
            "Os looks incredibly angry at your inconsideration, while Wynn seems to slightly appreciate your diminishing of the ordeal."
    mc "5 more minutes, 5 more minutes."
    w "..."
    o "..."
    "Both your companions seem uncomfortable. The atmosphere is tense, after all."
    menu:
        "I'm sorry, guys. I'm really sorry. Let's let Wynn sit out.":
            $ os_affec -= 10
            "Os seems to lose more respect for your surface-level consideration."
        "*Look at Wynn and grow concerned, then adamantly request she sit out*":
            $ os_affec += 10
            "Os seems to realise that you do have some humanity in you after all."

    jump branch_1_3_1


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
        "Better to be safe there than perishing in the cold. Let's get back to work.":
            jump branch_1_1
    