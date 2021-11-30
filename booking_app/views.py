from rest_framework import generics,status,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from booking_app.models import Advisor
from booking_app.serializers import BookingSerializer,AdvisorSerializer




class CreateAdvisor(APIView):
    '''Creates an advisor instance, only accessible by the admin'''
    
    permission_classes =[permissions.IsAdminUser]
    
    def post(self,request):
        serializer = AdvisorSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ListAdvisor(generics.ListAPIView):
    '''Retrives a list of all advisors'''

    authentication_classes = []
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer


class BookAppointment(APIView):
    '''Creates a booking instance based on parameters provided in the URL'''
    # Use {'appointment' : '2021-12-18T10:00'} format to pass date string

    def post(self,request,user_id,advisor_id):
        
        if request.user.id == user_id:
            
            try:
                advisor = Advisor.objects.get(pk=advisor_id)
            except Advisor.DoesNotExist:
                return Response({'error':'advisor does not exist'})

            serializer = BookingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user,advisor=advisor)
                return Response({'message':'appointment booked'},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':' Token does not matches your id in URL '})


class AllAppointments(APIView):
    '''Retrives all appointments of a user'''

    def get(self,request,user_id):

        try:
            if request.user.id == user_id:
                user = get_user_model().objects.get(pk=user_id)
            else:
                return Response({'error':' Can only check your own appointments'})    
        except Advisor.DoesNotExist:
            return Response({'error':' User does not exist'})
        
        queryset = user.booking_set.all()

        serializer = BookingSerializer(queryset,many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
        




