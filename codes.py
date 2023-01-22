#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Jan 2023
# This program makes a simple shooting game

import constants
import ugame
import stage

def menu_scene():
    # this function is the main game game scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("egg_collector_image_bank_test.bmp")

    # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20,10)
    text1.text("Egg Collecter")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # set the background to image 0 in the image bank
    background = stage.Grid(image_bank_background, constants.SCREEN_X,
                            constants.SCREEN_Y)

    # list to store the generated plants
    plants = []

    # procedurally generates the grass at the bottom of the screen
    for grass_number in range(0, 10):
        a_single_grass = stage.Sprite(image_bank_2, 5, constants.GRASS_POINT
                                      + increaser, 128 - 16)
        plants.append(a_single_grass)
        increaser += 16

    # create a stage for the background to show up on
    #  and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites, items show up in order
    game.layers = text + plants + [background]
    # render the background and initial lcation of sprite list
    # most likely you will only render the background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # A button to fire
        if keys & ugame.K_START != 0:
            game_scene

        # update game logic
        # redraw Sprites
        game.tick()  # wait until refresh rate finishes

def  game_scene():
    # this function is the main game game scene
    
    #image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("egg_collector_image_bank_test.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("egg_collector_image_bank_test.bmp")  

    # buttons that you want to keep state nformation on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("bloop.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # set the background to image 0 in the image bank
    #  and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    # add sprite
    chicken = stage.Sprite(
            image_bank_sprites, 2, 75, 112, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    egg = stage.Sprite(
        image_bank_sprites,
        3,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # create a stage for the background to show up on 
    #  and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    # set the layers of all sprites, items show up in order
    game.layers = [egg] + [chicken] + [background]

    # render all sprites
    # most likely you will only render the background once per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            if chicken.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                chicken.move(chicken.x + 1, chicken.y)
            else:
                chicken.move(constants.SCREEN_X - constants.SPRITE_SIZE, chicken.y)
        if keys & ugame.K_LEFT:
            if chicken.x >= 0:
                chicken.move(chicken.x -1, chicken.y)
            else:
                chicken.move(0, chicken.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass

        # update game logic

        # redraw Sprite
        game.render_sprites([egg] + [chicken])
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    menu_scene()
