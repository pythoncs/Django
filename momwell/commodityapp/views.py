from django.shortcuts import render, redirect
from .models import BigClassify, SmallClassify, Commodity, BuyToday, User, ShopCart
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.core.paginator import Paginator
from haystack.views import SearchView
from django.views.generic.base import View


# Create your views here.


# 注册
def register(request):
    # 注册后cookie会显示出内容 有很多bug 有更好的方式 尝试
    if request.method == 'GET':
        return render(request, 'commodityapp/register.html')
    else:
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        password_1 = request.POST.get('pnum')
        password_2 = request.POST.get('two_pnum')
        message = '所有字段必须填写完整'
        if name and password_1 and password_2 and phone:
            if len(phone) == 11:
                if len(password_1) > 8:

                    try:
                        user = User.objects.get(u_phone=phone)
                        message = '该手机号已注册'
                        return render(request, 'commodityapp/register.html', locals())
                    except:
                        if password_1 == password_2:
                            u = User()
                            u.u_phone = phone
                            u.u_name = name
                            password = make_password(password_1)
                            print('注册密码：', password)
                            u.u_password = password
                            u.save()
                            return redirect('commodity:login')
                        else:
                            message = '密码不一致'
                            return render(request, 'commodityapp/register.html', locals())

                else:
                    message = '密码至少8位或以上'
                    return render(request, 'commodityapp/register.html', locals())
            else:
                message = '请认真填写手机号'
                return render(request, 'commodityapp/register.html', locals())
        else:
            return render(request, 'commodityapp/register.html', locals())


def login(request):
    if request.method == 'GET':
        return render(request, 'commodityapp/login.html')
    else:
        phone = request.POST.get('phone')
        password = request.POST.get('pnum')
        message = '账号或密码不能为空'
        # 判断字段是否为空
        if phone and password:
            try:
                # 判断用户输入的账号和密码与数据库中的是否一致
                user = User.objects.get(u_phone=phone)
                if check_password(password, user.u_password):
                    # 状态保持
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['name'] = user.u_name
                    return redirect('commodity:index')
                else:
                    return render(request, 'commodityapp/login.html', {'message': '密码错误'})

            except:
                message = '账号或密码错误，请重新输入'
                return render(request, 'commodityapp/login.html', locals())
        else:
            return render(request, 'commodityapp/login.html', locals())


# 注销
def logout(request):
    request.session['is_login'] = False
    request.session.flush()
    return redirect('commodity:index')


# 首页
def index(request):
    try:
        userId = request.session.get('user_id')
        shop = ShopCart.objects.filter(user_id=userId).count()
        request.session['shop_num'] = shop
    except:
        pass
    # 大分类所有内容
    bigc = BigClassify.objects.all()
    # 今日必抢 按原价-时价最大的排序 只要8个
    comms = Commodity.objects.all()
    # 热销推荐 销量最高的
    sales = Commodity.objects.order_by('-c_sales')[0]
    sales1 = Commodity.objects.order_by('-c_sales')[1]
    sales2 = Commodity.objects.order_by('-c_sales')[2]
    sales3 = Commodity.objects.order_by('-c_sales')[3]
    sales4 = Commodity.objects.order_by('-c_sales')[5]
    sales5 = Commodity.objects.order_by('-c_sales')[6]
    sales6 = Commodity.objects.order_by('-c_sales')[7]

    # 宝宝服饰
    wear = SmallClassify.objects.get(s_title='童装')
    wear_comm = wear.commodity_set.all()[0:5]
    # 奶粉辅食 ---------------------------------------  改
    milk = SmallClassify.objects.get(s_title='奶粉')
    milk_comm = BigClassify.objects.get(b_title='奶粉辅食').smallclassify_set.get(s_title='奶粉').commodity_set.all()[0:3]
    food_comm = BigClassify.objects.get(b_title='奶粉辅食').smallclassify_set.get(s_title='辅食').commodity_set.all()[0:2]
    # 儿童用品
    things = SmallClassify.objects.get(s_title='孕婴童用品')
    childs = SmallClassify.objects.get(s_title='孕婴童用品').commodity_set.all()[0:2]
    child_shoes = SmallClassify.objects.get(s_title='童鞋').commodity_set.all()
    # 更多推荐
    more_recommend = Commodity.objects.filter(c_is_newProduct=True)[0:32]
    # 轮播图跳转--->奶粉
    milk_powder = SmallClassify.objects.get(s_title='奶粉')
    return render(request, 'commodityapp/index.html', locals())


