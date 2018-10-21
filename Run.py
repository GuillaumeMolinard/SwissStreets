import pandas as pd
import numpy as np
import re as re
cantons = ['AG', 'AI']
df = { i: pd.read_csv('Canton/{0}/{0}.csv'.format(i), sep=';') for i in cantons }   #dict comprehensions
df['AG'] =
dfAG=pd.read_csv('Canton/AG/AG.csv', sep=';')
dfAI=pd.read_csv('Canton/AI/AI.csv', sep=';')
dfAR=pd.read_csv('Canton/AR/AR.csv', sep=';')
dfBE=pd.read_csv('Canton/BE/BE.csv', sep=';')
dfBL=pd.read_csv('Canton/BL/BL.csv', sep=';')
dfBS=pd.read_csv('Canton/BS/BS.csv', sep=';')
dfFR=pd.read_csv('Canton/FR/FR.csv', sep=';')
dfGE=pd.read_csv('Canton/GE/GE.csv', sep=';')
dfGL=pd.read_csv('Canton/GL/GL.csv', sep=';')
dfGR=pd.read_csv('Canton/GR/GR.csv', sep=';')
dfJU=pd.read_csv('Canton/JU/JU.csv', sep=';')
dfLU=pd.read_csv('Canton/LU/LU.csv', sep=';')
dfNE=pd.read_csv('Canton/NE/NE.csv', sep=';')
dfNW=pd.read_csv('Canton/NW/NW.csv', sep=';')
dfOW=pd.read_csv('Canton/OW/OW.csv', sep=';')
dfSG=pd.read_csv('Canton/SG/SG.csv', sep=';')
dfSH=pd.read_csv('Canton/SH/SH.csv', sep=';')
dfSO=pd.read_csv('Canton/SO/SO.csv', sep=';')
dfSZ=pd.read_csv('Canton/SZ/SZ.csv', sep=';')
dfTG=pd.read_csv('Canton/TG/TG.csv', sep=';')
dfTI=pd.read_csv('Canton/TI/TI.csv', sep=';')
dfUR=pd.read_csv('Canton/UR/UR.csv', sep=';')
dfVD=pd.read_csv('Canton/VD/VD.csv', sep=';')
dfVS=pd.read_csv('Canton/VS/VS.csv', sep=';')
dfZG=pd.read_csv('Canton/ZG/ZG.csv', sep=';')
dfZH=pd.read_csv('Canton/ZH/ZH.csv', sep=';')

frames = [dfAG, dfAI, dfAR, dfBE, dfBL, dfBS, dfFR, dfGE, dfGL, dfGR, dfJU, dfLU, dfNE, dfNW, dfOW, dfSG, dfSH, dfSO, dfSZ, dfTG, dfTI, dfUR, dfVD, dfVS, dfZG, dfZH]
dfCONF = pd.concat(frames, sort=True)
dfCONF.drop_duplicates(['GDENAME', 'STRNAME'], inplace=True) #Drop duplicate of same street and city





pat = re.compile(r'\s+\([^()]{2}\)')
dfCONF['GDENAME'] = dfCONF['GDENAME'].apply(lambda x: pat.sub('', x))



raw_data = {'name_short': ['AG', 'AI', 'AR', 'BE', 'BL', 'BS', 'FR', 'GE', 'GL', 'GR', 'JU', 'LU', 'NE', 'NW', 'OW', 'SG', 'SH', 'SO', 'SZ', 'TG', 'TI', 'UR', 'VD', 'VS', 'ZG', 'ZH'],
            'name_long_native?': ['Aargau', 'Appenzell Innerrhoden', 'Appenzell Ausserrhoden', 'Bern', 'Basel-Landschaft', 'Basel-Stadt', 'Fribourg', 'Genève', 'Glarus', 'Graubünden', 'Jura', 'Luzern', 'Neuchâtel', 'Nidwalden', 'Obwalden', 'St. Gallen', 'Schaffhausen', 'Solothurn', 'Schwyz', 'Thurgau', 'Ticino', 'Uri', 'Vaud', 'Valais', 'Zug', 'Zürich']}
