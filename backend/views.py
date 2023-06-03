from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status as drf_status
from backend.models import Employee
from backend.report_serializers import ReportSerializer
from rest_framework.response import Response
# Create your views here.
class EmployeeReport(APIView):
    def get(self, request):
        emp_list = Employee.objects.all()
        data = ReportSerializer(emp_list, many=True).data


        

        status, message, data = (
        drf_status.HTTP_200_OK,
        True,
        {
            "data": data,
            "error": "",
            "message": "success"
        }
        )

        body = {
        "status": status,
        "message": message,
        "data": data,
        }
        return Response(status=status, data=body, headers={"Cache-Control": "no-cache"})
    

    def post(self,request):
        try:
            payload =request.data
            emp = ReportSerializer(data=payload)
            if emp.is_valid(raise_exception=True):
                emp.save()
            status, message, data = (
            drf_status.HTTP_200_OK,
            True,
            {
                "data": {"message":"employeecreated succufull"},
                "error": "",
                "message": "success"
            }
            )

            body = {
            "status": status,
            "message": message,
            "data": data,
            }
            return Response(status=status, data=body, headers={"Cache-Control": "no-cache"})
        except Exception as e:
            status, message, data = (
            drf_status.HTTP_400_BAD_REQUEST,
            False,
            {
                "data": {},
                "error": str(e),
                "message": "success"
            }
            )

            body = {
            "status": status,
            "message": message,
            "data": data,
            }
            return Response(status=status, data=body, headers={"Cache-Control": "no-cache"})


    
class EmployeeDetail(APIView):
    def get(self,request):
        emp_id = request.query_params.get("emp_id")
        
        try: 
            emp = Employee.objects.get(emp_id = emp_id)
            data = ReportSerializer(emp).data
            status, message, data = (
            drf_status.HTTP_200_OK,
            True,
            {
                "data": data,
                "error": "",
                "message": "success"
            }
            )

            body = {
            "status": status,
            "message": message,
            "data": data,
            }
            return Response(status=status, data=body, headers={"Cache-Control": "no-cache"})
        
        except Exception as e:
            status, message, data = (
            drf_status.HTTP_400_BAD_REQUEST,
            False,
            {
                "data":{},
                "error": "Not a valid id",
                "message": "Failure"
            }
            )

            body = {
            "status": status,
            "message": message,
            "data": data,
            }
            return Response(status=status, data=body, headers={"Cache-Control": "no-cache"})

        
