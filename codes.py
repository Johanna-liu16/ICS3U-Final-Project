#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Jan 2023
# This program makes a simple shooting game

import constants
import ugame
import random
import stage
import time
import supervisor

def splash_scene():
    # this function is the main game game scene

    # get sound ready
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.mute(True)
    sound.play(coin_sound)

    # image banks for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # set the background to image 0 in the image bank
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y
    )

    # create a stage for the background to show up on
    #  and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites, items show up in order
    game.layers = [background]
    # render the background and initial lcation of sprite list
    # most likely you will only render the background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # Wait for 1 sec
        time.sleep(1.0)
        menu_scene()

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
    menu_background = stage.Grid(image_bank_background, constants.SCREEN_X,
                            constants.SCREEN_Y)

    sprites = []
    chicken = stage.Sprite(image_bank_background, 1, 50, 55)
    sprites.insert(0, chicken)

    eggs = []
    egg = stage.Sprite(image_bank_background, 3, 75, 55)
    eggs.insert(0, egg)


    # create a stage for the background to show up on
    #  and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites, items show up in order
    game.layers = sprites + eggs + text + [menu_background]
    # render the background and initial lcation of sprite list
    # most likely you will only render the background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # A button to fire
        if keys & ugame.K_START != 0:
            game_scene()

        # update game logic
        # redraw Sprites
        game.tick()  # wait until refresh rate finishes

def  game_scene():
    # this function is the main game game scene

    # vars
    score = 0
    egg_count = 0
    bomb_count = 0
    lives = 3

    score_text = stage.Text(width=29, height=12)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    lives_text = stage.Text(width=29, height=12)
    lives_text.clear()
    lives_text.cursor(14, 0)
    lives_text.move(1, 1)
    lives_text.text("Lives: {0}".format(lives))

    def show_egg(): 
        # this function take an alien from off screen and moves it on screen
        for egg_number in range(len(eggs)):
            if eggs[egg_number].x < 0:
                eggs[egg_number].move(
                    random.randint(
                        0 + constants.SPRITE_SIZE,
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )
                break

    def show_bomb(): 
        # this function take an alien from off screen and moves it on screen
        for bomb_number in range(len(bombs)):
            if bombs[bomb_number].x < 0:
                bombs[bomb_number].move(
                    random.randint(
                        0 + constants.SPRITE_SIZE,
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )
                break

    #image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("egg_collector_image_bank_test.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("egg_collector_image_bank_test.bmp")  

    # buttons that you want to keep state nformation on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    bloop_sound = open("bloop.wav", "rb")
    boom_sound = open("boom.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(True)

    eggs = []
    for egg_number in range(constants.TOTAL_NUMBER_OF_EGGS):
        a_single_egg = stage.Sprite(
            image_bank_sprites,
            3,
            constants.OFF_SCREEN_X,
            constants.OFF_SCREEN_Y,
        )
        eggs.append(a_single_egg)
    # place 1 alien on the screen
    show_egg()

    bombs = []
    for bomb_number in range(constants.TOTAL_NUMBER_OF_BOMBS):
        a_single_bomb = stage.Sprite(
            image_bank_sprites,
            4,
            constants.OFF_SCREEN_X,
            constants.OFF_SCREEN_Y,
        )
        bombs.append(a_single_bomb)
    # place 1 alien on the screen
    show_bomb()

    # set the background to image 0 in the image bank
    #  and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    increaser = 0
    plants = []
    for grass_number in range(0, 10):
        a_single_grass = stage.Sprite(image_bank_background, 5, constants.GRASS_POINT
                                      + increaser, 128 - 16)
        plants.append(a_single_grass)
        increaser += 16

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
    game.layers = [lives_text] + [score_text] + bombs + eggs + [chicken] + plants + [background]

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

# each frame move the eggs down, that are on the screen
        for egg_number in range(len(eggs)):
            if eggs[egg_number].x > 0:
                eggs[egg_number].move(
                    eggs[egg_number].x,
                    eggs[egg_number].y + constants.EGG_SPEED,
                )
                if eggs[egg_number].y > constants.SCREEN_Y:
                    eggs[egg_number].move(
                        constants.OFF_SCREEN_X,
                        constants.OFF_SCREEN_Y,
                    )
                    show_egg()

# each frame move the bombs down, that are on the screen
        for bomb_number in range(len(bombs)):
            if bombs[bomb_number].x > 0:
                bombs[bomb_number].move(
                    bombs[bomb_number].x,
                    bombs[bomb_number].y + constants.EGG_SPEED,
                )
                if bombs[bomb_number].y > constants.SCREEN_Y:
                    bombs[bomb_number].move(
                        constants.OFF_SCREEN_X,
                        constants.OFF_SCREEN_Y,
                    )
                    show_bomb()

        # each frame check if any eggs are touching the chicken
        for egg_number in range(len(eggs)):
            if eggs[egg_number].x > 0:
                if stage.collide(
                    eggs[egg_number].x + 1,
                    eggs[egg_number].y,
                    eggs[egg_number].x + 15,
                    eggs[egg_number].y + 15,
                    chicken.x,
                    chicken.y,
                    chicken.x + 15,
                    chicken.y + 15,
                ):
                    eggs[egg_number].move(
                    constants.OFF_SCREEN_X,
                    constants.OFF_SCREEN_Y,
                    )
                    sound.stop()
                    sound.play(bloop_sound)
                    show_egg()
                    show_egg()
                    egg_count = egg_count + 1
                    score += 1
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))

        # each frame check if any bombs are touching the chicken
        for bomb_number in range(len(bombs)):
            if bombs[bomb_number].x > 0:
                if stage.collide(
                    bombs[bomb_number].x + 1,
                    bombs[bomb_number].y,
                    bombs[bomb_number].x + 15,
                    bombs[bomb_number].y + 15,
                    chicken.x,
                    chicken.y,
                    chicken.x + 15,
                    chicken.y + 15,
                ):
                    bombs[bomb_number].move(
                    constants.OFF_SCREEN_X,
                    constants.OFF_SCREEN_Y,
                    )
                    sound.stop()
                    sound.play(boom_sound)
                    show_bomb()
                    show_bomb()
                    bomb_count = bomb_count + 1
                    score -= 1
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))
                    lives -= 1
                    lives_text.clear()
                    lives_text.cursor(14, 0)
                    lives_text.move(1, 1)
                    lives_text.text("Lives: {0}".format(lives))
                    if lives == 0:
                        game_over_scene(score)

        # redraw Sprite
        game.render_sprites(bombs + eggs + [chicken])
        game.tick()  # wait until refresh rate finishes


def game_over_scene(score):
    # this function is the game over scene

    # turn off sound from last scene
    sound = ugame.audio
    sound.stop()

    # image banks for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the image
    background = stage.Grid(
        image_bank_2,
        constants.SCREEN_GRID_X,
        constants.SCREEN_GRID_Y,
    )

    # add text objects
    text = []
    text1 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text1.move(22, 20)
    text1.text("Final Score: {:0>2d}".format(score))
    text.append(text1)

    text2 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text2.move(43, 60)
    text2.text("GAME OVER")
    text.append(text2)

    text3 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    text3.move(32, 110)
    text3.text("PRESS SELECT")
    text.append(text3)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
    
        # Start button select
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()
        game.tick()

    
if __name__ == "__main__":
    splash_scene()