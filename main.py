def on_button_pressed_a():
    basic.show_string("Eine geschichte")
    basic.show_string("Ja Ja")
    basic.pause(100)
    basic.show_string("Ja ja")
    basic.show_string("Pssst ")
    basic.show_string("Hört ihr etwas ?")
    basic.show_string("Nein! Ich auch nicht aber gerade das ist es ja")
    basic.show_string("Früher konnte ich mir immer ein paar autogramme ")
    basic.show_string("Ähh okay was sucht Jeff the Killer hier")
    basic.show_string("Killer: A ja")
    basic.show_icon(IconNames.HAPPY)
    basic.show_icon(IconNames.SAD)
    basic.show_icon(IconNames.SWORD)
    basic.show_icon(IconNames.SILLY)
    basic.show_icon(IconNames.ASLEEP)
    basic.show_string("Heeeeellllllp mmmeeeee")
    basic.show_icon(IconNames.MEH)
    basic.show_icon(IconNames.SKULL)
    basic.show_string("Das wars mit der Geschichte")
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    pass
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_b():
    basic.show_string("Musik")
    music.play_melody("C5 G C5 C C5 G C5 C ", 260)
    music.play_melody("C5 G C5 C C5 G C5 C ", 260)
    music.play_melody("C5 G C5 C C5 G C5 C ", 260)
    basic.pause(200)
    music.play_melody("C5 G C5 E E D F F ", 281)
    music.play_melody("C5 G C5 E E D F F ", 281)
    music.play_melody("C5 G C5 E E D F F ", 281)
    basic.pause(200)
    music.play_melody("C5 A C5 - G F A C5 ", 302)
    music.play_melody("C5 A C5 - G F A C5 ", 302)
    music.play_melody("C5 A C5 - G F A C5 ", 302)
    basic.pause(200)
    music.play_melody("F C5 E F G C5 E F ", 293)
    music.play_melody("F C5 E F G C5 E F ", 293)
    music.play_melody("F C5 E F G C5 E F ", 293)
    basic.pause(200)
    music.play_melody("C C5 C C5 C C5 C C5 ", 220)
    music.play_melody("C C5 C C5 C C5 C C5 ", 220)
    music.play_melody("C G E D F C5 C C5 ", 220)
    music.play_melody("C C5 C C5 C C5 C C5 ", 220)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    basic.show_string("Emote only")
    basic.show_icon(IconNames.HEART)
    basic.pause(100)
    basic.show_icon(IconNames.SMALL_HEART)
    basic.pause(100)
    basic.show_icon(IconNames.YES)
    basic.pause(100)
    basic.show_icon(IconNames.NO)
    basic.pause(100)
    basic.show_icon(IconNames.HAPPY)
    basic.pause(100)
    basic.show_icon(IconNames.SAD)
    basic.pause(100)
    basic.show_icon(IconNames.CONFUSED)
    basic.pause(100)
    basic.show_icon(IconNames.ANGRY)
    basic.pause(100)
    basic.show_icon(IconNames.ASLEEP)
    basic.pause(100)
    basic.show_icon(IconNames.SURPRISED)
    basic.pause(100)
    basic.show_icon(IconNames.SILLY)
    basic.clear_screen()
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

basic.show_string("2")
music.play_melody("C5 - C5 C C - - - ", 292)
basic.show_string("Server 2 wird gestartet")
basic.pause(100)
basic.show_leds("""
    . # # # .
    # # . . #
    # . # . #
    # . . . #
    . # # # .
    """)
basic.pause(100)
basic.show_string("Lade hex")
basic.show_string("Lade Koordinaten")
basic.pause(100)
basic.show_leds("""
    . # # # .
    # . # . #
    # . # . #
    # . . . #
    . # # # .
    """)
basic.pause(100)
basic.show_string("Lade Codes")
basic.show_string("Lade Audios")
basic.pause(100)
basic.show_leds("""
    . # # # .
    # . . # #
    # . # . #
    # . . . #
    . # # # .
    """)
basic.pause(100)
basic.show_string("Lade Emotes")
basic.pause(100)
basic.show_string("Fertig")
basic.show_icon(IconNames.YES)
basic.show_number(2)

def on_forever():
    basic.show_icon(IconNames.SURPRISED)
    basic.show_icon(IconNames.HAPPY)
    basic.show_string("Hallo oder auch servus wie es die Franken sagen ")
    basic.show_string("Häääääää")
    basic.show_icon(IconNames.CONFUSED)
    basic.show_string("Jaaaaaaa")
    basic.show_icon(IconNames.SAD)
    basic.show_string("A ja")
    basic.show_icon(IconNames.SWORD)
    basic.show_string("oh weh")
    basic.show_icon(IconNames.SKULL)
basic.forever(on_forever)
