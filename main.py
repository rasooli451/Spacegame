import pygame
#Player1 Class
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/spaceship.png")
        self.image = pygame.transform.rotozoom(self.image,90,0.4)
        self.rect = self.image.get_rect(center=(100,225))
    def keyboardinput(self):
        if self.rect.right > BORDER_X:
            self.rect.right = BORDER_X - 5
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Y_HEIGHT:
            self.rect.bottom = Y_HEIGHT
        keys=pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= 10
        elif keys[pygame.K_a]:
            self.rect.x -= 10
        elif keys[pygame.K_d]:
            self.rect.x += 10
        elif keys[pygame.K_s]:
            self.rect.y += 10
    def getmidright(self):
        return self.rect.midright
    def getRect(self):
        return self.rect
    def update(self):
        self.keyboardinput()
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image=self.image=pygame.image.load(r"E:\witcher 3\spaceship.png")
        self.image = pygame.image.load("images/spaceship.png")
        self.image = pygame.transform.rotozoom(self.image,-90,0.4)
        self.rect = self.image.get_rect(center=(1100,225))
    def keyboardinput(self):
        if self.rect.left < BORDER_X:
            self.rect.left = BORDER_X + 5
        if self.rect.right > X_WIDTH:
            self.rect.right = X_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Y_HEIGHT:
            self.rect.bottom = Y_HEIGHT
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= 10
        elif keys[pygame.K_DOWN]:
            self.rect.y += 10
        elif keys[pygame.K_LEFT]:
            self.rect.x -= 10
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 10
    def getmidleft(self):
        return self.rect.midleft
    def getRect(self):
        return self.rect
    def update(self):
        self.keyboardinput()
#checks collision between bullet and player
def checkcollision(playerrect,bulletrect):
    if bulletrect.colliderect(playerrect):
        return True
    return False
def displayhealth(health, xpos, ypos):
    font=pygame.font.Font(None, 30)
    text=font.render(f"Health: {health}",False, "red")
    text_rect=text.get_rect(center=(xpos,ypos))
    screen.blit(text, text_rect)
pygame.init()
#important variables..
X_WIDTH = 1200
Y_HEIGHT = 900
FPS = 60
BULLETSPEED = 25
HEALTH = 10
MAX_BULLETS = 4
BORDER_X = X_WIDTH//2
gamestart = False
gameactive = True
gamerunning = True
bulletlistleft = []
bulletlistright = []
PLAYER1HEALTH = HEALTH
PLAYER2HEALTH = HEALTH
screen = pygame.display.set_mode((X_WIDTH,Y_HEIGHT))
pygame.display.set_caption("Spaceship fighter")
clock = pygame.time.Clock()
#making a group
f_player = pygame.sprite.GroupSingle()
P1_instance = Player1()
f_player.add(P1_instance)
P2_instance = Player2()
s_player = pygame.sprite.GroupSingle()
s_player.add(P2_instance)
#Images
BG = pygame.image.load("images/bg5.jpg")
BG = pygame.transform.scale(BG,(X_WIDTH,Y_HEIGHT)).convert_alpha()
renderer = pygame.font.Font(None,25)
bullet = pygame.image.load(
    "images/bullet.png")
bullet = pygame.transform.scale(bullet, (20, 20))
BGimage = pygame.image.load("images/SPACEBACKGROUND.jpg")
BGimage = pygame.transform.scale(BGimage,(X_WIDTH,Y_HEIGHT)).convert_alpha()
#Sounds
BULLETSOUND = pygame.mixer.Sound("sounds/Firing sound.wav")
EXPLOSIONSOUND = pygame.mixer.Sound("sounds/Explosion sound.wav")
#texts
welcme_text = renderer.render("SPACESHOOTER 2PLAYER",False,"red")
welcme_txt_rect = welcme_text.get_rect(center=(600,250))
instruc_txt = renderer.render("press P to play, Q to quit",False,"green")
instruc_txt_rect = instruc_txt.get_rect(center=(600,400))
player1wins = renderer.render("Player 1 won!!!",False,"red")
player1wins_rect = player1wins.get_rect(center=(600,250))
player2wins = renderer.render("Player2 won!!!", False, "red")
player2wins_rect = player2wins.get_rect(center=(600,250))
while gameactive:
    if gamerunning:
        screen.blit(BGimage,(0,0))
        screen.blit(welcme_text, welcme_txt_rect)
        screen.blit(instruc_txt, instruc_txt_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gamestart = True
                if event.key == pygame.K_q:
                    gameactive = False
        pygame.display.update()
        clock.tick(FPS)
        while gamestart:
            if PLAYER1HEALTH > 0 and PLAYER2HEALTH > 0:
                key = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            BULLETSOUND.play()
                            position = Player1.getmidright(P1_instance)
                            bulrect = bullet.get_rect(midleft=position)
                            bulletlistleft.append(bulrect)
                            if len(bulletlistleft) > MAX_BULLETS:
                                 del bulletlistleft[0]
                        if event.key == pygame.K_RCTRL:
                            BULLETSOUND.play()
                            position = Player2.getmidleft(P2_instance)
                            bulrect = bullet.get_rect(midright=position)
                            bulletlistright.append(bulrect)
                            if len(bulletlistright) > MAX_BULLETS:
                                del bulletlistright[0]
                screen.blit(BG,(0,0))
                pygame.draw.rect(screen,"black",[BORDER_X,0,20,900])
                f_player.draw(screen)
                f_player.update()
                s_player.draw(screen)
                s_player.update()
                displayhealth(PLAYER1HEALTH,100,50)
                displayhealth(PLAYER2HEALTH, 1100, 50)
                for rect in bulletlistleft:
                    screen.blit(bullet, rect)
                    rect.x += BULLETSPEED
                    if checkcollision(Player2.getRect(P2_instance),rect):
                         EXPLOSIONSOUND.play()
                         PLAYER2HEALTH -= 1
                         bulletlistleft.remove(rect)
                for rect in bulletlistright:
                     screen.blit(bullet, rect)
                     rect.x -= BULLETSPEED
                     if checkcollision(Player1.getRect(P1_instance),rect):
                        EXPLOSIONSOUND.play()
                        PLAYER1HEALTH -= 1
                        bulletlistright.remove(rect)
                pygame.display.update()
                clock.tick(FPS)
            else:
                gamerunning = False
                gamestart = False
    else:
        screen.blit(BGimage, (0, 0))
        if PLAYER1HEALTH > 0:
            screen.blit(player1wins, player1wins_rect)
        else:
            screen.blit(player2wins, player2wins_rect)
        screen.blit(instruc_txt, instruc_txt_rect)
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    PLAYER1HEALTH = 10
                    PLAYER2HEALTH = 10
                    bulletlistright = []
                    bulletlistleft = []
                    gamerunning = True
                    gamestart = True
                if event.key == pygame.K_q:
                    gameactive = False
