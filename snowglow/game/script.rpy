# The script of the game goes in this file.

#glossary code partial credit to philat on lemmasoft renai us forum
init python:
    def glossary_handler(target):
        x, y = renpy.get_mouse_pos()
        renpy.show_screen("glossary", target, x, y)
        renpy.restart_interaction()

    config.hyperlink_handlers["glossary"] = glossary_handler

    #TODO: make the glossary screen more aesthetic


#TODO: make a quick branch explaining the bug where stuff loops that unfinished branches jump to

default glossary_dict = {
'Elnaxanthine':'A mineral found in the local ice. An essential nutrient for survival in the cold. Its extraction is very complicated.',
'Quota':'Minimum volume of Elnaxanthine a team needs to harvest in a given expedition. If the quota is not met, exile is imminent.',
'Eolyusion': 'The spot where exiles are taken to.',
'Heda and Wren': 'Two other children that used to live at the orphanage. They signed up for the Elanxanthine expedition and failed to meet the quota.',
'Seolforstan': 'The only place you and your friends have ever known.'
}

#template: {a=glossary:Elnaxanthine}⫶🔻 Elnaxanthine{/a}
    
image ctc:
    #ctc code credit to CheeryMoya and OokamiKasumi lemmasoft renai us forum
    "gui/ctc_icon.png" with Dissolve(0.4), #This is your image
    subpixel True #This line makes sure that ATL is smooth 

    yalign 0.76 xalign 0.85 #Adjust these numbers to fit your own textbox
    linear 0.5 yalign 0.77
    linear 0.5 yalign 0.76
    
    repeat

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define o = Character("Osric", color="#af8a45", what_color="#f5d79f", ctc="ctc", ctc_position="fixed")
define w = Character("Wynfled", color="#0464ff", what_color="#bfd5f8", ctc="ctc", ctc_position="fixed")
define n = Character("Nightcumb", color="#ff19e8", what_color="#ffcafa", ctc="ctc", ctc_position="fixed")
define narrator = Character(what_italic = True, ctc="ctc", ctc_position="fixed")
default wynn_affec = 100
default os_affec = 60
default suspicion_list = []
define gui.text_font = "GlacialIndifference-Regular.otf"
define gui.text_instance = "light"
define gui.text_axis = {"width" : 125}
define gui.text_size = 35
 

label start:#MC mining ice with team

    play music [over_the_rise, ismere_theme] fadeout 1.0 fadein 1.0 loop volume 0.75
    play ambiance ambient_wind loop volume 0.1
    show mining site with dissolve
    with None
    "Before we begin, let's learn a bit more about you."
    define mc = Character("[nickname + ' (You)']", what_color="#bb799a", ctc="ctc", ctc_position="fixed")

    python:
        name = renpy.input("What's your name? (max 20 chars)", length=20, default="Maren Rime")
        name = name.strip().title()

        if not name:
            name = "Maren Rime"

        nickname = renpy.input("What nickname do you like to be called? (max 20 chars)", length=20, default="Mare")
        nickname = nickname.strip().title()
        if not nickname:
            nickname = "Mare"

    show wynfled normal at right
    mc "[glossary_dict['Quota']]"
    "This is Wynn (Wynfled). She's your best friend."
    hide wynfled
    show osric normal at left
    "This is Os (Osric). He's your other team-member for the {a=glossary:Elnaxanthine}⫶🔻 Elnaxanthine{/a} Elnaxanthine expedition."
    show wynfled sad at right
    w "I'm... so tired."
    "You look down at the shoddy pile of ice you've gathered."
    "There's definitely not enough Elnaxanthine in there to meet the quota."
    "You might as well give up at this rate."
    menu: 
        "We're still short on Elnaxanthine. Let's keep mining.":
            jump ch1_01a_keep_mining
        "...let's take a break.":
            jump ch1_01b_take_rest


