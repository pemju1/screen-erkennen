import pygame as py
import os
import pixel 


def add_pixel():
    index = 0
    for i in range(50):
        for j in range(50):
            pixel_group.add(pixel.Pixel(j*grid_size,i*grid_size,int(start_screen[index])))
            index += 1



py.init()

cwd = os.getcwd()
cwd = cwd.replace('\code','')
cwd += '/'


clock = py.time.Clock()
test_font = py.font.Font(cwd+'Pixeltype.ttf', 50)

grid_size = 15
screen = py.display.set_mode((grid_size*50,grid_size*55))
screen.fill((102, 98, 93))

pixel_group = py.sprite.Group()

start_screen = []
for i in range(50):
    for j in range(50):
        start_screen.append(255)

add_pixel()

current_screen = []
for i in range(50):
    for j in range(50):
        current_screen.append(255)


reset_button_image = py.Surface([7*grid_size, 3*grid_size])     #erzeugt leere Leinwand
reset_button_image.fill((40, 125, 94))
reset_button_rect = reset_button_image.get_rect(topleft=(1*grid_size, 51*grid_size))
screen.blit(reset_button_image, reset_button_rect)

reset_text_surf = test_font.render('Reset', False, 'black')
reset_text_surf = py.transform.scale(reset_text_surf, (7*grid_size, 3*grid_size))
reset_text_rect = reset_text_surf.get_rect(topleft = (1*grid_size+3, 51*grid_size+7))
screen.blit(reset_text_surf,reset_text_rect)

appendlist_buton_surf = py.Surface([7*grid_size, 3*grid_size])  #speichert was derzeit zu sehen ist
appendlist_buton_surf.fill((40, 125, 94))
appendlist_buton_rect = appendlist_buton_surf.get_rect(topleft=(40*grid_size, 51*grid_size))
screen.blit(appendlist_buton_surf, appendlist_buton_rect)

appendlist_text_surf = test_font.render('append', False, 'black')
appendlist_text_surf = py.transform.scale(appendlist_text_surf, (7*grid_size, 3*grid_size))
appendlist_text_rect = appendlist_text_surf.get_rect(topleft = (40*grid_size+1, 51*grid_size+2))
screen.blit(appendlist_text_surf,appendlist_text_rect)

read_buton_surf = py.Surface([7*grid_size, 3*grid_size])        #gibt gespeichertes wieder
read_buton_surf.fill((40, 125, 94))
read_buton_rect = read_buton_surf.get_rect(topleft=(20*grid_size, 51*grid_size))
screen.blit(read_buton_surf, read_buton_rect)

read_text_surf = test_font.render('read', False, 'black')
read_text_surf = py.transform.scale(read_text_surf, (7*grid_size, 3*grid_size))
read_text_rect = read_text_surf.get_rect(topleft = (20*grid_size+1, 51*grid_size+5))
screen.blit(read_text_surf,read_text_rect)

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        if event.type == py.MOUSEBUTTONDOWN:
                if reset_button_rect.collidepoint(event.pos):
                    pixel_group.empty()
                    add_pixel()
                    current_screen = start_screen.copy()
        if event.type == py.MOUSEBUTTONDOWN:
                if appendlist_buton_rect.collidepoint(event.pos):
                    with open(cwd+'Test.txt', 'w') as filehandle:
                        for current_screen in current_screen:
                            filehandle.write('%s\n' % str(current_screen))
                    current_screen = start_screen.copy()

        if event.type == py.MOUSEBUTTONDOWN:
                if read_buton_rect.collidepoint(event.pos):
                    pixel_group.empty()
                    current_screen = []

                    with open(cwd+'Test.txt', 'r') as filehandle:
                        for line in filehandle:
                            currentnum = line[:-1]
                            current_screen.append(int(currentnum))
                        
                        index = 0
                    for i in range(50):
                        for j in range(50):
                            pixel_group.add(pixel.Pixel(j*grid_size,i*grid_size,int(current_screen[index])))
                            index += 1

        keys = py.key.get_pressed() 
        if keys[py.K_1] or keys[py.K_2] or keys[py.K_3] or keys[py.K_4] or keys[py.K_5] or keys[py.K_6] or keys[py.K_7] or keys[py.K_8]:
            pixel_group.empty()
            current_screen = []
            if keys[py.K_1]: bild = 'Bilder/viereck_1.txt'
            if keys[py.K_2]: bild = 'Bilder/viereck_2.txt'
            if keys[py.K_3]: bild = 'Bilder/viereck_3.txt'
            if keys[py.K_4]: bild = 'Bilder/viereck_4.txt'
            if keys[py.K_5]: bild = 'Bilder/kreis_1.txt'
            if keys[py.K_6]: bild = 'Bilder/kreis_2.txt'
            if keys[py.K_7]: bild = 'Bilder/kreis_3.txt'
            if keys[py.K_8]: bild = 'Bilder/kreis_4.txt'
            with open(cwd+bild, 'r') as filehandle:
                        for line in filehandle:
                            currentnum = line[:-1]
                            current_screen.append(int(currentnum))
                        index = 0
            for i in range(50):
                for j in range(50):
                    pixel_group.add(pixel.Pixel(j*grid_size,i*grid_size,int(current_screen[index])))
                    index += 1

    pixel_group.draw(screen)
    pixel_group.update(current_screen)  
    

    py.display.update()
    clock.tick(60) 