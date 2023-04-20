
from .import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.registerpage,name="register"),
    path('login/',views.loginpage,name="login"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('otp/<uid>/',views.otp,name="otp"),
    path('customer/<uid>/',views.customer_home,name="customer"),
    path('admin_mainpage/',views.admin_mainpage,name="admin_mainpage"),
    path('adding_turf/',views.adding_turf,name="adding_turf"),
    path('About/',views.About,name="About"),
    path('booking/<turf_uid>/<uid>/',views.booking,name="booking_turf"),
    path('turf_detail/<uid>/<turf_uid>/',views.turf_detail,name="turf_detail"),
    path('payment/<turf_uid>/<uid>/<total>/',views.payment,name="payment"),
    path('success/',views.success,name="success"),
    path('delete_time_slots/',views.delete_time_slots,name="delete_time_slots"),
    path('submit_review/<turf_uid>/<uid>/', views.submit_review, name='submit_review'),
    path('basketball/',views.basketball,name="basketball"),
    path('callback/',views.callback,name="callback"),
    path('viewbooking/',views.viewbooking,name="viewbooking"),
    path('allturf/',views.allturf,name="allturf"),
    path('confirmation/<turf_uid>/<turf_name>/',views.confirm,name='confirm'),
    path('delete_confirm/<id>/<uid>/',views.delete_confirm,name='delete_confirm'),
    path('history/<uid>/',views.booked_history,name="history"),
    path('customer_details',views.customer_details,name="customer_details"),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
