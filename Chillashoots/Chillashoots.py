import pygame
import pygame.sprite
import os
import random
import math
from pygame import mixer

pygame.init()

# Defines width, height and frame rate of game screen
WIDTH = 800
HEIGHT = 600
FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CANVAS = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Defines used colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (200, 200, 200)

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action



# Makes buttons for Play and More, defines font for score display
start_img = pygame.image.load(os.path.join('button_start.png')).convert_alpha()
more_img = pygame.image.load(os.path.join('button_more.png')).convert_alpha()
start_button = Button(250, 300, start_img, 1)
more_button = Button(460, 430, more_img, 1)
font_score = pygame.font.Font('superstar_memesbruh03.ttf', 25)
font_score_gamov = pygame.font.Font('superstar_memesbruh03.ttf', 50)

# Defines high score variables
high_score_file = open("high_score.txt", "r")
high_score = int(high_score_file.read())
high_score_file.close()

HIGH_SCORE_FONT = pygame.font.Font('superstar_memesbruh03.ttf', 28)
HIGH_SCORE = HIGH_SCORE_FONT.render(f'Highscore: {high_score}', True, GREY, None)

HIGH_SCORE_RECT = HIGH_SCORE.get_rect()
HIGH_SCORE_RECT.center = (SCREEN_WIDTH // 2.3, SCREEN_HEIGHT // 1.30)

# Defines screensize
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Defines timers and groups enemies
enemy_timer = 0
bouncer_enemy_timer = 0
enemySprites = pygame.sprite.Group()

# Defines variables for score tracking
frame_count = 0
frame_rate = 60
start_time = 0

# Defines speed at which player moves when directional keys are pressed
player_speed = 15

# Calculate total seconds that have passed since game started
total_seconds = frame_count // frame_rate


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 144
bg = pygame.image.load("bg_stars_game.png").convert()
bg_width = bg.get_width()
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width + 1)

# Coordinates of where character sprite spawns in screen
player_x = 25
player_y = 320
# Defines variables for movement when no keys are pressed
player_x_change = 0
player_y_change = 0
# Defines the speed that the character sprite moves when keys are pressed
player_speed = 20


BACKGROUND = pygame.image.load('background-galaxy.jpg')


