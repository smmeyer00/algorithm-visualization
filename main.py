import pygame
import random
import time

'''
####################################################################################################
# Author: Steven Meyer                                                                             #
# Description: GUI application to give a visualization of common sorting algorithms                #
# Supported Algoithms: (bubblesort, quicksort, mergesort, insertionsort, selectionsort, heapsort)  #
####################################################################################################
'''

BUTTON_LOCATIONS = {
    'shuffle': [],
    'bubblesort': [],
    'quicksort': [],
    'mergesort': [],
    'insertionsort': [],
    'selectionsort': [],
    'heapsort': []
}

FRAMERATE = 200  # not really a framerate but more of a tickrate used for waiting times when doing an animated swap

WIDTH = 1000  # width in pixels 100 10px wide rectangles
HEIGHT = 700  # 500px for rectangles and 200px for buttons

BUTTON_COLOR = (7, 47, 95)  # dark blue
BUTTON_COLOR_HOVER = (18, 97, 160)  # slightly lighter blue

RECT_HEIGHTS = []  # contains heights of rectangles to be sorted
for i in range(1, 101, 1):
    RECT_HEIGHTS.append(i*5)

# set up pygame and the font
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sorting Algorithm Visualization')
FONT = pygame.font.SysFont('arial', 30)


# alternate sleep method to time.sleep, more accurate and does not actually sleep the thread
def wait(ms):
    start = time.perf_counter()
    while time.perf_counter() - start < ms:
        pass


# method to shuffle the array of rectangle heights
def shuffle():
    for i in range(1000):
        index1 = random.randint(0, 99)
        index2 = random.randint(0, 99)

        # swap
        temp = RECT_HEIGHTS[index1]
        RECT_HEIGHTS[index1] = RECT_HEIGHTS[index2]
        RECT_HEIGHTS[index2] = temp


# method to draw the rectangles to the screen
def draw_rects():
    for i in range(len(RECT_HEIGHTS)):
        height = RECT_HEIGHTS[i]
        width = 10

        x = 10*i
        y = 500 - height

        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(x, y, width, height))


# method to highlight rectangle at index index
def highlight(index):
    height = RECT_HEIGHTS[index]
    width = 10

    x = 10*index
    y = 500 - height

    pygame.draw.rect(SCREEN, (0, 255, 0), pygame.Rect(x, y, width, height))
    pygame.display.update()


# method to unhighlight rect at index index
def unhighlight(index):
    height = RECT_HEIGHTS[index]
    width = 10

    x = 10*index
    y = 500 - height

    pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(x, y, width, height))
    pygame.display.update()


