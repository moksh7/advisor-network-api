from django.urls import path
from booking_app import views


urlpatterns = [
    path('administrator/advisor/',views.CreateAdvisor.as_view(),name='create_advisor'),
    path('user/<int:user_id>/advisor/',views.ListAdvisor.as_view(),name='List_advisor'),
    path('user/<int:user_id>/advisor/booking/',views.AllAppointments.as_view(),name='appointments'),
    path('user/<int:user_id>/advisor/<int:advisor_id>/',views.BookAppointment.as_view(),name='book_appointment'),
    ]
