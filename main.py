
#Kivy Game Imports
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

#ScreenManager Imports
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager, WipeTransition
from kivy.core.audio import SoundLoader




class PongPaddle(Widget):
    score = NumericProperty(0)
    ballsound = SoundLoader.load('misc125.wav')

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset
            self.ballsound.play()

'''This is how fast the ball goes on the x and y axis. Also velocity = ReferenceListProperty from imports.'''
class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    '''This will move the ball one step. It will be called in equal intervals to animate the ball'''
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos



class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    started = False

    
'''By importing Clock and specifying the intervals we can update function of the game object to be called once every 60th of a second(60 times per second).'''
    #to start the game when it's called below on screemanager
    def __init__ (self, *args, **kwargs):
        super (PongGame, self).__init__(*args, **kwargs)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel
        self.started = True

    def update(self, dt):
        self.ball.move()

        # bounces of paddles
        if self.started:
            self.player1.bounce_ball(self.ball)
            self.player2.bounce_ball(self.ball)

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        #went of to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

        # if self.score.player1 <=3 or self.player2.score <=3:
        #     print 'Moving to level 2!'
'''This moves the rackets up and down and creates the rackets to be on the left and right side'''
    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y 



            


 

'''start up menu screen trying to add sound to it but won't load also tried adding another end game screen but it also won't go through'''
class StartMenu(ScreenManager):
    # def on_enter(self):
    #     self.entrancesong = SoundLoader.load('Detective.wav')
    #     entrancesong.play()
    pass

class EndMenu(ScreenManager):
    pass



class ScreensApp(App):
    def build(self):
        self.load_kv('pong.kv')#calls my kivy file
        return StartMenu(transition=WipeTransition())






if __name__ == '__main__':
    ScreensApp().run()