dfMASTERI = pd.DataFrame(raw_data)

#add citation column filled with nan to dfMASTERI
dfMASTERI["citation"] = np.nan

#search for string containing 'Aargau' in dfCONF['STRNAME'] and putting those rows in dfAargau
dfAargau = dfCONF[dfCONF['STRNAME'].str.contains('Aargau')]
dfAargauFR = dfCONF[dfCONF['STRNAME'].str.contains('Argovie')]
dfAargau = dfAargau.append(dfAargauFR, ignore_index=True)
dfAargauIT = dfCONF[dfCONF['STRNAME'].str.contains('Argovia')]
dfAargau = dfAargau.append(dfAargauIT, ignore_index=True)


#remove canton origin
dfAargau = dfAargau.replace('AG', np.nan).dropna()

#count lenght dataframe
dfMASTERI.iloc[0, 2] = dfAargau['STRNAME'].count()

#finish for all cantons


#Languages Done
dfAppenzellI = dfCONF[dfCONF['STRNAME'].str.contains('Innerrhoden')]
dfAppenzellII = dfCONF[dfCONF['STRNAME'].str.contains('Appenzell')]
dfAppenzellI = dfAppenzellI.append(dfAppenzellII, ignore_index=True)
dfAppenzellIIIT = dfCONF[dfCONF['STRNAME'].str.contains('Appenzello')]
dfAppenzellI = dfAppenzellI.append(dfAppenzellIIIT, ignore_index=True)
dfAppenzellI = dfAppenzellI.replace('AI', np.nan).dropna()
dfMASTERI.iloc[1, 2] = dfAppenzellI['STRNAME'].count()

#Languages Done
dfAppenzellA = dfCONF[dfCONF['STRNAME'].str.contains('Ausserrhoden')]
dfAppenzellAA = dfCONF[dfCONF['STRNAME'].str.contains('Appenzell')]
dfAppenzellA = dfAppenzellA.append(dfAppenzellAA, ignore_index=True)
dfAppenzellAIT = dfCONF[dfCONF['STRNAME'].str.contains('Appenzello')]
dfAppenzellA = dfAppenzellA.append(dfAppenzellAIT, ignore_index=True)
dfAppenzellA = dfAppenzellA.replace('AR', np.nan).dropna()
dfMASTERI.iloc[2, 2] = dfAppenzellA['STRNAME'].count()


#Languages Done
dfBern = dfCONF[dfCONF['STRNAME'].str.contains('Bern')]
dfBernFR = dfCONF[dfCONF['STRNAME'].str.contains('Berne')]
dfBern = dfBern.append(dfBernFR, ignore_index=True)
dfBernIT = dfCONF[dfCONF['STRNAME'].str.contains('Berna')]
dfBern = dfBern.append(dfBernIT, ignore_index=True)

dfBern = dfBern.replace('BE', np.nan).dropna()
#remove places containing Bernard
#dfBern = dfBern.replace('Bernard', np.nan).dropna()
dfMASTERI.iloc[3, 2] = dfBern['STRNAME'].count()

#Languages Done
dfBaselL = dfCONF[dfCONF['STRNAME'].str.contains('Basel')]
dfBaselLFR = dfCONF[dfCONF['STRNAME'].str.contains('Bâle')]
dfBaselL = dfBaselL.append(dfBaselLFR, ignore_index=True)
dfBaselLIT = dfCONF[dfCONF['STRNAME'].str.contains('Basilea')]
dfBaselL = dfBaselL.append(dfBaselLIT, ignore_index=True)
dfBaselL = dfBaselL.replace('BL', np.nan).dropna()
dfMASTERI.iloc[4, 2] = dfBaselL['STRNAME'].count()

