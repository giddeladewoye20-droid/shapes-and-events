import  pygame


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
        pygame.draw.circle(screen,self.color,self.radius,(self.x,self.y))

object=Circle()

        
while run==True:
    screen.fill("teal")
    object.draw()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    pygame.display.update()

    

            