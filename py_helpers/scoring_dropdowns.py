from kivymd.uix.boxlayout import MDBoxLayout
from py_helpers.IncrementValue import IncrementValue
from py_helpers.CheckValue import SingleCheckValue, DoubleCheckValue, TripleCheckValue

class ScoringDropDown(MDBoxLayout):
    title="Scoring:"

    scoring_elements = []

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app

        self.orientation = "vertical"
        self.adaptive_height = True

    def add_scoring(self, ValueType, text):
        scoring = ValueType(self.app)
        scoring.text = text
        self.add_widget(scoring)
        self.scoring_elements.append(scoring)
        return scoring

    def reset(self):
        for scoring in self.scoring_elements:
            scoring.reset()

    def get_title(self):
        return self.title

class AutonomousDropDown(ScoringDropDown):
    title="Autonomous:"

    def __init__(self, app, **kwargs):
        super().__init__(app, **kwargs)

        self.duck = self.add_scoring(SingleCheckValue, "Duck Delivered")
        self.unit = self.add_scoring(IncrementValue, "In Storage Unit")
        #self.hub = self.add_scoring(IncrementValue, "In Shipping Hub")
        self.low = self.add_scoring(IncrementValue, "On Level 1")
        self.middle = self.add_scoring(IncrementValue, "On Level 2")
        self.high = self.add_scoring(IncrementValue, "On Level 3")
        self.duck_bonus = self.add_scoring(DoubleCheckValue, "Duck Bonus")
        self.tse_bonus = self.add_scoring(DoubleCheckValue, "TSE Bonus")

class TeleOpDropDown(ScoringDropDown):
    title="Tele-Op:"

    def __init__(self, app, **kwargs):
        super().__init__(app, **kwargs)

        self.unit = self.add_scoring(IncrementValue, "In Storage Unit")
        self.shared = self.add_scoring(IncrementValue, "On Shared Hub")
        self.low = self.add_scoring(IncrementValue, "On Level 1")
        self.middle = self.add_scoring(IncrementValue, "On Level 2")
        self.high = self.add_scoring(IncrementValue, "On Level 3")

class EndgameDropDown(ScoringDropDown):
    title="Endgame:"

    def __init__(self, app, **kwargs):
        super().__init__(app, **kwargs)

        self.ducks = self.add_scoring(IncrementValue, "Ducks Delivered")
        self.balanced = self.add_scoring(SingleCheckValue, "Alliance Hub Balanced")
        self.tipped = self.add_scoring(SingleCheckValue, "Shared Hub Tipped")
        self.capped = self.add_scoring(DoubleCheckValue, "TSE Capped")

class PenaltiesDropDown(ScoringDropDown):
    title="Penalties:"

    def __init__(self, app, **kwargs):
        super().__init__(app, **kwargs)

        self.minors = self.add_scoring(IncrementValue, "Minor Penalties")
        self.majors = self.add_scoring(IncrementValue, "Major Penalties")