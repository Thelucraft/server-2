input.onButtonPressed(Button.A, function () {
    basic.showString("Eine geschichte")
    basic.showString("Ja Ja")
    basic.pause(100)
    basic.showString("Ja ja")
    basic.showString("Pssst ")
    basic.showString("Hört ihr etwas ?")
    basic.showString("Nein! Ich auch nicht aber gerade das ist es ja")
    basic.showString("Früher konnte ich mir immer ein paar autogramme ")
    basic.showString("Ähh okay was sucht Jeff the Killer hier")
    basic.showString("Killer: A ja")
    basic.showIcon(IconNames.Happy)
    basic.showIcon(IconNames.Sad)
    basic.showIcon(IconNames.Sword)
    basic.showIcon(IconNames.Silly)
    basic.showIcon(IconNames.Asleep)
    basic.showString("Heeeeellllllp mmmeeeee")
    basic.showIcon(IconNames.Meh)
    basic.showIcon(IconNames.Skull)
    basic.showString("Das wars mit der Geschichte")
    basic.showIcon(IconNames.Happy)
})
input.onPinPressed(TouchPin.P2, function () {
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.showLeds(`
        . # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.showLeds(`
        . . # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.showLeds(`
        . . . # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.showLeds(`
        . . . . #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.showLeds(`
        . . . . .
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.showLeds(`
        . . . . .
        # # # # .
        # # # # .
        # # # # #
        # # # # #
        `)
    basic.showLeds(`
        . . . . .
        # # # # .
        # # # # .
        # # # # .
        # # # # .
        `)
    basic.showLeds(`
        . . . . .
        # # # # .
        # # # # .
        # # # # .
        # # . . .
        `)
    basic.showLeds(`
        . . . . .
        # # # # .
        # # # # .
        # # # # .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        # # # # .
        . # # # .
        . # # # .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . # # .
        . # # # .
        . # # # .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
})
input.onButtonPressed(Button.B, function () {
    basic.showString("Musik")
    music.playMelody("C5 G C5 C C5 G C5 C ", 260)
    music.playMelody("C5 G C5 C C5 G C5 C ", 260)
    music.playMelody("C5 G C5 C C5 G C5 C ", 260)
    basic.pause(200)
    music.playMelody("C5 G C5 E E D F F ", 281)
    music.playMelody("C5 G C5 E E D F F ", 281)
    music.playMelody("C5 G C5 E E D F F ", 281)
    basic.pause(200)
    music.playMelody("C5 A C5 - G F A C5 ", 302)
    music.playMelody("C5 A C5 - G F A C5 ", 302)
    music.playMelody("C5 A C5 - G F A C5 ", 302)
    basic.pause(200)
    music.playMelody("F C5 E F G C5 E F ", 293)
    music.playMelody("F C5 E F G C5 E F ", 293)
    music.playMelody("F C5 E F G C5 E F ", 293)
    basic.pause(200)
    music.playMelody("C C5 C C5 C C5 C C5 ", 220)
    music.playMelody("C C5 C C5 C C5 C C5 ", 220)
    music.playMelody("C G E D F C5 C C5 ", 220)
    music.playMelody("C C5 C C5 C C5 C C5 ", 220)
})
input.onPinPressed(TouchPin.P1, function () {
    basic.showString("Emote only")
    basic.showIcon(IconNames.Heart)
    basic.pause(100)
    basic.showIcon(IconNames.SmallHeart)
    basic.pause(100)
    basic.showIcon(IconNames.Yes)
    basic.pause(100)
    basic.showIcon(IconNames.No)
    basic.pause(100)
    basic.showIcon(IconNames.Happy)
    basic.pause(100)
    basic.showIcon(IconNames.Sad)
    basic.pause(100)
    basic.showIcon(IconNames.Confused)
    basic.pause(100)
    basic.showIcon(IconNames.Angry)
    basic.pause(100)
    basic.showIcon(IconNames.Asleep)
    basic.pause(100)
    basic.showIcon(IconNames.Surprised)
    basic.pause(100)
    basic.showIcon(IconNames.Silly)
    basic.clearScreen()
})
basic.showString("2")
music.playMelody("C5 - C5 C C - - - ", 292)
basic.showString("Server 2 wird gestartet")
basic.pause(100)
basic.showLeds(`
    . # # # .
    # # . . #
    # . # . #
    # . . . #
    . # # # .
    `)
basic.pause(100)
basic.showString("Lade hex")
basic.showString("Lade Koordinaten")
basic.pause(100)
basic.showLeds(`
    . # # # .
    # . # . #
    # . # . #
    # . . . #
    . # # # .
    `)
basic.pause(100)
basic.showString("Lade Codes")
basic.showString("Lade Audios")
basic.pause(100)
basic.showLeds(`
    . # # # .
    # . . # #
    # . # . #
    # . . . #
    . # # # .
    `)
basic.pause(100)
basic.showString("Lade Emotes")
basic.pause(100)
basic.showString("Fertig")
basic.showIcon(IconNames.Yes)
basic.showNumber(2)
basic.forever(function () {
    basic.showIcon(IconNames.Surprised)
    basic.showIcon(IconNames.Happy)
    basic.showString("Hallo oder auch servus wie es die Franken sagen ")
    basic.showString("Häääääää")
    basic.showIcon(IconNames.Confused)
    basic.showString("Jaaaaaaa")
    basic.showIcon(IconNames.Sad)
    basic.showString("A ja")
    basic.showIcon(IconNames.Sword)
    basic.showString("oh weh")
    basic.showIcon(IconNames.Skull)
})