label ch1_01a_keep_mining:
    w "How'd I get roped into this again?"
    show osric laughing
    o "We've got to meet the {a=glossary:Quota}🔻 quota{/a}, Wynn. We signed up for this, remember?"
    show wynfled angry
    w "Well, the quota's STUPID."
    show wynfled thinking
    w "Come to think of it, I haven't seen {a=glossary:Heda and Wren}⫶🔻 Heda and Wren{/a} since they were sent to {a=glossary:Eolyusion}⫶🔻 Eolyusion.{/a}"
    show osric normal
    menu:
        "They're never coming back. Don't you get it? It's permanent.":
            pass
        "Hey, I'm sure you're overthinking it...":
            jump ch1_con1a_mention_punishment
    show wynfled sad
    w "But that's just terrible!"
    show osric happy
    o "It's a punishment, Wynn. It's meant to set an example for all of us."
    o "So let's follow suit and work hard, ok?"
    jump ch1_01a1_1st_dig_fails


label ch1_01a1_1st_dig_fails:
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
    "You hammer your rod-needle into the ice, creating a rough circle outline against the smooth surface."
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
            jump ch1_01a1a_2nd_dig_succeeds
        "The punishment doesn't sound so bad after all...":
            jump ch1_01b_take_rest


label ch1_01a1a_2nd_dig_succeeds:
    show wynfled thinking
    show osric normal
    "The deadline is very soon, and you can all feel it."
    "Wynn's gaze is clearer and she's making less jokes now."
    "There are no words between you. You don't need them, having learnt to extract your whole lives."
    "You hammer a circle into the ice, and Os spreads the reagents more carefully this time."
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
            jump ch1_01a1a1_play_to_night
        "Wynn, one last push? We're on a roll!":
            jump ch1_01a1a2_wynn_works


label ch1_01a1a2_wynn_works:
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
            jump ch1_con01a1a2_wynn_hurts
        "Yeah, she should rest.":
            $ os_affec += 2
            show osric happy
            "Os seems to appreciate your gesture."
            jump branch_ch1_01a1a2a_dig_with_os


label branch_ch1_01a1a2a_dig_with_os:
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
            jump ch1_01a1a2a1_wynn_sneaks_away
        "Got it!":
            jump ch1_end01_explosion
    

label ch1_01a1a2a1_wynn_sneaks_away:
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
            jump ch1_01a1a2a1a_confront_wynn
        "*She must have her reasons for sneaking away, she knows what she's doing*":
            $ wynn_affec += 3
            jump ch1_01a1a2a1b_let_wynn_go
    


label ch1_01a1a2a1b_let_wynn_go:
    "You continue the conversation, pretending you saw nothing."
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
    show osric normal
    o "Well, it's not like we have a choice."
    menu:
        "Who wouldn't choose to help others?":
            show osric laughing
            o "We only signed up to get better experience. Don't lie."
            show osric happy
            mc "Caught me there."
            jump ch1_01a1a2a1b1_notice_time
        "Right. They've been lowering the minimum age too.":
            jump ch1_con01a1a2a1b_sus_sustainability

    
label ch1_01a1a2a1b1_notice_time:
    show osric normal
    "You end up doing more talking than working."
    "Even so, you collect enough ice to meet the quota."
    o "Say, hasn't Wynn been gone for quite a while?"
    menu:
        "Should we go search?":
            jump ch1_01a1a2a1b1_search_for_wynn
        "She'll probably be able to find her way back.":
            jump ch1_01a1a2a1b2_wait_it_out