# 全文检索 重写父类get_context方法  加入自己的数据
class Search(SearchView):
    def get_context(self):
        (paginator, page) = self.build_page()

        bigcls = BigClassify.objects.all()
        context = {
            'query': self.query,
            'form': self.form,
            'page': page,
            'paginator': paginator,
            'suggestion': None,
            'bigcls': bigcls,
        }
        if hasattr(self.results, 'query') and self.results.query.backend.include_spelling:
            context['suggestion'] = self.form.get_suggestion()

        context.update(self.extra_context())

        return context


# 所有商品
def commoditys(request, cid='', pindex='', sid=''):
    # -------------------------------- 查询关键字传参和位置参数的区别
    if cid == '':
        bigcls = BigClassify.objects.all()
        # 搜索关键字
        keyword = request.GET.get('keyword')
        if pindex == '':
            pindex = '1'
        pindex = int(pindex)

        if sid == '':
            comm = Commodity.objects.all()
            # 分页 按每页20条数据
            pc = Paginator(comm, 9)
            # 获取第pIndex页的数据
            pcindex_queryList = pc.page(pindex)
            # 获取所有页码
            pcList = pc.page_range
        # 销量
        elif sid == '1':
            comm = Commodity.objects.order_by('-c_sales')
            pc = Paginator(comm, 6)
            pcindex_queryList = pc.page(pindex)
            pcList = pc.page_range
        # 价格
        elif sid == '2':
            comm = Commodity.objects.order_by('current_price')
            pc = Paginator(comm, 6)
            pcindex_queryList = pc.page(pindex)
            pcList = pc.page_range
        # 是否为新品
        elif sid == '3':
            comm = Commodity.objects.filter(c_is_newProduct=True)
            pc = Paginator(comm, 6)
            pcindex_queryList = pc.page(pindex)
            pcList = pc.page_range
        # 是否收藏
        elif sid == '4':
            comm = Commodity.objects.filter(c_is_collect=True)
            pc = Paginator(comm, 6)
            pcindex_queryList = pc.page(pindex)
            pcList = pc.page_range

        return render(request, 'commodityapp/commodity.html', locals())
    else:
        bigcls = BigClassify.objects.all()
        if pindex == '':
            pindex = '1'
        pindex = int(pindex)
        # 小标题下全部无序排列
        if sid == '':
            comm = SmallClassify.objects.get(id=cid).commodity_set.all()
            pc = Paginator(comm, 2)
            pcindex_queryList = pc.page(pindex)
            pcList = pc.page_range
        # 按销量
        elif sid == '1':
            comm = SmallClassify.objects.get(id=cid).commodity_set.order_by('-c_sales')
            pc = Paginator(comm, 2)
            pcindex_queryList = pc.page(pindex)
            pcList = pc.page_range
        # 按价格
        elif sid == '2':
            comm = SmallClassify.objects.get(id=cid).commodity_set.order_by('current_price')
            pc = Paginator(comm, 2)
            pcindex_queryList = pc.page(pindex)
            pcList = pc.page_range
        # 按是否新品
        elif sid == '3':
            comm = SmallClassify.objects.get(id=cid).commodity_set.filter(c_is_newProduct=True)
            pc = Paginator(comm, 2)
            pcindex_queryList = pc.page(pindex)
            pcList = pc.page_range
        # 按是否收藏
        elif sid == '4':
            comm = SmallClassify.objects.get(id=cid).commodity_set.filter(c_is_collect=True)
            pc = Paginator(comm, 2)
            pcindex_queryList = pc.page(pindex)
            pcList = pc.page_range

        return render(request, 'commodityapp/commodity.html', locals())


# 单商品详情页
def details(request, cid='', bid=''):
    if cid:
        # 商品信息
        commInfo = Commodity.objects.get(pk=cid)
        # 相关推荐 step1：获取商品类别 step2:获取商品类别的大类别下所有商品销量最高的6个
        salesTop = commInfo.small_classify.commodity_set.exclude(id=commInfo.id).order_by('-c_sales')

        return render(request, 'commodityapp/details.html', locals())
    if bid:
        commInfo = BuyToday.objects.get(pk=bid)
        salesTop = BuyToday.objects.exclude(id=bid).order_by('-b_sales')[:3]
        return render(request, 'commodityapp/details.html', locals())


