from pygame import *

window = display.set_mode((700,500))
display.set_caption('Догонялки')
background = transform.scale(image.load('background.png'),(700,500))
sprite1 = transform.scale(image.load('sprite1.png'),(50,50))
sprite2 = transform.scale(image.load('sprite2.png'),(50,50))
game = True
clock = time.Clock()

x1,y1 = 0,0
x2,y2 = 50,50    
speed = 5
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))
  
    

    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 <0:
        x1 -= speed
    if keys_pressed[K_RIGHT]:
        x1 += speed
    if keys_pressed[K_UP]:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1<400:
        y1 += speed
    if keys_pressed[K_a] and x2 <0:
        x2 -= speed
    if keys_pressed[K_d]:
        x2 += speed
    if keys_pressed[K_w]:
        y2 -= speed
    if keys_pressed[K_s]and y2<400:
        y2 += speed
    clock.tick(60)
    display.update()

#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"»