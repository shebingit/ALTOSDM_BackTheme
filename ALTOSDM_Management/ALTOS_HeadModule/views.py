from django.shortcuts import render


def head_dashboard(request):
    return render(request,'HD_Dashboard.html')


#Project -------------

def HD_task_provide(request):
    return render(request,'HD_TaskProvide.html')

def HD_client_list(request):
    return render(request,'HD_ClientList.html')

def HD_client_registration(request):
    return render(request,'HD_ClientRegister.html')


def HD_work_list(request):
    return render(request,'HD_WorkList.html')

def HD_add_details_allocate_tasks(request):
    return render(request,'HD_Allocation.html')

def HD_work_task_details(request):
    return render(request,'HD_TaskDetails.html')



#Schedules -----------

def schedules(request):
    return render(request,'HD_Schedule.html')




#Leave ---------------

def HD_leave_apply(request):
    return render(request,'HD_LeaveApply.html')

def HD_leave_pending(request):
    return render(request,'HD_LeavePending.html')

def HD_leave_approved(request):
    return render(request,'HD_LeaveApproved.html')

def HD_leave_declined(request):
    return render(request,'HD_LeaveDeclined.html')

def HD_leave_history(request):
    return render(request,'HD_LeaveHistory.html')





def SignOut(request):
    return render(request,'SingIn.html')
