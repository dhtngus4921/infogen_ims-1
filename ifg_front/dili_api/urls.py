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
    url(r'^getHldyMgmt/', views.getHldyMgmt, name='getHldyMgmt'),
    url(r'^scheduleMgmt/', views.scheduleMgmt, name='scheduleMgmt'),
    url(r'^scheduleMgmtPop/', views.scheduleMgmtPop.as_view(), name='scheduleMgmtPop'),
    url(r'^wrkApvlReq/', views.wrkApvlReq.as_view(), name='wrkApvlReq'),
    url(r'^yryApvlReq/', views.yryApvlReq.as_view(), name='yryApvlReq'),
    url(r'^apvlReqPop/', views.apvlReqPop.as_view(), name='apvlReqPop'),
    url(r'^apvlReqBfrPop/', views.apvlReqBfrPop.as_view(), name='apvlReqBfrPop'),   #선결재 팝업
    url(r'^getDuplApvlReqCnt/', views.getDuplApvlReqCnt, name='getDuplApvlReqCnt'), #선결재 동일 일자 결재 건수 조회
    url(r'^apvlReqLtrPop/', views.apvlReqLtrPop.as_view(), name='apvlReqLtrPop'),   #후결재 팝업
    url(r'^apvlAcptPop/', views.apvlAcptPop.as_view(), name='apvlAcptPop'), 
    url(r'^noticeLst/', views.noticeLst.as_view(), name='noticeLst'),
    url(r'^getNoticeLst/', views.getNoticeLst, name='getNoticeLst'),
    url(r'^getNoticePopCnt/', views.getNoticePopCnt, name='getNoticePopCnt'),
    url(r'^getNoticePopUp/', views.getNoticePopUp, name='getNoticePopUp'),
    url(r'^getNoticeMjrCnt/', views.getNoticeMjrCnt, name='getNoticeMjrCnt'),
    url(r'^noticeDtl/', views.noticeDtl.as_view(), name='noticeDtl'),
    url(r'^getNoticeOne/', views.getNoticeOne, name='getNoticeOne'),
    url(r'^noticeSave/post', views.noticeSave, name='noticeSave'),
    url(r'^noticeDelete/post', views.noticeDelete, name='noticeDelete'),
    url(r'^getWrkApvlReq/', views.getWrkApvlReq, name='getWrkApvlReq'),
    url(r'^saveApvlReq/post', views.saveApvlReq, name='saveApvlReq'),
    url(r'^saveApvlAcpt/post', views.saveApvlAcpt, name='saveApvlAcpt'),
    url(r'^apvlReqHist/', views.apvlReqHist.as_view(), name='apvlReqHist'),
    url(r'^getApvlReqHist/', views.getApvlReqHist, name='getApvlReqHist'),
    url(r'^getApvlAcptHist/', views.getApvlAcptHist, name='getApvlAcptHist'),
    url(r'^empMgmt/', views.empMgmt.as_view(), name='empMgmt'),
    url(r'^empMgmtPop/', views.empMgmtPop.as_view(), name='empMgmtPop'),
    url(r'^getEmpList/', views.getEmpList, name='getEmpList'),
    url(r'^getEmpInfo/', views.getEmpInfo, name='getEmpInfo'),
    url(r'^getEmpName/', views.getEmpName, name='getEmpName'),
    url(r'^getEmpDept/', views.getEmpDept, name='getEmpDept'),
    url(r'^getEmpDeptGm/', views.getEmpDeptGm, name='getEmpDeptGm'),
    url(r'^getApvlReqHistDetl/', views.getApvlReqHistDetl, name='getApvlReqHistDetl'),
    url(r'^getCalendarData/', views.getCalendarData, name='getCalendarData'),
    url(r'^saveYryApvlReq/post', views.saveYryApvlReq, name='saveYryApvlReq'),
    url(r'^getWeekGridData/', views.getWeekGridData, name='getWeekGridData'),
    url(r'^getMonthGridData/', views.getMonthGridData, name='getMonthGridData'),
    url(r'^empMgmtRegPop', views.empMgmtRegPop.as_view(), name='empMgmtRegPop'),
    url(r'^empMgmtReg/post', views.empMgmtReg, name='empMgmtReg'),
    url(r'^empMgmtEditPop/', views.empMgmtEditPop.as_view(), name='empMgmtEditPop'),
    url(r'^empMgmtEdit/post', views.empMgmtEdit, name='empMgmtEdit'),
    url(r'^getEditEmpInfo/', views.getEditEmpInfo, name='getEditEmpInfo'),
    url(r'^empMgmtDel/post', views.empMgmtDel, name='empMgmtDel'),
    url(r'^isExistEmpNm/', views.isExistEmpNm, name='isExistEmpNm'),

    url(r'^getTotalWrktm/', views.getTotalWrktm, name='getTotalWrktm'),

    url(r'^saveStrtTm/', views.saveStrtTm, name='saveStrtTm'),
    url(r'^saveEndTm/', views.saveEndTm, name='saveEndTm'),

    url(r'^getApvlInfo/', views.getApvlInfo, name='getApvlInfo'),
    url(r'^getYryUseDays/', views.getYryUseDays, name='getYryUseDays'),

    url(r'^question/', views.question.as_view(), name='question'), #QNA 게시판페이지 이동
    url(r'^questionDtl/', views.questionDtl.as_view(), name='questionDtl'),
    url(r'^getquestionInfo/', views.getquestionInfo, name='getquestionInfo'),
    url(r'^getquestionLst/', views.getquestionLst, name='getquestionLst'),
    url(r'^getQnaPopCnt/', views.getQnaPopCnt, name='getQnaPopCnt'),  # 미사용
    url(r'^getQnaPopUp/', views.getQnaPopUp, name='getQnaPopUp'),
    url(r'^questionWrPop', views.questionWrPop.as_view(), name='questionWrPop'), #QNA 게시판 게시글 등록 페이지 이동
    url(r'^questionWr', views.questionWr, name='questionWr'), #QNA 게시판 게시글 등록
    url(r'^questionEditPop', views.questionEditPop.as_view(), name='questionEditPop'), #QNA 게시판 게시글 상세보기 페이지 이동
    url(r'^questiondetail', views.questiondetail, name='questiondetail'), #QNA 게시판 게시글 상세보기
    url(r'^questionDelete', views.questionDelete, name='questionDelete'), #QNA 게시판 게시글 삭제
    url(r'^questionAnsw', views.questionAnsw.as_view(), name='questionAnsw'), #QNA 게시판 답변 등록페이지 이동
    url(r'^questionAw', views.questionAw, name='questionAw'),
    url(r'^qnaAnserReg', views.qnaAnserReg, name='qnaAnserReg'), #QNA 게시판 답변 등록
    url(r'^questionUpdateReq', views.questionUpdateReq.as_view(), name='questionUpdateReq'), #QNA 게시판 게시글 수정페이지 이동
    url(r'^qnaUpdate', views.qnaUpdate, name='qnaUpdate'), #QNA 게시판 게시글 수정
    url(r'^qnaUpdateCnt', views.qnaUpdateCnt, name='qnaUpdateCnt'), #QNA 게시판 조회수 증가
    url(r'^qnaSearch', views.qnaSearch, name='qnaSearch'), #QNA 게시판 검색기능
    
    # 공통 코드 조회
    url(r'^retrieveCmmCd/', views.retrieveCmmCd, name='retrieveCmmCd'),

    # 스케줄현황조회
    url(r'^scheduleStatLst/', views.scheduleStatLst.as_view(), name='scheduleStatLst'),
    url(r'^getScheduleStatLst/', views.getScheduleStatLst, name='getScheduleStatLst'),

    # 공지사항 파일업로드 추가
    url(r'^my_view/', views.my_view, name='my-view'),
    # web UI 샘플
    url(r'^diliWebUiSamp/', views.diliWebUiSamp.as_view(), name='diliWebUiSamp')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)