#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Jan 2023
# This program makes a simple shooting game

import ugame
import stage

def  game_scene():
    # this function is the main game game scene
    
    #image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("egg_collector_image_bank_test.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("egg_collector_image_bank_test.bmp")  

    # set the background to image 0 in the image bank
    #  and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    # add sprite
    chicken = stage.Sprite(image_bank_sprites, 2, 75, 112)

    # create a stage for the background to show up on 
    #  and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    # set the layers of all sprites, items show up in order
    game.layers = [chicken] + [background]

    # render all sprites
    # most likely you will only render the background once per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            print("A")
        if keys & ugame.K_O:
            print("B")
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        if keys & ugame.K_RIGHT:
            chicken.move(chicken.x + 1, chicken.y)
        if keys & ugame.K_LEFT:
            chicken.move(chicken.x - 1, chicken.y)
        if keys & ugame.K_UP:
            chicken.move(chicken.x, chicken.y - 1)
        if keys & ugame.K_DOWN:
            chicken.move(chicken.x, chicken.y + 1)

        # update game logic

        # redraw Sprite
        game.render_sprites([chicken])
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    game_scene()