def title():
    # Font and color of title
    title_font = pygame.font.Font('gametitle_04B_30__.ttf', 60)
    grey = (200, 200, 200)
    black = (0, 0, 0)

    # Create text surface object
    title_1 = title_font.render('CHILLA', True, grey, None)
    title_2 = title_font.render('SHOOTS', True, black, None)

    # Create rectangular object for text surface object
    title_rect_1 = title_1.get_rect()
    title_rect_2 = title_2.get_rect()

    # Set center of rectangular object
    title_rect_1.center = (SCREEN_WIDTH // 3.09, SCREEN_HEIGHT // 3)
    title_rect_2.center = (SCREEN_WIDTH // 1.39, SCREEN_HEIGHT // 3)

    # Title and Icon in toolbar
    pygame.display.set_caption("ChillaShoots")
    icon = pygame.image.load(os.path.join('chinchilla_icon.png'))
    pygame.display.set_icon(icon)

    # Gets drawn first
    # Background image and coordinates of image appearance
    CANVAS.blit(BACKGROUND, (0, 0))
    CANVAS.blit(title_1, title_rect_1)
    CANVAS.blit(title_2, title_rect_2)


# Creates function for player to draw image of sprite icon on given coordinates
def player_sprite(x, y):
    player_img = pygame.image.load(os.path.join('chinchilla_sprite_light.png'))
    CANVAS.blit(player_img, (x, y))



# Title and Icon
pygame.display.set_caption("ChillaShoots")
icon = pygame.image.load(os.path.join('chinchilla_icon.png'))
pygame.display.set_icon(icon)


def setting_page():
    # Font and color of title
    title_font = pygame.font.Font('gametitle_04B_30__.ttf', 60)
    grey = (200, 200, 200)

    # Create text surface object
    title_1 = title_font.render('Settings', True, grey, None)

    # Create rectangular object for text surface object
    title_rect_1 = title_1.get_rect()

    # Set center of rectangular object
    title_rect_1.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5)

    # Title and Icon
    pygame.display.set_caption("ChillaShoots")
    icon = pygame.image.load('chinchilla_icon.png')
    pygame.display.set_icon(icon)

    # Gets drawn first
    # Background image and coordinates of image appearance
    CANVAS.blit(BACKGROUND, (0, 0))
    CANVAS.blit(title_1, title_rect_1)

    color_white = (0.2, 0.4, 0.6)
    pygame.draw.rect(CANVAS, color_white, pygame.Rect(50, 200, 700, 350), 0, 7)

def sound_maker():
    # Instantiate mixer
    mixer.init()

    # Load audio file
    mixer.music.load('Powerful-Trap-.mp3')

    # Set preferred volume
    mixer.music.set_volume(1.0)

    # Play the music
    mixer.music.play()


def game_over():
    # Font and color of title
    title_font = pygame.font.Font('gametitle_04B_30__.ttf', 60)
    red = (255, 0, 0)

    # Create text surface object
    title_1 = title_font.render('GAME', True, red, None)
    title_2 = title_font.render('OVER', True, red, None)

    # Create rectangular object for text surface object
    title_rect_1 = title_1.get_rect()
    title_rect_2 = title_2.get_rect()

    # Set center of rectangular object
    title_rect_1.center = (SCREEN_WIDTH // 3.09, SCREEN_HEIGHT // 3)
    title_rect_2.center = (SCREEN_WIDTH // 1.39, SCREEN_HEIGHT // 3)

    # Gets drawn first
    # Background image and coordinates of image appearance
    CANVAS.blit(BACKGROUND, (0, 0))
    CANVAS.blit(title_1, title_rect_1)
    CANVAS.blit(title_2, title_rect_2)


class BaseEnemy(pygame.sprite.Sprite):
    def __init__(
            self,
            enemy_speed_x=random.randint(6, 10),
            enemy_speed_y=random.randint(6, 10)
    ):
        x_start = 860
        y_start = random.randint(0, 536)
        enemy_image = pygame.image.load(os.path.join('ghost.png')).convert_alpha()

        # Create index thing of the speed variables for reversing
        super().__init__()
        self.enemy_speed_x = -enemy_speed_x
        self.enemy_speed_y = enemy_speed_y
        self.current_speed = [self.enemy_speed_x, self.enemy_speed_y]

        # Load the image
        self.image = enemy_image

        # Object rectangle needed for collision and starting position
        self.rect = self.image.get_rect()
        self.rect.x = x_start
        self.rect.y = y_start

    # Draw the object on the display, collision rectangle checking canvas size,
    # and equalling object speed to the rectangle
    def update(self, canvas):
        self.bounce_if_required(canvas.get_width(), canvas.get_height())
        self.rect = self.rect.move(self.current_speed)
        canvas.blit(self.image, self.rect)

    def bounce_if_required(self, screen_width, screen_height):
        # Enemy reverses when hitting the top side of the display.
        if self.rect.top <= 0:
            self.current_speed[1] = self.enemy_speed_y
        # Enemy reverses when hitting the bottom side of the display.
        elif self.rect.bottom >= screen_height:
            self.current_speed[1] = -self.enemy_speed_y

        # Enemy gets deleted when going off-screen.
        if self.rect.left <= -64:
            pygame.sprite.Sprite.kill(self)

    def reverse(self):
        self.current_speed[0] = -self.current_speed[0]
        self.current_speed[1] = -self.current_speed[1]


class Bouncer(BaseEnemy):
    def __init__(
            self,
            enemy_speed_x=10,
            enemy_speed_y=10
    ):
        enemy_image = pygame.image.load(os.path.join('EnemyBird.png'))
        x_start = 664,
        y_start = random.randint(0, 536)

        # Create index thing of the speed variables for reversing
        super().__init__()
        self.enemy_speed_x = enemy_speed_x
        self.enemy_speed_y = enemy_speed_y
        self.current_speed = [self.enemy_speed_x, self.enemy_speed_y]

        # These lines are always needed when creating enemy derivatives with different images or starting positions
        self.image = enemy_image

    def bounce_if_required(self, screen_width, screen_height):
        # Enemy reverses when hitting the left side of the display.
        if self.rect.left <= 0:
            self.current_speed[0] = self.enemy_speed_x - (self.enemy_speed_x / 2)
        # Enemy reverses when hitting the right side of the display.
        elif self.rect.right >= screen_width:
            self.current_speed[0] = -self.enemy_speed_x

        # Enemy reverses when hitting the top side of the display.
        if self.rect.top <= 0:
            self.current_speed[1] = self.enemy_speed_y
        # Enemy reverses when hitting the bottom side of the display.
        elif self.rect.bottom >= screen_height:
            self.current_speed[1] = -self.enemy_speed_y


class Upper(BaseEnemy):
    def __init__(
            self,
            enemy_speed_x=random.randint(3, 6),
            enemy_speed_y=random.randint(7, 11)
    ):
        super().__init__()
        x_start = 860
        y_start = random.randint(0, 240)

        self.enemy_speed_x = -enemy_speed_x
        self.enemy_speed_y = enemy_speed_y
        self.current_speed = [self.enemy_speed_x, self.enemy_speed_y]

        # These lines are always needed when creating enemy derivatives with different images or starting positions
        self.rect.x = x_start
        self.rect.y = y_start

    def bounce_if_required(self, screen_width, screen_height):
        # Enemy bounces down when hitting the top side of the display.
        if self.rect.top <= 0:
            self.current_speed[1] = self.enemy_speed_y
        # Enemy bounces up when hitting the middle of the display.
        elif self.rect.bottom >= 300:
            self.current_speed[1] = -self.enemy_speed_y

        # Enemy gets deleted when going off-screen.
        if self.rect.left <= -64:
            pygame.sprite.Sprite.kill(self)


class Lower(BaseEnemy):
    def __init__(
            self,
            enemy_speed_x=random.randint(3, 6),
            enemy_speed_y=random.randint(7, 11)
    ):
        super().__init__()
        x_start = 860
        y_start = random.randint(300, 540)

        self.enemy_speed_x = -enemy_speed_x
        self.enemy_speed_y = enemy_speed_y
        self.current_speed = [self.enemy_speed_x, self.enemy_speed_y]

        # These lines are always needed when creating enemy derivatives with different images or starting positions
        self.rect.x = x_start
        self.rect.y = y_start

    def bounce_if_required(self, screen_width, screen_height):
        # Enemy bounces down when hitting the middle of the display.
        if self.rect.top <= 300:
            self.current_speed[1] = self.enemy_speed_y
        # Enemy bounces up when hitting the bottom side of the display.
        elif self.rect.bottom >= screen_height:
            self.current_speed[1] = -self.enemy_speed_y

        # Enemy gets deleted when going off-screen.
        if self.rect.left <= -64:
            pygame.sprite.Sprite.kill(self)




def get_high_score():
    # Default high score
    high_score = 0

    # Try to read high score from file
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There is a file, but we don't understand the number
        print("I'm confused. Starting with no high score.")

    return high_score


def save_high_score(new_high_score):
    try:
        # Write file to disk
        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        # Can't write it
        print("Unable to save high score.")


def high_score_main():
    # Get high score
    high_score = get_high_score()

    # Get score from current game
    current_score = total_seconds

    # See if we have a new high score
    if current_score > high_score:
        # There is a new high score, save to disk
        save_high_score(current_score)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('asteroid.png')).convert_alpha()
        self.rect = self.image.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(5, 10)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.rect = self.image.get_rect(
                center=(
                    random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                    random.randint(0, SCREEN_HEIGHT)
                )
            )


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Loads sprite image
        self.image = pygame.image.load(os.path.join('chinchilla_sprite_light.png'))
        # Gets rectangle of image automatically
        self.rect = self.image.get_rect()
        # Defines coordinates of sprite spawn position
        self.rect.top = 25
        self.rect.bottom = 320
        # Defines at which speed the sprite moves
        self.speedx = 1
        self.speedy = 1

    def update(self):
        # Defines movement speed of player sprite before key gets pressed
        self.speedx = 0
        self.speedy = 0
        # Defines player movement when directional keys are pressed
        userinput = pygame.key.get_pressed()
        if userinput[pygame.K_LEFT]:
            self.speedx = -player_speed
        if userinput[pygame.K_RIGHT]:
            self.speedx = +player_speed
        if userinput[pygame.K_UP]:
            self.speedy = -player_speed
        if userinput[pygame.K_DOWN]:
            self.speedy = +player_speed

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Stops player movement when borders of screen are reached
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 736:
            self.rect.x = 736
        elif self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > 536:
            self.rect.y = 536

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y + 25
        self.rect.centerx = x + 33
        self.speedx = +25

    def update(self):
        self.rect.x += self.speedx
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


def quit_game():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()


running = True
while running:
    title()
    sound_maker()
    CANVAS.blit(HIGH_SCORE, HIGH_SCORE_RECT)
    if more_button.draw(CANVAS):
        running = True
        while running:
            setting_page()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

    if start_button.draw(CANVAS):
        # Player sprite
        player_sprite(player_x, player_y)
        run = True
        scroll = 0
        while run:
            quit_game()
            # Gets drawn first
            # Background image and coordinates of image appearance
            CANVAS.blit(BACKGROUND, (0, 0))
            clock.tick(FPS)
            for i in range(0, tiles):
                screen.blit(bg, (i * bg_width + scroll, 0))
            scroll -= 10
            if abs(scroll) > bg_width:
                scroll = 0

            test = 0
            if test == 0:
                get_high_score()
                high_score_main()

            # String formatting to format score counter by +1
            output_time = "Score {0}".format(total_seconds)

            # Timer going up
            total_seconds = start_time + (frame_count // frame_rate)

            # Increase frame count
            frame_count += 22

            # Limit frames per second
            clock.tick(frame_rate)

            # Blit score to the screen
            text_score = font_score.render(output_time, True, GREY)
            CANVAS.blit(text_score, [650, 25])

            # Spawning enemies
            enemySprites.update(CANVAS)
            enemy_timer += 1
            if enemy_timer == 40:
                enemySprites.add(Upper(random.randint(6, 10)))
                enemySprites.add(Lower(random.randint(6, 10)))
            elif enemy_timer >= 70:
                enemySprites.add(BaseEnemy(random.randint(8, 12)))
                enemy_timer = 0

            # Increase spawn frequency of existing timer
            if total_seconds >= 500:
                enemy_timer += 1

            # Time-triggered enemy spawning
            if total_seconds >= 910:
                bouncer_enemy_timer += 1
                if bouncer_enemy_timer == 90:
                    enemySprites.add(Bouncer(10))
                    bouncer_enemy_timer = 0

            pygame.time.delay(30)
            all_sprites.update()

            hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
            for hit in hits:
                m = Mob()
                all_sprites.add(m)
                mobs.add(m)
            hit = pygame.sprite.groupcollide(enemySprites, bullets, True, True)

            hits = pygame.sprite.spritecollide(player, mobs, False)
            if hits:
                run = False
                running = False

            hit = pygame.sprite.spritecollide(player, enemySprites, False)
            if hit:
                run = False
                running = False
            all_sprites.draw(screen)
            pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

if not run:
    endgame = True
    while endgame:
        game_over()
        text_score_rect = text_score.get_rect()
        text_score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        text_score = font_score_gamov.render(output_time, True, BLACK)
        CANVAS.blit(text_score, text_score_rect)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                endgame = False

            if event.type == pygame.QUIT:
                endgame = False
        pygame.display.update()