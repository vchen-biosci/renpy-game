init python:
    location_gallery = Gallery()
    location_gallery.transition = fade

    location_gallery.button("test_a")
    location_gallery.image("death 1")


screen gallery():
    tag menu
    add "death 1.png"
    frame:
        xalign 0.5
        yalign 1.0
        default page = 1
        hbox:
            textbutton "Page 1" action SetScreenVariable("page", 1)
            textbutton "Page 2" action SetScreenVariable("page", 2)
            
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        if page == 1:
            text "You are on page 1"
            grid 1 1:
                spacing 10
                vbox:
                    add location_gallery.make_button(name="test_a", unlocked="images/bg/wider ismere.png")
        else:
            text "You are on page 2"

    frame:
        xalign 1.0
        yalign 1.0
        xpadding 10
        ypadding 10 
        textbutton "Return" action Return()