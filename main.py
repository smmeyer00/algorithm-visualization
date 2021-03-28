import pygame
import random
import time

# Sorting algorithms: bubblesort, quicksort, mergesort, insertionsort, selectionsort, heapsort

#implemented:


BUTTON_LOCATIONS = {
    'shuffle': [],
    'bubblesort': [],
    'quicksort': [],
    'mergesort': [],
    'insertionsort': [],
    'selectionsort': [],
    'heapsort': []
}


FRAMERATE = 200
DELAY_TIME = 100 #delay between swaps in ms

WIDTH = 1000 # width in pixels 100 10px wide rectangles
HEIGHT = 700 # 500px for rectangles and 200px for buttons

BUTTON_COLOR = (7, 47, 95) #dark blue
BUTTON_COLOR_HOVER = (18, 97, 160) #slightly lighter blue

RECT_HEIGHTS = []
for i in range(1, 101, 1):
    RECT_HEIGHTS.append(i*5)


pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont('arial', 30)



def wait(ms):
    start = time.perf_counter()
    while time.perf_counter() - start < ms:
        pass




def shuffle():
    for i in range(1000):
        index1 = random.randint(0, 99)
        index2 = random.randint(0, 99)

        #swap
        temp = RECT_HEIGHTS[index1]
        RECT_HEIGHTS[index1] = RECT_HEIGHTS[index2]
        RECT_HEIGHTS[index2] = temp


def draw_rects():
    for i in range(len(RECT_HEIGHTS)):
        height = RECT_HEIGHTS[i]
        width = 10

        x = 10*i
        y = 500 - height

        pygame.draw.rect(SCREEN, (0,0,0), pygame.Rect(x, y, width, height))

def highlight(index): #highlight rect at index
    height = RECT_HEIGHTS[index]
    width = 10

    x = 10*index
    y = 500 - height

    pygame.draw.rect(SCREEN, (0,255,0), pygame.Rect(x, y, width, height))
    pygame.display.update()

def unhighlight(index): #highlight rect at index
    height = RECT_HEIGHTS[index]
    width = 10

    x = 10*index
    y = 500 - height

    pygame.draw.rect(SCREEN, (0,0,0), pygame.Rect(x, y, width, height))
    pygame.display.update()







