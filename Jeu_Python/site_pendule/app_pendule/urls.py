from django.urls import path
from .views import home
from .views import process_form
from .views import guess_letter

from  django.conf import  settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home,name='home'),
    path('process_form/', process_form, name='process_form'),
    path('guess_letter/', guess_letter, name='guess_letter'),
]