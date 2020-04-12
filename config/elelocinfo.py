#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import yaml
#打开yaml元素包
patth = os.getcwd()
parent_path = os.path.dirname(patth)
file = open(parent_path + '/data/elelocinfo.yaml', 'r', encoding='utf-8')
data = yaml.load(file)
file.close()

# 登录页面元素
username_xpath = data['login']['username_xpath']
password_id = data['login']['password_id']
login_btn_xpath = data['login']['login_btn_xpath']
account_text_xpath = data['login']['account_text_xpath']
exist_id = data['login']['exist_id']
#退出按钮
logout_xpath = data['logout']['logout_xpath']
#首页页面元素
huidaodingbu_id = data['first_pager']['huidaodingbu_id']
spfl_xpath = data['first_pager']['spfl_xpath']
shangpinfenlei_xpath = data['first_pager']['shangpinfenlei_xpath']
zbnf_xpath= data['first_pager']['zbnf_xpath']
zhengbannaifen_xpath= data['first_pager']['zhengbannaifen_xpath']
myyp_xpath= data['first_pager']['myyp_xpath']
muyingyongpin_xpath= data['first_pager']['muyingyongpin_xpath']
mzgh_xpath= data['first_pager']['mzgh_xpath']
meizhuanggeghu_xpath= data['first_pager']['meizhuanggeghu_xpath']
yybj_xpath = data['first_pager']['yybj_xpath']
yingyangbaojian= data['first_pager']['yingyangbaojian']
qt_xpath = data['first_pager']['qt_xpath']
qita_xpath = data['first_pager']['qita_xpath']
page_xpath = data['first_pager']['page_xpath']
page_xpath1 = data['first_pager']['page_xpath1']
page_xpath2 = data['first_pager']['page_xpath2']
country_xpath = data['first_pager']['country_xpath']
top_brand_xpath = data['first_pager']['top_brand_xpath']
sub_bar = data['first_pager']['sub_bar']
sub_sort = data['first_pager']['sub_sort']
search_btn_id = data['search']['search_btn_id']
productsysno_xpath = data['search']['productsysno_xpath']
search_shopping_id = data['search']['search_shopping_id']
ProductSysNo_number_class = data['ProductDetail']['ProductSysNo_number_class']
Order_Now_class = data['ProductDetail']['Order_Now_class']
Entry_into_the_bill_of_goods_class = data['ProductDetail']["Entry_into_the_bill_of_goods_class"]
myJhds_icon_class = data['ProductDetail']['myJhds_icon_class']
select_All_class = data['ProductDetail']['select_All_class']
settlement_class = data['ProductDetail']["settlement_class"]
Adress_Consignee_class = data['ProductDetail']['Adress_Consignee_class']
Adress_Contact_number_class = data['ProductDetail']['Adress_Contact_number_class']
Adress_ID_number_class = data['ProductDetail']['Adress_ID_number_class']
Adress_province_class = data['ProductDetail']['Adress_province_class']
Adress_city_class = data['ProductDetail']['Adress_city_class']
Adress_area_class = data['ProductDetail']['Adress_area_class']
Adress_Detailed_class = data['ProductDetail']['Adress_Detailed_class']
Distribution_class = data['ProductDetail']['Distribution_class']
Distribution_id = data['ProductDetail']['Distribution_id']
Distribution_xpath = data['ProductDetail']['Distribution_xpath']
submit_order_id = data['ProductDetail']['submit_order_id']
attention = data['ProductDetail']['attention']
attention_Popup_xpath = data['ProductDetail']['attention_Popup_xpath']
goodsInfo_xpath = data["personal_center"]["goodsInfo_xpath"]