label ch1_con01a1a2a1b_sus_sustainability:
    o "People have been dying and getting exiled left and right."
    "You tense up."
    mc "Well, that was a bit direct, wasn't it?"
    show osric angry
    o "Well, am I lying?"
    o "How long can they keep going until everyone's gone?"
    $ suspicion_list.append("The orphanage doesn't seem to care about sustainability, removing more people than it keeps or takes in.")
    mc "You wouldn't mention stuff like this if Wynn was here."
    show osric surprised
    o "You also noticed her sneaking off?"
    mc "O-oh. Um, yeah."
    show osric happy
    o "Looks like you're thinking along my lines."
    menu:
        "Well, you know how she'd react if we called her out.":
            show osric laughing
            $ os_affec += 10
            $ wynn_affec -= 6
            o "She does get like that."
            "You feel bad for talking about Wynn in this way, but your bond with Os seems to have grown over your secret."
        "We need to give her space. Even if it's a bit dangerous...":
            $ wynn_affec += 10
            o "...yeah. That's basically it."
    jump ch1_01a1a2a1b1_notice_time


label ch1_01a1a2a1b1_search_for_wynn:
    mc "But... where do you think she might be?"
    "You look around you. Gentle slopes stretch on and on, ice formation rolling softly down."
    o "I don't think she'd descend down a cliff alone."
    mc "Right, it'd be hard for her to find her way back, hm?"
    pass

label ch1_01a1a2a1b2_wait_it_out:
    #TODO: work on this branch
    pass


label ch1_01a1a2a1a_confront_wynn:
    show wynfled surprised at right
    show osric surprised at left
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
    "Osric looks hurt."
    show osric sad
    o "Then we'd be worried for the friend that means so much to us."
    show wynfled sad
    w "I..."
    mc "We're in this together, Wynn."
    show wynfled happy
    w "Thanks, guys."
    menu:
        "*Press her on where she was going*":
            jump ch1_01a1a2a1a_confront_wynn_1
        "*Focus on making Wynn feel happy and seen*":
            show wynfled laughing
            $ wynn_affec += 5
            "Wynn looks happy. You feel your bond growing slightly stronger."
            jump ch1_01a1a2a1a1_elna_sus

label ch1_01a1a2a1a1_elna_sus:
    #change the scene to show night-time at the glacier
    show osric happy at right
    show wynfled laughing at right
    "Wynn sits and cuddles her knees while watching you and Os work."
    o "[nickname], can you lift the ice just a bit higher so I can get underneath?"
    "You oblige."
    "He chips at it slowly and carefully."
    "After a while, you've finished lifting it."
    w "That one took a while."
    mc "I'd say we've worked quite hard today. What say you?"
    "You all stare at the heap of ice you've collected."
    show osric laughing
    o "That's enough Elnaxan to keep Seolforstan fed for months!"
    show wynfled thinking
    w "But what happens once we completely run out of Elnaxan near the orphanage?"
    mc "I guess we'd have to come out to wider Ismere more often, no?"
    #TODO: work on this branch


label ch1_end01_explosion:
    "You lean over, trying to focus."
    "{color=#f00}You accidentally tip out far too much reactant.{/color}"
    "{color=#f00}Out of the corner of your eye, you see Os drawing back the blast trigger of his pipe.{/color}"
    "{color=#f00}It's too late. You can feel it.{/color}"
    mc "{color=#f00}Wait! Os! Don't - !{/color}" with vpunch
    play music death_ost loop volume 0.75
    show death 1 with dissolve
    hide osric 
    "The next time you look up, it's the sky that covers your view."
    "The world blurs slowly."
    show screen vignette()
    "And then it hits you; you're about to die."
    "You're met with an instant clarity." with vpunch
    "Accidents like this happen all the time. You were prepared."
    "All in all, it wasn't a bad way to go out."
    "You leave the world free, and your soul soars, higher and higher."
    "Your mind gradually detaches from your body."
    $ MainMenu(confirm=False)()


label ch1_con01a1a2_wynn_hurts:
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
            jump branch_ch1_01a1a2a_dig_with_os
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

    jump branch_ch1_01a1a2a_dig_with_os


