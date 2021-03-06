#!/usr/bin/env python
# encoding: utf-8

name = "primaryThermoLibrary"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 1,
    label = "H2",
    molecule = 
"""
1 H 0 {2,S}
2 H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.895,6.975,6.994,7.009,7.081,7.219,7.72],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (31.233,'cal/(mol*K)','+|-',0.0007),
    ),
    shortDesc = u"""library value for H2""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "H",
    molecule = 
"""
1 H 1
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.968,4.968,4.968,4.968,4.968,4.968,4.968],'cal/(mol*K)'),
        H298 = (52.103,'kcal/mol','+|-',0.001),
        S298 = (27.419,'cal/(mol*K)','+|-',0.0005),
    ),
    shortDesc = u"""library value for H radical""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "O2",
    molecule = 
"""
1 O 1 {2,S}
2 O 1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.0233,7.1986,7.4285,7.6673,8.0656,8.3363,8.7407],'cal/(mol*K)'),
        H298 = (-0.0010244,'kcal/mol'),
        S298 = (49.0236,'cal/(mol*K)'),
    ),
    shortDesc = u"""from GRI-Mech 3.0""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "OH",
    molecule = 
"""
1 O 1
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.1402,7.0675,7.0458,7.0581,7.1493,7.3353,7.8741],'cal/(mol*K)'),
        H298 = (9.4021,'kcal/mol'),
        S298 = (43.9063,'cal/(mol*K)'),
    ),
    shortDesc = u"""taken from GRI-Mech 3.0 species s00010102""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "CO3s1",
    molecule = 
"""
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 0 {1,S} {4,S}
4 O 0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.82,13.53,14.8,15.76,17.05,17.85,18.84],'cal/(mol*K)'),
        H298 = (-37.9,'kcal/mol'),
        S298 = (61.28,'cal/(mol*K)'),
    ),
    shortDesc = u"""Mebel et al (2004) http:""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "CO3t1",
    molecule = 
"""
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 1 {1,S}
4 O 1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.43,14.02,15.23,16.16,17.4,18.14,19.01],'cal/(mol*K)'),
        H298 = (-11.5,'kcal/mol'),
        S298 = (64.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""Mebel et al (2004) http:""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "CO3t2",
    molecule = 
"""
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.48,14.83,15.83,16.59,17.62,18.26,19.05],'cal/(mol*K)'),
        H298 = (28.7,'kcal/mol'),
        S298 = (67.06,'cal/(mol*K)'),
    ),
    shortDesc = u"""Mebel et al (2004) http:""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "cyclopropene12diyl",
    molecule = 
"""
1 C 1 {2,D} {3,S}
2 C 1 {1,D} {3,S}
3 C 0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.32,13.42,15.16,16.58,18.74,20.29,22.63],'cal/(mol*K)'),
        H298 = (188.13,'kcal/mol'),
        S298 = (59.26,'cal/(mol*K)'),
    ),
    shortDesc = u"""doi:10.1016/j.chemphys.2008.01.057 and doi:10.1021/jp003224c""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "cyclopropynylidyne",
    molecule = 
"""
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {3,S}
3 C 1 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.43,11.93,13.18,14.18,15.61,16.59,17.99],'cal/(mol*K)'),
        H298 = (169.8,'kcal/mol'),
        S298 = (57.47,'cal/(mol*K)'),
    ),
    shortDesc = u"""doi:10.1016/j.chemphys.2008.01.057 and doi:10.1021/jp003224c""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "OCCO(S)",
    molecule = 
"""
1 O 0 {2,D}
2 C 0 {1,D} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.66,14.78,15.66,16.41,17.57,18.39,19.53],'cal/(mol*K)'),
        H298 = (18.31,'kcal/mol'),
        S298 = (90.63,'cal/(mol*K)'),
    ),
    shortDesc = u"""QCI""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "OCCO",
    molecule = 
"""
1 O 1 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.21,15.2,15.98,16.65,17.72,18.49,19.58],'cal/(mol*K)'),
        H298 = (5.6,'kcal/mol'),
        S298 = (61.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""QCI""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "C3H2",
    molecule = 
"""
1 C 2S {2,S} {3,S}
2 C 0  {1,S} {3,D}
3 C 0  {1,S} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.61,12.79,14.81,16.48,18.71,20.33,22.59],'cal/(mol*K)'),
        H298 = (113.99,'kcal/mol'),
        S298 = (56.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat's recommended value for 16165-40-5: C3H2 CYCLOPROPENYLIDENE BI-RADICAL SINGLET on 3/25/2011 (MRH converted from NASA-7 to RMG format)""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "S2",
    molecule = 
"""
1 S 1 {2,S}
2 S 1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.81,8.17,8.4,8.54,8.7,8.78,8.87],'cal/(mol*K)'),
        H298 = (29.19,'kcal/mol'),
        S298 = (55.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 value A.G. Vandeputte""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "HCS",
    molecule = 
"""
1 C 1 {2,D}
2 S 0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.77,9.46,10.04,10.51,11.22,11.76,12.62],'cal/(mol*K)'),
        H298 = (71.7,'kcal/mol'),
        S298 = (56.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""NIST value + B3LYP/cbsb7 entropy and heat cap A.G. Vandeputte""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "Ar",
    molecule = 
"""
1     Ar    0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(Tmin=(298,"K"), Tmax=(1000,"K"), coeffs=[2.5,0,0,0,0,-745.375,4.366]),
            NASAPolynomial(Tmin=(1000,"K"), Tmax=(5000,"K"), coeffs=[2.5,0,0,0,0,-745.375,4.366]),
        ],
        Tmin = (298,"K"),
        Tmax = (5000,"K"),
    ),
    reference = Reference(authors=["G. P. Smith", "D. M. Golden", "M. Frenklach", "N. W. Moriarty", "B. Eiteneer", "M. Goldenberg", "C. T. Bowman", "R. K. Hanson", "S. Song", "W. C. Gardiner, Jr.", "V. V. Lissianski", "Z. Qin."], title='GRI-Mech 3.0.', year="1999", url="http://www.me.berkeley.edu/gri-mech/version30/text30.html"),
    referenceType = "review",
    shortDesc = u"""Copied from GRI-Mech 3.0""",
    longDesc = 
