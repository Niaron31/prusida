# напиши тут свою програму
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput 
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
 
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test

from seconds import Seconds
 
age = 7
name = " "
p1, p2, p3 = 0, 0, 0
 
def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False
class page1(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        instr = Label(test=txt_instruction)
        lbl1 = Label(text = "Ім'я:")
        self.in_name=TextInput(multiline = False)

        lbl2 = Label(text = "вік")
        self.in_age=TextInput(multiline = False)

        self.btn= Button(text="Почати", size_hint = (0.3,0.5))

        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint = (0,9, None))
        line2 = BoxLayout(size_hint = (0,9, None))

        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)

        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)

        main_l1 = BoxLayout(orientation="vertical", padding = 8, spacing=8)
        main_l1.add_widget(instr)
        main_l1.add_widget(line1)
        main_l1.add_widget(line2)
        main_l1.add_widget(self.btn)

        def next(self):
            name = self.in_name.text
            age = check_int(self.in_age.text)
            if age == False or age  < 7:
                age = 7
            else:
                self.manager.current = 'page2'
class Page2Scr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(test=txt_test1)
        self.lb_sec = Seconds(15)

        lb_resul = Label(text = "Результат:")
        self.in_result = TextInput(text = "0", multiline = False)
        line = BoxLayout()
        line.add_widget(lb_resul)
        line.add_widget(self.in_result)
        
        self.btn = Button(text = "Продовжити", size_hint = (0.3,0.5))
        self.btn.on_press = self.next
        main_l2 = BoxLayout()
        main_l2.add_widget(instr)
        main_l2.add_widget(self.lb_sec)
        main_l2.add_widget(line)
        main_l2.add_widget(self.btn)