#Languages Done
dfBaselS = dfCONF[dfCONF['STRNAME'].str.contains('Basel')]
dfBaselSFR = dfCONF[dfCONF['STRNAME'].str.contains('Bâle')]
dfBaselS = dfBaselS.append(dfBaselSFR, ignore_index=True)
dfBaselSIT = dfCONF[dfCONF['STRNAME'].str.contains('Basilea')]
dfBaselS = dfBaselS.append(dfBaselSIT, ignore_index=True)
dfBaselS = dfBaselS.replace('BS', np.nan).dropna()
dfMASTERI.iloc[5, 2] = dfBaselS['STRNAME'].count()

#Languages Done
dfFribourg = dfCONF[dfCONF['STRNAME'].str.contains('Fribourg')]
dfFribourgGE = dfCONF[dfCONF['STRNAME'].str.contains('Freiburg')]
dfFribourg = dfFribourg.append(dfFribourgGE, ignore_index=True)
dfFribourgIT = dfCONF[dfCONF['STRNAME'].str.contains('Friburgo')]
dfFribourg = dfFribourg.append(dfFribourgIT, ignore_index=True)
dfFribourgRO = dfCONF[dfCONF['STRNAME'].str.contains('Friburg')]
dfFribourg = dfFribourg.append(dfFribourgRO, ignore_index=True)
dfFribourg = dfFribourg.replace('FR', np.nan).dropna()
dfMASTERI.iloc[6, 2] = dfFribourg['STRNAME'].count()

#Languages Done
dfGeneve = dfCONF[dfCONF['STRNAME'].str.contains('Genève')]
dfGeneveGE = dfCONF[dfCONF['STRNAME'].str.contains('Genf')]
dfGeneve = dfGeneve.append(dfGeneveGE, ignore_index=True)
dfGeneveIT = dfCONF[dfCONF['STRNAME'].str.contains('Ginevra')]
dfGeneve = dfGeneve.append(dfGeneveIT, ignore_index=True)
dfGeneveRO = dfCONF[dfCONF['STRNAME'].str.contains('Genevra')]
dfGeneve = dfGeneve.append(dfGeneveRO, ignore_index=True)
dfGeneve = dfGeneve.replace('GE', np.nan).dropna()
dfMASTERI.iloc[7, 2] = dfGeneve['STRNAME'].count()

#Languages Done
dfGlarus = dfCONF[dfCONF['STRNAME'].str.contains('Glarus')]
dfGlarusFR = dfCONF[dfCONF['STRNAME'].str.contains('Glaris')]
dfGlarus = dfGlarus.append(dfGlarusFR, ignore_index=True)
dfGlarusIT = dfCONF[dfCONF['STRNAME'].str.contains('Glarona')]
dfGlarus = dfGlarus.append(dfGlarusIT, ignore_index=True)
dfGlarusRO = dfCONF[dfCONF['STRNAME'].str.contains('Glaruna')]
dfGlarus = dfGlarus.append(dfGlarusRO, ignore_index=True)
dfGlarus = dfGlarus.replace('GL', np.nan).dropna()
dfMASTERI.iloc[8, 2] = dfGlarus['STRNAME'].count()



#Languages Done
dfGraubunden = dfCONF[dfCONF['STRNAME'].str.contains('Graubünden')]
dfGraubundenFR = dfCONF[dfCONF['STRNAME'].str.contains('Grisons')]
dfGraubunden = dfGraubunden.append(dfGraubundenFR, ignore_index=True)
dfGraubundenIT = dfCONF[dfCONF['STRNAME'].str.contains('Grigioni')]
dfGraubunden = dfGraubunden.append(dfGraubundenIT, ignore_index=True)
dfGraubundenRO = dfCONF[dfCONF['STRNAME'].str.contains('Grischun')]
dfGraubunden = dfGraubunden.append(dfGraubundenRO, ignore_index=True)
dfGraubunden = dfGraubunden.replace('GR', np.nan).dropna()
dfMASTERI.iloc[9, 2] = dfGraubunden['STRNAME'].count()

