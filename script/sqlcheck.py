#-*- coding:utf-8 -*-

import re,random
from lib.core import Downloader


class spider(object):

    def run(self,url,html):
        if(not url.find("?")):
            return False
    
        #创建一个下载器实例
        downloader = Downloader.Downloader()

        BOOLEAN_TESTS = ("AND %d=%d","OR NOT (%d=%d)")
        DNMS_ERRORS ={
        #regular expressions used for DBMS recognition based on error message response
            "MySQL": (r"SQL syntax.*MySQL",r"Warning.*mysql_.*",r"valid MySQL result",r"MySqlClient\."),
            "PostgreSQL": (r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*", r"valid PostgreSQL result", r"Npgsql\."),
            "Microsoft SQL Server": (r"Driver.* SQL[\-\_\ ]*Server", r"OLE DB.* SQL Server", r"(\W|\A)SQL Server.*Driver", r"Warning.*mssql_.*", r"(\W|\A)SQL Server.*[0-9a-fA-F]{8}", r"(?s)Exception.*\WSystem\.Data\.SqlClient\.", r"(?s)Exception.*\WRoadhouse\.Cms\."),
            "Microsoft Access": (r"Microsoft Access Driver", r"JET Database Engine", r"Access Database Engine"),
            "Oracle": (r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Oracle.*Driver", r"Warning.*\Woci_.*", r"Warning.*\Wora_.*"),
            "IBM DB2": (r"CLI Driver.*DB2", r"DB2 SQL error", r"\bdb2_\w+\("),
            "SQLite": (r"SQLite/JDBCDriver", r"SQLite.Exception", r"System.Data.SQLite.SQLiteException", r"Warning.*sqlite_.*", r"Warning.*SQLite3::", r"\[SQLITE_ERROR\]"),
            "Sybase": (r"(?i)Warning.*sybase.*", r"Sybase message", r"Sybase.*Server message.*"),
        }

        _url = url + "%29%28%22%27"
        _content = downloader.get(_url)
        for (dbms,regex) in ((dbms,regex) for dbms in DNMS_ERRORS for regex in DNMS_ERRORS[dbms]):
            if(re.search(regex,_content)):
                return True
        content = {}
        content["origin"] = downloader.get(_url)
        for test_payload in BOOLEAN_TESTS:
            RANDINT = random.randint(1,255)
            _url = url + test_payload%(RANDINT,RANDINT)
            content["true"] = downloader.get(_url)
            _url = url + test_payload%(RANDINT,RANDINT + 1)
            content["false"] = downloader.get(_url)
            if content["origin"] == content["true"] != content["false"]:
                return ("sql found: %s"%url)