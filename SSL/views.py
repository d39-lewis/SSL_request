from django.http import Http404
from django.views import View
from django.shortcuts import render
from .forms import SSLrequestform
from .models import SSLRequest


class SSLView(View):
    def home(self, request):
        # Ensure the HTTP method check is case-insensitive and corrected to 'GET'.
        if request.method == 'GET':
            return render(self, request, 'SSL/home.html')
        else:
            raise Http404()  # Handle non-GET requests appropriately

    def ssl_request_view(self, request):
        if request.method == "POST":
            form = SSLrequestform(request.POST)
            if form.is_valid():
                # Save the data to the SSLRequest model
                ssl_request = SSLRequest.objects.create(
                    domain=form.cleaned_data["domain"],
                    country=form.cleaned_data["country"],
                    state=form.cleaned_data["state"],
                    locality=form.cleaned_data["locality"],
                    organisation=form.cleaned_data["organisation"],
                    san_list=form.cleaned_data.get("san_list"),
                    key_decision=form.cleaned_data["key_decision"],
                    key_yes_size=form.cleaned_data.get("key_yes_size"),
                    key_yes_password=form.cleaned_data.get("key_yes_password"),
                    key_yes_name=form.cleaned_data.get("key_yes_name") if form.cleaned_data["key_decision"] == "yes" else None,
                    key_no_name=form.cleaned_data.get("key_no_name") if form.cleaned_data["key_decision"] == "no" else None,
                )
                # Redirect to a success page or render a completion template
                return render(self, request, "SSL/complete.html", {"ssl_request": ssl_request})
        else:
            # Initialize a blank form for GET requests
            form = SSLrequestform()

        # Render the SSL request form template with the form instance
        return render(request, "SSL/user.html", {"form": form})