#Languages Done
dfJura = dfCONF[dfCONF['STRNAME'].str.contains('Jura')]
dfJuraIT = dfCONF[dfCONF['STRNAME'].str.contains('Giura')]
dfJura = dfJura.append(dfJuraIT, ignore_index=True)
dfJura = dfJura.replace('JU', np.nan).dropna()
dfMASTERI.iloc[10, 2] = dfJura['STRNAME'].count()


#Languages Done
dfLuzern = dfCONF[dfCONF['STRNAME'].str.contains('Luzern')]
dfLuzernFR = dfCONF[dfCONF['STRNAME'].str.contains('Lucerne')]
dfLuzern = dfLuzern.append(dfLuzernFR, ignore_index=True)
dfLuzernIT = dfCONF[dfCONF['STRNAME'].str.contains('Lucerna')]
dfLuzern = dfLuzern.append(dfLuzernIT, ignore_index=True)
dfLuzern = dfLuzern.replace('LU', np.nan).dropna()
dfMASTERI.iloc[11, 2] = dfLuzern['STRNAME'].count()

#Languages Done
dfNeuchatel = dfCONF[dfCONF['STRNAME'].str.contains('Neuchâtel')]
dfNeuchatelGE = dfCONF[dfCONF['STRNAME'].str.contains('Neuenburg')]
dfNeuchatel = dfNeuchatel.append(dfNeuchatelGE, ignore_index=True)
dfNeuchatelIT = dfCONF[dfCONF['STRNAME'].str.contains('Neocastello')]
dfNeuchatel = dfNeuchatel.append(dfNeuchatelIT, ignore_index=True)
dfNeuchatel = dfNeuchatel.replace('NE', np.nan).dropna()
dfMASTERI.iloc[12, 2] = dfNeuchatel['STRNAME'].count()

#Languages Done
dfNidwalden = dfCONF[dfCONF['STRNAME'].str.contains('Nidwalden')]
dfNidwaldenFR = dfCONF[dfCONF['STRNAME'].str.contains('Nidwald')]
dfNidwalden = dfNidwalden.append(dfNidwaldenFR, ignore_index=True)
dfNidwaldenRO = dfCONF[dfCONF['STRNAME'].str.contains('Sutsilvania')]
dfNidwalden = dfNidwalden.append(dfNidwaldenRO, ignore_index=True)
dfNidwaldenIT = dfCONF[dfCONF['STRNAME'].str.contains('Nidvaldo')]
dfNidwalden = dfNidwalden.append(dfNidwaldenIT, ignore_index=True)
dfNidwalden = dfNidwalden.replace('NI', np.nan).dropna()
dfMASTERI.iloc[13, 2] = dfNidwalden['STRNAME'].count()

#Languages Done
dfObwalden = dfCONF[dfCONF['STRNAME'].str.contains('Obwalden')]
dfObwaldenFR = dfCONF[dfCONF['STRNAME'].str.contains('Obwald')]
dfObwalden = dfObwalden.append(dfObwaldenFR, ignore_index=True)
dfObwaldenIT = dfCONF[dfCONF['STRNAME'].str.contains('Obvaldo')]
dfObwalden = dfObwalden.append(dfObwaldenIT, ignore_index=True)
dfObwaldenRO = dfCONF[dfCONF['STRNAME'].str.contains('Sursilvania')]
dfObwalden = dfObwalden.append(dfObwaldenRO, ignore_index=True)
dfObwalden = dfObwalden.replace('OW', np.nan).dropna()
dfMASTERI.iloc[14, 2] = dfObwalden['STRNAME'].count()