u"""
This was copied from the GRI-Mech3.0 library.
The official GRI-Mech 3.0 has the minimum temperature on the NASA polynomial at 300K.
This prevents it from being used to evaluate the standard properties at 298K as required
by some parts of RMG. Extrapolating 2 degrees beyond the the recommended range probably
introduces less error than not using the thermo at all, so the range has been extended
to 298K.
""",
    history = [
        ("Tue May 24 11:29:29 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
        ("Sat Jun 11 11:51:00 2011","Richard West <rwest@mit.edu>","action","""Changed the Tmin from 300K to 298K."""),
    ],
)

entry(
    index = 16,
    label = "N2",
    molecule = 
"""
1     N     0 {2,T}
2     N     0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(Tmin=(298,"K"), Tmax=(1000,"K"), coeffs=[3.29868,0.00140824,-3.96322e-06,5.64152e-09,-2.44485e-12,-1020.9,3.95037]),
            NASAPolynomial(Tmin=(1000,"K"), Tmax=(5000,"K"), coeffs=[2.92664,0.00148798,-5.68476e-07,1.0097e-10,-6.75335e-15,-922.798,5.98053]),
        ],
        Tmin = (298,"K"),
        Tmax = (5000,"K"),
    ),
    reference = Reference(authors=["G. P. Smith", "D. M. Golden", "M. Frenklach", "N. W. Moriarty", "B. Eiteneer", "M. Goldenberg", "C. T. Bowman", "R. K. Hanson", "S. Song", "W. C. Gardiner, Jr.", "V. V. Lissianski", "Z. Qin."], title='GRI-Mech 3.0.', year="1999", url="http://www.me.berkeley.edu/gri-mech/version30/text30.html"),
    referenceType = "review",
    shortDesc = u"""Copied from GRI-Mech 3.0""",
    longDesc = 
u"""
This was copied from the GRI-Mech3.0 library.
The official GRI-Mech 3.0 has the minimum temperature on the NASA polynomial at 300K.
This prevents it from being used to evaluate the standard properties at 298K as required
by some parts of RMG. Extrapolating 2 degrees beyond the the recommended range probably
introduces less error than not using the thermo at all, so the range has been extended
to 298K.
""",
    history = [
        ("Tue May 24 11:29:29 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
        ("Sat Jun 11 11:51:00 2011","Richard West <rwest@mit.edu>","action","""Changed the Tmin from 300K to 298K."""),
    ],
)

entry(
    index = 17,
    label = "He",
    molecule = 
"""
1     He    0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(Tmin=(200,"K"), Tmax=(1000,"K"), coeffs=[2.5,0,0,0,0,-745.375,0.9287]),
            NASAPolynomial(Tmin=(1000,"K"), Tmax=(6000,"K"), coeffs=[2.5,0,0,0,0,-745.375,0.9287]),
        ],
        Tmin = (200,"K"),
        Tmax = (6000,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep 22 15:44:29 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 18,
    label = "Cl2",
    molecule = 
"""
1     Cl    0 {2,S}
2     Cl    0 {1,S}
""",
    thermo = NASA(
        polynomials=[
            NASAPolynomial(Tmin=(200,"K"), Tmax=(1000,"K"), coeffs=[2.73638,0.00783526,-1.45105e-05,1.25731e-08,-4.13247e-12,-1058.8,9.44557]),
            NASAPolynomial(Tmin=(1000,"K"), Tmax=(6000,"K"), coeffs=[4.74728,-0.000488582,2.68445e-07,-2.43476e-11,-1.03683e-15,-1511.02,-0.344539]),
        ],
        Tmin = (200,"K"),
        Tmax = (6000,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Burcat Thermo Data""",
    longDesc = 
u"""
Burcat Thermo Data

REFERENCE ELEMENT REF=Gurvich 1989 V1 py.1 p.177 HF298=0.00 kcal Max Lst 
Sq Error Cp @ 6000 **1.26%** (Cp @ 700 K 0.08%)
""",
    history = [
        ("Tue Sep 17 12:44:29 2013","Connie Gao <connieg@mit.edu>","action","""connieg added this entry to the database."""),
    ],
)

entry(
    index = 19,
    label = "Cl",
    molecule = 
"""
1     Cl    1
""",
    thermo = NASA(
        polynomials=[
            NASAPolynomial(Tmin=(200,"K"), Tmax=(1000,"K"), coeffs=[2.26062,0.00154154,-6.80284e-07,-1.59973e-09,1.15417e-12,13855.3,6.57021]),
            NASAPolynomial(Tmin=(1000,"K"), Tmax=(6000,"K"), coeffs=[2.94658,-0.000385985,1.36139e-07,-2.17033e-11,1.28751e-15,13697,3.1133]),
        ],
        Tmin = (200,"K"),
        Tmax = (6000,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Burcat Thermo Data""",
    longDesc = 
u"""
Burcat Thermo Data

HF298=121.302+/-0.008 kJ HF0=119.633+/- 0.008 kJ  REF=JANAF  {HF298=121.302
+/-0.002 kJ  REF=ATcT A}
""",
    history = [
        ("Tue Sep 17 12:44:29 2013","Connie Gao <connieg@mit.edu>","action","""connieg added this entry to the database."""),
    ],
)

entry(
    index = 20,
    label = "HCl",
    molecule = 
"""
1     Cl    0
""",
    thermo = NASA(
        polynomials=[
            NASAPolynomial(Tmin=(200,"K"), Tmax=(1000,"K"), coeffs=[3.46376,0.000476484,-2.00301e-06,3.31714e-09,-1.44958e-12,-12144.4,2.66428]),
            NASAPolynomial(Tmin=(1000,"K"), Tmax=(6000,"K"), coeffs=[2.75758,0.00145387,-4.79647e-07,7.77909e-11,-4.79574e-15,-11913.8,6.52197]),
        ],
        Tmin = (200,"K"),
        Tmax = (6000,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Burcat Thermo Data""",
    longDesc = 
u"""
Burcat Thermo Data

HYDROCHLORIC ACID CALCULATED FROM ORIGINAL TABLES  REF=Gurvich 1989
HF298=-92.31 kJ {HF298=-92.17+/-0.006 kJ   REF=ATcT C}  Max Lst Sq Error Cp @ 
6000 K 0.17%
""",
    history = [
        ("Tue Sep 17 12:44:29 2013","Connie Gao <connieg@mit.edu>","action","""connieg added this entry to the database."""),
    ],
)