# 今日团购
def buyToday(request):
    # 今日团购 按库存
    bts = BuyToday.objects.order_by('-b_repertory')
    # 明日预告 按打折率
    temorrow_advance = BuyToday.objects.order_by('b_reducedRate')
    # 团购热销榜
    salesTop = BuyToday.objects.order_by('-b_sales')[0:3]
    return render(request, 'commodityapp/buytoday.html', locals())


# 购物车
class ShopcartsView(View):
    def get(self, request, cid=''):

        """
        每个用户都有自己的用户车  模型自关联 用户ID 用户名 商品
        step1：获取该用户id     request.session['user_id'] = user.id
        step2：获取加入购物车的商品信息
        step3：将商品信息存入数据库

        :param request:
        :param cid: 详情页传过来的商品id

        """
        try:
            # 获取用户ID
            userId = request.session.get('user_id')
            try:
                # 获取详情页传来的商品信息
                commIndfo = Commodity.objects.get(pk=cid)
                # 将商品信息存入数据库
                try:
                    # 如果同一个用户将同一件商品加入购物车，数据库中直接将该用户的同件数量加传进来的数量
                    cart = User.objects.get(id=userId).shopcart_set.get(cart_commoditys_id=cid)
                    print(cart)
                    cart.commodity_nums += int(request.GET.get('nums'))
                    cart.save()
                except Exception as e:
                    commod = Commodity.objects.get(id=cid)
                    commod.user.add(userId)
                    commod.save()
                    cart = ShopCart()
                    cart.cart_commoditys_id = cid
                    cart.commodity_nums = request.GET.get('nums')
                    cart.user_id = User.objects.get(id=userId)
                    cart.save()

                # 获取购物车信息
                commIndfo = User.objects.get(id=userId).commodity_set.all()
                return render(request, 'commodityapp/shopcart.html', locals())

            except Exception as e:
                # 获取登录者加入购物车商品信息
                commIndfo = User.objects.get(id=userId).commodity_set.all()
                # message = e
                return render(request, 'commodityapp/shopcart.html', locals())

        # 没有获取到用户ID
        except Exception as e:
            message = '请登录后再进购物车'
            return render(request, 'commodityapp/login.html', locals())

    def post(self, request):
        pass


# 购物车删除某条数据
def delete(request, cid=''):
    '''
    如果点击删除，清空Commodity类user_id,删除ShopCart中传入商品ID的一条数据
    :param cid: 传入商品ID
    :return:
    '''
    userId = request.session.get('user_id')
    cartCls = User.objects.get(id=userId).shopcart_set.get(cart_commoditys_id=cid)
    cartCls.delete()
    commCls = User.objects.get(id=userId).commodity_set.get(id=cid)
    commCls.user.remove(userId)
    commCls.save()
    # 获取登录者加入购物车商品删除后的信息
    commIndfo = User.objects.get(id=userId).commodity_set.all()
    if commIndfo:
        return render(request, 'commodityapp/shopcart.html', locals())
    else:
        message = '没有商品，请添加要购买的宝贝'
        return render(request, 'commodityapp/shopcart.html', locals())








# 结算
def settlement(request):
    '''
    当点击结算的时候 删除该用户ShopCart全部数据，删除该用户所有商品user_id
    :param request:
    :return:
    '''
    userId = request.session.get('user_id')
    # 获取结算商品ID
    single = request.GET.getlist('single')
    # 删除商品user_id
    for cid in single:
        commCls = Commodity.objects.get(id=cid)
        commCls.user.remove(userId)
        # 删除该用户shopCart数据
        cartCls = ShopCart.objects.filter(user_id=userId).get(cart_commoditys_id=cid)
        cartCls.delete()

    commIndfo = User.objects.get(id=userId).commodity_set.all()
    if commIndfo:
        return render(request, 'commodityapp/shopcart.html', locals())
    else:
        message = '没有商品，请添加要购买的宝贝'
        return render(request, 'commodityapp/shopcart.html', locals())


def about(request):
    return render(request, 'commodityapp/about.html')


def information(request):
    return render(request, 'commodityapp/information.html')
