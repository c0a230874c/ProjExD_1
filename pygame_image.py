import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_flip = pg.transform.flip(bg_img, True, False) #練習7
    kt_img = pg.image.load("fig/3.png") #練習2
    kt_img = pg.transform.flip(kt_img, True, False) #練習２
    img_rct = kt_img.get_rect() #練習8
    img_rct.center = 300, 200 #練習8
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        img_rct.move_ip((-1,0)) #演習1
        key_list = pg.key.get_pressed() #練習8
        if key_list[pg.K_UP]: #上移動
            img_rct.move_ip((0, -1)) 
        if key_list[pg.K_DOWN]: #下移動
            img_rct.move_ip((0, 1)) 
        if key_list[pg.K_RIGHT]: #右移動
            img_rct.move_ip((2, 0)) #演習1
        if key_list[pg.K_LEFT]: #左移動
            img_rct.move_ip((-1,0)) 
        x = -(tmr%3200) #練習7
        screen.blit(bg_img, [x, 0]) #練習6
        screen.blit(bg_flip, [x+1600, 0]) #練習7
        screen.blit(bg_img, [x+3200, 0]) #練習7
        screen.blit(bg_flip, [x+4800, 0]) #練習7
        screen.blit(kt_img, img_rct) #練習４
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()