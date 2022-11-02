import pygame, time, random
pygame.init()

def snake(xr, yr, screen, snake_body, size):
    Green1 = 0, 0, 255
    Green = 0, 255, 0
    for pos in snake_body:
        if pos == snake_body[0]:
            pygame.draw.rect(screen, Green1, (pos[0], pos[1], size, size))
        else:
            pygame.draw.rect(screen, Green, (pos[0], pos[1], size, size))

def move(xr, yr, size, changedirection, direction):

    # logic di chuyển là rắn chỉ di chuyển được 3 hướng trừ hướng ngược với chiều di chuyển của nó. 
    # Nên muốn quay đầu thì phải thông qua bước cua.
    # vì vậy điều kiện ở đây nên là: Nếu hướng thay đổi khác với hướng ngược với chiều di chuyển của nó thì mới được thực thi. 
    # Ngược lại thì không có gì xảy ra.

    if ((changedirection == 'LEFT') and (direction != 'RIGHT')):
        direction = 'LEFT'
    elif ((changedirection == 'RIGHT') and (direction != 'LEFT')):
        direction = 'RIGHT'
    elif ((changedirection == 'UP') and (direction != 'DOWN')):
        direction = 'UP'
    elif ((changedirection == 'DOWN') and (direction != 'UP')):
        direction = 'DOWN'

    if direction == 'LEFT':
        xr -= size
    elif direction == 'RIGHT':
        xr += size
    elif direction == 'UP':
        yr -= size
    elif  direction == 'DOWN':
        yr += size
    return xr, yr, direction

def food(width, height, screen, size, xf, yf, xr, yr):
    Red = 255, 0, 0
    if (xf != xr) or (yf != yr):
        pygame.draw.rect(screen, Red, (xf, yf, size, size))

def eat(xr, yr, xf, yf, width, height, size, snake_body, score):
    if (xr == xf) and (yr == yf):
        snake_body.insert(0, [xr, yr])
        xf = random.randrange(size*2, width - size*3, size)
        yf = random.randrange(size*2, height - size*3, size)
        score += 1
    return xf, yf, score

def show_score(width, height, score, screen):
    my_font = pygame.font.SysFont('consolas', 20) #tạo font chữ cho score khi chơi.
    Red = 255, 0, 0
    score_surface = my_font.render("Score: {0}".format(score), True, Red) #tạo chữ, {0}.format(socre) dùng để hiện số điểm.
    score_pos = (width/100, height/100)
    screen.blit(score_surface, score_pos)

def gameover(xr, yr, width, height, screen, score, Black, running):
    while running:
        Red = 255, 0, 0
        my_font1 = pygame.font.SysFont('consolas', 50) #tạo font chữ Game Over.
        my_font2 = pygame.font.SysFont('consolas', 30) #tạo font chữ score khi game over
        my_font3 = pygame.font.SysFont('consolas', 25) #tạo font chữ play again, quit game.
        
        text_surface = my_font1.render("Game Over", True, Red)#tạo chữ
        text_pos = (width/2 - 125, height/2 - 50)
        screen.blit(text_surface, text_pos) #Hien chu Game Over


        score_surface = my_font2.render("Score: {0}".format(score), True, Red) 
        score_pos = (width/2 - 70, height/2+20)
        screen.blit(score_surface, score_pos) #hiện Score.


        #Chữ Play Again.
        rect_play_again = (width/2 - 77, height/2+65, 150, 50) #(width/2 - 77, height/2 +65) là số qua vài lần thử nghiệm thì đó là số hợp lí nhất cho vị trí x và y của khung hình chữ nhật
        pygame.draw.rect(screen, Black, rect_play_again, 3) #vẽ khung chữ play again.
        play_again_surface = my_font3.render("Play Again", True, Black) #tạo chữ play again.
        play_again_pos = (rect_play_again[0]+5, rect_play_again[1]+15) #+5 và +15 là số qua những lần thử nghiệm là số hợp lý nhất cho vị trí của chữ play again nằm trong khung của nó.
        screen.blit(play_again_surface, play_again_pos) #hiện chữ Play Again.

        #Chữ quit game.
        rect_quit_game = (width/2 - 77, height/2+65 + 50 + 25, 150, 50) 
        pygame.draw.rect(screen, Black, rect_quit_game, 3) #vẽ khung chữ quit game.
        quit_game_surface = my_font3.render("Quit Game", True, Black) #tạo chữ play again.
        quit_game_pos = (rect_quit_game[0]+10, rect_quit_game[1]+15)
        screen.blit(quit_game_surface, quit_game_pos) #hiện chữ quit game.

        mousex, mousey = pygame.mouse.get_pos() #lấy toạ độ x, y của chuột khi di chuyển trên màn hình. Chỉ cần 1 câu lệnh vẫn có thể gán cho 2 biếN là mousex và mousey. Vì hàm mặc định return (x, y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # 1 là index của nút chuột trái.
                    if ((width/2 - 77 <= mousex <= width/2 - 77 + 150) and (height/2+65 <= mousey <= height/2+65 + 50)):
                        #ở đây vì chưa biết tạo button nên sẽ làm nút giả thông qua việc so sánh toạ độ của chuột có nằm trong khung chữ 
                        # play again hay không. Nếu nằm trong thì đoạn lệnh sẽ được thực thi. Ngược lại thì không có gì xảy ra.
                        main()
                    if ((width/2 - 77 <= mousex <= width/2 - 77 + 150) and ((height/2+65 + 50 + 25) <= mousey <= (height/2+65 + 50 + 25 + 50))):
                        running = False
        pygame.display.flip()
    pygame.quit()

def main():
    width, height = 1000, 600
    size = 20
    score = 0
    xr, yr = int(width/2), int(height/2)
    snake_body = []
    xf = random.randrange(size*2, width - size*3, size)
    yf = random.randrange(size*2, height - size*3, size)
    Grey = 96, 96, 96
    Black = 0, 0, 0
    direction = "RIGHT"
    changedirection = direction
    FPS = 15
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake by NHN")
    running = True  
    while running:
        screen.fill(Grey)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    changedirection = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    changedirection = 'RIGHT'
                elif event.key == pygame.K_UP:
                    changedirection = 'UP'
                elif event.key == pygame.K_DOWN:
                    changedirection = 'DOWN'
                    
        xr, yr, direction = move(xr, yr, size, changedirection, direction)          
        snake_pos = [xr, yr]
        snake_body.insert(0,snake_pos)

        if ((xr < size*2 or xr >= width - size*2) or (yr < size*2 or yr >= height - size*2)):
            gameover(xr, yr, width, height, screen, score, Black, running)
        snake(xr, yr, screen, snake_body, size)
        food(width, height, screen, size, xf, yf, xr, yr)
        xf, yf, score = eat(xr, yr, xf, yf, width, height, size, snake_body, score)
        show_score(width, height, score, screen)

        del snake_body[len(snake_body)-1]

        if len(snake_body) >= 4:
            if (snake_pos in snake_body[4:]):
                gameover(xr, yr, width, height, screen, score, Black, running)

        pygame.draw.line(screen, Black, (size*2, size*2), (width - size*2, size*2), 2)#tren
        pygame.draw.line(screen, Black, (size*2, height - size*2), (width - size*2, height - size*2), 2)#duoi
        pygame.draw.line(screen, Black, (size*2, size*2), (size*2, height - size*2), 2)#trai
        pygame.draw.line(screen, Black, (width - size*2, size*2), (width - size*2, height - size*2), 2)#phai

        pygame.display.flip()
        fpsClock.tick(FPS)
    pygame.quit()

main()