#Filename: antiFrogger.py
#Author: Trevor Hebert
#Last Modified by: Trevor Hebert
#Date Last Modified: July 12, 2012
#Program Description: This is a simple avoid the obstacles type game. Avoid the potholes, while trying to hit the frogs.
#Revision History: 2.0.0

    
import pygame, random
pygame.init()

screen = pygame.display.set_mode((640, 580))

class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/car.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init()
            self.sndSquish = pygame.mixer.Sound("Sounds/squish.ogg")
            self.sndHit = pygame.mixer.Sound("Sounds/pothole.ogg")
            self.sndEngine = pygame.mixer.Sound("Sounds/engine.ogg")
            self.sndEngine.play(-1)
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (195, mousey)
                
class GreenFrog(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/gfrog.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
    def update(self):
        self.rect.centery -= self.dy
        self.rect.centerx -= self.dx 
        if self.rect.top < 0:
            self.reset()
            
    def reset(self):
        self.rect.top = 640
        self.rect.centerx = random.randrange(500,900)
        self.dy = random.randrange(2, 6)
        self.dx = random.randrange(3,6 )
        
class RedFrog(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/rfrog.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
    def update(self):
        self.rect.centery -= self.dy
        self.rect.centerx -= self.dx 
        if self.rect.top < 0:
            self.reset()
            
    def reset(self):
        self.rect.top = 640
        self.rect.centerx = random.randrange(500,900)
        self.dy = random.randrange(1, 2)
        self.dx = random.randrange(1, 7)        
      
class PotHole(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/pothole.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()

    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.left < -75:
            self.reset()
    
    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(700,4000)  #random x placement
        self.rect.centery = random.randrange(135, 500)  #random y placement
        self.dy = 0
        self.dx = 9 # set x speed
    
class Road(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/background.gif")
        self.rect = self.image.get_rect()
        self.dy = 6
        self.reset()
        
    def update(self):
        self.rect.left -= self.dy
        if self.rect.left <= -800:
            self.reset() 
    
    def reset(self):
        self.rect.left = 1
        
class RoadBg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/background.gif")
        self.rect = self.image.get_rect()
        self.dy = 2
        self.reset()
        
    def update(self):
        self.rect.left -= self.dy
        if self.rect.left <= -800:
            self.reset() 
    
    def reset(self):
        self.rect.left = 1        

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 7
        self.score = 0
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        self.text = "Cars: %d   Score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (0, 255, 0))
        self.rect = self.image.get_rect()
    
def game():
    pygame.display.set_caption("Mail Pilot!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    car = Car()
    #create frogs
    gFrog = GreenFrog()
    gFrog2 = GreenFrog()
    gFrog3 = GreenFrog()
    gFrog4 = GreenFrog()
    gFrog5 = GreenFrog()
    rFrog = RedFrog()
    rFrog2 = RedFrog()
    #create potholes
    potHole1 = PotHole()
    potHole2 = PotHole()
    potHole3 = PotHole()
    potHole4 = PotHole()
    potHole5 = PotHole()
    potHole6 = PotHole()
    potHole7 = PotHole()
    potHole8 = PotHole()
    potHole9 = PotHole()
    potHole10 = PotHole()
    potHole11 = PotHole()
    potHole12 = PotHole()
    #create the road and scoreboard
    road = Road()
    scoreboard = Scoreboard()

    friendSprites = pygame.sprite.OrderedUpdates(road, car)
    greenFrogSprites = pygame.sprite.OrderedUpdates(gFrog, gFrog2, gFrog3, gFrog4, gFrog5)
    redFrogSprites = pygame.sprite.OrderedUpdates(rFrog, rFrog2)
    potHoleSprites = pygame.sprite.Group(potHole1, potHole2, potHole3, potHole4, potHole5, potHole6, potHole7, potHole8, potHole9, potHole10, potHole11, potHole12)
    scoreSprite = pygame.sprite.Group(scoreboard)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(60)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        
        #check collisions
        hitGreenFrogs = pygame.sprite.spritecollide(car, greenFrogSprites, False)
        if hitGreenFrogs:
            car.sndSquish.play()
            for gFrog in hitGreenFrogs:
                gFrog.reset()
            scoreboard.score += 50
        
        hitRedFrogs = pygame.sprite.spritecollide(car, redFrogSprites, False)
        if hitRedFrogs:
            car.sndSquish.play()
            for rFrog in hitRedFrogs:
                rFrog.reset()
            scoreboard.score += 500    

        hitPotHoles = pygame.sprite.spritecollide(car, potHoleSprites, False)
        if hitPotHoles:
            car.sndHit.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
            for thePotHole in hitPotHoles:
                thePotHole.reset()
        
        friendSprites.update()
        greenFrogSprites.update()
        redFrogSprites.update()
        potHoleSprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
        greenFrogSprites.draw(screen)
        redFrogSprites.draw(screen)
        potHoleSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    car.sndEngine.stop()
    #return mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score
    
def instructions(score):
    pygame.display.set_caption("Anti Frogger!")
    
    #create road
    road = RoadBg()
    
    allSprites = pygame.sprite.Group(road)
    insFont = pygame.font.SysFont(None, 38, True)
    insLabels = []
    instructions = (
    "",
    "Instructions: You are a regular guy", 
    "driving down the street. A dangerous",
    "species of frog has the tendencies",
    "to cross the road in great numbers.",
    "These frogs need to be killed to",
    "prevent further generations.",
    "",
    "It is your duty as a citizen to run",
    "over these frogs. While doing so",    
    "be careful of the potholes which",
    "will damage your car. Your car",
    "can only go over about 7 potholes",
    "before it will break down. ",
    "Steer with the mouse.",
    "",
    "Click to start, Esc to quit..."
    )
    
    title = (
    "Anti-Frogger        Last score: %d" % score ,
    ""
    )
 
    for line in title:
        tempTitleLabel = insFont.render(line, 1, (0, 255, 0))
        insLabels.append(tempTitleLabel) 
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (0, 0, 0))
        insLabels.append(tempLabel)
      
        
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
    
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
        
    #car.sndEngine.stop()    
    pygame.mouse.set_visible(True)
    return donePlaying
   

def main():
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = instructions(score)
        if not donePlaying:
            score = game()
        


if __name__ == "__main__":
    main()
    
    
