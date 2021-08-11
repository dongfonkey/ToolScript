# ToolScript 个人工具集使用说明

标签（空格分隔）： 教程整理

---

> ###前言
> 该工具合集是鄙人在日常处理数据过程中所积累的一些常用功能的python实现。大多是随手一写，本着能用即可的目的，所以代码并不美丽，更没有面面俱到去做测试和优化，但确实能省去了很多重复编码的时间，姑且觉得还是有用且有必要的，所以将它们公开出来，同时也是为了方便鄙人自己回顾浏览。

> 后期还会不定时进行更新。。。更新时间视鄙人的懒惰程度和心情指数而定。。。

> 自娱自乐的东西。欢迎提交分支，但大概率懒得去看；可以提出意见，但大概率懒得去理。

----

###**<font color="red">一、 如何使用</font>**
----------

 - 将`ToolScript`文件夹放到任一目录下，推荐为C盘根目录
 - 将文件夹路径添加到系统变量中
 ![image_1fcpj896m10qh1jum1tgjre5j2p9.png-9kB][1]
 - 在终端中输入`path_test`，测试能否成功输出系统变量和文件夹路径。成功获得输出则安装成功。
 ![image_1fcpjbnfg13nnrt01ngkidr3bjm.png-2.7kB][2]
<br />

----

###**<font color="red">二、工具详细说明</font>**

>直接在终端中输入工具命令和参数即可，如
> ```
> txt_de_emphasis -f test.txt
> ```
>在各个小工具命令后使用`-h`即可查看使用说明

####1. **文本文件处理**

**<font color="green">① txt_de_emphasis：去除txt文件中的重复行</font>**
参数简写 | 参数详写 | 说明 | 备注
:--:|:--:|:--:|:--:
-f | --file | 欲处理的文件名或文件路径 |

**<font color="green">② txt2csv：按照分隔符将文本文件转换为csv文件</font>**
参数简写 | 参数详写 | 说明 | 备注
:--:|:--:|:--:|:--:
-f | --file | 欲处理的文件名或文件路径 |
-o | --output | 输出文件名或文件路径 | 如不指定，则默认与输入文件同名
-s | --splitLabel | 分隔符 | 如不指定，则默认为"\t"

**<font color="green">③ extract_top_n_lines：抽取文件的前n行</font>**
参数简写 | 参数详写 | 说明 | 备注
:--:|:--:|:--:|:--:
-f | --file | 欲处理的文件名或文件路径 |
-o | --output | 结果输出文件名或文件路径 | 如不指定，则在控制台中打印
-n | | 欲抽取的行数 | 

####2. **CSV文件处理**

**<font color="green">① count_by_keys：统计csv中每个字段的非空数据条目</font>**
参数简写 | 参数详写 | 说明 | 备注
:--:|:--:|:--:|:--:
-f | --file | 欲处理的文件名或文件路径 |
-o | --output | 结果输出文件名或文件路径 | 如不指定，则在控制台中打印

**<font color="green">② csv_remove_column：根据字段删除某一列</font>**
参数简写 | 参数详写 | 说明 | 备注
:--:|:--:|:--:|:--:
-f | --file | 欲处理的文件名或文件路径 |
-o | --output | 结果输出文件名或文件路径 | 
-t | --title | 欲删除的列的字段名 | 目前只支持删除单一的列，且必须指定字段名

**<font color="green">③ group_by_title：根据某一字段的值进行分组</font>**
参数简写 | 参数详写 | 说明 | 备注
:--:|:--:|:--:|:--:
-f | --file | 欲处理的文件名或文件路径 |
-t | --title | 分组所依据的字段名（列名） | 
-g | --group | 分组类别 | ○ 在指定字段下分组使用的值，彼此间用","隔开<br>○ 如"children,teen,adult,old"，未指定的条目自动分类为“其它”<br>○ csv文件将按照分组自动转储到以值命名的csv文件中<br>○ 若不指定，则自动按照字段下所有的值自动进行分组

**<font color="green">④ sorted_by_title：按照某一字段的值进行排序</font>**
参数简写 | 参数详写 | 说明 | 备注
:--:|:--:|:--:|:--:
-f | --file | 欲处理的文件名或文件路径 |
-o | --output | 结果输出文件名或文件路径 | 如不指定，默认为"output.csv"
-t | --title | 排序所依据的字段名（列名） | 该字段的值必须是数字
-r | --reverse | 是否降序排列 | 可选值为"True"和"False"，默认为True

**<font color="green">⑤ sum_by_title：按照某一字段的值进行排序</font>**
参数简写 | 参数详写 | 说明 | 备注
:--:|:--:|:--:|:--:
-f | --file | 欲处理的文件名或文件路径 |
-t | --title | 求和所依据的字段名（列名） | 该字段的值必须是数字
    
####2. **PDF文件处理**

**<font color="green">① pdf_to_txt：抽取PDF中的文本</font>**
参数简写 | 参数详写 | 说明 | 备注
:--:|:--:|:--:|:--:
-f | --file | 欲处理的PDF名称或路径 |
-o | --output | 结果输出文件名或文件路径 | 如不指定，则默认与PDF同名

**<font color="green">② pdf_translate：PDF文本翻译</font>**
参数简写 | 参数详写 | 说明 | 备注
:--:|:--:|:--:|:--:
-f | --file | 欲处理的PDF名称或路径 |
-o | --output | 翻译内容输出文件名或文件路径 | 如不指定，则默认与PDF同名

<font color="#990000">*注：调用百度翻译API，但需要自己申请APP ID和秘钥，并配置到`pdf_translate_config.json`文件中，并在使用时保持网络连接*<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;详细使用说明见`PDF_Translate使用说明`文件</font>
 


  [1]: http://static.zybuluo.com/dongfonkey/w49x7aces7322u3phq99d2v0/image_1fcpj896m10qh1jum1tgjre5j2p9.png
  [2]: http://static.zybuluo.com/dongfonkey/5kojzq8o4xbr9qqg110l2q5b/image_1fcpjbnfg13nnrt01ngkidr3bjm.png