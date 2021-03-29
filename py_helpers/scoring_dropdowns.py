from kivymd.uix.boxlayout import MDBoxLayout
from py_helpers.IncrementValue import IncrementValue
from py_helpers.CheckValue import SingleCheckValue, DoubleCheckValue, TripleCheckValue

class AutonomousDropDown(MDBoxLayout):
    title="Autonomous:"

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app

        self.orientation = "vertical"
        self.adaptive_height = True

        self.high_goals = IncrementValue(app)
        self.high_goals.text = "High Goals"
        self.add_widget(self.high_goals)

        self.mid_goals = IncrementValue(app)
        self.mid_goals.text = "Middle Goals"
        self.add_widget(self.mid_goals)

        self.low_goals = IncrementValue(app)
        self.low_goals.text = "Low Goals"
        self.add_widget(self.low_goals)

        self.power_shots = TripleCheckValue(app)
        self.power_shots.text = "Power Shots"
        self.add_widget(self.power_shots)

        self.wobbles = DoubleCheckValue(app)
        self.wobbles.text = "Wobbles Delivered"
        self.add_widget(self.wobbles)

        self.parked = SingleCheckValue(app)
        self.parked.text = "Parked"
        self.add_widget(self.parked)



class TeleOpDropDown(MDBoxLayout):
    title="Tele-Op:"

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app

        self.orientation = "vertical"
        self.adaptive_height = True

        self.high_goals = IncrementValue(app)
        self.high_goals.text = "High Goals"
        self.add_widget(self.high_goals)

        self.mid_goals = IncrementValue(app)
        self.mid_goals.text = "Middle Goals"
        self.add_widget(self.mid_goals)

        self.low_goals = IncrementValue(app)
        self.low_goals.text = "Low Goals"
        self.add_widget(self.low_goals)

class EndgameDropDown(MDBoxLayout):
    title="Endgame:"

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app

        self.orientation = "vertical"
        self.adaptive_height = True

        self.high_goals = IncrementValue(app)
        self.high_goals.text = "High Goals"
        self.add_widget(self.high_goals)

        self.mid_goals = IncrementValue(app)
        self.mid_goals.text = "Middle Goals"
        self.add_widget(self.mid_goals)

        self.low_goals = IncrementValue(app)
        self.low_goals.text = "Low Goals"
        self.add_widget(self.low_goals)

        self.power_shots = TripleCheckValue(app)
        self.power_shots.text = "Power Shots"
        self.add_widget(self.power_shots)

        self.wobbles_drop = DoubleCheckValue(app)
        self.wobbles_drop.text = "Wobbles Dropped"
        self.add_widget(self.wobbles_drop)

        self.wobbles_start = DoubleCheckValue(app)
        self.wobbles_start.text = "Wobbles On Start Line"
        self.add_widget(self.wobbles_start)

        self.wobble_rings = IncrementValue(app)
        self.wobble_rings.text = "Rings on Wobbles"
        self.add_widget(self.wobble_rings)

class PenaltiesDropDown(MDBoxLayout):
    title="Penalties:"

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app

        self.orientation = "vertical"
        self.adaptive_height = True

        self.minors = IncrementValue(app)
        self.minors.text = "Minor Penalties"
        self.add_widget(self.minors)

        self.majors = IncrementValue(app)
        self.majors.text = "Major Penalties"
        self.add_widget(self.majors)