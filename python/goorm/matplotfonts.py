from typing import Text
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

mpl.rcParams['axes.unicode_minus']=False
data=np.random.randint(-100,100,50).cumsum()
# print(data)

# plt.plot(range(50),data,'r')
# mpl.rcParams['axes.unicode_minus']=False
# plt.title('시간별 가격 추이')
# plt.ylabel('주식 가격')
# plt.xlabel('시간(분)')

# plt.show()

# print ('설치 위치: ', mpl.__file__)
# print ('설정 위치: ', mpl.get_configdir())
# print ('캐시 위치: ', mpl.get_cachedir())
# print ('설정파일 위치: ', mpl.matplotlib_fname())

# font_list =fm.findSystemFonts(fontpaths=None,fontext='ttf')

# f = [f.name for f in fm.fontManager.ttflist]
# print(len(font_list))
# # 10개의 폰트명 만 출력

# print(f[:10])
# print(mpl.get_cachedir())
# print([(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name])

path = '/Library/Fonts/NanumBarunGothic.ttf'
font_name = fm.FontProperties(fname=path, size=50).get_name()
print(font_name)
plt.rc('font', family=font_name)

fig, ax = plt.subplots()
ax.plot(data)
ax.set_title('시간별 가격 추이')
plt.ylabel('주식 가격')
plt.xlabel('시간(분)')
plt.style.use('ggplot')
plt.show()