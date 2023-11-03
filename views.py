from django.shortcuts import render,redirect

from .models import TableCreation

def errFunc(req2):
    return render(req2,'Error Page.html')

def goCourseTab(req3):
    return render(req3,'TableFileHTML.html')

def goHomePage(req):
    if req.method == 'POST':

        NAME_swap = req.POST['Cname']
        FNAME_swap = req.POST['Cdadname']
        GENDER_swap = req.POST['FetchGender']
        #FIRST_3 COLUMNS

        SUBLEVELQUALIF = req.POST['FetchQualification']

        SCHOOL_NAME = req.POST['Cschname']

        DEGREE = req.POST['FetchDegree']
        DEPT = req.POST['FetchDept']

        DIPQUALIF = req.POST['Cdip']

        INSTITUTION = req.POST['Cclgname']

        if True:
            if SUBLEVELQUALIF == 'SSLC' or SUBLEVELQUALIF == 'HSC':
                QUALIF_swap = SUBLEVELQUALIF
                INSTIT_swap = SCHOOL_NAME

            elif SUBLEVELQUALIF == 'Degree':
                QUALIF_swap = DEGREE + ' ' + DEPT
                INSTIT_swap = INSTITUTION

            elif SUBLEVELQUALIF == 'Others':
                QUALIF_swap = DIPQUALIF
                INSTIT_swap = INSTITUTION
        YOPO_swap = req.POST['Cyr']
        YOPO_swap = int(YOPO_swap)
        # COLUMNS 4,5,6

        EMAIL_swap = req.POST['Cem']
        CONTACT_swap = req.POST['Ccntct']

        CONTACT_swap = str(CONTACT_swap)
        CONTACT_swap  = CONTACT_swap.replace('-','')
        CONTACT_swap = int(CONTACT_swap)
        # COLUMNS 7,8

        FIELD_swap = req.POST['FetchField']
        COURSES_swap = req.POST['FetchCourse']
        # COLUMNS 9,10

        MODE_swap = req.POST['FetchMode']
        # COLUMN 11

        from datetime import datetime
        now = datetime.now()

        DATE_swap = str(now.strftime('%d')) + ',' + now.strftime('%B') + ' ' + str(now.strftime('%Y'))
        # COLUMN 12

        viewsTable = TableCreation()

        viewsTable.Gender_COL = GENDER_swap
        viewsTable.FathersName_COL = FNAME_swap
        viewsTable.Name_COL = NAME_swap

        viewsTable.DateOfEntry_COL = DATE_swap
        viewsTable.OptedField_COL = FIELD_swap

        viewsTable.EmailID_COL = EMAIL_swap

        viewsTable.OptedCourse_COL = COURSES_swap

        viewsTable.ModeOfClass_COL = MODE_swap

        viewsTable.MobileNumber_COL = CONTACT_swap

        viewsTable.YearOfPassedOut_COL = YOPO_swap

        viewsTable.Institution_COL = INSTIT_swap

        viewsTable.Qualification_COL = QUALIF_swap
        #assigned to the respective column

        viewsTable.save()
        return redirect('Err404')
        #saved the values to the column

    return render(req,'HomeFileHTML.html')

