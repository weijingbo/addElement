"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('getSpectrumConfig/experimentId=<int:experiment_id>&consId=<int:cons_id>', views.getSpectrumConfig),
    path('saveSpectrumConfig', views.saveSpectrumConfig),
    path('getExperimentDetail/<int:experiment_id>', views.getExperimentDetail),

    path('experiment/<int:experiment_id>/addConstellationGroup', views.addConstellationGroup),
    path('deleteConstellationGroupList', views.deleteConstellationGroupList),

    path('addConstellation', views.addConstellation),
    path('deleteConstellation', views.deleteConstellation),
    path('modifyConstellationName',views.modifyConstellationName),

    path('modifyNodeDeviceList',views.modifyNodeDeviceList),

    path('modifyGroundRegionAndTerminal', views.modifyGroundRegionAndTerminal),
    path('deleteGroundRegionAndTerminal', views.deleteGroundRegionAndTerminal),
    path('modifyNode', views.modifyNode),
    path('deleteNodeList', views.deleteNodeList),

    path('user/login',views.login)
]
