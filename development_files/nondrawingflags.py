nonDrawingFlags = []
nonDrawing = ['A1 - ', 'A2 - ', 'A3 - ', "B1 - ", 'B10 - ', 'B100 - ', 'B11 - ', 'B12 - ', 'B13 - ', 'B2 - ', 'B3 - ', 'B4 - ', 'B5 - ', 'B6 - ', 'B7 - ', 'B8 -  ', 'B8.1 - ', 'B9 - ', 'C1 - ', 'C1.1 - ', 'C1.2 - ', 'C1.3 - ', 'C2 - ', 'C2.1 - ', 'C2.2 - ', '.\\C2.3 - Agreement', '.\\D1 - Environmental Correspondence', '.\\D2 - EIC Forms', '.\\D3 - CEQA Documentation', '.\\D4 - Mitigation Monitoring Program', '.\\E1 - DPP', '.\\E2 - PPG', '.\\E3 - Budget Cost Estimates', '.\\E4 - Planning Schedules', '.\\E5 - Program and Design Correspondence', '.\\E5.1 - Executive Architect to.from', '.\\E5.2 - Special Consultants', '.\\E5.3 - Users. Building Committee. Campus to.from', '.\\E5.4 - PPC and PP', '.\\E5.5 - Office of the President to.from', '.\\E5.6 - Building Committee to.from', '.\\E5.7 - Other', '.\\E5.8 - Office of General Counsel', '.\\E6 - Reports (soils, structural, calcs)', '.\\E7 - Value Engineering', '.\\E7.1 - Value Engineering Correspondence', '.\\E7.2 - VE Workshop Minutes, Summaries, Final Reports', '.\\E8 - Program and Design Meeting Minutes', '.\\F1 - Bid and Contract Award Correspondence', '.\\F1.1 - Executive Architect to.from', '.\\F1.2 - Special Consultatns to.from', '.\\F1.3 - Users.Building Committee.Campus to.from', '.\\F1.4 - PPC and PP', '.\\F1.5 - Office of the President to.from', '.\\F1.6 - General Cousel to.from', '.\\F1.6A - Gerneal Counsel Confidential', '.\\F1.7 - Pre-Qualification', '.\\F1.8 - Other', '.\\F10 - Escrow Agreement', '.\\F2 - Reviews', '.\\F2.1 - Constructibility, Code Reviews', '.\\F2.2 - In-house. PP reviews', '.\\F2.3 - Independent Cost Review', '.\\F2.4 - Independent Seismic Review', '.\\F2.5 - Other', '.\\F3 - Structural. Title 24. Mechanical Calcs Approved Docs', '.\\F4 - Plan Deposits. Planholders.Advertisements for Bid', '.\\F5 - Drawings and Specifications.Bidding Documents.Addenda', '.\\F6 - Affirmative Action (prebid meeting notes)', '.\\F7 - Bid Summary Forms', '.\\F7.1 - Bid Protest', '.\\F8 - Contract', '.\\F9 - Builders Risk Insurance', '.\\G1 - Construction Correspondence', '.\\G1.1 - Contractor to.from', '.\\G1.2 - Executive Architect to.from', '.\\G1.3 - Users.Building Committee.Campus to.from', '.\\G1.4 - PPC and PP. Certified Payroll', '.\\G1.5 - Geotechnical Engineer to.from', '.\\G1.6 - Testing and Inspection to Laboratory to.from', '.\\G1.7 - General Counsel to.from', '.\\G1.7A - General Counsel Confidential', '.\\G1.8 - Other', '.\\G10 - Testing and Inspection Reports.Other', '.\\G11 - Proposal Request. Bulletins. Contractors Response', '.\\G11.1 - Proposal Request 1 with back up', '.\\G11.2 - Proposal Request 2', '.\\G11.3 - Proposal Request 3', '.\\G12 - Request for Information RFI', '.\\G13 - Letter of Instruction LOI', '.\\G14 - User Request Change in Scope', '.\\G15 - Change Order', '.\\G15.1 - Change Order 1 with back up', '.\\G15.2 - Change Order 2', '.\\G15.3 - Change Order 3', '.\\G16 - Field Orders', '.\\G17 - Warranties and Guarantees', '.\\G18 - Punchlist', '.\\G19 - Notice of Complete NOC. Notice of Substantial Completion NOSC', '.\\G2 - Certificate of Payment', '.\\G20 - Warrranty Deficiency', '.\\G21 - Construction Photos', '.\\G22 - Claims. Public Records Act', '.\\G22.1 - Claims Confidential', '.\\G23 - Commissioning', '.\\G24 - Building Permits', ".\\G3 - Contractor's Schedule and Updates", '.\\G4 - Progress Meeting Notes', '.\\G5 - UCSC Inspectors Daily Reports', '.\\G5.1 - Hot Work Permits', '.\\G6 - UCSC Memoranda', '.\\G6.1 - Architects Field Reports', '.\\G7 - Contractors Daily Reports', '.\\G8 - ', 'G9 - ', 'H - ', 'I - ', 'J - ', 'K - ']


