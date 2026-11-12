"""
Iraqi-Arabic dialect-marker lexicons and the marker-density diagnostic.
Released with: "Egyptian in Iraqi Clothing: A Native-Speaker Audit of a
Mislabelled 'Iraqi' Partition in a Public Arabic Dialect Corpus."

This is a DESCRIPTIVE screening diagnostic (word-list matching + counting),
not a trained classifier. It reproduces the marker-density audit in the paper.
"""
import re

# Iraqi-exclusive markers (phonological anchors weighted highest)
IRAQI = ["چ","گ","هسه","هسع","اكو","ماكو","شكو","وين","هواية","هواي","خوش","باجر",
         "شنو","منين","هيچي","هيچ","گاعد","گلت","اشلون","شلون","كلش","شكد","منو","يابه",
         "مو","بس","اريد","اكدر","تره","لعد","خل","عاشت","احنه","هيج","ليش"]
EGYPTIAN  = ["بتاع","بتاعت","احنا","هنعمل","عايز","عاوز","دلوقتي","كده","اوي","مش",
             "دي","ده","زي","عشان","ازاي","يبقى","علشان","لسه","معلش","تانى","تاني"]
GULF_SAUDI = ["وش","ويش","كذا","المملكة","الرياض","حنا","ابغى","ابغا","طاري","كيفك",
              "عساك","السعود","جده","الدمام"]
LEVANTINE = ["هلق","لهيك","بدي","منيح","هيك","كتير"]

def normalize(t: str) -> str:
    t = re.sub(r'[ً-ْـ]', '', t)
    t = t.replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ى','ي').replace('ة','ه')
    return t

def _match(tn, markers):
    out=[]
    for m in markers:
        mn=normalize(m)
        if len(mn)==1:
            if mn in tn: out.append(m)
        elif re.search(r'(^|\s)'+re.escape(mn)+r'($|\s|[.,!؟،])', tn):
            out.append(m)
    return out

def iraqi_marker_count(text: str) -> int:
    return len(_match(normalize(text), IRAQI))

def dialect_markers(text: str) -> dict:
    tn = normalize(text)
    return {"iraqi":_match(tn,IRAQI), "egyptian":_match(tn,EGYPTIAN),
            "gulf":_match(tn,GULF_SAUDI), "levantine":_match(tn,LEVANTINE)}
