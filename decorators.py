from django.core.exceptions import PermissionDenied
from .models import File
def user_check(function):
    def wrap(request,*args,**kwargs):
        entry = File.objects.get(pk=kwargs['entry_id'])
        if entry.created_by == request.user:
            return function(request,*args,**kwargs)
        else:
            raise PermissionDenied
    return wrap