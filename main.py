
import math

import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from functools import partial   # to make kivy bind be useful. really?!

import mygymgear as mygg
import barbells as bb
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
Progname = 'aboc PowerHaus BarCalc'
Version = '0.1a01'
debug = True




class WarmupCalcApp(BoxLayout):
    def __init__(self, **kwargs):
        super(WarmupCalcApp, self).__init__(orientation='vertical', **kwargs)
        # defaultBB = barbellWeight
        if debug:
            print("WarmupCalcApp()")
        self.barbells = BoxLayout(orientation='horizontal')
        defaultBB = True
        for bar in mygg.myBarbells:
            print('mygg barbells : ', bar.weight, bar.name)
            if defaultBB:
                checkbox = CheckBox(group='bars',active=True)
                self.barbellWeight = bar.weight
                defaultBB = False
            else:
                checkbox = CheckBox(group='bars')
            #checkbox.bind(on_press=partial(self.setActive, bar.weight))
            checkbox.bind(active=partial(self.setActive, bar.weight))

            self.barbells.add_widget(checkbox)
            self.barbells.add_widget(Label(text=bar.name))

        self.add_widget(self.barbells)
        self.input = TextInput(hint_text = 'Workset Weight (kg)', multiline=False, input_filter='float',
                               halign='center')
        self.input.bind(on_text_validate=self.wupCalc)
        self.add_widget(self.input)

        self.result_label = Label(text='Result will appear here')
        self.add_widget(self.result_label)

    def setActive(self,bbweight: int,foo,baz):
        print(bbweight, bar.weight)
        self.barbellWeight = bbweight
        print(f'setActive() made the barbell weight {self.barbellWeight}kg')

    def wupCalc(self, instance):
        try:
            workSetWeight = float(self.input.text)
            print(f'wupCalc() Calculating aboc PH squat warmup for {worksetWeight} with the {self.barbellWeight}kg bar')
            squatWUp = bb.squatWarmupWeights(barbellWeight=self.barbellWeight, worksetWeight=workSetWeight)  #
            number = float(self.input.text)
            print("wupCalc() : ", number)
            # result = "Barbell weight : %d\n" % (int(barbellWeight))
            result = f'Warm up the bar 2 x 5 @ {squatWUp.barbellWeight:n}\n'
            result += f'2nd (40%) 1 x 5 @ {squatWUp.second:n} ({squatWUp.secondPerSide:n} per side)\n'
            result += f'3rd (60%) 1 x 5 @ {squatWUp.third:n} ({squatWUp.thirdPerSide:n} per side)\n'
            result += f'4th (80%) 1 x 2 @ {squatWUp.forth:n} ({squatWUp.forthPerSide:n} per side)\n'
            result += f'Rest for at least {squatWUp.minRestTimeMins:n} minutes\n'
            result += f'Work Set 3 x 5 @ {squatWUp.worksetWeight:n} ({squatWUp.worksetPerSide:n} per side'

            self.result_label.text = result
        except ValueError:
            self.result_label.text = "Invalid input! Please enter a number."


class BarCalcApp(App):
    # pass
    kv_directory = 'kv_files'


    def build(self):
    #    return Label()
        return WarmupCalcApp()
        # return Label(text=Progname)

if __name__ == "__main__":
    # Builder.load_file('barcalc.kv')
    worksetWeight = 72.5
    barbellWeight = 20
    print("Calculating aboc PH squat warmup for ", worksetWeight)
    print("In my gym I have ")
    for bar, num in mygg.myBarbells.items():
        print(num, bar.weight, bar.name)
    for plate, num in mygg.myPlates.items():
        print(num, plate.weight, plate.colour)
    # print(mygg.myBarbells, mygg.myWeightPlates)
    squatWUp = bb.squatWarmupWeights(barbellWeight=barbellWeight, worksetWeight=worksetWeight)
    #print(barbellWeight, squatWUp.second, squatWUp.third, squatWUp.forth, worksetWeight )
    print("Warmup for ", worksetWeight,"with a ",barbellWeight,"kg barbell")
    print("Warm up the bar, 2 x 5 @", barbellWeight)
    print("40% 1 x 5 @", squatWUp.second, "( load per side :", squatWUp.secondPerSide, ")")
    print("60% 1 x 5 @", squatWUp.third, "( load per side :", squatWUp.thirdPerSide, ")")
    print("80% 1 x 2 @", squatWUp.forth, "( load per side :", squatWUp.forthPerSide, ")")
    print("work sets 3 x 5 @", worksetWeight, "( load per side :", squatWUp.worksetPerSide, ")")

    BarCalcApp().run()