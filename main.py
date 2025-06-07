from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import math

class CalculatorLayout(BoxLayout):
    def on_button_press(self, value):
        expr = self.ids.expression.text
        if expr == "0" or expr == "Error":
            expr = ""
        self.ids.expression.text = expr + value

    def clear_expression(self):
        self.ids.expression.text = ""
        self.ids.result.text = "Result"

    def calculate(self, expression):
        try:
            # Allow use of math functions in eval
            allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            result = str(eval(expression, {"__builtins__": None}, allowed_names))
            self.ids.result.text = result
            self.ids.expression.text = result  # Update the expression field to show the result
        except Exception:
            self.ids.result.text = "Error"

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == '__main__':
    CalculatorApp().run()
