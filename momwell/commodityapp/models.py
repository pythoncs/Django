from django.db import models


# Create your models here.
# 大分类 名字、索引、创建时间、更新时间、是否删除
class BigClassify(models.Model):
    b_title = models.CharField(max_length=20, verbose_name='标题')
    b_index = models.IntegerField( verbose_name='索引')
    b_createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    b_updateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    b_isDelete = models.BooleanField(default=False, verbose_name='是否删除')

    def __str__(self):
        return self.b_title

    class Meta:
        db_table = 'bigClassify'
        verbose_name = '大分类'
        verbose_name_plural = verbose_name


# 小分类 名字、索引、创建时间、更新时间、是否删除、外键
class SmallClassify(models.Model):
    s_title = models.CharField(max_length=20, verbose_name='标题')
    s_index = models.IntegerField( verbose_name='索引')
    s_createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    s_updateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    s_isDelete = models.BooleanField(default=False, verbose_name='是否删除')
    big_classify = models.ForeignKey(BigClassify)

    def __str__(self):
        return self.s_title

    class Meta:
        db_table = 'smallClassify'
        verbose_name = '小分类'
        verbose_name_plural = verbose_name




# 今日团购 title、折后价格、折前价格、折数、图片、创建时间、更新时间、是否删除、库存、是否收藏、详情属性、属性值、详情图片
class BuyToday(models.Model):
    title = models.CharField(max_length=50,verbose_name='标题')
    current_price = models.FloatField(max_length=10,verbose_name='活动价')
    original_price = models.FloatField(max_length=10,verbose_name='原价') #b_originalPrice
    b_reducedRate = models.FloatField(max_length=3,verbose_name='打折率')
    image = models.ImageField(upload_to='buyToday/',verbose_name='团购图片')
    b_createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    b_updateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    b_isDelete = models.BooleanField(default=False, verbose_name='是否删除')
    b_repertory = models.IntegerField( verbose_name='库存')
    b_is_collect = models.BooleanField(default=False, verbose_name='是否收藏')
    b_sales = models.CharField(max_length=20,verbose_name='销量',default=0)
    deatailPic = models.ImageField(upload_to='buytoday/',null=True,verbose_name='详情图片')
    attribute = models.CharField(max_length=5,null=True,default=None,verbose_name='属性')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'buyToday'
        verbose_name = '今日团购'
        verbose_name_plural = verbose_name


# 用户
class User(models.Model):
    u_phone = models.CharField(max_length=20,verbose_name='手机号')
    u_password = models.CharField(max_length=100,verbose_name='密码')
    u_name = models.CharField(max_length=10,verbose_name='昵称')

    def __str__(self):
        return self.u_name

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


# 购物车
class ShopCart(models.Model):

    cart_commoditys_id = models.IntegerField(verbose_name='购物车商品id')
    commodity_nums = models.IntegerField(default=1,verbose_name='商品数量')
    user_id = models.ForeignKey(User)


    def __str__(self):
        return str(self.user_id)

    class Meta:
        db_table = 'shopCart'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

# 商品 名字、现价、图片，季节、原价、销量、创建时间、更新时间、是否删除、库存、是否为新品、是否收藏、外键、详情属性、详情图片
# 应删除今日团购模型类 在商品类中添加字段is_buyToday
class Commodity(models.Model):
    title = models.CharField(max_length=15,verbose_name='商品标题')
    current_price = models.FloatField(max_length=10,verbose_name='时价')
    original_price = models.FloatField(max_length=10,verbose_name='原价')
    image = models.ImageField(upload_to='commodity/',verbose_name='图片')
    c_season = models.CharField(max_length=5,verbose_name='季节')
    c_sales = models.IntegerField(verbose_name='销量')
    c_createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    c_updateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    c_isDelete = models.BooleanField(default=False, verbose_name='是否删除')
    c_repertory =models.IntegerField(verbose_name='库存')
    c_is_newProduct = models.BooleanField(default=True,verbose_name='是否新品')
    c_is_collect = models.BooleanField(default=False,verbose_name='是否收藏')
    deatailPic = models.ImageField(upload_to='buytoday/',null=True,verbose_name='详情图片')
    small_classify = models.ForeignKey(SmallClassify)
    user = models.ManyToManyField(User,null=True,blank=True)
    attribute = models.CharField(max_length=5,null=True,default=None,verbose_name='属性')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'commodity'
        verbose_name = '商品'
        verbose_name_plural = verbose_name

class AttributeDetail(models.Model):
    name = models.CharField(max_length=5,verbose_name='属性详情')
    buyToday = models.ForeignKey(BuyToday)
    commoDity = models.ForeignKey(Commodity)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'AttributeDetail'
        verbose_name = '属性详情'
        verbose_name_plural = verbose_name

