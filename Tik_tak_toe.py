import pygame


FPS = 60
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

def check_position(x, y, sign):
    if 300 < x < 300+ 200  and 100 < y < 100+200 and matrix[0][0] == '':
        matrix[0][0] = sign
    if 300 < x < 500 and 300 < y < 500 and matrix[1][0] == '':
        matrix[1][0] = sign
    if 300 < x < 500 and 500 < y < 700 and matrix[2][0] == '':
        matrix[2][0] = sign 

    if 500 < x < 700 and 100 < y < 100+200 and matrix[0][1] == '':
        matrix[0][1] = sign
    if 500 < x < 700 and 300 < y < 500 and matrix[1][1] == '':
        matrix[1][1] = sign
    if 500 < x < 700 and 500 < y < 700 and matrix[2][1] == '':
        matrix[2][1] = sign 

    if 700 < x < 900  and 100 < y < 100+200 and matrix[0][2] == '':
        matrix[0][2] = sign
    if 700 < x < 900 and 300 < y < 500 and matrix[1][2] == '':
        matrix[1][2] = sign
    if 700 < x < 900 and 500 < y < 700 and matrix[2][2] == '':
        matrix[2][2] = sign 

def check_end():
    if matrix[0][0] == matrix[0][1] == matrix[0][2] != '':
        return matrix[0][0]
    if matrix[0][0] == matrix[1][0] == matrix[2][0] != '':
        return matrix[1][0]
    if matrix[1][1] == matrix[0][1] == matrix[2][1] != '':
        return matrix[1][1]
    if matrix[2][0] == matrix[2][1] == matrix[2][2] != '':
        return matrix[2][0]
    if matrix[1][0] == matrix[1][1] == matrix[1][2] != '':
        return matrix[1][0]
    if matrix[0][2] == matrix[1][2] == matrix[2][2] != '':
        return matrix[0][2]
    if matrix[2][0] == matrix[1][1] == matrix[0][2] != '':
        return matrix[2][0]
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != '':
        return matrix[0][0]
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == '':
                return None
    return 'ничья!'
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

font=pygame.freetype.SysFont(None, 30)
font.origin=True

tik_tok = pygame.font.SysFont('serif', 170)
main_font = pygame.font.SysFont('serif', 24)
header_font = pygame.font.SysFont('Arial', 48)

cross = tik_tok.render('X', True, GREEN)
zero = tik_tok.render('O', True, GREEN)

header_text = header_font.render("Tik Tak Toe", True, GRAY)
time_text = main_font.render("Время игры: ", True, WHITE)
start_text = main_font.render("Новая игра", True, WHITE)
exit_text = main_font.render("Конец игры", True, WHITE)
win_text_X = main_font.render("Победили - крестики", True, RED)
win_text_O = main_font.render("Победили - нолики", True, RED)
win_text = None
button = False

matrix = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

start_ticks = pygame.time.get_ticks()
ticks=pygame.time.get_ticks() - start_ticks
is_game = True
while True:
    clock.tick(FPS)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if event.button == 1:
                if 5 <= x <= 5 + 135 and 545 <= y <= 545 + 50:
                    exit()
                if 5 <= x <= 5 + 125 and 345 <= y <= 345 + 50:
                    matrix = [
                        ['', '', ''],
                        ['', '', ''],
                        ['', '', '']
                    ]
                    is_game = True
                    start_ticks = pygame.time.get_ticks()
                if is_game: 
                    check_position(x, y, 'X')
            elif event.button == 3 and is_game:
                check_position(x, y, 'O')
            res = check_end()
            if res == 'X':
                is_game = False
                win_text = win_text_X
            elif res == 'O':
                is_game = False
                win_text = win_text_O
            elif res == 'ничья!':
                pass
                print('ничья')

    
    screen.fill(pygame.Color('grey12'))
    if is_game:
        ticks=pygame.time.get_ticks() - start_ticks
    millis= (ticks%1000) // 100
    seconds= ticks//1000 % 60
    minutes= ticks//60000 % 24
    out='{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
    font.render_to(screen, (175, 180), out, pygame.Color('dodgerblue'))
    pygame.draw.line(screen, WHITE, (300, 100), (900, 100), 5)
    pygame.draw.line(screen, WHITE, (300, 300), (900, 300), 5)
    pygame.draw.line(screen, WHITE, (300, 500), (900, 500), 5)
    pygame.draw.line(screen, WHITE, (300, 700 ), (900, 700), 5)
        
    pygame.draw.line(screen, WHITE, (300, 700), (300, 100), 5)
    pygame.draw.line(screen, WHITE, (500, 700), (500, 100), 5)
    pygame.draw.line(screen, WHITE, (700, 700), (700, 100), 5)
    pygame.draw.line(screen, WHITE, (900, 700), (900, 100), 5)
    
    pygame.draw.rect(screen, BLUE,(5, 145, 155 , 50))
    pygame.draw.rect(screen, BLUE,(5, 345, 125 , 50))
    pygame.draw.rect(screen, BLUE,(5, 545, 135 , 50))
    screen.blit(header_text, (500 , 25))
    
    screen.blit(time_text, (10, 150))
    screen.blit(start_text, (10, 350))
    screen.blit(exit_text, (10, 550))
    if is_game == False:
        screen.blit(win_text, (10, 33))
    
    LEFT = 340
    UP = 100
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 'X':
                screen.blit(cross, (LEFT + j * 200, UP + i * 200))
            elif matrix[i][j] == 'O':
                screen.blit(zero, (LEFT + j * 200, UP + i * 200))


    pygame.display.update()
