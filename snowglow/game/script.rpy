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
 

label start:#MC mining ice with team

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
    "This is Os (Osric). He's your other team-member for the Elnaxanthine expedition."
    show wynfled sad at right
    w "I'm... so tired."
    "You look down at the shoddy pile of ice you've gathered."
    "There's definitely not enough Elnaxanthine in there to meet the quota."
    "You might as well give up at this rate."
    menu: 
        "We're still short on Elnaxan. Let's keep mining.":
            jump branch_1
        "...let's take a break.":
            jump branch_2


label branch_1:
    w "How'd I get roped into this again?"
    show osric laughing
    o "We've got to meet the quota, Wynn. We signed up for this, remember?"
    show wynfled angry
    w "Well, the quota's STUPID."
    show wynfled thinking
    w "Come to think of it, I haven't seen Heda and Wren since they were sent to Eolyusion."
    show osric normal
    menu:
        "They're never coming back. Don't you get it? It's permanent.":
            pass
        "Hey, I'm sure you're overthinking it...":
            jump con_branch_1
    show wynfled sad
    w "But that's just terrible!"
    show osric happy
    o "It's a punishment, Wynn. It's meant to set an example for all of us."
    o "So let's follow suit and work hard."
    jump branch_1_1


label branch_1_1:
    "The cold bites at your bare fingers, but none of you complain."
    "The faster you get this part done, the better."
    show wynfled thinking
    w "Os, some of the reducing agent please."
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
    "The deadline is very soon, and you can all feel it."
    "Wynn's gaze is clearer and she's making less jokes now."
    "There are no words between you. You don't need them, having learnt to extract your whole lives."
    "The shape is hammered in the ice, and Os spreads the reagents more carefully this time."
    "You all nod at each other."
    "BAM!"
    show wynfled happy
    show osric laughing
    "The ice block makes a hissing sound and slides out of the cap."
    w "woo... WOAHHH!!!"
    o "..."
    mc "YES! Ugh, my hands are freezing."
    "You all put your mitts on."
    show wynfled laughing
    w "I know, right? Ahhhh, it's so warmmm! It feels like I'm melting."
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
            jump branch_3
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
            show osric happy
            "Os seems to appreciate your gesture."
            jump branch_1_3_1


label branch_1_3_1:
    show wynfled sad
    show osric happy
    w "I feel really bad to sit out like this..."
    mc "Your safety comes first, Wynn."
    show wynfled happy
    w "I really appreciate you guys."
    hide wynfled
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
            $ wynn_affec += 3
    mc "Nah, it's all thanks to our hard work, definitely!"
    "You tip the red powder evenly and carefully."
    mc "Wynn does have a point though. Seolforstan really is a prison, hm?"
    show osric normal
    o "What would the alternative be? Dying out in the cold?"
    mc "I suppose. We're lucky, you're right."
    "Os sighs."
    show osric happy
    o "I get what you mean. I've always wondered what's farther out there in the world."
    mc "At least we get get the chance to contribute to society like this."
    o "Once a month..."
    show osric laughing
    "You laugh together."


label branch_1_3_1_3:
    show wynfled surprised
    show osric surprised
    "Wynn turns around."
    o "Where were you going?"
    show wynfled sad
    w "Sorry. I'll sit back down."
    show osric angry
    o "Where were you going, Wynn? I'm asking."
    show wynfled angry
    w "And I'm obliged to answer, huh?"
    mc "It's dangerous heading out alone. What if you got lost?"
    $ wynn_affec -= 10
    $ os_affec -= 5
    w "And if I got lost? Then? Huh?"


label branch_1_3_1_2:
    "You lean over, trying to focus."
    "{color=#f00}You accidentally tip out far too much reactant.{/color}"
    "{color=#f00}Out of the corner of your eye, you see Os drawing back the blast trigger of his pipe.{/color}"
    "{color=#f00}It's too late. You can feel it.{/color}"
    mc "{color=#f00}Wait! Os! Don't - !{/color}"


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
            show osric laughing
            $ os_affec += 2
            $ wynn_affec -= 1
            "Os seems to appreciate your considerosity, while Wynn seems to feel patronised."
            jump branch_1_3_1
        "*gloss over Os's question*":
            show osric angry
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


