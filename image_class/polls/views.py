from django.http import request
from django.shortcuts import render
from django.http import HttpResponse , Http404
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import *
import io
import base64
import cv2
# from django.core.files.temp import NamedTemporaryFile
import tempfile
# from tempfile import NamedTemporaryFile
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from .forms import img_form
import numpy as np
from skin_disease import main1
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    data_img= Dataset.objects.all()
    context={'data_img':data_img}
    return render(request, 'render.html', context)


def ind(request):
    if request.method =="POST":
        m="b"
        train_list_mod=['Acne and Rosacea Photos', 'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions', 'Atopic Dermatitis Photos', 'Eczema Photos', 'Nail Fungus and other Nail Disease', 'Psoriasis pictures Lichen Planus and related diseases']
        f = request.FILES["img"]
        myfile = f.read()
        image = cv2.imdecode(np.frombuffer(myfile , np.uint8), cv2.IMREAD_UNCHANGED)
        print(image)
        x=main1.get_class(image)
        print(x)
        print(train_list_mod[x])
        z=train_list_mod[x]
        context={'m':m, 'z':z }
    else:
        m="a"
        z=""
        context={'m':m }
    return render(request, 'index.html', context)



def test(request):
    if request.method=="POST":
        train_list_mod=['Acne and Rosacea Photos', 'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions', 'Atopic Dermatitis Photos', 'Eczema Photos', 'Nail Fungus and other Nail Disease', 'Psoriasis pictures Lichen Planus and related diseases']
        f = request.FILES["img"]
        myfile = f.read()
        image = cv2.imdecode(np.frombuffer(myfile , np.uint8), cv2.IMREAD_UNCHANGED)
        print(image)
        x=main1.get_class(image)
        print(x)
        print(train_list_mod[x])
    context={}
    return render(request, 'test.html', context )


# def test(request):
#     if request.method=="POST":
#         # inImg = request.FILES["inputImage"].read()
#         input_file = request.FILES.get("inputImage")
#         # a new file which is a temp file.
#         fp = tempfile.NamedTemporaryFile()
#         # we write the uploaded image in temp file
#         for chunk in input_file.chunks():
#             fp.write(chunk)
#         # fp.write(input_file)
#         # x=fp.name + ".jgp"
#         print(fp.name)
#         # OpenCV read file
#         image = cv2.imread(fp.name)
#         print(image)
#         context={}
#     else:
#         context={}
#     return render(request, 'test.html', context )

# def test(request):
#     fr=img_form()
#     context={"fr":fr}
#     return render(request, 'test.html', context )

@api_view(['POST', 'GET'])
def get_image(request):
    if request.method == 'POST':
        ser = Image_req_serealize(data=request.data)
        if ser.is_valid():
            train_list_mod=['Acne and Rosacea Photos', 'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions', 'Atopic Dermatitis Photos', 'Eczema Photos', 'Nail Fungus and other Nail Disease', 'Psoriasis pictures Lichen Planus and related diseases']
            image = request.FILES['image'].read()
            print(image)
            image_array = cv2.imdecode(np.frombuffer(image , np.uint8), cv2.IMREAD_UNCHANGED)
            print(image_array)
            # cv2.imshow('window',image_array)
            # cv2.waitKey(0)
            # cv2.displayAllWindows()
            x=main1.get_class(image_array)
            print(x)
            print(train_list_mod[x])
            y=train_list_mod[x]
            jsss = JSONRenderer().render(y)
            # print(image)
            # print(json)
            # save_image_from_url(form,image)
            return Response( jsss , status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        raise Http404


# def save_image_from_url(model, img):
#     r = request.FILES[img]

#     img_temp = NamedTemporaryFile(delete=True)
#     img_temp.write(r.content)
#     img_temp.flush()

#     i = model.image.save("image.jpg", File(img_temp), save=True)
#     return HttpResponse(i.read(), mimetype="YOUR MIME TYPE")


@api_view(['POST'])
def data_save(request):
    serializer = Dataset_name(data=request.data)
    if serializer.is_valid():

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class Admin_Menu(APIView):
#     permission_classes = [IsAuthenticated]
#     parser_classes =[MultiPartParser, FormParser]

#     def postmenu(self, request, format=None):
#         print(request.data)
#         serializer = MenuSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

