from django.urls import path
from using_api_view import views

# Routers are used with ViewSets in django rest framework to auto config the urls.
# Routers provides a simple, quick and consistent way of wiring ViewSet logic to a set of URLs.
# OR
# router.register(r'member', views.MemberViewSet, base_name='Member')
# The base to use for the URL names that are created. If unset the basename will be automatically
# generated based on the queryset attribute of the viewset, if it has one.
# Note that if the viewset does not include a queryset attribute then you must set
# basename when registering the viewset. The basename could be anything but the convention is
# to name it the same as your model.

urlpatterns = [
    path('category_av', views.catgory_av_list),#GET and post
    path('category_av/<int:pk>', views.catgory_av_detail),#get,put,delete
    path('sub_category_av', views.sub_category_av_list),#get and post
    path('sub_category_av/<int:pk>', views.sub_category_av_detail),#get,put,delete
    path('vendor_av', views.vendor_av_list),
    path('delivery_av', views.delivery_av_list)
]
#https://127.0.0.1:8000/apiview/vendor_av