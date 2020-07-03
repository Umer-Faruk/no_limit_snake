import pygame
import time
import random
try:
    import pkg_resources.py2_warn
    
except ImportError:
    pass
dis = pygame.display.set_mode((800,700))
pygame.display.set_caption("snake")
pygame.init()

class snake():
     def __init__(self):
          self.x= 50
          self.y= 50
          self.width = 20
          self.height = 20
          self.speed = 5
          self.snake_body = []
          self.Length_of_snake = 1
          self.nx = 0
          self.ny = 0
          self.score = 0

     

               

     def drawsnake(self):
          for i in self.snake_body:
               pygame.draw.rect(dis,(255,255,255),[i[0],i[1],20,20])





font_style = pygame.font.SysFont("Arial", 30)

def nextspeed(speed,score):
     try:
               if score% 100 == 0:
                    print("yes inscre speed")
                    speed +=2
                    return speed 
     except:
                    print("error")
     
def message(msg, color, w, h):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [w, h])




def main():
     over = True
     clock = pygame.time.Clock()
     
     
     s=snake()
     fx = 30
     fy = 90
    
     
     
     while over:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    over = False
               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                         s.nx = s.speed
                         s.ny = 0
                    elif event.key == pygame.K_LEFT:
                         s.nx = -s.speed
                         s.ny = 0
                    elif event.key == pygame.K_UP:
                         s.nx = 0
                         s.ny = -s.speed
                    elif event.key == pygame.K_DOWN:
                         s.nx = 0
                         s.ny = s.speed
                    elif event.key == pygame.K_i:
                         # print("increse speed") 
                         s.speed += 1
                    elif event.key == pygame.K_d:
               
                         # 
                         # print("decrese speed")
                         s.speed -= 1
          s.x += s.nx
          s.y += s.ny
          
          

         
         

          dis.fill((0,0,0))
          
         

          
          


          head=pygame.Rect(s.x,s.y,s.width,s.height)
          pygame.draw.rect(dis,(0,0,255),head)

          food = pygame.Rect(fx,fy,30,30)
          pygame.draw.rect(dis,(255,0,0),food)          
          snake_Head = []
          snake_Head.append(s.x)
          snake_Head.append(s.y)
          s.snake_body.append(snake_Head)

          if len(s.snake_body) > s.Length_of_snake:
            del s.snake_body[0]

          s.drawsnake()
          

          if food.colliderect(head):
               s.Length_of_snake += 5
               s.score += 10
               # s.speed=nextspeed(s.speed,s.score)
               s.speed += 0.2
               print(s.speed)
               fx = random.randrange(500)
               fy = random.randrange(500)
               
              

         
          message("Score:"+str(s.score),(255,255,0),0,0)
          #message("i +speed",(255,255,0),650,0)
          #message("d --speed",(255,255,0),650,50)
          message("spped "'{:.2f}'.format(s.speed),(255,255,0),0,50)
              

          pygame.display.update()
          
          clock.tick(30)
     pygame.quit()
     quit()

main()
