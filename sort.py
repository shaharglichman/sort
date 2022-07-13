import pygame
import random

pygame.init()
win = pygame.display.set_mode((900, 700))


class Wall:
    def __init__(self, x, height, wallN):
        self.x = x
        self.height = height
        self.wallN = wallN
        self.walls_list = []
        self.wList = []
        self.generate()
        self.speed = ""
        self.set_speed = 0
        self.GRADIENTS = [
            (128, 128, 128),
            (160, 160, 160),
            (192, 192, 192)
        ]

    def draw(self, color_positions={}):
        win.fill((255, 255, 255))
        for n in range(len(self.wList)):
            color = self.GRADIENTS[n % 3]
            if n in color_positions:
                color = color_positions[n]
            pygame.draw.rect(win, (color), (40 + 6 * n, 230, 4, self.wList[n]))

    def reset(self):
        for b in range(1, self.wallN, 6):
            for v in range(len(self.wList)):
                self.wList[v] = random.randint(1, 400)

    def generate(self):
        for b in range(1, self.wallN, 6):
            self.wList.append(random.randint(1, 400))

    def move(self):
        for _ in range(50):
            self.walls_list.append(Wall(100, 100, 400))
        for i in self.walls_list:
            i.draw()


w = Wall(100, 100, 400)
clock = pygame.time.Clock()


class Main:
    def __init__(self):
        self.color1 = (100, 100, 100)
        self.color2 = (100, 100, 100)
        self.color3 = (100, 100, 100)

    def bubble_sort(self, arr):
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] < arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp

                    w.draw({j: (0, 255, 0), j + 1: (255, 0, 0)})
                    pygame.time.delay(w.set_speed)
                    pygame.display.update()

    def merge_sort(self, arr):
        size = len(arr)
        if size > 1:
            middle = size // 2
            left_arr = arr[:middle]
            right_arr = arr[middle:]
            self.merge_sort(left_arr)
            self.merge_sort(right_arr)
            p = 0
            q = 0
            r = 0
            left_size = len(left_arr)
            right_size = len(right_arr)
            while p < left_size and q < right_size:
                if left_arr[p] < right_arr[q]:
                    arr[r] = left_arr[p]
                    p += 1
                else:
                    arr[r] = right_arr[q]
                    q += 1

                r += 1
            while p < left_size:
                arr[r] = left_arr[p]
                p += 1
                r += 1

            while q < right_size:
                arr[r] = right_arr[q]
                q += 1
                r += 1
            w.draw({p: (0, 255, 0), q: (255, 0, 0)})
            pygame.time.delay(w.set_speed)
            pygame.display.update()

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

            w.draw({i - 1: (0, 255, 0), i: (255, 0, 0)})
            pygame.time.delay(w.set_speed)
            pygame.display.update()

    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
                    w.draw({j: (0, 255, 0), j + 1: (255, 0, 0)})
                    pygame.time.delay(w.set_speed)
                    pygame.display.update()

            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    def dis(self):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 18)
        txtb = font.render('press b to bubble sort', True, (30, 30, 30))
        txts = font.render('press s to selection sort', True, (30, 30, 30))
        txti = font.render('press i to insertion sort', True, (30, 30, 30))
        txtm = font.render('press m to merge sort', True, (30, 30, 30))
        txtspeed = font.render('speed:', True, (30, 30, 30))
        txtr = font.render('press r to reset array', True, (30, 30, 30))
        win.blit(txtb, (10, 20))
        win.blit(txts, (10, 50))
        win.blit(txti, (10, 80))
        win.blit(txtm, (10, 110))
        win.blit(txtr, (10, 140))
        win.blit(txtspeed, (10, 170))

        text1 = font.render("slow", 1, (0, 0, 0))
        pygame.draw.rect(win, self.color1, [70, 170, 50, 40])
        win.blit(text1, (70, 170))

        text2 = font.render("normal", 1, (0, 0, 0))
        pygame.draw.rect(win, self.color2, [130, 170, 50, 40])
        win.blit(text2, (130, 170))

        text3 = font.render("fast", 1, (0, 0, 0))
        pygame.draw.rect(win, self.color3, [190, 170, 50, 40])
        win.blit(text3, (190, 170))

        pygame.display.update()

    def check_btn(self):
        mouse = pygame.mouse.get_pos()

        if 70 <= mouse[0] <= 70 + 50 and 170 <= mouse[1] <= 170 + 40:
            w.set_speed = 100
            self.color1 = (200, 200, 255)
        else:
            self.color1 = (100, 100, 100)
        if 130 <= mouse[0] <= 130 + 50 and 170 <= mouse[1] <= 170 + 40:
            w.set_speed = 30
            self.color2 = (200, 200, 255)
        else:
            self.color2 = (100, 100, 100)
        if 190 <= mouse[0] <= 190 + 50 and 170 <= mouse[1] <= 170 + 40:
            w.set_speed = 2
            self.color3 = (200, 200, 255)
        else:
            self.color3 = (100, 100, 100)

        pygame.display.update()

    def main(self):
        run = True
        w.move()
        w.generate()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_btn()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        self.bubble_sort(w.wList)
                    elif event.key == pygame.K_s:
                        self.selection_sort(w.wList)
                    elif event.key == pygame.K_i:
                        self.insertion_sort(w.wList)
                    elif event.key == pygame.K_m:
                        self.merge_sort(w.wList)
                    elif event.key == pygame.K_r:
                        w.reset()

            clock.tick(60)
            w.draw()
            self.dis()
            pygame.display.update()
        pygame.quit()


m = Main()
m.main()
