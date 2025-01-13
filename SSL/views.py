from django.shortcuts import render
from django.http import Http404
from .forms import SSLrequestform
from .SSL_request import SSLRequest  # Import SSLRequest class here


def index(request, choice):
    match choice:
        case 'home':
            return render(request, 'SSL/home.html')
        case 'user':
            if request.method == 'POST':
                form = SSLrequestform(request.POST)
                if form.is_valid():
                    # Use form.cleaned_data to interact with your SSLRequest class
                    sslrequest = SSLRequest(
                        domain=form.cleaned_data["domain"],
                        country=form.cleaned_data["country"],
                        state=form.cleaned_data["state"],
                        locality=form.cleaned_data["locality"],
                        organization=form.cleaned_data["organisation"],
                        san_list=form.cleaned_data.get("san_list"),
                        key_path=None,  # Update as needed
                        key_password=form.cleaned_data.get("key_yes_password"),
                        key_size=form.cleaned_data.get("key_yes_size", 2048),
                    )
                    # Example: Redirect to a success page or render a success template
                    return render(request, 'SSL/admin.html', {'sslrequest': sslrequest})

                    # If the form is not valid, return the form with errors
                return render(request, 'SSL/user.html', {'form': form})

                # If GET request, initialize an empty form
            else:
                    form = SSLrequestform()
                    return render(request, 'SSL/user.html', {'form': form})

        case 'admin':
            return render(request, 'SSL/admin.html')
        case _:
            raise Http404()



