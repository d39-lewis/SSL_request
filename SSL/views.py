from django.views import View
from django.shortcuts import render
from .forms import SSLrequestform
from .SSLREQUEST import SSLRequest


class SSLView(View):
    def get(self, request):
        context = {
            'form': SSLrequestform()
        }
        return render(request,"SSL/user.html", context=context)

    def post(self, request):
        form = SSLrequestform(request.POST)
        if form.is_valid():
            # Save the data to the SSLRequest model
            request = SSLRequest(
                domain= form.cleaned_data['domain'],
                country= form.cleaned_data['country'],
                state= form.cleaned_data['state'],
                locality= form.cleaned_data['locality'],
                organization= form.cleaned_data['organization'],

            )

            print(request)
            return


        # Render the SSL request form template with the form instance
        return render(request, "SSL/user.html", {"form": form})
