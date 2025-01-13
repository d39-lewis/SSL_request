from django import forms
from django.forms import ChoiceField
from django.core.validators import RegexValidator
from SSL.SSL_request import SSLRequest


class SSLrequestform(forms.Form):
    domain = forms.CharField(
        label="Domain name",
        max_length= 1000,
        required= True,
        widget=forms.TextInput(attrs={"placeholder": "e.g., example.com"}),
        validators = [
            RegexValidator(
                regex=r"^(?!:\/\/)([a-zA-Z0-9-_]+\.)*[a-zA-Z0-9][a-zA-Z0-9-_]+\.[a-zA-Z]{2,11}?$",
                message="Enter a valid domain name.",
            )
        ],
    )

    country = forms.CharField(
        label="Country code",
        max_length= 3,
        required= True,
        widget=forms.TextInput(attrs={"placeholder": "e.g., GB"})
    )

    state = forms.CharField(
        label="State/province",
        max_length= 300,
        required= True,
        widget=forms.TextInput(attrs={"placeholder": "e.g. England"})
    )
    locality = forms.CharField(
        label="Locality/city",
        max_length= 300,
        required= True,
        widget=forms.TextInput(attrs={"placeholder": "e.g., London"})
    )

    organisation = forms.CharField(
        label="Organisation",
        max_length= 300,
        required= True,
        widget=forms.TextInput(attrs={"placeholder": "e.g. example corp"})
    )

    san_list = forms.JSONField(
        label="Subject Alternative Names (SANs)",
        required=False,
        widget=forms.HiddenInput(),  # Managed by JavaScript
        help_text="Add multiple domains for SANs.",
    )

    key_choice = [
        ("yes", "Yes"),
        ("no", "No"),
    ]

    key_decision = ChoiceField(
        choices=key_choice,
        label = "Do you need to generate a key?",
        required = True,
        widget=forms.RadioSelect(attrs={"ID": "yes or no"}),
    )

    key_yes_size = forms.IntegerField(
        label="Key size (optional), default key: 2048",
        required= False,
        initial=2048,
        widget=forms.NumberInput(attrs={"placeholder": "2048"})
    )
    key_yes_password = forms.CharField(
        label="Key password (optional)",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": " <PASSWORD>"})
    )

    key_yes_name = forms.CharField(
        label="Key name",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": ".key (not required)"})

    )
    key_no_name = forms.CharField(
        label="personal key name",
        required=True,
        widget=forms.TextInput(attrs={"placeholder": ".key (not required)"})
    )

    def clean_san_list(self):
        san_list = self.cleaned_data.get("san_list", [])
        if not isinstance(san_list, list):
            raise forms.ValidationError("SAN list must be a list of domains.")

        # Validate each domain in the list
        for domain in san_list:
            if not RegexValidator(
                    regex=r"^(?!:\/\/)([a-zA-Z0-9-_]+\.)*[a-zA-Z0-9][a-zA-Z0-9-_]+\.[a-zA-Z]{2,11}?$"
            )(domain):
                raise forms.ValidationError(f"Invalid domain in SAN list: {domain}")

        return san_list

    class Meta:
        model = SSLRequest
        fields = "__all__"
