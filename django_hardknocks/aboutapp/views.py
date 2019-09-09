from django.shortcuts import render,reverse
from django.views.generic.base import View
from .models import SideShow, AboutHd, ScienceBehind, Skill, FocusPoints, Team, WorkPage, WorkCategory, Work,WorkCategoryTwo,WorkTwo,Contact,Us
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

class IndexView(View):
    def get(self, request):
        side_list = SideShow.objects.all()
        ctx = {
            'side_list': side_list
        }
        return render(request, 'index.html', ctx)

    def post(self, request):
        pass


class AboutView(View):

    def get(self, request):
        # 輪播圖
        side_list = SideShow.objects.all()
        # 關於HD
        abouthd_list = AboutHd.objects.all()
        # 背後的科學
        science_list = ScienceBehind.objects.all()
        for sciences in science_list:
            sciences.s_content = sciences.s_content[:120] + '...'
        # 技術
        skill_list = Skill.objects.all()
        # 焦点
        focuspoints_list = FocusPoints.objects.all()
        # 团队
        team_list = Team.objects.order_by('-t_contribute')[:2]
        for member in team_list:
            member.t_intro = member.t_intro[:146] + '...'
        ctx = {
            'side_list': side_list,
            'abouthd_list': abouthd_list,
            'science_list': science_list,
            'skill_list': skill_list,
            'focuspoints_list': focuspoints_list,
            'team_list': team_list,
        }
        return render(request, 'about.html', ctx)

    def post(self, request):
        pass


class OurWorkView(View):

    def get(self, request):
        side_list = SideShow.objects.all()
        # 产品页
        works = WorkPage.objects.filter(wp_title='Case show')
        # 产品类
        workcategory_list = WorkCategory.objects.all()
        # 产品
        work_list = Work.objects.all()
        ctx = {
            'side_list': side_list,
            'works': works,
            'workcategory_list': workcategory_list,
            'work_list': work_list,
        }
        return render(request, '3-column.html', ctx)

    def post(self, request):
        pass


# def workDetail(request,wid=-1):
#     workcategory_list = WorkCategory.objects.all()
#
#     side_list = SideShow.objects.all()
#     if wid != -1:
#         work_list = Work.objects.filter(w_category=wid)
#     ctx = {
#         'side_list': side_list,
#         'work_list':work_list,
#         'workcategory_list':workcategory_list
#     }
#     return render(request,'3-column.html',ctx)


def oneColumn(request):
    side_list = SideShow.objects.all()
    #产品页
    works = WorkPage.objects.filter(wp_title='Case show 2')
    #产品分类
    workcategory_list = WorkCategoryTwo.objects.all()
    #产品
    worktwo_list = WorkTwo.objects.all()
    ctx = {
        'side_list': side_list,
        'works':works,
        'workcategory_list':workcategory_list,
        'worktwo_list':worktwo_list
    }
    return render(request, '1-column.html', ctx)


class ContactView(View):
    def get(self, request):
        side_list = SideShow.objects.all()
        #contact us
        us_list = Us.objects.all()

        ctx = {
            'side_list': side_list,
            'us_list':us_list,
        }
        return render(request, 'contact.html', ctx)

    def post(self, request):
        name = request.POST.get('name')
        cemail = request.POST.get('cemail')
        ccomment = request.POST.get('ccomment')
        contact = Contact()
        contact.c_name = name
        contact.c_email = cemail
        contact.c_message = ccomment
        contact.save()

        return HttpResponseRedirect(reverse('hardknocks:index'))
        # return render(request,'contact.html')