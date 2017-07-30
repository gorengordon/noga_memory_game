#!/usr/bin/python
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from random import shuffle
from kivy.clock import Clock

# declaration of forms
# connection to .kv file
class FirstForm(BoxLayout):
    pass


class TheForm(BoxLayout):
    pass


class RegisterForm(BoxLayout):
    pass


class GridForm(BoxLayout):
    pass


class MyButton(Button):
    num = -1
    num_id = -1
    the_app = None
    in_the_game = True
    game_text = [
        'i want to stay at home',
        'lets play a game',
        'go to a trip',
        'dancing is fun',
        'i love nature',
        'i am the best',
        'i love my family',
        'stand on my head',
        'תיבב ראשיהל הצור ינא',
        'קחשמ קחשנ ואוב',
        'לויטל ךלנ ואוב',
        'ףיכ הז דוקרל',
        'עבט תבהוא ינא',
        'הבוט יכה ינא',
        'ילש החפשמה תא תבהוא ינא',
        'ילש שארה לע דומעת'
    ]



# the app definition
class KivyBasicApp(App):


    def button_press(self, *args):
        b = args[0]
        b.background_normal = ''
        b.background_color = (255.0/255.0,20.0/255.0,147.0/255.0, 1)
        b.text = b.game_text[b.num]
        b.font_name = 'fonts/the_font.ttf'
        self.cards_turned.append(b)
        if len(self.cards_turned) >= 2:
            if abs(self.cards_turned[0].num - self.cards_turned[1].num) == 8:
                self.cards_turned[0].in_the_game = False
                self.cards_turned[1].in_the_game = False
            Clock.schedule_once(self.turn_over_all_cards, 2.0)

    def turn_over_all_cards(self, dt):
        self.cards_turned = []
        for b in self.gf.ids['grid_id'].children:
            if b.in_the_game:
                b.background_normal = 'mandala.jpg'
                b.background_color = (1,1,1,1)
                b.text = ''
            else:
                b.background_color = (0, 0, 0, 0)
                b.disabled = True


    def build(self):
        self.cards_turned = []
        # connect internal variables to forms
        self.ff = FirstForm()
        self.tf = TheForm()
        self.rf = RegisterForm()
        self.gf = GridForm()
        number_list = range(16)
        shuffle(number_list)
        for i in range(16):
            b = MyButton()
            b.the_app = self
            b.num_id = i
            b.num = number_list[i]
            b.background_normal = 'mandala.jpg'
            b.bind(on_press=self.button_press)
            self.gf.ids['grid_id'].add_widget(b)

        # define the screen manager, moves between forms
        self.sm = ScreenManager()

        # connect each form to a screen
        # screen = Screen(name='firstform')
        # screen.add_widget(self.ff)
        # self.sm.add_widget(screen)
        #
        # screen = Screen(name='theform')
        # screen.add_widget(self.tf)
        # self.sm.add_widget(screen)
        #
        # screen = Screen(name='registerform')
        # screen.add_widget(self.rf)
        # self.sm.add_widget(screen)

        screen = Screen(name='gridform')
        screen.add_widget(self.gf)
        self.sm.add_widget(screen)

        return self.sm

    def on_pause(self):
        return True

    # functions connecting to button presses
    def login(self):
        self.sm.current = "theform"

    def register(self):
        self.sm.current = "registerform"

    def select(self):
        self.sm.current = "gridform"

if __name__ == '__main__':
    KivyBasicApp().run()