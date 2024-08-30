# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#%%
import os

os.chdir('C:\\Users\\aurel\\OneDrive\\Documents (2)\\École Aurelien\\MIT\\Recherche\\Biblio')

bib='bibFiberoptics.bib'

with open(bib,'r', encoding="utf-8") as fr:
    bibw=bib.split(".bib")[0]+"_custom.bib"
    L=fr.readlines()
    name=""
    NAMEurlEXCEP = ["duin_duin_nodate","govindarajan_atomic-scale_2011",
                    "morana_gamma-rays_2013","the_fiber_optic_association_inc_foa_2018",
                    "atomic_energy_of_canada_limited_instruction_1968","buehler_methods_2021",
                    "bende_nakulbendettl_trigger_2023","short_co-60_nodate","vaughan_edf_2017",
                    "noauthor_comsol_nodate","noauthor_mass_nodate","noauthor_superk_nodate"]
    NAMEissnEXCEP = []
    with open(bibw,'w', encoding="utf-8") as fw:
        for l in L:
            # print(l)
            if "@" in l:
                name = l.split("{")[1].split(",")[0]
            if (not("url" in l) or name in NAMEurlEXCEP) and\
               (not("issn" in l) or name in NAMEissnEXCEP) and\
                not("urldate" in l) :
                # print(l)
                fw.write(l.replace(u"\u2009",' '))
print("New bib written")