from django.urls import path
from .views import UserHomeView,ProductsView,DetailsView,addtocart,CartListView,CartDeleteView,addreview,PlaceHolderView,OrderListView,cancelorder


urlpatterns = [
    path("uhome",UserHomeView.as_view(),name="uhome"),
    path("prolist/<str:cat>",ProductsView.as_view(),name="pro"),
    path("lcart",CartListView.as_view(),name="lcart"),
    path("det/<int:pid>",DetailsView.as_view(),name="det"),
    path("del/<int:cid>",CartDeleteView.as_view(),name="cdel"),
    path("acart/<int:pid>",addtocart,name="acart"),
    path("addrw/<int:pid>",addreview,name="addr"),
    path("phr/<int:cid>",PlaceHolderView.as_view(),name="phr"),
    path("orl",OrderListView.as_view(),name="orl"),
    path("codr/<int:oid>",cancelorder,name="codr"),
]