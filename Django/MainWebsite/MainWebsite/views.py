from django.shortcuts import render


def welcomeView(request):
    return render(request, 'welcome.html')


# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'catalog/signup.html'
