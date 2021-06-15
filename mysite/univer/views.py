from .serializer import UniversitySerializer, FacultySerializer, ChairSerializer, GroupSerializer, TeacherSerializer, StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from .models import *
from rest_framework.exceptions import NotFound
from . import servise


class UniversityView(GenericAPIView):
    serializer_class = UniversitySerializer

    def get_object(self, *args, **kwargs):
        try:
            university = University.objects.get(id=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return university

    def get(self, request, pk=None):
        if pk:
            univ = servise.get_university(univ_id=pk)
            if not univ:
                raise NotFound('University not found')
            return Response(univ, status=status.HTTP_200_OK)
        else:
            univs = servise.get_universitys()
            return Response(univs, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        univer = self.get_object(id=pk)
        serializer = self.get_serializer(data=request.data, instance=univer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        univer = University.objects.get(id=pk)
        univer.delete()
        return Response({"delete": f"University with pk = {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)


class FacultyView(GenericAPIView):
    serializer_class = FacultySerializer

    def get_object(self, *args, **kwargs):
        try:
            faculty = Faculty.objects.get(id=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return faculty

    def get(self, request, pk=None):
        if pk:
            faculty = servise.get_faculty(fac_id=pk)
            if faculty is None:
                raise NotFound('Faculty not found')
            return Response(faculty, status=status.HTTP_200_OK)
        else:
            faculties = servise.get_faculties()
            return Response(faculties, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        faculty = self.get_object(id=pk)
        serializer = self.get_serializer(data=request.data, instance=faculty)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        faculty = Faculty.objects.get(id=pk)
        faculty.delete()
        return Response({'delete': f"Faculty with pk = {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)


class ChairView(GenericAPIView):
    serializer_class = ChairSerializer

    def get_object(self, *args, **kwargs):
        try:
            chair = Chair.objects.get(id=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return chair

    def get(self, request, pk=None):
        if pk:
            chair = servise.get_chair(car_id=pk)
            if chair is None:
                raise NotFound('Chair not found')
            return Response(chair, status=status.HTTP_200_OK)
        else:
            chairs = servise.get_chairs()
            return Response(chairs, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        chair = self.get_object(id=pk)
        serializer = self.get_serializer(data=request.data, instance=chair)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        chair = Chair.objects.get(id=pk)
        chair.delete()
        return Response({'delete': f"Chair with pk = {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)


class GroupView(GenericAPIView):
    serializer_class = GroupSerializer

    def get_object(self, *args, **kwargs):
        try:
            group = Group.objects.get(id=kwargs['pk'])
        except Exception as e:
            raise NotFound("Group not found")
        return group

    def get(self, request, pk=None):
        if pk:
            group = servise.get_group(group_id=pk)
            if group is None:
                raise NotFound('Group not found')
            return Response(group, status=status.HTTP_200_OK)
        else:
            groups = servise.get_groups()
            return Response(groups, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        group = self.get_object(id=pk)
        serializer = self.get_serializer(data=request.data, instance=group)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        group = Group.objects.get(id=pk)
        group.delete()
        return Response({'delete': f"Group with pk = {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)


class TeacherView(GenericAPIView):
    serializer_class = TeacherSerializer

    def get_object(self, *args, **kwargs):
        try:
            teacher = Teacher.objects.get(id=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return teacher

    def get(self, request, pk=None):
        if pk:
            teacher = servise.get_teacher(teach_id=pk)
            if teacher is None:
                raise NotFound
            return Response(teacher, status=status.HTTP_200_OK)
        else:
            teachers = servise.get_teachers()
            return Response(teachers, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        teacher = self.get_object(id=pk)
        serializer = self.get_serializer(data=request.data, instance=teacher)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delet(self, request, pk):
        teacher = Teacher.objects.get(id=pk)
        teacher.delete()
        return Response({'delete': f"Teacher with pk = {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)


class StudentView(GenericAPIView):
    serializer_class = StudentSerializer

    def get_object(self, *args, **kwargs):
        try:
            student = Student.objects.get(id=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return student

    def get(self, request, pk=None):
        if pk:
            student = servise.get_student(std_id=pk)
            if student is None:
                raise NotFound('Student not found')
            return Response(student, status=status.HTTP_200_OK)
        else:
            students = servise.get_students()
            return Response(students, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        student = self.get_object(id=pk)
        serializer = self.get_serializer(data=request.data, instance=student)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({'delete': f"Student with pk = {pk} has been deleted successfully!"}, status=status.HTTP_200_OK)