# method to draw the menu, buttons drawn as fonts with opaque backgrounds, Y=582
def draw_menu():
    mouse = pygame.mouse.get_pos()

    padding = 5
    current_x = padding

    # shuffle button
    size = FONT.size(' Shuffle ')
    BUTTON_LOCATIONS['shuffle'] = [current_x, 582, size[0], size[1]]
    if current_x < mouse[0] < current_x + size[0] and 582 < mouse[1] < 582+size[1]:
        shuffle_txt = FONT.render(' Shuffle ', True, (255, 255, 255), BUTTON_COLOR_HOVER)
    else:
        shuffle_txt = FONT.render(' Shuffle ', True, (255, 255, 255), BUTTON_COLOR)

    SCREEN.blit(shuffle_txt, [current_x, 582])
    current_x += size[0] + padding
    # end shuffle button

    # bubblesort button
    size = FONT.size(' Bubble Sort ')
    BUTTON_LOCATIONS['bubblesort'] = [current_x, 582, size[0], size[1]]
    if current_x < mouse[0] < current_x + size[0] and 582 < mouse[1] < 582+size[1]:
        bubblesort_txt = FONT.render(' Bubble Sort ', True, (255, 255, 255), BUTTON_COLOR_HOVER)
    else:
        bubblesort_txt = FONT.render(' Bubble Sort ', True, (255, 255, 255), BUTTON_COLOR)

    SCREEN.blit(bubblesort_txt, [current_x, 582])
    current_x += size[0] + padding
    # end bubblesort button

    # insertionsort button
    size = FONT.size(' Insertion Sort ')
    BUTTON_LOCATIONS['insertionsort'] = [current_x, 582, size[0], size[1]]
    if current_x < mouse[0] < current_x + size[0] and 582 < mouse[1] < 582+size[1]:
        insertionsort_txt = FONT.render(' Insertion Sort ', True, (255, 255, 255), BUTTON_COLOR_HOVER)
    else:
        insertionsort_txt = FONT.render(' Insertion Sort ', True, (255, 255, 255), BUTTON_COLOR)

    SCREEN.blit(insertionsort_txt, [current_x, 582])
    current_x += size[0] + padding
    # end insertionsort button

    # selectionsort button
    size = FONT.size(' Selection Sort ')
    BUTTON_LOCATIONS['selectionsort'] = [current_x, 582, size[0], size[1]]
    if current_x < mouse[0] < current_x + size[0] and 582 < mouse[1] < 582+size[1]:
        selectionsort_txt = FONT.render(' Selection Sort ', True, (255, 255, 255), BUTTON_COLOR_HOVER)
    else:
        selectionsort_txt = FONT.render(' Selection Sort ', True, (255, 255, 255), BUTTON_COLOR)

    SCREEN.blit(selectionsort_txt, [current_x, 582])
    current_x += size[0] + padding
    # end selectionsort button

    # quicksort button
    size = FONT.size(' Quick Sort ')
    BUTTON_LOCATIONS['quicksort'] = [current_x, 582, size[0], size[1]]
    if current_x < mouse[0] < current_x + size[0] and 582 < mouse[1] < 582+size[1]:
        quicksort_txt = FONT.render(' Quick Sort ', True, (255, 255, 255), BUTTON_COLOR_HOVER)
    else:
        quicksort_txt = FONT.render(' Quick Sort ', True, (255, 255, 255), BUTTON_COLOR)

    SCREEN.blit(quicksort_txt, [current_x, 582])
    current_x += size[0] + padding
    # end quicksort button

    # mergesort button
    size = FONT.size(' Merge Sort ')
    BUTTON_LOCATIONS['mergesort'] = [current_x, 582, size[0], size[1]]
    if current_x < mouse[0] < current_x + size[0] and 582 < mouse[1] < 582+size[1]:
        mergesort_txt = FONT.render(' Merge Sort ', True, (255, 255, 255), BUTTON_COLOR_HOVER)
    else:
        mergesort_txt = FONT.render(' Merge Sort ', True, (255, 255, 255), BUTTON_COLOR)

    SCREEN.blit(mergesort_txt, [current_x, 582])
    current_x += size[0] + padding
    # end mergesort button

    # heapsort button
    size = FONT.size(' Heap Sort ')
    BUTTON_LOCATIONS['heapsort'] = [current_x, 582, size[0], size[1]]
    if current_x < mouse[0] < current_x + size[0] and 582 < mouse[1] < 582+size[1]:
        heapsort_txt = FONT.render(' Heap Sort ', True, (255, 255, 255), BUTTON_COLOR_HOVER)
    else:
        heapsort_txt = FONT.render(' Heap Sort ', True, (255, 255, 255), BUTTON_COLOR)

    SCREEN.blit(heapsort_txt, [current_x, 582])
    current_x += size[0] + padding
    # end heapsort button


# method to check if px coord pos is in a 'button'
def contains(pos, button_name):
    info = BUTTON_LOCATIONS[button_name]
    if info[0] < pos[0] < info[0]+info[2] and info[1] < pos[1] < info[1]+info[3]:
        return True
    else:
        return False


