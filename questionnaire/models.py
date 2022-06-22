# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Candidates(models.Model):
    #candidateid = models.AutoField(db_column='CandidateId')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    consent = models.CharField(db_column='Consent', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    examsitting = models.CharField(db_column='ExamSitting', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    candidateidentityno = models.CharField(db_column='CandidateIdentityNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    race = models.CharField(db_column='Race', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    homelanguage = models.CharField(db_column='HomeLanguage', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricschool = models.CharField(db_column='MatricSchool', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricyear = models.CharField(db_column='MatricYear', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricteachinglanguage = models.CharField(db_column='MatricTeachingLanguage', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricassesmentlanguage = models.CharField(db_column='MatricAssesmentLanguage', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricschooltype = models.CharField(db_column='MatricSchoolType', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matrichouseholdstatus = models.CharField(db_column='MatricHouseholdStatus', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubjectscountcompleted = models.IntegerField(db_column='MatricSubjectsCountCompleted', blank=True, null=True)  # Field name made lowercase.
    matricsubject1 = models.CharField(db_column='MatricSubject1', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade1 = models.CharField(db_column='MatricGrade1', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject2 = models.CharField(db_column='MatricSubject2', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade2 = models.CharField(db_column='MatricGrade2', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject3 = models.CharField(db_column='MatricSubject3', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade3 = models.CharField(db_column='MatricGrade3', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject4 = models.CharField(db_column='MatricSubject4', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade4 = models.CharField(db_column='MatricGrade4', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject5 = models.CharField(db_column='MatricSubject5', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade5 = models.CharField(db_column='MatricGrade5', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject6 = models.CharField(db_column='MatricSubject6', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade6 = models.CharField(db_column='MatricGrade6', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject7 = models.CharField(db_column='MatricSubject7', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade7 = models.CharField(db_column='MatricGrade7', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject8 = models.CharField(db_column='MatricSubject8', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade8 = models.CharField(db_column='MatricGrade8', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject9 = models.CharField(db_column='MatricSubject9', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade9 = models.CharField(db_column='MatricGrade9', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject10 = models.CharField(db_column='MatricSubject10', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade10 = models.CharField(db_column='MatricGrade10', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicaentrychannel = models.CharField(db_column='SAICAEntryChannel', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicadegree = models.CharField(db_column='SAICADegree', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicauniversity = models.CharField(db_column='SAICAUniversity', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicayearofcompletion = models.CharField(db_column='SAICAYearOfCompletion', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicanoofyears = models.IntegerField(db_column='SAICANoOfYears', blank=True, null=True)  # Field name made lowercase.
    saicateachinglanguage = models.CharField(db_column='SAICATeachingLanguage', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicaassesmentlanguage = models.CharField(db_column='SAICAAssesmentLanguage', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    firsttoattenduniversity = models.BooleanField(db_column='FirstToAttendUniversity', blank=True, null=True)  # Field name made lowercase.
    saicafinaccountingscores = models.CharField(db_column='SAICAFinAccountingScores', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicataxationscores = models.CharField(db_column='SAICATaxationScores', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicaauditingscores = models.CharField(db_column='SAICAAuditingScores', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicamgtaccountingscores = models.CharField(db_column='SAICAMgtAccountingScores', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    undergradempstatus = models.CharField(db_column='UndergradEmpStatus', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaattempt1university = models.CharField(db_column='PGDAAttempt1University', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaattempt1year = models.CharField(db_column='PGDAAttempt1Year', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaattempt2university = models.CharField(db_column='PGDAAttempt2University', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaattempt2year = models.CharField(db_column='PGDAAttempt2Year', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaattempt3university = models.CharField(db_column='PGDAAttempt3University', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaattempt3year = models.CharField(db_column='PGDAAttempt3Year', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaattempt4university = models.CharField(db_column='PGDAAttempt4University', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaattempt4year = models.CharField(db_column='PGDAAttempt4Year', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdasuccessfulyear = models.CharField(db_column='PGDASuccessfulYear', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaserviceprovider = models.CharField(db_column='PGDAServiceProvider', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdateachinglanguage = models.CharField(db_column='PGDATeachingLanguage', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaassesmentlanguage = models.CharField(db_column='PGDAAssesmentLanguage', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdafinaccountingscores = models.CharField(db_column='PGDAFinAccountingScores', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdataxationscores = models.CharField(db_column='PGDATaxationScores', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaauditingscores = models.CharField(db_column='PGDAAuditingScores', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdamgtaccountingscores = models.CharField(db_column='PGDAMgtAccountingScores', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdafinaccountingstatus = models.CharField(db_column='PGDAFinAccountingStatus', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdataxationstatus = models.CharField(db_column='PGDATaxationStatus', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaauditingstatus = models.CharField(db_column='PGDAAuditingStatus', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdamgtaccountingstatus = models.CharField(db_column='PGDAMgtAccountingStatus', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaempstatus = models.CharField(db_column='PGDAEmpStatus', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaempname = models.CharField(db_column='PGDAEmpName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdafundingtype = models.CharField(db_column='PGDAFundingType', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdafundingyears = models.IntegerField(db_column='PGDAFundingYears', blank=True, null=True)  # Field name made lowercase.
    pgdastudymode = models.CharField(db_column='PGDAStudyMode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaaccomodationtype = models.CharField(db_column='PGDAAccomodationType', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdamaritalstatus = models.CharField(db_column='PGDAMaritalStatus', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaroommatesdetails = models.CharField(db_column='PGDARoomMatesDetails', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdachildrendetails = models.CharField(db_column='PGDAChildrenDetails', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcattempt1provider = models.CharField(db_column='ITCAttempt1Provider', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcattempt1year = models.CharField(db_column='ITCAttempt1Year', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcattempt2provider = models.CharField(db_column='ITCAttempt2Provider', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcattempt2year = models.CharField(db_column='ITCAttempt2Year', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcattempt3provider = models.CharField(db_column='ITCAttempt3Provider', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcattempt3year = models.CharField(db_column='ITCAttempt3Year', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcattempt4provider = models.CharField(db_column='ITCAttempt4Provider', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcattempt4year = models.CharField(db_column='ITCAttempt4Year', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcsuccessfulyear = models.CharField(db_column='ITCSuccessfulYear', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcempname = models.CharField(db_column='ITCEmpName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcempstatus = models.CharField(db_column='ITCEmpStatus', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcfundingtype = models.CharField(db_column='ITCFundingType', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itctrainingelective = models.CharField(db_column='ITCTrainingElective', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcleavedaysgrant = models.CharField(db_column='ITCLeaveDaysGrant', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcleavedaysfairness = models.CharField(db_column='ITCLeaveDaysFairness', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcattempt1provider = models.CharField(db_column='APCAttempt1Provider', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcattempt1year = models.CharField(db_column='APCAttempt1Year', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcattempt2provider = models.CharField(db_column='APCAttempt2Provider', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcattempt2year = models.CharField(db_column='APCAttempt2Year', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcattempt3provider = models.CharField(db_column='APCAttempt3Provider', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcattempt3year = models.CharField(db_column='APCAttempt3Year', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcattempt4provider = models.CharField(db_column='APCAttempt4Provider', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcattempt4year = models.CharField(db_column='APCAttempt4Year', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcsuccessfulyear = models.CharField(db_column='APCSuccessfulYear', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcempname = models.CharField(db_column='APCEmpName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcemployedyearsitting = models.CharField(db_column='APCEmployedYearSitting', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcfundtype = models.CharField(db_column='APCFundType', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcleavedaysgrant = models.CharField(db_column='APCLeaveDaysGrant', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcleavedaysfairness = models.CharField(db_column='APCLeaveDaysFairness', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    extracomment = models.CharField(db_column='ExtraComment', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    formdate = models.DateTimeField(db_column='FormDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Candidates'
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'

    def __str__(self):
        return self.email


class Candidatesold(models.Model):
    #candidateid = models.AutoField(db_column='CandidateId')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    consent = models.BooleanField(db_column='Consent')  # Field name made lowercase.
    examsitting = models.BooleanField(db_column='ExamSitting', blank=True, null=True)  # Field name made lowercase.
    candidateidentityno = models.CharField(db_column='CandidateIdentityNo', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    race = models.CharField(db_column='Race', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    homelanguage = models.CharField(db_column='HomeLanguage', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricschool = models.CharField(db_column='MatricSchool', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricyear = models.CharField(db_column='MatricYear', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricteachinglanguage = models.CharField(db_column='MatricTeachingLanguage', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricassesmentlanguage = models.CharField(db_column='MatricAssesmentLanguage', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricschooltype = models.CharField(db_column='MatricSchoolType', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matrichouseholdstatus = models.CharField(db_column='MatricHouseholdStatus', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubjectscountcompleted = models.IntegerField(db_column='MatricSubjectsCountCompleted', blank=True, null=True)  # Field name made lowercase.
    matricsubject1 = models.CharField(db_column='MatricSubject1', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade1 = models.CharField(db_column='MatricGrade1', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject2 = models.CharField(db_column='MatricSubject2', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade2 = models.CharField(db_column='MatricGrade2', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject3 = models.CharField(db_column='MatricSubject3', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade3 = models.CharField(db_column='MatricGrade3', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject4 = models.CharField(db_column='MatricSubject4', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade4 = models.CharField(db_column='MatricGrade4', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject5 = models.CharField(db_column='MatricSubject5', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade5 = models.CharField(db_column='MatricGrade5', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject6 = models.CharField(db_column='MatricSubject6', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade6 = models.CharField(db_column='MatricGrade6', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject7 = models.CharField(db_column='MatricSubject7', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade7 = models.CharField(db_column='MatricGrade7', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject8 = models.CharField(db_column='MatricSubject8', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade8 = models.CharField(db_column='MatricGrade8', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject9 = models.CharField(db_column='MatricSubject9', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade9 = models.CharField(db_column='MatricGrade9', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricsubject10 = models.CharField(db_column='MatricSubject10', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    matricgrade10 = models.CharField(db_column='MatricGrade10', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicaentrychannel = models.CharField(db_column='SAICAEntryChannel', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicadegree = models.CharField(db_column='SAICADegree', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicauniversity = models.CharField(db_column='SAICAUniversity', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicayearofcompletion = models.CharField(db_column='SAICAYearOfCompletion', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicanoofyears = models.IntegerField(db_column='SAICANoOfYears', blank=True, null=True)  # Field name made lowercase.
    saicateachinglanguage = models.CharField(db_column='SAICATeachingLanguage', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicaassesmentlanguage = models.CharField(db_column='SAICAAssesmentLanguage', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    firsttoattenduniversity = models.BooleanField(db_column='FirstToAttendUniversity', blank=True, null=True)  # Field name made lowercase.
    saicafinaccountingscores = models.CharField(db_column='SAICAFinAccountingScores', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicataxationscores = models.CharField(db_column='SAICATaxationScores', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicaauditingscores = models.CharField(db_column='SAICAAuditingScores', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    saicamgtaccountingscores = models.CharField(db_column='SAICAMgtAccountingScores', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    undergradempstatus = models.CharField(db_column='UndergradEmpStatus', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaattempt1university = models.CharField(db_column='PGDAAttempt1University', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaattempt1year = models.CharField(db_column='PGDAAttempt1Year', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaattempt2university = models.CharField(db_column='PGDAAttempt2University', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaattempt2year = models.CharField(db_column='PGDAAttempt2Year', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaattempt3university = models.CharField(db_column='PGDAAttempt3University', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaattempt3year = models.CharField(db_column='PGDAAttempt3Year', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaattempt4university = models.CharField(db_column='PGDAAttempt4University', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaattempt4year = models.CharField(db_column='PGDAAttempt4Year', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdasuccessfulyear = models.CharField(db_column='PGDASuccessfulYear', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaserviceprovider = models.CharField(db_column='PGDAServiceProvider', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdateachinglanguage = models.CharField(db_column='PGDATeachingLanguage', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaassesmentlanguage = models.CharField(db_column='PGDAAssesmentLanguage', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdafinaccountingscores = models.CharField(db_column='PGDAFinAccountingScores', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdataxationscores = models.CharField(db_column='PGDATaxationScores', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaauditingscores = models.CharField(db_column='PGDAAuditingScores', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdamgtaccountingscores = models.CharField(db_column='PGDAMgtAccountingScores', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdafinaccountingstatus = models.CharField(db_column='PGDAFinAccountingStatus', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdataxationstatus = models.CharField(db_column='PGDATaxationStatus', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaauditingstatus = models.CharField(db_column='PGDAAuditingStatus', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdamgtaccountingstatus = models.CharField(db_column='PGDAMgtAccountingStatus', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaempstatus = models.CharField(db_column='PGDAEmpStatus', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaempname = models.CharField(db_column='PGDAEmpName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdafundingtype = models.CharField(db_column='PGDAFundingType', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdafundingyears = models.IntegerField(db_column='PGDAFundingYears', blank=True, null=True)  # Field name made lowercase.
    pgdastudymode = models.CharField(db_column='PGDAStudyMode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaaccomodationtype = models.CharField(db_column='PGDAAccomodationType', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdamaritalstatus = models.CharField(db_column='PGDAMaritalStatus', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdaroommatesdetails = models.CharField(db_column='PGDARoomMatesDetails', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pgdachildrendetails = models.CharField(db_column='PGDAChildrenDetails', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcattempt1provider = models.CharField(db_column='ITCAttempt1Provider', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcattempt1year = models.CharField(db_column='ITCAttempt1Year', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcattempt2provider = models.CharField(db_column='ITCAttempt2Provider', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcattempt2year = models.CharField(db_column='ITCAttempt2Year', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcattempt3provider = models.CharField(db_column='ITCAttempt3Provider', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcattempt3year = models.CharField(db_column='ITCAttempt3Year', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcattempt4provider = models.CharField(db_column='ITCAttempt4Provider', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcattempt4year = models.CharField(db_column='ITCAttempt4Year', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcsuccessfulyear = models.CharField(db_column='ITCSuccessfulYear', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcempname = models.CharField(db_column='ITCEmpName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcempstatus = models.CharField(db_column='ITCEmpStatus', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcfundingtype = models.CharField(db_column='ITCFundingType', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itctrainingelective = models.CharField(db_column='ITCTrainingElective', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcleavedaysgrant = models.CharField(db_column='ITCLeaveDaysGrant', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itcleavedaysfairness = models.CharField(db_column='ITCLeaveDaysFairness', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcattempt1provider = models.CharField(db_column='APCAttempt1Provider', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcattempt1year = models.CharField(db_column='APCAttempt1Year', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcattempt2provider = models.CharField(db_column='APCAttempt2Provider', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcattempt2year = models.CharField(db_column='APCAttempt2Year', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcattempt3provider = models.CharField(db_column='APCAttempt3Provider', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcattempt3year = models.CharField(db_column='APCAttempt3Year', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcattempt4provider = models.CharField(db_column='APCAttempt4Provider', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcattempt4year = models.CharField(db_column='APCAttempt4Year', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcsuccessfulyear = models.CharField(db_column='APCSuccessfulYear', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcempname = models.CharField(db_column='APCEmpName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcemployedyearsitting = models.CharField(db_column='APCEmployedYearSitting', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcfundtype = models.CharField(db_column='APCFundType', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcleavedaysgrant = models.CharField(db_column='APCLeaveDaysGrant', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apcleavedaysfairness = models.CharField(db_column='APCLeaveDaysFairness', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    extracomment = models.CharField(db_column='ExtraComment', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    formdate = models.DateTimeField(db_column='FormDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CandidatesOld'
        verbose_name = 'Old Candidate'
        verbose_name_plural = 'Old Candidates'

    def __str__(self):
        return self.email


class Homelanguages(models.Model):
    languages = models.CharField(db_column='Languages', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HomeLanguages'
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.languages

class Matricschools(models.Model):
    schoolname = models.CharField(db_column='SchoolName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    schooltype = models.CharField(db_column='SchoolType', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    quintile = models.CharField(db_column='Quintile', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    urban_rural = models.CharField(db_column='Urban_Rural', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MatricSchools'
        verbose_name = 'Matric School'
        verbose_name_plural = 'Matric Schools'
        
    def __str__(self):
        return self.schoolname


class Matricsubjects(models.Model):
    subjects = models.CharField(db_column='Subjects', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MatricSubjects'
        verbose_name = 'Matric Subject'
        verbose_name_plural = 'Matric Subjects'
    
    def __str__(self):
        return self.subjects


class Postgradqualifications(models.Model):
    qualification = models.CharField(db_column='Qualification', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PostgradQualifications'
        verbose_name = 'Post-Grad Qualification'
        verbose_name_plural = 'Post-Grad Qualifications'

    def __str__(self):
        return self.qualification


class Postgraduniversities(models.Model):
    university = models.CharField(db_column='University', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PostgradUniversities'
        verbose_name = 'Post-Grad University'
        verbose_name_plural = 'Post-Grad Universities'

    def __str__(self):
        return self.university


class Questions(models.Model):
    #questionid = models.AutoField(db_column='QuestionId')  # Field name made lowercase.
    CHOICES = (
        ('Checkbox', 'Checkbox'),
        ('ShortAns', 'ShortAnswer'),
        ('LongAns', 'LongerAnswer'),
        ('DropDown', 'DropDownList'),
        ('Likert','Likert'),
        ('Rate', 'Rate'),
        ('Date','Date')
    )
    question_type = models.CharField(max_length=300, choices = CHOICES)
    question = models.CharField(db_column='Question', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    

    class Meta:
        #managed = False
        db_table = 'Questions'
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
    
    def __str__(self):
        return self.question


class Trainingelectives(models.Model):
    trainingelective = models.CharField(db_column='TrainingElective', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrainingElectives'
        verbose_name = 'Training Elective'
        verbose_name_plural = 'Training Electives'
    
    def __str__(self):
        return self.trainingelective


class Undergradqualifications(models.Model):
    qualification = models.CharField(db_column='Qualification', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UndergradQualifications'
        verbose_name = 'Under-Grad Qualification'
        verbose_name_plural = 'Under-Grad Qualifications'
    
    def __str__(self):
        return self.qualification


class Undergraduniversities(models.Model):
    universityname = models.CharField(db_column='UniversityName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UndergradUniversities'
        verbose_name = 'Under-Grad University'
        verbose_name_plural = 'Under-Grad Universities'

    def __str__(self):
        return self.universityname


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'



class QuestionnaireQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    question_type = models.CharField(max_length=32, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'questionnaire_question'
        
    
    def __str__(self):
        return self.title


class TestModel(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name