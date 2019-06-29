from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import AreaInfo,UploadImage
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os


def showarea(request):

    return render(request,'areas.html')


def get_province(request):
    #获取省
    province = AreaInfo.objects.filter(parent__isnull=True).values()
    # print(province)
    return JsonResponse({'data':list(province)})

@csrf_exempt
def get_city(request,id):
    city = AreaInfo.objects.filter(parent_id=id).values()
    # print(city)
    return JsonResponse({'data':list(city)})

@csrf_exempt
def showImage(request):
    if request.method == 'GET':
        return render(request,'uploadPic.html')
    else:
        # 获取上传图片 二进制格式
        pic = request.FILES.get('pic')
        # 构建路径
        pic_path = os.path.join(settings.MEDIA_ROOT,pic.name)
        print(pic_path)
        # 将图片写入指定路径
        with open(pic_path,'wb') as f:
            # chunks():将图片切片
            for i in pic.chunks():
                f.write(i)
        # 将数据存入数据库
        u = UploadImage()
        u.utitle = pic.name
        u.uhead = 'areaapp/%s'%(pic.name)
        u.save()
        return HttpResponse(pic_path)
