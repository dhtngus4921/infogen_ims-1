from flask import Flask, jsonify, request
from flask_restful import Api, Resource
#from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.DEBUG)
import bcrypt

#from bson.json_util import dumps
import json
import pymysql

app = Flask(__name__)
api = Api(app)
logger = logging.getLogger(__name__)

import datetime
from json import JSONEncoder

class DateTimeEncoder(JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()

def dateConverter(param):
    if isinstance(param, datetime.datetime):
        return param.__str__()


def userExist(username):
    if users.find({"Username": username}).count() == 0:
        return False
    else:
        return True


def verifyUser(username, password):
    if not userExist(username):
        return False

    user_hashed_pw = users.find({
        "Username": username
    })[0]["Password"]

    if bcrypt.checkpw(password.encode('utf8'), user_hashed_pw):
        return True
    else:
        return False


def getUserMessages(username):
    # get the messages
    return users.find({
        "Username": username,
    })[0]["Messages"]


"""
RESOURCES
"""


class Hello(Resource):
    def get(self):
        return "This is Dili Management API!"


class Register(Resource):
    def post(self):
        # Get posted data from request
        data = request.get_json()

        # get data
        username = data["username"]
        password = data["password"]

        # check if user exists
        if userExist(username):
            retJson = {
                "status": 301,
                "msg": "Invalid Username"
            }
            return jsonify(retJson)

        # encrypt password
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        # Insert record
        users.insert({
            "Username": username,
            "Password": hashed_pw,
            "Messages": []
        })

        # Return successful result
        retJosn = {
            "status": 200,
            "msg": "Registration successful"
        }
        return jsonify(retJosn)


class Retrieve(Resource):
    def post(self):
         # Get posted data from request
        data = request.get_json()

        # get data
        username = data["username"]
        password = data["password"]

        # check if user exists
        if not userExist(username):
            retJson = {
                "status": 301,
                "msg": "Invalid Username"
            }
            return jsonify(retJson)

        # check password
        correct_pw = verifyUser(username, password)
        if not correct_pw:
            retJson = {
                "status": 302,
                "msg": "Invalid password"
            }
            return jsonify(retJson)

        # get the messages
        messages = getUserMessages(username)

        # Build successful response
        retJson = {
            "status": 200,
            "obj": messages
        }

        return jsonify(retJson)


class Save(Resource):
    def post(self):

         # Get posted data from request
        data = request.get_json()

        # get data
        username = data["username"]
        password = data["password"]
        message = data["message"]

        # check if user exists
        if not userExist(username):
            retJson = {
                "status": 301,
                "msg": "Invalid Username"
            }
            return jsonify(retJson)

        # check password
        correct_pw = verifyUser(username, password)
        if not correct_pw:
            retJson = {
                "status": 302,
                "msg": "Invalid password"
            }
            return jsonify(retJson)

        if not message:
            retJson = {
                "status": 303,
                "msg": "Please supply a valid message"
            }
            return jsonify(retJson)

        # get the messages
        messages = getUserMessages(username)

        # add new message
        messages.append(message)

        # save the new user message
        users.update({
            "Username": username
        }, {
            "$set": {
                "Messages": messages
            }
        })

        retJson = {
            "status": 200,
            "msg": "Message has been saved successfully"
        }

        return jsonify(retJson)


class mariatestDB(Resource): # Mariadb 연결 진행
    def get(self):

        logging.debug(request.get_json())

        #requirements pymysql import 후 커넥트 사용
        mysql_con = pymysql.connect(host='218.151.225.142', port=3306, db='IFG_IMS', user='ims2', password='1234',
                                        charset='utf8')
        try:
            with mysql_con.cursor(pymysql.cursors.DictCursor) as cursor:
                #쿼리문 실행
                sql = "SELECT * FROM WEB_CONN_TEST "
                cursor.execute(sql)

        finally:
            mysql_con.close()

        result2 = cursor.fetchall()
        for row in result2:
            logging.debug('====== row====')
            logging.debug(row)
            logging.debug('===============')
        array = list(result2)  # 결과를 리스트로

        return result2

class yryMgmt(Resource): # Mariadb 연결 진행
    def get(self):

        data = request.get_json()

        #requirements pymysql import 후 커넥트 사용
        mysql_con = pymysql.connect(host='218.151.225.142', port=3306, db='IFG_IMS', user='ims2', password='1234',
                                        charset='utf8')
        try:
            with mysql_con.cursor(pymysql.cursors.DictCursor) as cursor:
                #쿼리문 실행
                sql = "SELECT * FROM TB_YRY_MGMT_M WHERE EMP_EMAL_ADDR = '" + data["email"] + "'"
                cursor.execute(sql)

        finally:
            mysql_con.close()

        result2 = cursor.fetchall()
        for row in result2:
            logging.debug('====== row====')
            logging.debug(row)
            logging.debug('===============')
        array = list(result2)  # 결과를 리스트로

        return result2


class wrkTimeInfoByEml(Resource): # Mariadb 연결 진행
    def get(self):

        data = request.get_json()

        logging.debug('================== App Start ==================')
        logging.debug(data)
        logging.debug(data["email"])
        logging.debug('================== App End ==================')

        #requirements pymysql import 후 커넥트 사용
        mysql_con = pymysql.connect(host='218.151.225.142', port=3306, db='IFG_IMS', user='ims2', password='1234',
                                        charset='utf8')
        try:
            with mysql_con.cursor(pymysql.cursors.DictCursor) as cursor:
                #쿼리문 실행
                sql = "SELECT * FROM TB_WRK_TM_MGMT_M WHERE EMP_EMAL_ADDR = '" + data["email"] + "'"
                logging.debug(sql)
                cursor.execute(sql)

        finally:
            mysql_con.close()

        result2 = cursor.fetchall()
        for row in result2:
            logging.debug('====== row====')
            logging.debug(row)
            logging.debug('===============')
        array = list(result2)  # 결과를 리스트로

        return json.dumps(result2, indent=4, cls=DateTimeEncoder)

class wrkApvlReq(Resource): # Mariadb 연결 진행
    def get(self):

        data = request.get_json()

        #requirements pymysql import 후 커넥트 사용
        mysql_con = pymysql.connect(host='218.151.225.142', port=3306, db='IFG_IMS', user='ims2', password='1234',
                                        charset='utf8')
        try:
            with mysql_con.cursor(pymysql.cursors.DictCursor) as cursor:
                #쿼리문 실행
                sql = "SELECT *, CASE WHEN HLDY_WRK_TM != 000000 AND NGHT_WRK_TM = 000000 THEN '휴일근무' " \
                    + "               WHEN HLDY_WRK_TM = 000000 AND NGHT_WRK_TM != 000000 THEN '야근근무' " \
                    + "               ELSE '' END WRK_TYPE " \
                    + "  FROM TB_WRK_TM_MGMT_M WHERE EMP_EMAL_ADDR = '" + data["email"] + "'"
                logging.debug("wrkApvlReq SQL문" + sql)
                cursor.execute(sql)

        finally:
            mysql_con.close()

        result2 = cursor.fetchall()
        for row in result2:
            logging.debug('====== row====')
            logging.debug(row)
            logging.debug('===============')
        array = list(result2)  # 결과를 리스트로

        return json.dumps(result2, indent=4, cls=DateTimeEncoder)
    
class saveApvlReq(Resource): # Mariadb 연결 진행
    def post(self):

        data = request.get_json()

        #requirements pymysql import 후 커넥트 사용
        mysql_con = pymysql.connect(host='218.151.225.142', port=3306, db='IFG_IMS', user='ims2', password='1234',
                                        charset='utf8')
        try:
            with mysql_con.cursor(pymysql.cursors.DictCursor) as cursor:
                #쿼리문 실행
                sql = "INSERT INTO TB_APVL_REQ_MGMT_M (EMP_EMAL_ADDR)"\
                    + "VALUES(%s)"
                logging.debug("saveApvlReq SQL문" + sql)
                cursor.execute(sql, data["email"] )
                mysql_con.commit()

        finally:
            mysql_con.close()

            retJson = {
                "status": 200,
                "msg": "Data has been saved successfully"
            }

        return jsonify(retJson)
    
class apvlReqHist(Resource): # Mariadb 연결 진행
    def get(self):

        data = request.get_json()

        #requirements pymysql import 후 커넥트 사용
        mysql_con = pymysql.connect(host='218.151.225.142', port=3306, db='IFG_IMS', user='ims2', password='1234',
                                        charset='utf8')
        try:
            with mysql_con.cursor(pymysql.cursors.DictCursor) as cursor:
                # 쿼리문 실행
                sql = "SELECT *, CASE WHEN APVL_REQ_DIVS = '01' THEN '휴일근무' " \
                    + "               WHEN APVL_REQ_DIVS = '02' THEN '야근근무' " \
                    + "               WHEN APVL_REQ_DIVS = '03' THEN '연차결재'  " \
                    + "               ELSE '' END APVL_REQ_NM  " \
                    + "        , CASE WHEN TH1_APRV_STUS != '' AND TH2_APRV_STUS = '' THEN '미승인'" \
                    + "               WHEN TH1_APRV_STUS != '' AND TH2_APRV_STUS != '' THEN '승인'" \
                    + "               ELSE '미승인' END APRV_STUS_NM" \
                    + "  FROM TB_APVL_REQ_MGMT_M WHERE EMP_EMAL_ADDR = '" + data["email"] + "'"
                logging.debug("apvlReqHist SQL문" + sql)
                cursor.execute(sql)

        finally:
            mysql_con.close()

        result2 = cursor.fetchall()
        for row in result2:
            logging.debug('====== row====')
            logging.debug(row)
            logging.debug('===============')
        array = list(result2)  # 결과를 리스트로

        return json.dumps(result2, indent=4, cls=DateTimeEncoder)

class noticeLst(Resource): # Mariadb 연결 진행
    def get(self):
        logging.debug("noticeLst start")
        logging.debug(request.get_json())
        # get data
        dept = request.args.get('dept')
        name = request.args.get('name')
        division = request.args.get('division')
        skilKind = request.args.get('skilKind')
        skil = request.args.get('skil')
        category = request.args.get('category')
        searchStr = request.args.get('searchStr')

        logging.debug('---------------SEARCH---------------')
        logging.debug('dept : ' + dept)
        logging.debug('name : ' + name)
        logging.debug('division : ' + division)
        logging.debug('skilKind : ' + skilKind)
        logging.debug('skil : ' + skil)
        logging.debug('category : ' + category)
        logging.debug('searchStr : ' + searchStr)
        logging.debug('------------------------------------')

        #requirements pymysql import 후 커넥트 사용
        mysql_con = pymysql.connect(host='218.151.225.142', port=3306, db='IFG_IMS', user='ims2', password='1234',
                                        charset='utf8')
        try:
            with mysql_con.cursor(pymysql.cursors.DictCursor) as cursor:
                #쿼리문 실행
                #sql = "SELECT TIT, CNTN, KD_DIVS_CD, MJR_YN, POP_OPEN_YN, DATA_INPT_ID, DATA_INPT_PGM_ID, DATA_UPD_ID, DATA_UPD_PGM_ID FROM TB_STTS_POST_MGMT_M "
                sql = "SELECT A.POST_ID, A.TIT, A.CNTN, A.KD_DIVS_CD, A.MJR_YN, A.POP_OPEN_YN, A.DATA_INPT_ID, B.EMP_NAME, DATE_FORMAT(A.DATA_INPT_DTTM, '%Y-%M-%D %H:%I:%S') AS DATA_INPT_DTTM, A.DATA_INPT_PGM_ID, A.DATA_UPD_ID, DATE_FORMAT(A.DATA_UPD_DTTM, '%Y-%M-%D %H:%I:%S') AS DATA_UPD_DTTM, A.DATA_UPD_PGM_ID " \
                        "FROM TB_STTS_POST_MGMT_M A LEFT OUTER JOIN TB_EMP_MGMT B ON A.DATA_INPT_ID = B.EMP_ID " \
                        "WHERE 1=1 "
                if searchStr != "":
                    if category == "00":
                        sql += "AND TIT LIKE '%" + searchStr + "%' "
                    if category == "01":
                        sql += "AND CNTN LIKE '%" + searchStr + "%' "
                    if category == "02":
                        sql += "AND (TIT LIKE '%" + searchStr + "%' OR CNTN LIKE '%" + searchStr + "%') "
                    if category == "03":
                        sql += "AND B.EMP_NAME LIKE '%" + searchStr + "%' "
                sql += "ORDER BY POST_ID DESC "
                logging.debug(sql)
                cursor.execute(sql)
                
        finally:
            mysql_con.close()

        result2 = cursor.fetchall()
        #for row in result2:
        #    logging.debug('====== row====')
        #    logging.debug(row)
        #    logging.debug('===============')
        #array = list(result2)  # 결과를 리스트로

        return result2


api.add_resource(Hello, '/hello')
api.add_resource(Register, '/register')
api.add_resource(Retrieve, '/retrieve')
api.add_resource(Save, '/save')

api.add_resource(mariatestDB,'/mariatestDB') #api 선언
api.add_resource(wrkTimeInfoByEml,'/wrkTimeInfoByEml') #api 선언
api.add_resource(yryMgmt,'/yryMgmt') #api 선언
api.add_resource(wrkApvlReq,'/wrkApvlReq') #api 선언
api.add_resource(saveApvlReq,'/saveApvlReq') #api 선언
api.add_resource(apvlReqHist,'/apvlReqHist') #api 선언
api.add_resource(noticeLst,'/noticeLst') #api 선언


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5006, debug=True)