label ch1_01b_take_rest:
    "*time skip*"
    show wynfled laughing
    show osric laughing
    o "We've really done nothing, huh!"
    w "Should we go explore out there instead?"
    o "Wynn!"
    w "It's our first time this far from Seolforstan anyways..."
    menu:
        "I'm curious about what's out there too.":
            o "Really?"
            mc "Yeah, let's explore!"
            show osric normal
            o "Osric looks annoyed for a second."
            $ os_affec -= 1
            show osric happy
            w "YES!"
            jump ch1_con01b1_explore
        "It's dangerous out there. Let's stay here.":
            w "Haha, you're right!"
            "Wynn steals Os's shovel."
            jump ch1_01a1a1_play_to_night

    
label ch1_con01b1_explore:
    menu:
        "How are we going to find our way back later?":
            show osric normal
            o "That's a good point. We can't risk getting lost."
            w "What if we melt the ice every 50 meters?"
            mc "How would that work?"
            show wynfled thinking
            w "On the way back, we each travel in one direction to find the hole we made before."
            w "And one of us will find the hole. Then we all regroup and walk to the next meeting point."
            o "I like that idea!"
            menu:
                "That's too dangerous. We can't risk splitting up.":
                    show wynfled happy
                    w "What do you think then?"
                    "Your idea consists of using rope to connect each other while searching."
                    "Fundamentally, you'd have one person walking around the hole with everyone else covering a wide circle."
                    "It's much more time and energy consuming, but perhaps safer."
                    menu:
                        "On second thought, let's go with your strategy.":
                            show wynfled laughing
                            w "Hehe!"
                            $ wynn_affec += 2
                            define way_back = "searching"
                        "*Modify her plan*":
                            define way_back = "circling"
                            show osric laughing
                            o "Smart!"
                            $os_affec += 2
                "That's a good idea, Wynn!":
                    $ wynn_affec += 2
                    define way_back = "searching"
            mc "Looks like we've finished our plan. Let's go that way!"
        "Let's go that way!":
            define way_back = None
    w "Alright!"
    jump ch1_01b1_explore


label ch1_01b1_explore:

    show osric laughing at left
    show wynfled laughing at right
    "You walk west of the mining spot."
    w "Hey, after we get exiled, every day'll be full of this!"
    show osric normal
    "The mood seems to sober up, but Wynn doesn't realise it."
    mc "We're taking the exile quite lightly, huh."
    o "..."
    mc "Come on, let's hurry forward."
    "You walk on for what seems like ages."
    "Curiosity. Excitement. Awe."
    "All these emotions spur you on to keep going."
    hide osric 
    hide wynfled
    show wider ismere with dissolve
    play music wider_ismere loop volume 0.75 fadein 1.0
    show osric blushing at left
    show wynfled surprised at right
    o "It... it's beautiful."
    menu:
        "They've kept us from this all our lives.":
            $ os_affec += 3
            show wynfled sad
            show osric happy
            "Wynn looks pensive, while Os smiles cynically."
            o "We've really been missing out."
        "This doesn't even look real. It can't be real. It doesn't feel like it.":
            $ wynn_affec += 3
            show wynfled laughing
            w "Right? Seolforstan, it wasn't just a prison."
            w "It was a sealed box, and Nightcumb was the reflective coating, keeping all this beauty away from every reaching the inside."
            show osric happy
            o "Wynn! I didn't know you had that poetic spark in you..."
            show wynfled angry
            w "Say that again! I dare you!" with vpunch
    show wynfled happy
    show osric laughing
    mc "*You laugh hopelessly, then gaze at the expanse before you.*"
    "Your mind spins. You feel like you're entirely lost."
    "Rended apart, then whole again."
    show osric happy
    o "Earth to [nickname]..."
    #TODO: work on this branch


label ch1_01a1a1_play_to_night:
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
            jump ch1_con01a1a1_dismiss_punishment
        "*Say nothing and continue to rest*":
            jump ch1_01a1a1a_wasted_day