simpleFlag = ['.\\A1 -', '.\\A2 -', '.\\A3 -', '.\\B1 -', '.\\B10 -', '.\\B100 -', '.\\B11 -', '.\\B12 -', '.\\B13 -', '.\\B2 -', '.\\B3 -', '.\\B4 -', '.\\B5 -', '.\\B6 -', '.\\B7 -', '.\\B8 -', '.\\B8.1 -', '.\\B9 -', '.\\C1 -', '.\\C1.1 -', '.\\C1.2 -', '.\\C1.3 -', '.\\C2 -', '.\\C2.1 -', '.\\C2.2 -', '.\\C2.3 -', '.\\D1 -', '.\\D2 -', '.\\D3 -', '.\\D4 -', '.\\E1 -', '.\\E2 -', '.\\E3 -', '.\\E4 -', '.\\E5 -', '.\\E5.1 -', '.\\E5.2 -', '.\\E5.3 -', '.\\E5.4 -', '.\\E5.5 -', '.\\E5.6 -', '.\\E5.7 -', '.\\E5.8 -', '.\\E6 -', '.\\E7 -', '.\\E7.1 -', '.\\E7.2 -', '.\\E8 -', '.\\F1 -', '.\\F1.1 -', '.\\F1.2 -', '.\\F1.3 -', '.\\F1.4 -', '.\\F1.5 -', '.\\F1.6 -', '.\\F1.6A -', '.\\F1.7 -', '.\\F1.8 -', '.\\F10 -', '.\\F2 -', '.\\F2.1 -', '.\\F2.2 -', '.\\F2.3 -', '.\\F2.4 -', '.\\F2.5 -', '.\\F3 -', '.\\F4 -', '.\\F5 -', '.\\F6 -', '.\\F7 -', '.\\F7.1 -', '.\\F8 -', '.\\F9 -', '.\\G1 -', '.\\G1.1 -', '.\\G1.2 -', '.\\G1.3 -', '.\\G1.4 -', '.\\G1.5 -', '.\\G1.6 -', '.\\G1.7 -', '.\\G1.7A -', '.\\G1.8 -', '.\\G10 -', '.\\G11 -', '.\\G11.1 -', '.\\G11.2 -', '.\\G11.3 -', '.\\G12 -', '.\\G13 -', '.\\G14 -', '.\\G15 -', '.\\G15.1 -', '.\\G15.2 -', '.\\G15.3 -', '.\\G16 -', '.\\G17 -', '.\\G18 -', '.\\G19 -', '.\\G2 -', '.\\G20 -', '.\\G21 -', '.\\G22 -', '.\\G22.1 -', '.\\G23 -', '.\\G24 -', '.\\G3 -', '.\\G4 -', '.\\G5 -', '.\\G5.1 -', '.\\G6 -', '.\\G6.1 -', '.\\G7 -', '.\\G8 -', '.\\G9 -', '.\\H -', '.\\I -', '.\\J -', '.\\K -']


flags = ['A1 -', 'A2 -', 'A3 -', 'B1 -', 'B10 -', 'B100 -', 'B11 -', 'B12 -', 'B13 -', 'B2 -', 'B3 -', 'B4 -', 'B5 -', 'B6 -', 'B7 -', 'B8 -', 'B8.1 -', 'B9 -', 'C1 -', 'C1.1 -', 'C1.2 -', 'C1.3 -', 'C2 -', 'C2.1 -', 'C2.2 -', 'C2.3 -', 'D1 -', 'D2 -', 'D3 -', 'D4 -', 'E1 -', 'E2 -', 'E3 -', 'E4 -', 'E5 -', 'E5.1 -', 'E5.2 -', 'E5.3 -', 'E5.4 -', 'E5.5 -', 'E5.6 -', 'E5.7 -', 'E5.8 -', 'E6 -', 'E7 -', 'E7.1 -', 'E7.2 -', 'E8 -', 'F1 -', 'F1.1 -', 'F1.2 -', 'F1.3 -', 'F1.4 -', 'F1.5 -', 'F1.6 -', 'F1.6A -', 'F1.7 -', 'F1.8 -', 'F10 -', 'F2 -', 'F2.1 -', 'F2.2 -', 'F2.3 -', 'F2.4 -', 'F2.5 -', 'F3 -', 'F4 -', 'F5 -', 'F6 -', 'F7 -', 'F7.1 -', 'F8 -', 'F9 -', 'G1 -', 'G1.1 -', 'G1.2 -', 'G1.3 -', 'G1.4 -', 'G1.5 -', 'G1.6 -', 'G1.7 -', 'G1.7A -', 'G1.8 -', 'G10 -', 'G11 -', 'G11.1 -', 'G11.2 -', 'G11.3 -', 'G12 -', 'G13 -', 'G14 -', 'G15 -', 'G15.1 -', 'G15.2 -', 'G15.3 -', 'G16 -', 'G17 -', 'G18 -', 'G19 -', 'G2 -', 'G20 -', 'G21 -', 'G22 -', 'G22.1 -', 'G23 -', 'G24 -', 'G3 -', 'G4 -', 'G5 -', 'G5.1 -', 'G6 -', 'G6.1 -', 'G7 -', 'G8 -', 'G9 -', 'H -', 'I -', 'J -', 'K -']

def flagExt(flagList):
    newList = []
    for i in flagList:
        newflag = i.split('-')[0]
        newflag = newflag + '-'
        print(newflag)
        newList.append(newflag)
    return(newList)

def flagger(flist):
    new = []
    for i in flist:
        flag = i.split('\\')[-1]
        new.append(flag)
    return(new)