from django.shortcuts import render

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        if not request.session.get("customer"):
            return render(request, 'login.html')
        response = get_response(request)

        return response

    return middleware