def draw_menu(): #draw all fonts with solid backgrounds as buttons, Y=582
    mouse = pygame.mouse.get_pos()

    padding = 5
    current_x = padding

    #shuffle button
    size = FONT.size(' Shuffle ')
    BUTTON_LOCATIONS['shuffle'] = [current_x, 582, size[0], size[1]]
    if current_x < mouse[0] < current_x + size[0] and 582 < mouse[1] < 582+size[1]:
        shuffle_txt = FONT.render(' Shuffle ', True, (255,255,255), BUTTON_COLOR_HOVER)
    else:
        shuffle_txt = FONT.render(' Shuffle ', True, (255,255,255), BUTTON_COLOR)

    SCREEN.blit(shuffle_txt, [current_x, 582])
    current_x += size[0] + padding
    #end shuffle button



    #bubblesort button
    size = FONT.size(' Bubble Sort ')
    BUTTON_LOCATIONS['bubblesort'] = [current_x, 582, size[0], size[1]]
    if current_x < mouse[0] < current_x + size[0] and 582 < mouse[1] < 582+size[1]:
        bubblesort_txt = FONT.render(' Bubble Sort ', True, (255,255,255), BUTTON_COLOR_HOVER)
    else:
        bubblesort_txt = FONT.render(' Bubble Sort ', True, (255,255,255), BUTTON_COLOR)

    SCREEN.blit(bubblesort_txt, [current_x, 582])
    current_x += size[0] + padding
    #end bubblesort button

    #insertionsort button
    size = FONT.size(' Insertion Sort ')
    BUTTON_LOCATIONS['insertionsort'] = [current_x, 582, size[0], size[1]]
    if current_x < mouse[0] < current_x + size[0] and 582 < mouse[1] < 582+size[1]:
        insertionsort_txt = FONT.render(' Insertion Sort ', True, (255,255,255), BUTTON_COLOR_HOVER)
    else:
        insertionsort_txt = FONT.render(' Insertion Sort ', True, (255,255,255), BUTTON_COLOR)

    SCREEN.blit(insertionsort_txt, [current_x, 582])
    current_x += size[0] + padding
    #end insertionsort button

    #selectionsort button
    size = FONT.size(' Selection Sort ')
    BUTTON_LOCATIONS['selectionsort'] = [current_x, 582, size[0], size[1]]
    if current_x < mouse[0] < current_x + size[0] and 582 < mouse[1] < 582+size[1]:
        selectionsort_txt = FONT.render(' Selection Sort ', True, (255,255,255), BUTTON_COLOR_HOVER)
    else:
        selectionsort_txt = FONT.render(' Selection Sort ', True, (255,255,255), BUTTON_COLOR)

    SCREEN.blit(selectionsort_txt, [current_x, 582])
    current_x += size[0] + padding
    #end selectionsort button

    #quicksort button
    size = FONT.size(' Quick Sort ')
    BUTTON_LOCATIONS['quicksort'] = [current_x, 582, size[0], size[1]]
    if current_x < mouse[0] < current_x + size[0] and 582 < mouse[1] < 582+size[1]:
        quicksort_txt = FONT.render(' Quick Sort ', True, (255,255,255), BUTTON_COLOR_HOVER)
    else:
        quicksort_txt = FONT.render(' Quick Sort ', True, (255,255,255), BUTTON_COLOR)

    SCREEN.blit(quicksort_txt, [current_x, 582])
    current_x += size[0] + padding
    #end quicksort button

    #mergesort button
    size = FONT.size(' Merge Sort ')
    BUTTON_LOCATIONS['mergesort'] = [current_x, 582, size[0], size[1]]
    if current_x < mouse[0] < current_x + size[0] and 582 < mouse[1] < 582+size[1]:
        mergesort_txt = FONT.render(' Merge Sort ', True, (255,255,255), BUTTON_COLOR_HOVER)
    else:
        mergesort_txt = FONT.render(' Merge Sort ', True, (255,255,255), BUTTON_COLOR)

    SCREEN.blit(mergesort_txt, [current_x, 582])
    current_x += size[0] + padding
    #end mergesort button

    #heapsort button
    size = FONT.size(' Heap Sort ')
    BUTTON_LOCATIONS['heapsort'] = [current_x, 582, size[0], size[1]]
    if current_x < mouse[0] < current_x + size[0] and 582 < mouse[1] < 582+size[1]:
        heapsort_txt = FONT.render(' Heap Sort ', True, (255,255,255), BUTTON_COLOR_HOVER)
    else:
        heapsort_txt = FONT.render(' Heap Sort ', True, (255,255,255), BUTTON_COLOR)

    SCREEN.blit(heapsort_txt, [current_x, 582])
    current_x += size[0] + padding
    #end heapsort button


def contains(pos, button_name):
    info = BUTTON_LOCATIONS[button_name]
    if info[0] < pos[0] < info[0]+info[2] and info[1] < pos[1] < info[1]+info[3]:
        return True
    else:
        return False


def handle_click(pos):
    if contains(pos, 'shuffle'):
        shuffle()
    elif contains(pos, 'bubblesort'):
        bubblesort()
    elif contains(pos, 'quicksort'):
        pass
    elif contains(pos, 'mergesort'):
        pass
    elif contains(pos, 'insertionsort'):
        pass
    elif contains(pos, 'selectionsort'):
        pass
    elif contains(pos, 'heapsort'):
        pass



def draw(): # method responsible for drawing everything to the screen
    SCREEN.fill((255,255,255))
    draw_rects()
    draw_menu()
    pygame.display.flip()

    print(FONT.size('Shuffle'))



def swap_with_animation(i, j): #swap with timing between and color change of rectangles being swapped
    highlight(i)
    highlight(j)
    wait(.5/FRAMERATE)
    draw()

    temp = RECT_HEIGHTS[i]
    RECT_HEIGHTS[i] = RECT_HEIGHTS[j]
    RECT_HEIGHTS[j] = temp

    draw()
    highlight(i)
    highlight(j)
    wait(.5/FRAMERATE)







def bubblesort():
    for i in range(len(RECT_HEIGHTS)-1):
        for j in range(0, len(RECT_HEIGHTS)-i-1):
            if RECT_HEIGHTS[j] > RECT_HEIGHTS[j+1]:
                swap_with_animation(j, j+1)


def insertionsort():
    



shuffle()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(pygame.mouse.get_pos())

    SCREEN.fill((255,255,255)) #clears screen
    draw()
    pygame.display.flip()