#Languages Done
dfStGallen = dfCONF[dfCONF['STRNAME'].str.contains('St. Gallen')]
dfStGallenFR = dfCONF[dfCONF['STRNAME'].str.contains('Saint-Gall')]
dfStGallen = dfStGallen.append(dfStGallenFR, ignore_index=True)
dfStGallenIT = dfCONF[dfCONF['STRNAME'].str.contains('San Gallo')]
dfStGallen = dfStGallen.append(dfStGallenIT, ignore_index=True)
dfStGallenGE = dfCONF[dfCONF['STRNAME'].str.contains('Sanggale')]
dfStGallen = dfStGallen.append(dfStGallenGE, ignore_index=True)
dfStGallenRO = dfCONF[dfCONF['STRNAME'].str.contains('Sogn Gagl')]
dfStGallen = dfStGallen.append(dfStGallenRO, ignore_index=True)
dfStGallen = dfStGallen.replace('SG', np.nan).dropna()
dfMASTERI.iloc[15, 2] = dfStGallen['STRNAME'].count()

#Languages Done
dfSchaffhausen = dfCONF[dfCONF['STRNAME'].str.contains('Schaffhausen')]
dfSchaffhausenFR = dfCONF[dfCONF['STRNAME'].str.contains('Schaffhouse')]
dfSchaffhausen = dfSchaffhausen.append(dfSchaffhausenFR, ignore_index=True)
dfSchaffhausenIT = dfCONF[dfCONF['STRNAME'].str.contains('Sciaffusa')]
dfSchaffhausen = dfSchaffhausen.append(dfSchaffhausenIT, ignore_index=True)
dfSchaffhausenRO = dfCONF[dfCONF['STRNAME'].str.contains('Schaffusa')]
dfSchaffhausen = dfSchaffhausen.append(dfSchaffhausenRO, ignore_index=True)
dfSchaffhausen = dfSchaffhausen.replace('SH', np.nan).dropna()
dfMASTERI.iloc[16, 2] = dfSchaffhausen['STRNAME'].count()

#Languages Done
dfSolothurn = dfCONF[dfCONF['STRNAME'].str.contains('Solothurn')]
dfSolothurnFR = dfCONF[dfCONF['STRNAME'].str.contains('Soleure')]
dfSolothurn = dfSolothurn.append(dfSolothurnFR, ignore_index=True)
dfSolothurnIT = dfCONF[dfCONF['STRNAME'].str.contains('Soletta')]
dfSolothurn = dfSolothurn.append(dfSolothurnIT, ignore_index=True)
dfSolothurnRO = dfCONF[dfCONF['STRNAME'].str.contains('Soloturn')]
dfSolothurn = dfSolothurn.append(dfSolothurnRO, ignore_index=True)
dfSolothurn = dfSolothurn.replace('SO', np.nan).dropna()
dfMASTERI.iloc[17, 2] = dfSolothurn['STRNAME'].count()

#Languages Done
dfSchwyz = dfCONF[dfCONF['STRNAME'].str.contains('Schwyz')]
dfSchwyzFR = dfCONF[dfCONF['STRNAME'].str.contains('Schwytz')]
dfSchwyz = dfSchwyz.append(dfSchwyzFR, ignore_index=True)
dfSchwyzIT = dfCONF[dfCONF['STRNAME'].str.contains('Svitto')]
dfSchwyz = dfSchwyz.append(dfSchwyzIT, ignore_index=True)
dfSchwyzRO = dfCONF[dfCONF['STRNAME'].str.contains('Sviz')]
dfSchwyz = dfSchwyz.append(dfSchwyzRO, ignore_index=True)
dfSchwyz = dfSchwyz.replace('SZ', np.nan).dropna()
dfMASTERI.iloc[18, 2] = dfSchwyz['STRNAME'].count()

