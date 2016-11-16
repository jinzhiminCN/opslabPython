#!/usr/bin/python
# coding:utf-8

import fileinput
import os

SQL = "update tbl_sheet_problem_tree t set " \
      "t.time_limit1='%s',t.time_limit1_accept='%s',t.time_limit1_deal='%s',t.time_limit1_check='%s',t.time_limit1_recall='%s'," \
      "t.time_limit2='%s',t.time_limit2_accept='%s',t.time_limit2_deal='%s',t.time_limit2_check='%s',t.time_limit2_recall='%s'," \
      "t.time_limit3='%s',t.time_limit3_accept='%s',t.time_limit3_deal='%s',t.time_limit3_check='%s',t.time_limit3_recall='%s' " \
      "where t.problem_type_id like '%s';"

SS = "%s-%s-%s-%s"
for line in fileinput.input(os.getcwd() + "/yxjscn.txt"):
    tt = line.split()
    s1 = tt[3].split(",")
    s2 = tt[2].split(",")
    s3 = tt[1].split(",")
    # print SS % (s1[0], s1[1], str(int(s1[0]) - int(s1[1]) - int(s1[2])), s1[2])
    print SQL % (s1[0], s1[1], str(float(s1[0]) - float(s1[1]) - float(s1[2])), '0', s1[2],
                 s2[0], s2[1], str(float(s2[0]) - float(s2[1]) - float(s2[2])), '0', s2[2],
                 s3[0], s3[1], str(float(s3[0]) - float(s3[1]) - float(s3[2])), '0', s3[2], tt[0])
