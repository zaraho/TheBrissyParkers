from django import forms


class ParkingSearchForm(forms.Form):
    address = forms.CharField(
        label="Destination",
        max_length=255,
        widget=forms.TextInput(
            attrs={"placeholder": "e.g. George Street"}
        ),
    )

    max_distance = forms.IntegerField(
        label="Maximum distance (m)",
        min_value=100,
        max_value=5000,
        initial=1000,
    )

    required_stay = forms.DecimalField(
        label="Parking duration (hours)",
        min_value=1,
        max_value=12,
        initial=2,
    )