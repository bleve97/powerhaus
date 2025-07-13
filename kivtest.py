from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class MultiplyApp(BoxLayout):
    def __init__(self, **kwargs):
        super(MultiplyApp, self).__init__(orientation='vertical', **kwargs)

        self.input = TextInput(hint_text='Enter a number', multiline=False, input_filter='float')
        self.add_widget(self.input)

        self.button = Button(text='Multiply by 2')
        self.button.bind(on_press=self.multiply)
        self.add_widget(self.button)

        self.result_label = Label(text='Result will appear here')
        self.add_widget(self.result_label)

    def multiply(self, instance):
        try:
            number = float(self.input.text)
            result = number * 2
            self.result_label.text = f"Result: {result}"
        except ValueError:
            self.result_label.text = "Invalid input! Please enter a number."


class MyApp(App):
    def build(self):
        return MultiplyApp()


if __name__ == '__main__':
    MyApp().run()
