from pico2d import *
open_canvas()
grass = load_image('grass.png')
sprite1 = load_image('1.png')
sprite2 = load_image('2.png')
sprite3 = load_image('3.png')

x = 0
frame = 0

while x < 800:
    clear_canvas()
    grass.draw(400, 30)
    sprite1.clip_draw(frame * 587, 0, 587, 707, 150, 150, 200, 200)
    sprite2.clip_draw(frame * 587, 0, 587, 707, 350, 150, 200, 200)
    sprite3.clip_draw(frame * 587, 0, 587, 707, 550, 150, 200, 200)
    update_canvas()
    frame = (frame + 1) % 10
    x += 5
    delay(0.05)
    get_events()

close_canvas()