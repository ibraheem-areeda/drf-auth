from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    message = "only owner can edit his/her feedback !!"
    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return True
        
        if request.user == obj.purcheser:
            return True 

        if request.user.id == 1:  # only ibraheem user can edit all feedbacks for all users
            return True

        else : 
            return False 
        
