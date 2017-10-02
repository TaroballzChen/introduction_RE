#正則表達式用來匹配字符串的
#引入正則:進行模糊匹配
import re

ret=re.findall('w\w{2}l','hello world')
print(ret)

ret1=re.findall('alex','adsfdsfdsafalexasdfasdfasalexdf') #字符完全匹配  不需要用到re
print(ret1)

#元字符 . ^ $ * + ? { }  [ ] | ( ) \  共11個
#\t \n \s 等等皆代表一個字符

ret2 = re.findall('w..l','hello world')  #  . 代指所有的字符 除了\n  一個.代指一個字符 ----> 通配符
print(ret2)

ret3 = re.findall('w..l','hello w\nld')  # .無法代指 \n  ---->其他都可以
print(ret3)

#re.findall(pattern,string,flags) 第三個參數flags可以修改成其他參數讓他匹配所有內容 一般不用

ret4 = re.findall('^h...o','hadfodfhello')  # ^ 只在開始的位置匹配^後面跟的字符 --------> 只看開始
print(ret4)

ret5 = re.findall('h...o$','hadfodfhello')  # $ 只在結尾的位置匹配$前面跟的字符 ----------> 只看結束
print(ret5)

ret6 = re.findall('a.*i','adlfjsdfkjsdaflasdfkljbsdjsdlkfjsdi') # * 代指 * 前面的字符重複多次匹配 若為. 則任意字符匹配多次(0到無限次)
print(ret6)

ret7 = re.findall('a.+i','axi') # + 代指前面的字符重複多次匹配，若為 . 則任意字符匹配多次 (1到無限次)
print(ret7)

ret8 = re.findall('ho?','dsfhhello') # ? 代指前面的字符只能重複一次或0次
print(ret8)

ret9 = re.findall('a{5}b','aaaaaaaaaabbbbbb') # {N} 代指前面的字符重複匹配大括號中間的數字次
print(ret9)

ret10 = re.findall('a{1,3}b','aaaaaaaaaaabbbbbbbbbbbb')  # {n,n} 代指匹配前面字符一個範圍內的次數 但是能匹配越多次越好 (貪婪匹配)
print(ret10)

# * 也指的是{0,正無窮}  + 也指的是{1,正無窮}  ? 等價於{0,1}  要是 正無窮也可用 "甚麼不加替代" 例如{1,} 指1到正無窮

#[]字符集
ret11 = re.findall('a[c,d]x','acx')  #[] 可匹配[]中間任一字符 ----->匹配c或d
print(ret11)

ret12 = re.findall('a[a-z]','acx') # [] 也可匹配一個範圍的字母
print(ret12)

#[]字符集: 可取消元字符的特殊功能 (例外: \ , ^ , -)
ret12= re.findall('[w.]','awdx.,')  # 找出原本具有功能的特殊字元 讓他取消功能
print(ret12)

ret13=re.findall('[1-9a-zA-Z]','12tyAS')  #也可以用作匹配一個範圍內的字符 等同於 [1-9,a-z,A-Z]
print(ret13)

ret14=re.findall('[^t]','sdtslklj')  # [^ t]  匹配't'字符外的其他字符 ----->將t不匹配 ----> 取反值
print(ret14)

# \ 反斜槓後邊跟元字符去除特殊功能， 反斜槓後邊跟普通字符實現特殊功能

# \d 匹配任何十進位數 相當於[0-9]
# \D 匹配任何非數字字符 相當於 [^0-9]
# \s 匹配任何空白字符 相當於 [ \t\n\r\f\v]
# \S 匹配任何非空白字符 相當於 [^ \t\n\r\f\v]
# \w 匹配任何字母數字字符 相當於 [a-zA-Z0-9_]
# \W 匹配任何字母數字字符 相當於 [^a-zA-Z0-9_]
# \b 匹配一個要字符後面為特殊字符 (單詞)邊界, 也就是指單詞和空格間的位置

print(re.findall('\d{11}','adfjkdfbioundfb54156798451454'))
print(re.findall('\sasd','fak asd'))
print(re.findall('\wasd','fak asd'))
print(re.findall(r'I\b',"Hello, I am a LIST"))   #\b代表一個單詞的邊界 前面

###################################################################################
# search 指返回滿足條件的第一個結果--->但是為一個對象---->顯示的是範圍
# finall是返回全部結果

print(re.search('sb','fjasksdfkjsdfsb'))   #返回的是一個對象
ret15 = re.search('sb','fjasksdfkjsdfsb')
print(ret15.group())            #search對象  使用方法.group即可得到內容

print(re.search('a\.','a.gj').group())   # 反斜槓後面接特殊符號 其特殊符號不具特殊功能
print(re.search('a\+','a+123').group())

########################################################################################
# () 小括號用作分組

print(re.search('(as)+','asasasasasasdfdfdfdf').group())   #小括號裡面的字符串作為一個整體 藉由+號疊加去匹配

# | 代表的是 "或"  匹配左或右邊的字符

print(re.search('(as)+|3','3asasasasasasdfdfdfdf').group())   # search指匹配第一個 要是使用findall則會全部匹配到
print(re.findall('(as)+|3','3asasasasasasdfdfdfdf'))
##########################進階用法####################
#匹配時同時賦值 一定得加(?P<你賦值的名稱>賦值的內容)

ret_ = re.search('(?P<id>\d{3})/(?P<name>\w{3})','weew34ttt123/ooo')

print(ret_.group())
print(ret_.group('id'))
print(ret_.group("name"))
##########正則表達式的方法#################################################################

# 1. findall(): 所有的結果皆返回到一個列表中
# 2. search(): 返回匹配到的第一個對象(包含信息)，對象可以調用group()方法拿取返回結果
# 3. match(): 指在字符串開始匹配 也只返回一個對象(object)(包含信息)，對象可以調用group()方法拿取返回結果
print(re.match('asd','fhdsasd'))     # 返回None值
print(re.match("asd",'asdbdfbdsfb').group()) # 返回對象 可用group取得結果

# 4. split():
print(re.split('k','djksal'))
print(re.split('[k,s]','djkdsal'))    # 先透過k 進行split之後得到的字符串再用s進行split得到最終的結果 ----> 列表

# 5. sub() 替換  ---->re.sub('要找到的字符串規則','要替換的內容','要替換的內容')
print(re.sub('a..x','Louis','lksdalexjflsk'))

# 6. compile()  有一種規則可能會應用多次 將其編譯成對象------>調用其他正則方法操作
obj = re.compile('\.com')     #可以把正則表達式編譯成正則表達式對象

print(obj.findall('tw.yahoo.com'))     #用對象調用其他re的方法