label branch_3:
    show wynfled happy at right
    w "Osriccc! Come get it! [nickname], quit scowling!"
    "Wynfled waves Os's shovel around, giggling."
    show osric happy at left
    o "...Give it here."
    w "No, no, I've got it."
    mc "Should we really be playing around right now?"
    show wynfled laughing at left
    show osric laughing at right
    w "Tch, go mine alone for all we care if you're that set on it!"
    w "Wait, no! Ahhhh! [nickname], catch!" 
    "You catch the shovel."
    w "Oh nooo, where'd your shovel go, Os?"
    show osric happy
    o "You serious?"

    "You grow slightly restless looking at the pile."
    "You really don't have enough ice to guarantee anything."
    menu:
        "Hey, we might not have met the Elnaxan quota yet.":
            jump con_branch_3_to_3
        "*Say nothing and continue to rest*":
            jump branch_3_1


label branch_3_1:
    show wynfled happy at left
    show osric laughing at right
    "You three did exactly what you said you'd do: mess around instead of mining ice."
    "But now as the sky grows darker, you feel a growing sense of unease."
    menu:
        "Should we mine a bit more before Nightcumb comes?":
            show wynfled normal
            show osric happy
            w "Fat chance of that now..."
            o "We probably should have done more work."
            "Os looks just as uneasy as you do."
            show wynfled thinking
            w "The pile DOES look a bit small..."
            o "Well, all we can do is wait."
            "You all decide to play again, distracting yourselves from the mild sense of impending doom."
        "*Tuck the sense of unease away*":
            "Yeah, that's right. You decide it's too late to do anything anyways."
    "You mess around more until night falls over the glacier."
    show wynfled scared 
    show osric normal
    w "Nightcumb's about to come, isn't he?"
    mc "Q-quick, let's at least pile it up..."
    "Os grabs his shovel and begins hauling ice onto the wooden carrier."
    "You all work together, but you certainly haven't met the quota."
    jump branch_3_2


label branch_3_2:
    pass


label con_branch_1_to_2:
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
    

label con_branch_3_to_3:
    show osric normal
    "Os glances down at the pile too."
    o "Right, we might not meet the quota."
    show wynfled happy
    w "So what?? Heck, I want to get the punishment! Exploring wider Ismere sounds so cool!"
    show osric happy
    o "Exploring permanently?"
    show wynfled laughing
    w "Yeah, without anyone watching us. Doesn't that sound cool?"
    menu:
        "But nobody survives alone. Especially not outside of Seolforstan.":
            show wynfled sad
            w "But that would mean Heda and Wren..."
            "You remain silent."
            show osric normal
            "Os shuffles his feet."
            o "Yeah, let's get back to work."
            show wynfled surprised
            w "My hands are really going to shrivel up if I take my mitts off again!"
            menu: 
                "You were messing around with the shovel just fine earlier...":
                    show wynfled sad
                    $ wynn_affec -= 3
                    "Wynn looks hurt, perhaps feeling unheard. You feel your bond drifting slightly."
                "C'mon, one last push?":
                    show wynfled laughing
                    show osric laughing
                    $ wynn_affec += 2
                    $ os_affec += 2
                    "Both Wynn and Osric seem grateful that you got them back on track."
            jump branch_1_3
        "Os, loosen up! Even if we get exiled, it'll be the three of us, together, eh?":
            show osric angry
            show wynfled happy
            $ os_affec -= 3
            $ wynn_affec += 6
            "Wynn looks pleased that you value your friendship so much, while Os looks strangely bitter."
            jump branch_3_1
        "Whatever, I'm tired. Let's just forget about Elnaxan for a while.":
            show wynfled laughing
            w "Well, not the tired part, but hear! Hear!"
            jump branch_3_1