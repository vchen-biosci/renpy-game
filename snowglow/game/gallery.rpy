init python:
    location_gallery = Gallery()
    location_gallery.transition = fade

    location_gallery.button("mining_site")
    location_gallery.image("images/bg/mining site.png")
    location_gallery.button("wider_ismere")
    location_gallery.image("images/bg/wider ismere.png")
    location_gallery.button("ismere_sky")
    location_gallery.image("images/bg/death 1.png")


screen gallery():
    tag menu
    add "images/gallery images/gallery_bg.png"
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
            grid 2 2:
                spacing 50
                vbox:
                    add location_gallery.make_button(name="mining_site", unlocked="images/gallery images/mining_site.png")
                    text "1: Mining Site"
                vbox:
                    add location_gallery.make_button(name="wider_ismere", unlocked="images/gallery images/wider_ismere.png")
                    text "2: Wider Ismere"
                vbox:
                    add location_gallery.make_button(name="ismere_sky", unlocked="images/gallery images/ismere_sky.png")
                    text "3: Ismere's Sky"
                vbox:
                    add location_gallery.make_button(name="mining_site", unlocked="images/gallery images/mining_site.png")
                    text "1: Mining site"
                    
        else:
            text "You are on page 2"

    frame:
        xalign 1.0
        yalign 1.0
        xpadding 10
        ypadding 10 
        textbutton "Return" action Return()