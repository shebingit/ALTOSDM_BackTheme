

from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   
    # Head Module --------------------------------
    path('',views.head_dashboard,name='head_dashboard'),


    #Project ---------------------
    path('Work-Task/',views.HD_task_provide,name='HD_task_provide'),
    path('Our-Clients/',views.HD_client_list,name='HD_client_list'),
    path('Client-Registration/',views.HD_client_registration,name='HD_client_registration'),

    path('Work-List/',views.HD_work_list,name='HD_work_list'),
    path('Task-Allocation/',views.HD_add_details_allocate_tasks,name='HD_add_details_allocate_tasks'),
    path('Task-Details/',views.HD_work_task_details,name='HD_work_task_details'),
    


    #Schedules --------------------
    path('Schedules-Management/',views.schedules,name='schedules'),

    #Leave ------------------------
    path('Leave-Apply-Form/',views.HD_leave_apply,name='HD_leave_apply'),
    path('Leave-Pending-List/',views.HD_leave_pending,name='HD_leave_pending'),
    path('Leave-Approved-List/',views.HD_leave_approved,name='HD_leave_approved'),
    path('Leave-Declined-List/',views.HD_leave_declined,name='HD_leave_declined'),
    path('Leave-HistoryTrack/',views.HD_leave_history,name='HD_leave_history'),


    path('SignOut/',views.SignOut,name='SignOut')
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)