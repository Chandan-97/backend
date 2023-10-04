from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data

        name = data["name"] 
        email = data["email"]
        password = data["password"]
        password2 = data["password2"]
        is_ca = data["is_ca"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({"error": "Email already exists"})
            else:
                if len(password) < 6:
                    return Response({"error": "Password must be at least 6 characters"})
                else:
                    resp = ""
                    if is_ca:
                        user = User.objects.create_ca(email=email, password=password, name=name)
                        resp = "CA created successfully"
                    else:
                        user = User.objects.create_user(email=email, password=password, name=name)
                        resp = "User created successfully"
                    
                    user.save()

                    return Response({"success": resp})

        else:
            return Response({"error": "Passwords do not match"})


