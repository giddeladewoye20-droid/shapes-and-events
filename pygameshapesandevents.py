import  pygame
import random



WIDTH=600
HEIGHT=600
TITLE="PAQUETA CRISPS"

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PAQUETA CRISPS")
run=True

class Circle():
    def __init__(self):
        self.color="red"
        self.radius=50
        self.x=300
        self.y=300
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,WIDTH)

object=Circle()

        
while run==True:
    screen.fill("teal")
    object.draw()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            object.radius=object.radius+10
        if event.type==pygame.MOUSEBUTTONUP:
            object.color=("yellow")
            object.x=random.randint(100,300)
            object.y=random.randint(100,300)
        if event.type==pygame.MOUSEMOTION:
            position=pygame.mouse.get_pos()
            object.x,object.y=position
    
    pygame.display.update()

    

            