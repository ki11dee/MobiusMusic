from bwv1073_cello import cello
from bwv1073_viola import viola_mod
from bwv1073_violin import violin_mod
from bwv1073_flute import flute_mod
from music21 import note, stream, instrument

score = stream.Score()
score.append(cello)  # 첼로 성부 추가
score.append(viola_mod)  # 비올라 성부 추가
score.append(violin_mod)  # 바이올린 성부 추가
score.append(flute_mod)  # 플루트 성부 추가

cello.insert(0, instrument.Violoncello())
viola_mod.insert(0, instrument.Viola())
violin_mod.insert(0, instrument.Violin())
flute_mod.insert(0, instrument.Flute())



score.show('text')
score.show('midi')