#Languages Done
dfThurgau = dfCONF[dfCONF['STRNAME'].str.contains('Thurgau')]
dfThurgauFR = dfCONF[dfCONF['STRNAME'].str.contains('Thurgovie')]
dfThurgau = dfThurgau.append(dfThurgauFR, ignore_index=True)
dfThurgauIT = dfCONF[dfCONF['STRNAME'].str.contains('Turgovia')]
dfThurgau = dfThurgau.append(dfThurgauIT, ignore_index=True)
dfThurgau = dfThurgau.replace('TG', np.nan).dropna()
dfMASTERI.iloc[19, 2] = dfThurgau['STRNAME'].count()

#Languages Done
dfTicino = dfCONF[dfCONF['STRNAME'].str.contains('Ticino')]
dfTicinoFR = dfCONF[dfCONF['STRNAME'].str.contains('Tessin')]
dfTicino = dfTicino.append(dfTicinoFR, ignore_index=True)
dfTicino = dfTicino.replace('TI', np.nan).dropna()
dfMASTERI.iloc[20, 2] = dfTicino['STRNAME'].count()

#Languages Done
dfUri = dfCONF[dfCONF['STRNAME'].str.contains('Uri')]
dfUri = dfUri.replace('UR', np.nan).dropna()
dfMASTERI.iloc[21, 2] = dfUri['STRNAME'].count()

#Languages Done
dfVaud = dfCONF[dfCONF['STRNAME'].str.contains('Vaud')]
dfVaudGE = dfCONF[dfCONF['STRNAME'].str.contains('Waadt')]
dfVaud = dfVaud.append(dfVaudGE, ignore_index=True)
dfVaudRO = dfCONF[dfCONF['STRNAME'].str.contains('Vad')]
dfVaud = dfVaud.append(dfVaudRO, ignore_index=True)
dfVaud = dfVaud.replace('VD', np.nan).dropna()
dfMASTERI.iloc[22, 2] = dfVaud['STRNAME'].count()

#Languages Done
dfValais = dfCONF[dfCONF['STRNAME'].str.contains('Valais')]
dfValaisGE = dfCONF[dfCONF['STRNAME'].str.contains('Wallis')]
dfValais = dfValais.append(dfValaisGE, ignore_index=True)
dfValaisIT = dfCONF[dfCONF['STRNAME'].str.contains('Vallese')]
dfValais = dfValais.append(dfValaisIT, ignore_index=True)
dfValaisRO = dfCONF[dfCONF['STRNAME'].str.contains('Vallais')]
dfValais = dfValais.append(dfValaisRO, ignore_index=True)
dfValais = dfValais.replace('VS', np.nan).dropna()
dfMASTERI.iloc[23, 2] = dfValais['STRNAME'].count()

#Languages Done
dfZug = dfCONF[dfCONF['STRNAME'].str.contains('Zug')]
dfZugFR = dfCONF[dfCONF['STRNAME'].str.contains('Zoug')]
dfZug = dfZug.append(dfZugFR, ignore_index=True)
dfZugIT = dfCONF[dfCONF['STRNAME'].str.contains('Zugo')]
dfZug = dfZug.append(dfZugIT, ignore_index=True)
dfZug = dfZug.replace('ZG', np.nan).dropna()
dfMASTERI.iloc[24, 2] = dfZug['STRNAME'].count()

#Languages Done
dfZurich = dfCONF[dfCONF['STRNAME'].str.contains('Zürich')]
dfZurichIT = dfCONF[dfCONF['STRNAME'].str.contains('Zurigo')]
dfZurich = dfZurich.append(dfZurichIT, ignore_index=True)
dfZurichFR = dfCONF[dfCONF['STRNAME'].str.contains('Zurich')]
dfZurich = dfZurich.append(dfZurichFR, ignore_index=True)
dfZurichRO = dfCONF[dfCONF['STRNAME'].str.contains('Turitg')]
dfZurich = dfZurich.append(dfZurichRO, ignore_index=True)
dfZurich = dfZurich.replace('ZH', np.nan).dropna()
dfMASTERI.iloc[25, 2] = dfZurich['STRNAME'].count()
