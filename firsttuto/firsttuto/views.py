from django.views.generic import TemplateView

class IndexView(TemplateView):
  template_name = 'index.html'

class Login(TemplateView):
  template_name = 'login.html'

class RegisterView(TemplateView):
  template_name = 'register.html'

class LogoutView(TemplateView):
  template_name = 'logout.html'