label ch1_01a1a1a_wasted_day:
    show wynfled happy at left
    show osric laughing at right
    "*Time skip*"
    "In the end, you three did exactly what you said you'd do: mess around instead of mining ice."
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
    jump ch1_01a1a1a1_regret


label ch1_01a1a1a1_regret:
    #put scene change to darker sky/overlay a darker colour to show that its nighttme
    show wynfled normal
    w "It's tidy now, but..."
    "All three of you are silent. In hindsight, maybe you shouldn't have messed around so much."
    "Finally, Osric breaks the silence."
    o "So tonight'll be our last night in Seolforstan, huh."
    mc "What do you mean?"
    w "Don't say that. Maybe... maybe somehow..."
    "Her words die down as she speaks."
    w "...maybe there's just really... really concentrated Elnaxan in the ice."
    mc "I wonder how they detect Elnaxan anyways?"
    o "That's up to the scientists to do. We don't have the privilege of knowing."
    show wynfled laughing
    w "Hey, think we could bribe a scient-AAAAAAA!"
    show nightcumb normal
    show wynfled scared
    w "He-hello, sir!" 
    n "Hello, children."
    "You all straighten your posture and avert your eyes as he walks over."
    n "And this is what you've produced today?"
    show osric sad
    o "Yes, sir. We... we understand that we didn't meet the quota."
    n "Ha! Ha! One can never be sure until one checks!"
    n "Well, I'll begin the process now."
    menu:
        "*Watch him measure the Elnaxan concentration*":
            jump ch1_01a1a1a1a_quota_check
        "*Plot with the others on what to do next*":
            hide nightcumb
            jump ch1_01a1a1a1b_plot_during_quota

label ch1_01a1a1a1a_quota_check:
    show nightcumb normal
    "You watch Nightcumb procure his elnaxanthine detector kit. He scatters green powder all over the ice."
    "The powder fully coats the ice's surface."
    "But that can't possibly be a reliable method, can it?"
    n "Hm. Dark green concentration."
    "His eyebrows go up."
    n "Kids, looks like you're very lucky! With this much ice you somehow managed to meet the quota."
    show wynfled surprised
    show osric surprised
    n "Well then, I'll be off! Stay here and wait so that all groups  together, alright?"
    n "And make sure not to wander too far, alright?"
    hide nightcumb 

label ch1_01a1a1a1b_plot_during_quota:
    show wynfled thinking
    show osric normal
    "You stand up. Wynn and Os follow you to a nearby stone formation. You climb up together."
    w "So, [nickname]? You've been thinking for a while, haven't you?"
    o "Do you really have a plan?"
    menu:
        "N-nevermind. I don't. Let's head back and pray for the best...":
            $ wynn_affec -= 1
            $ os_affec -= 1
            "Both your companions seem mildly disappointed."
            o "There's no way praying's going to work, [nickname]."
            show wynfled normal
            w "Well, do you have a plan? I don't."
            o "Damn it. Fine, let's head back then."
            jump ch1_01a1a1a1a_quota_check
        ""

    

label ch1_con1a_mention_punishment:
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
            jump ch1_01b_take_rest
        "Better to be safe there than perishing in the cold. Let's get back to work.":
            jump ch1_01a1_1st_dig_fails
    

label ch1_con01a1a1_dismiss_punishment:
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
            w "But that would mean {a=glossary:Heda and Wren}⫶🔻 Heda and Wren{/a}..."
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
            jump ch1_01a1a2_wynn_works
        "Os, loosen up! Even if we get exiled, it'll be the three of us, together, eh?":
            show osric angry
            show wynfled happy
            $ os_affec -= 3
            $ wynn_affec += 6
            "Wynn looks pleased that you value your friendship so much, while Os looks strangely bitter."
            jump ch1_01a1a1a_wasted_day
        "Whatever, I'm tired. Let's just forget about Elnaxan for a while.":
            show wynfled laughing
            w "Well, not the tired part, but hear! Hear!"
            jump ch1_01a1a1a_wasted_day