# method called whenever mouse clicked, checks if mouse in any buttons then calls appropriate method
def handle_click(pos):
    if contains(pos, 'shuffle'):
        shuffle()
    elif contains(pos, 'bubblesort'):
        bubblesort()
    elif contains(pos, 'quicksort'):
        quicksort(0, len(RECT_HEIGHTS)-1)
    elif contains(pos, 'mergesort'):
        mergesort(0, len(RECT_HEIGHTS)-1)
    elif contains(pos, 'insertionsort'):
        insertionsort()
    elif contains(pos, 'selectionsort'):
        selectionsort()
    elif contains(pos, 'heapsort'):
        heapsort()


# method to draw everything to the screen, uses drawing helper methods
def draw():
    SCREEN.fill((255, 255, 255))
    draw_rects()
    draw_menu()
    pygame.display.flip()


# method to swap rects at index i and j ,but slightly animated
def swap_with_animation(i, j):
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


# method to move val into RECT_HEIGHTS arr at index index, but slightly animated
def move_with_animation(index, val):
    highlight(index)
    wait(.5/FRAMERATE)
    draw()

    RECT_HEIGHTS[index] = val

    draw()
    highlight(index)
    wait(.5/FRAMERATE)


# bubble sort method
def bubblesort():
    for i in range(len(RECT_HEIGHTS)-1):
        for j in range(0, len(RECT_HEIGHTS)-i-1):
            highlight(j)
            if RECT_HEIGHTS[j] > RECT_HEIGHTS[j+1]:
                swap_with_animation(j, j+1)
            unhighlight(j)


# insertion sort method
def insertionsort():
    for i in range(1, len(RECT_HEIGHTS)):
        key = RECT_HEIGHTS[i]
        highlight(i)
        j = i-1
        highlight(j)

        while j >= 0 and key < RECT_HEIGHTS[j]:
            draw()
            move_with_animation(j+1, RECT_HEIGHTS[j])
            j -= 1
            highlight(j)

        move_with_animation(j+1, key)


# selection sort method
def selectionsort():
    for i in range(len(RECT_HEIGHTS)):
        min = i
        highlight(i)
        for j in range(i+1, len(RECT_HEIGHTS)):
            if RECT_HEIGHTS[min] > RECT_HEIGHTS[j]:
                min = j
                draw()
                highlight(j)

        swap_with_animation(i, min)


# partition helper method for quicksort
def partition(low, high):
    i = low-1
    pivot = RECT_HEIGHTS[high]

    for j in range(low, high):
        if RECT_HEIGHTS[j] <= pivot:
            i += 1
            swap_with_animation(i, j)

    swap_with_animation(i+1, high)
    return i+1


# quicksort method
def quicksort(low, high):
    if low < high:
        p = partition(low, high)

        quicksort(low, p-1)
        quicksort(p+1, high)


# merge helper method for merge sort
def merge(l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = RECT_HEIGHTS[l+i]

    for j in range(0, n2):
        R[j] = RECT_HEIGHTS[m+1+j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            move_with_animation(k, L[i])
            i += 1
        else:
            move_with_animation(k, R[j])
            j += 1
        k += 1

    while i < n1:
        move_with_animation(k, L[i])
        i += 1
        k += 1

    while j < n2:
        move_with_animation(k, R[j])
        j += 1
        k += 1


# mergesort method
def mergesort(l, r):
    if l < r:

        m = (l+(r-1))//2

        mergesort(l, m)
        mergesort(m+1, r)
        merge(l, m, r)


# heapify helper method for heap sort
def heapify(n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l < n and RECT_HEIGHTS[largest] < RECT_HEIGHTS[l]:
        largest = l

    if r < n and RECT_HEIGHTS[largest] < RECT_HEIGHTS[r]:
        largest = r

    if largest != i:
        swap_with_animation(i, largest)
        heapify(n, largest)


# heapsort method
def heapsort():
    n = len(RECT_HEIGHTS)

    for i in range(n//2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n-1, 0, -1):
        swap_with_animation(i, 0)
        heapify(i, 0)


shuffle()  # initially shuffles RECT_HEIGHTS so it does not start sorted
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(pygame.mouse.get_pos())

    draw()
