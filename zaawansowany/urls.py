from django.contrib import admin
from django.urls import path, include
from biblioteka.views import main, sending_mail, our_form
from django.contrib.auth.views import(
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('email', sending_mail),
    path('our_form', our_form, name='our_form'),

    path('password_reset', PasswordResetView.as_view()),
    path('password_reset_done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete', PasswordResetCompleteView.as_view(),name='password_reset_complete'),

path('__debug__/', include('debug_toolbar.urls')),
    ]

