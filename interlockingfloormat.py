from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image

SS = '''
<MainScreen>:
    md_bg_color: "darkorange"
    MDLabel:
        id: label
        text: 'How many Interlocking Floor Mat might you need?'
        haligh: "center"
        pos_hint: {"center_x": 0.55, "center_y": 0.95}
        theme_text_color: "Custom"
        text_color: "brown"
    
    MDTextField:
        id: l_input
        hint_text: "How Much Meters  "
        pos_hint: {"center_x": 0.5, "center_y": 0.77}
        size_hint_x: 0.8
        mode: "rectangle"
        text_color: "brown"
        line_color_normal: "brown"
    
        
    MDTextField:
        id: h_input
        hint_text: "Of How Much meters?"
        pos_hint: {"center_x": 0.5, "center_y": 0.67}
        size_hint_x: 0.8
        mode: "rectangle"
        text_color: "brown"
        line_color_normal: "brown"



    MDTextField:
        id: d_input
        hint_text: "How much cm is the side of floor Mat?"
        pos_hint: {"center_x": 0.5, "center_y": 0.87}
        size_hint_x: 0.8
        mode: "rectangle"
        text_color: "brown"
        line_color_normal: "brown"
        
    MDRaisedButton:
        text: "Calculate"
        pos_hint: {"center_x": 0.5, "center_y": 0.58}
        md_bg_color: "brown"
        theme_text_color: "Custom"
        text_color: "white"
        on_release: root.calcular()
        
    MDLabel:
        id: result
        text: "Result "
        pos_hint: {"center_x": 0.5, "center_y": 0.52}
        halign: "center"
        theme_text_color: "Custom"
        text_color: "brown"


    Image:
        id: img
        source: 'floor.png'
        allow_stretch: True
        keep_ratio: True
        pos_hint: {"center_x":0.5,"center_y":0.26}
        
'''

class MainScreen(MDScreen):
    def calcular(self):
        try:
            l = int(self.ids.l_input.text)
            h = int(self.ids.h_input.text)
            d = int(self.ids.d_input.text)

            quadrado = d*d
            result = l * h
            result2 = quadrado/10000
            result3 = int((result / result2)+1)

            self.ids.result.text = f"You Might Need: {result3} Floor Mat"
        except ValueError:
            self.ids.result.text = "Type a valid number please"

class FloorMatApp(MDApp):
    def build(self):
        
        self.theme_cls.theme_style = "Light"  
        self.theme_cls.primary_palette = "Amber"  
        
       
        Builder.load_string(SS)
        
        
        return MainScreen()

if __name__ == '__main__':
    Window.size = (350, 650)  
    FloorMatApp().run()