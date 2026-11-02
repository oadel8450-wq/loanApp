# AGRICULTURAL BANK - ASHMANT
# LOAN CALCULATOR V3.1

from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, RoundedRectangle

Window.clearcolor = (0.94, 0.97, 0.94, 1)


class LoanCalculator(App):

    def build(self):
        self.title = "Agricultural Bank Ashmant"

        scroll = ScrollView()
        root = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(14),
            size_hint_y=None
        )
        root.bind(minimum_height=root.setter("height"))

        title = Label(
            text="AGRICULTURAL BANK",
            font_size="25sp",
            bold=True,
            color=(0.02, 0.35, 0.16, 1),
            size_hint_y=None,
            height=dp(65)
        )
        root.add_widget(title)

        subtitle = Label(
            text="ASHMANT BRANCH\nLOAN CALCULATOR V3.1",
            font_size="18sp",
            color=(0.1, 0.3, 0.2, 1),
            size_hint_y=None,
            height=dp(75)
        )
        root.add_widget(subtitle)

        self.amount = self.add_input(
            root, "Loan Amount (EGP)", "float"
        )

        self.rate = self.add_input(
            root, "Annual Interest Rate (%)", "float"
        )

        self.months = self.add_input(
            root, "Loan Duration (Months)", "int"
        )

        self.result = Label(
            text="Enter loan information",
            font_size="18sp",
            bold=True,
            color=(0.02, 0.35, 0.16, 1),
            size_hint_y=None,
            height=dp(130)
        )
        root.add_widget(self.result)

        calculate = Button(
            text="CALCULATE INSTALLMENT",
            size_hint_y=None,
            height=dp(58),
            background_normal="",
            background_color=(0.02, 0.42, 0.19, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        calculate.bind(on_press=self.calculate)
        root.add_widget(calculate)

        reset = Button(
            text="RESET",
            size_hint_y=None,
            height=dp(50),
            background_normal="",
            background_color=(0.35, 0.40, 0.35, 1)
        )
        reset.bind(on_press=self.reset)
        root.add_widget(reset)

        note = Label(
            text=(
                "INDICATIVE CALCULATION ONLY\n"
                "Not an official bank offer."
            ),
            font_size="12sp",
            color=(0.3, 0.3, 0.3, 1),
            size_hint_y=None,
            height=dp(65)
        )
        root.add_widget(note)

        scroll.add_widget(root)
        return scroll

    def add_input(self, root, hint, filter_type):

        field = TextInput(
            hint_text=hint,
            input_filter=filter_type,
            multiline=False,
            size_hint_y=None,
            height=dp(55),
            font_size="17sp",
            padding=dp(12)
        )

        root.add_widget(field)
        return field

    def calculate(self, instance):

        try:
            amount = float(self.amount.text)
            rate = float(self.rate.text)
            months = int(self.months.text)

            if amount <= 0 or rate < 0 or months <= 0:
                raise ValueError

            monthly_rate = rate / 1200

            if monthly_rate == 0:
                payment = amount / months
            else:
                payment = (
                    amount * monthly_rate /
                    (1 - (1 + monthly_rate) ** (-months))
                )

            total = payment * months
            interest = total - amount

            self.result.text = (
                "MONTHLY INSTALLMENT\n"
                f"{payment:,.2f} EGP\n\n"
                f"TOTAL REPAYMENT: {total:,.2f} EGP\n"
                f"TOTAL INTEREST: {interest:,.2f} EGP"
            )

        except (ValueError, ZeroDivisionError):
            self.result.text = "PLEASE ENTER VALID INFORMATION"

    def reset(self, instance):

        self.amount.text = ""
        self.rate.text = ""
        self.months.text = ""
        self.result.text = "Enter loan information"


if __name__ == "__main__":
    LoanCalculator().run()
