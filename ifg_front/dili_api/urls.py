from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

# 공지사항 파일업로드 임시추가
#from views import my_view

from django.conf import settings
from django.conf.urls.static import static

app_name = 'dili_api'

urlpatterns = [
    path('', login_required(views.Dili_api_index.as_view()), name='dili_api'),
    url(r'^$', views.Dili_api_index.as_view(), name='dili_api'),

    #mariadb 연결 샘플
    url(r'^mariatest/', views.mariatest.as_view(), name='mariatest'),
    url(r'^getMaria/', views.getMaria, name='getMaria'),
    url(r'^getWrkTimeInfoByEml/', views.getWrkTimeInfoByEml, name='getWrkTimeInfoByEml'),
    url(r'^getYryMgmt/', views.getYryMgmt, name='getYryMgmt'),
    url(r'^scheduleMgmt/', views.scheduleMgmt, name='scheduleMgmt'),
    url(r'^scheduleMgmtPop/', views.scheduleMgmtPop.as_view(), name='scheduleMgmtPop'),
    url(r'^wrkApvlReq/', views.wrkApvlReq.as_view(), name='wrkApvlReq'),
    url(r'^yryApvlReq/', views.yryApvlReq.as_view(), name='yryApvlReq'),
    url(r'^noticeLst/', views.noticeLst.as_view(), name='noticeLst'),
    url(r'^getNoticeLst/', views.getNoticeLst, name='getNoticeLst'),
    url(r'^getNoticePopCnt/', views.getNoticePopCnt, name='getNoticePopCnt'),
    url(r'^getNoticePopUp/', views.getNoticePopUp, name='getNoticePopUp'),
    url(r'^getNoticeMjrCnt/', views.getNoticeMjrCnt, name='getNoticeMjrCnt'),
    url(r'^noticeDtl/', views.noticeDtl.as_view(), name='noticeDtl'),
    url(r'^getNoticeOne/', views.getNoticeOne, name='getNoticeOne'),
    url(r'^noticeSave/post', views.noticeSave, name='noticeSave'),
    url(r'^getWrkApvlReq/', views.getWrkApvlReq, name='getWrkApvlReq'),
    url(r'^saveApvlReq/post', views.saveApvlReq, name='saveApvlReq'),
    url(r'^apvlReqHist/', views.apvlReqHist.as_view(), name='apvlReqHist'),
    url(r'^getApvlReqHist/', views.getApvlReqHist, name='getApvlReqHist'),
    url(r'^empMgmt/', views.empMgmt.as_view(), name='empMgmt'),
    url(r'^empMgmtPop/', views.empMgmtPop.as_view(), name='empMgmtPop'),
    url(r'^getEmpList/', views.getEmpList, name='getEmpList'),
    url(r'^getEmpInfo/', views.getEmpInfo, name='getEmpInfo'),
    url(r'^getApvlReqHistDetl/', views.getApvlReqHistDetl, name='getApvlReqHistDetl'),
    url(r'^getCalendarData/', views.getCalendarData, name='getCalendarData'),
    url(r'^saveYryApvlReq/post', views.saveYryApvlReq, name='saveYryApvlReq'),
    url(r'^getWeekGridData/', views.getWeekGridData, name='getWeekGridData'),
    url(r'^getMonthGridData/', views.getMonthGridData, name='getMonthGridData'),


    # 공지사항 파일업로드 추가
    url(r'^my_view/', views.my_view, name='my-view'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)