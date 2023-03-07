# Python-OpenCV
## ①图像处理的基本操作（IMG）
### 读取图像
		cv2.imread（filename,flags)
			filename:读取的完整文件名
			flags:读取图像颜色类型的标记
### 显示图像
		cv2.imshow(winname,mat)
			winname:显示图像的窗口名称
			mat:要显示的图像
		retval=cv2.waitkey(delay)
			retval:与被按下的按键对于的ASCII码
			delay:等待用户按下键盘上按键的时间
		cv2.destroyAllWindows()
			用于销毁所有正在显示图像的窗口
### 保存图像
		cv2.imwrite(filename,img)
			filename:保存图像时所用的完整路径
			img:要保存的图像
### 获取图像的属性
		img.shape
			shape:如果是彩色图像，那么获取的是一个包含图像的水平像素、垂直像素和通道数的数组；若为灰度图像，那么获取的是一个包含图像的水平像素和垂直像素的数组
		img.size
			size:获取的是图像包含的像素个数，其值为"水平像素*垂直像素*通道数"。灰度图像的通道数为1
		img.dtype
			dtype:获取的是图像的数据类型

## ②像素的操作（Array）
### 像素
		确定像素的位置
			imread()读取图片
			img[x,y]坐标xy上的像素
		获取像素的BGR值
			print()xy坐标上的像素值
		修改像素的BGR值
			强制修改
		0:B;1:G;2R
### 使用NumPy模块操作像素
		NumPy概述
			强大的N维数组对象ndarray
			广播功能方法
			线性代数、傅里叶变换、随机数生成、图形操作等功能
			整合C/C++/Fortran代码的工具
		数组的类型
			bool_
				存储为一个字节的布尔值
			int_
				默认整数，相当于C的long，通常为int32或int64
			intc
				相当于C语言的int，通常为int32或int64
			intp
				用于索引的整数，相当于C语言中的size_t，通常为int32或int64
			int8
				字节（-128~128）
			int16
				16位整数
			int32
				32位整数
			int64
				64位整数
			uint8
				8位无符号整数
			uint16
				16位无符号整数
			uint32
				32位无符号整数
			uint64
				64位无符号整数
			float_
				_float64的简写
			float16
				半精度浮点
			float32
				单精度浮点
			float64
				双精度浮点
			complex_
				complex128类型的简写
			complex64
				复数，由两个32 位浮点表示
			complex128
				复数，由两个64位浮点表示
			datatime64
				日期时间类型
			timedalta64
				两个时间之间的间隔
### 创建数组:Array()方法
			numpy.array(object,dtype,copy,order,subok,ndmin)
				object:任何具有数组接口方法的对象
				dtype:数据类型
				copy:可选参数，布尔型，默认值为True，则object对象被复制；否则，只有当_array_返回副本，object参数为嵌套序列，或者需要副本满足数据类型的顺序要求时，才会生成副本。
				order:元素在内存中的出现顺序，其值为K、A、C、F。如果object参数不是数组，则新穿件的数组将按行数列，如果值为F，则按照列排列；如果object参数是一个数组，则以下顺序成立：C（按行）、F（按列）、A（原顺序）、K（元素在内存中的出现顺序）。
				subok:布尔型。如果值为True，则传递子类，否则返回的数组将强制为基类数组（默认值）
				ndmin:指定生成数组的最小维数
### 创建随机数组
			numpy.random.randint(low,high,size)
				low:随机数最小取值范围
				high:可选参数，随机数最大取值范围。若high为空，取值范围为（0，low）。若high不为空，则high必须大于low。
				size:可选参数，数组维数
			randint()方法用于生成一定范围内的随机整数数组，左闭右开区间([low,high])
### 操作数组
			幂运算：**
			比较运算：>=/==/<=/!=
			复制数组:copy()
### 数组的索引和切片
			索引:x[obj]进行索引，x是数组，obj是选择方式
				切片式索引[start,stop,step]
					start:起始索引，若不写任何值，则表示从0开始的全部索引
					stop:终止索引，若不写任何值，则表示直到末尾的全部索引
					step:步长
### 创建图像
			创建黑白图像
				像素值为0表示纯黑，像素值为255表示纯白
				纯白使用ones函数*255
				纯黑使用zeros函数
			彩色图像
				为每个通道复制一个img（图像），然后为每一个通道设置像素值
			随机图像
				使用random和randint函数实现
### 拼接图像
#### 水平拼接数组
				array=numpy.hstack(tup)
					tup:要拼接的数组元组
					array:将参数元组中的数组水平拼接后生成的新数组
					hstack()方法可以拼接多个数组
#### 垂直拼接数组
				array=np.vstack(tup)
					tup:要拼接的数组
					array:将参数元组中的数组垂直拼接后生成的新数组
					vstack()方法可以拼接多个数组

## ③色彩空间与通道（Colour）
### 色彩空间
		BRG--->GRAY
			dst=cv2.cvtColor(sec,code)
				dse：转换后的图像
				src：转换前的初始图像
				code：色彩空间转换码
		BGR--->HSV（H：色调；S：饱和度；V：亮度）
			同上
### 通道
#### 拆分通道
			b,g,r=cv2.split（bgr_image）
				b：B通道图像
				g：G通道图像
				r：R通道图像
				bgr_image：一幅BGR图像
			h,s,v=cv2.split（hsv_image）
				h：H通道图像
				s：S通道图像
				v：V通道图像
				hsv_image：一幅HSV图像
#### 合并通道
			bgr=cv2.merge([b,g,r])
				bgr：按B-->G-->R的顺序合并通道后得到的图像
				b：B通道图像
				g：G通道图像
				r：R通道图像
			hsv=cv2.merge([h,s,v])
				hsv：合并H通道图像、S通道图像和V通道图像后得到的图像
				h：H通道图像
				s：S通道图像
				v：V通道图像

## ④绘制图形和文字（Draw）
### 线段的绘制（segment）
		img=cv2.line（img,pt1,pt2,color,thickness)
			img：画布
			pt1：线段的起点坐标
			pt2：线段的终点坐标
			color：绘制线段时的线条颜色
			thickness：绘制线段时的线条宽度
### 矩形的绘制（rectangle）
		img=cv2.rectangle（img,pt,pt2,color,thickness）
			img：画布
			pt1：矩形的左上角坐标
			pt2：矩形的右下角坐标
			color：绘制矩形时的线条颜色
			thickness：绘制矩形时的线条宽度
### 圆形的绘制（circle）
		img=cv2.circle（img,center,radius,color,thickness)
			img：画布
			center：圆形的圆心坐标
			radius：圆形的半径
			color：绘制圆形时的线条颜色
			thickness：绘制圆形时的线条宽度
### 多边形的绘制（polygon）
		img=cv2.ploylines（img,pts,isClosed,color,thickness）
			img：画布
			pts：由多边形各个顶点的坐标组成的一个列表，这个列表是一个numpy的数组类型
			isClosed：如果值为True，表示一个闭合的多边形；如果值为False，表示一个不闭合的多边形
			color：绘制多边形时的线条颜色
			thickness：绘制多边形时的线条宽度
### 文字的绘制（word）
		img=cv2.putText（img,text,org,fontFace,fontScale,color,thickness,lineType,bottomLeftOrigin）
			img：画布
			text：要绘制的文字内容
			org：文字在画布中的左下角坐标
			fontFace：字体样式
				百度
			fontScale：字体大小
			color：绘制文字时的线条颜色
			thickness：绘制文字时的线条宽度
			lineType：线型（线型指的是线的产生算法，有4和8两个值，默认值为8）
			bottomLeftOrigin：绘制文字时的方向（有True和False两个值，默认False）
### 动态绘制图形（dynamicDrawing）
		time.sleep(seconds)
			seconds:休眠时间，单位为s，可以为小数，如1/10表示（1/10）s

## ⑤图像的几何变换（pictureChange）
### 缩放（zoom）
		dst=cv2.resize(src,dsize,fx,fy,interpolation)
			src：原始图像
			dsize：输出图像的大小，格式为（宽，高），单位为像素
			fx：可选参数。水平方向的缩放比例
				新图像宽度=round(fx*原图像宽度)
			fy：可选参数。垂直方向的缩放比例
				新图像高等=round(fy*原图像高度)
			interpolation：可选参数。缩放的插值方式。在图像缩小或放大时需要删减或补充像素，该参数可以指定使用哪种算法对像素进行增减。建议使用默认值
			dst：缩值之后的图像
### 翻转（overTurn）
		dst=cv2.flip(src,flipCode)
			src：原始图像
			flipCode：翻转类型（0：沿X轴翻转；正数：沿Y轴翻转；负数：同时沿X轴、Y轴翻转）
			dst：翻转之后的图像
### 仿射变换（affineTransformation）
#### 平移（translation）
			dst=cv2.warpAffine(src,M,dsize,flags,borderMode,borderValue)
				src：原始图像
				M：一个2行3列的矩阵，根据此矩阵的值变换原图中的像素位置
				dsize：输出图像的尺寸大小
				flags：可选参数，插值方式，建议使用默认值
				borderMode：可选参数，边界类型，建议使用默认值
				borderValue：可选参数，边界值，默认为0，建议使用默认值
				dst：经过反射变换后输出图像
#### 旋转（rotation）
			M=cv2.getRotationMatrix2D(center,angle,scale)
				center：旋转的中心点坐标
				angle：旋转的角度（不是弧度）。正数表示逆时针旋转，负数表示顺时针旋转
				scale：缩放比例，浮点类型。如果取值1，表示图像保存原来的比例。
				M：getRotationMatrix2D（）方法计算出仿射矩阵
#### 倾斜（tilt）
			M=cv2.getAffineTransform(src,dst)
				src：原图3个点坐标，格式为3行2列的32位浮点数列表，例如：[[0,1],[1,0],[1,1]]
				dst：倾斜图像的3个点坐标，格式与src一样
				M：getAffineTransform（）方法计算出的仿射矩阵
#### 透视（perspective）
			dst=cv2.warpPerspective(src,M,dsize,flags,borderMode,borderValue)
				src：原始图像
				M：一个3行3列的矩阵，根据次矩阵的值变换原图中的像素位置
				dsize：输出图像的尺寸大小
				flags：可选参数，插值方式，建议使用默认值
				borderMode：可选参数，边界类型，建议使用默认值
				borderValue：可选参数，边界值，默认为0，建议使用默认值
				dst：经过透视变换后输出图像
			M=cv2.getPerspectiveTransform(src,dst)
				src：原图4个点坐标，格式为4行2列的32位浮点数列表，例如：[[0,0],[1,0],[0,1],[1,1]]
				dst：透视图的4个点坐标，格式与src一样
				M：getPerspectiveTransform（）方法计算出的仿射矩阵

## ⑥图像的阈值处理
### 阈值处理函数（threshold）
	retval，dst=cv2.threshold(src,thresh,maxval,type)
		src：被处理的图像，可以是多通道图像
		thresh：阈值，阈值在125~150取值的效果最好
		maxval：阈值处理采用的最大值
		type：阈值处理类型。
			cv2.THRESH_BINARY----->二值化阈值处理
			cv2.THRESH_BINARY_INV----->反二值化阈值处理
			cv2.THRESH_TOZERO----->低于阈值零处理
			cv2.THRESH_TOZERO_INV----->超出阈值零处理
			cv2.THRESH_TRUNC----->截断阈值处理
		retval：处理时采用的阈值
		dst：经过阈值处理后的图像

### “非黑即白”的图像（blcakORwhite）
#### 二值化处理（twoNumber）
		if  像素值<=阈值：像素值=0
		if  像素值>阈值：像素值=最大值
#### 反二值化处理（notTwoNumber）
		if  像素值 <= 阈值：像素值 = 最大值
		if  像素值 > 阈值：像素值 = 0

### 零处理（Zero）
#### 低于阈值零处理（belowZero）
		if  像素值 <= 阈值：像素值 = 0
		if  像素值 > 阈值：像素值 = 原值
#### 超出阈值零处理（beyondZero）
		if  像素值 <= 阈值：像素值 = 原值
		if  像素值 > 阈值：像素值 = 0

### 截断处理（truncation）
	if  像素值 < 阈值：像素值 = 原值
	if  像素值 > 阈值：像素值 = 阈值

### 自适应处理（adaptiveProcessing）
	dst=cv2.adaptiveThreshold(src,maxValue,adaptiveMethod,thresholdType,blockSize,C)
		src：被处理的图像。需要注意的是，该图像是灰度图像
		maxValue：阈值处理采用的最大值
		adaptiveMethod：自适应阈值的计算方法
			cv2.ADAPTIVE_THRESH_MEAN_C：对一个正方形区域内的所有像素平均加权
			cv2.ADAPTIVE_THRESH_GAUSSIAN_C：根据高斯函数按照像素与中心点的距离对一个正方形区域内的所有像素进行加权计算
		thresholdType：阈值处理类型；需要注意的是，阈值处理类型需是cv2.THRESH_BINARY或cv2.THRESH_BINARY_INV中的一个
		blockSize：一个正方形区域的大小。eg：5指的是5*5的区域
		C：常量。阈值等于均值或者加权值减去这个常量
		dst：经过阈值处理后的图像

### Otsu方法（Otsu）
	retval,dst=cv2.threshold(src,thresh,maxval,type)
		src：被处理的图像。需注意该图像应为灰度图像
		thresh：阈值，且要吧阈值设置为0
		maxval：阈值处理采用的最大值，即255
		type：阈值处理类型
		retval：由Otus方法计算得到并使用的最合适的阈值
		dst：经过阈值处理后的图像

### 阈值处理的作用（function）

## ⑦图像的运算（imageOperation）
### 掩模（masking）
	创建一个三通道的掩模，利用numpy库的zero()方法

### 图像的加法运算（addImage）
	dst=cv2.(src1,src2,mask,dtype)
		src1：第一幅图像
		src2：第二幅图像
		mask：可选参数，掩模，建议使用默认值
		dtype：可选参数，图像深度，建议使用默认值
		dst：相加之后的图像。如果相加之后值的结果大于255，则取255

### 图像的位运算（bitOperation）
#### 位与运算（bitAndOperation
		dst=cv2.bitwise_and(src1,src2,mask)
			src1：第一幅图像
			src2：第二幅图像
			mask：可选参数，掩模
			dst：与运算之后的图像
		与运算特点
			①如果某像素与纯白像素做与运算，结果仍然是某像素的原值
			②如果某像素与纯黑像素做与运算，结果为纯黑像素
#### 位或运算（bitOrOperation）
		dst=cv2.bitwise_or(src1,src2,mask)
			src1：第一幅图像
			src2：第二幅图像
			mask：可选参数，掩模
			dst：或运算之后的图像
		或运算特点
			①如果某像素与纯白像素做或运算，结果为纯白像素
			②如果某像素与纯黑像素做或运算，结果仍然是某像素的原值
#### 位取反运算（bitFetchAndRexerseOperation）
		dst=cv2.bitwise_not(src,mask)
			src：参与运算的图像
			msak：可选参数，掩模
			dst：取反运算之后的图像
		取反运算特点
			图像经过取反运算后呈现与原图颜色完全相反的效果
#### 位异或运算（bitXorOperation）
		dst=cv2.bitwise_xor(src,mask)
			src：参与运算的图像
			mask：可选参数，掩模
			dst：异或运算之后的图像
		异或运算特点
			①如果某像素与纯白像素做异或运算，结果为原像素的取反结果
			②如果某像素与纯黑像素做异或运算，结果仍然是某像素的原值
### 合并图像（mergedImage）
#### 加权和（addWeighted）
		dst=cv2.addWeighted(src1,alpha,src2,beta,gamma)
			src1：第一幅图像
			alpha：第一幅图像的权重
			src：第二幅图像
			beta：第二幅图像的权重
			gamma：在和结果上添加的标量。该值越大，结果图像越亮，反之则越暗。可以是负数
			dst：加权和后的图像
#### 覆盖（cover）

## ⑧模板匹配（templateMatching）
### 模板匹配方法（matchTemplate）
		result=cv2.matchTemplate(image,templ,method,mask)
			image：原始图像
			templ：模板图像，尺寸必须小于或等于原始图像
			method：匹配方法
				cv2.TM_SQDIFF（值：0）：差值平方和匹配，也叫平方差匹配。可以理解为差异程度。匹配程度越高，计算结果越小。完全匹配的结果为0
				cv2.TM_SQDIFF_NORMED（值：1）：标准差值平方和匹配，也叫标准平方差匹配，规则同上
				cv2.TM_CCORR（值：2）：相关匹配。可以理解为相似程度，匹配程度越高，计算结果越大
				cv2.TM_CCORR_NORMED（值：3）：标准相关匹配，规则同上
				cv2.TM_CCOEFF（值：4）：相关系数匹配，也属于相似程度，计算结果为-1~1的浮点数，1表示完全匹配，0表示毫无关系，-1表示2张图片亮度刚好相反
				cv2.TM_CCOEFF_NORMED（值：5）：标准相关系数匹配，规则同上
			mask：可选参数。掩模，只有cv2.TM_SQDIFF和cv2.TM_CCORR_NORMED支持此参数，建议采用默认值
			result：计算得出的匹配结果。如果原始图像的宽、高分别为W、H，模板图像的宽、高分别为w、h，result就是一个W-w+1列、H-h+1行的32位浮点型数组。数组中每一个浮点数都是原始图像中对应像素位置的匹配结果，其含义需要根据method参数来解读
### 单模板匹配（minMaxLoc）
		minValue,maxValue,minLoc,maxLoc=cv2.minMaxLoc(src,mask)
			src：matchTemplate()方法计算得出的数组
			mask：可选参数，掩模，建议使用默认值
			minValue：数组中的最小值
			maxValue：数组中的最大值
			minLoc：最小值的坐标，格式为（x，y）
			maxLoc：最大值的坐标，格式为（x，y）
### 多目标匹配（multiobjective）

### 多模板匹配（multitemplate）

## ⑨滤波器（Filter）
### 均值滤波器（blur）
		dst=cv2.blur(src,ksize,anchor,borderType)
			src：被处理的图像
			ksize：滤波核大小，其格式为（高度，宽度），建议使用如（3,3）、（5,5）、（7,7）等宽、高相等的奇数边长。滤波核越大，处理之后的图像就越模糊
			anchor：可选参数，滤波核的锚点，建议采用默认值，可以自动计算锚点
			borderType：可选参数，边界样式，建议采用默认值
			dst：经过均值滤波处理之后的图像
### 中值滤波器（medianBlur）
		dst=cv2.medianBlur(src,ksize)
			src：被处理的图像
			ksize：滤波核的边长，必须是大于1的奇数，如3、5、7等。该方法根据此边长自动创建一个正方形的列表核
			dst：经过中值滤波处理之后的图像
### 高斯滤波（GaussianBlur）
		dst=cv2.GaussianBlur(src,ksize,sigmaX,sigmaY,borderType)
			src：被处理的图像
			ksize：滤波核的大小，宽高必须是奇数，如（3,3）、（5,5）等
			sigmaX：卷积核水平方向的标准差
			sigmaY：卷积核垂直方向的标准差
			borderType：可选参数，边界样式，建议使用默认值
			dst：经过高斯滤波处理之后的图像
			修改sigmaX或sigmaY的值都可以改变卷积核中的权重比例。如果不知道如何设计这两个参数值，就直接把这两个参数的值写成零，该方法就会根据滤波核的大小自动计算合适的权重比例
### 双边滤波器（bilateralFilter）
		dst=cv2.bilateralFilter(src,d,sigmaColor,sigmaSpace,borderType)
			src：被处理的图像
			d：以当前像素为中心的整个滤波区域的直径。如果d<0，则自动根据sigmaSpace参数计算得到，该值与保留的边缘信息数量成正比，与方法运行效率成反比
			sigmaColor：参与计算的颜色范围，这个值是像素颜色值与周围颜色值的最大差值，只有颜色值之差小于这个值时，周围的像素才进行滤波计算。值为255时，表示所有颜色都参与计算
			sigmaSpace：坐标空间的sigma值，该值越大，参与计算的像素数量就越多
			borderType：可选参数，边界样式，建议默认
			dst：经过双边滤波处理之后的图像

## ⑩腐蚀与膨胀（corrosionAndExpansion）
### 腐蚀（erode）
		dst=cv2.erode(src,kernel,anchor,iterations,borderType,borderValue)
			src：原始图像
			kernel：腐蚀使用的核
			anchor：可选参数，核的锚点位置
			iterations：可选参数，腐蚀操作的迭代次数，默认值为1
			borderType：可选参数，边界样式，建议默认
			borderValue：可选参数，边界值，建议默认
			dst：经过腐蚀之后的图像
### 膨胀（dilate）
		dst=cv2.dilate(src,kernel,anchor,iterations,borderType,borderValue)
			src：原始图像
			kernel：膨胀使用的核
			anchor：可选参数，核的锚点位置
			iterations：可选参数，腐蚀操作的迭代次数，默认值为1
			borderType：可选参数，边界样式，建议默认
			borderValue：可选参数，边界值，建议默认
			dst：经过膨胀之后的图像
### 开运算（openOperation）
		先腐蚀再膨胀
### 闭运算（closedOperation）
		先膨胀再腐蚀
### 形态学运算（morphologicalOperation）
		梯度运算（gradientOperation）
		dst=cv2.morphologyEx(src,op,kernel,anchor,iterations,borderType,borderValue)
			src：原始图像
			op：操作类型
				cv2.MORPH_ERODE-----腐蚀操作
				cv2.MORPH_DILATE-----膨胀操作
				cv2.MORPH_OPEN-----开运算，先腐蚀后膨胀
				cv2.MORPH_CLOSE-----闭运算，先膨胀后腐蚀
				cv2.MORPH_GRADIENT-----梯度运算，膨胀图减腐蚀图
				cv2.MORPH_TOPHAT-----顶帽运算，原始图减开运算图
				cv2.MORPH_BLACKHAT-----黑帽运算，闭运算图减原始图
			kernel：操作过程中使用的核
			anchor：可选参数，核的锚点位置
			iterations：可选参数，迭代次数，默认值为1
			borderType：可选参数，边界样式，建议默认
			borderValue：可选参数，边界值，建议默认
			dst：操作之后得到的图像
		顶帽运算（topHatOperation）
		黑帽运算（blackHatOperation）
## ⑪图形监测（graphicMonitoring）
### 图像的轮廓（findContoursAndDrawContours）
		contours,hierarchy=cv2.findContoours(image,mode,methode)
			image：被检测的图像，必须是8位单通道二值图像。如果原始图像是彩色图像，必须转为灰度图像，并经过二值化处理

			mode：轮廓的检索模式
				cv2.RETR_EXTERNAL-----只检测外轮廓
				cv2.RETR_LIST-----检测所有轮廓，但不建立层次关系
				cv2.RETR_CCOMP-----检测所有轮廓，并建立两级层次关系
				cv2.RETR_TREE-----检测所有轮廓，并建立树状结构的层次关系

			methode：检测轮廓时使用的方法
				cv2.CHAIN_APPROX_NONE-----储存轮廓上的所有点
				cv2.CHAIN_APPROX_SIMPLE-----只保存水平、垂直或对角线轮廓的端点
				cv2.CHAIN_APPROX_TC89_L1-----Ten-Chinl近似算法中的一种
				cv2.CHAIN_APPROX_TC89_KCOS-----Ten-Chinl近似算法中的一种

			contours：检测出的所有轮廓，list类型，每一个元素都是某个轮廓的像素坐标数组

			hierarchy：轮廓之间的层次关系

		image=cv2.drawContours(image,contours,contourIdx,color,thickness,linTypee,hierarchy,maxLevel,offse)
			image：被绘制轮廓的原始图像，可以是多通道图像
			contours：findContours()方法得出的轮廓列表
			contoursIdx：绘制轮廓的索引，如果为-1则绘制所有轮廓
			color：绘制颜色，使用BGR格式
			thickness：可选参数，画笔的粗细程度，如果该值为-1则绘制实心轮廓
			lineTypee：可选参数，绘制轮廓的线型
			hierarchy：可选参数，findContours()方法得出的层次关系
			maxLevel：可选参数，绘制轮廓的层次深度，最深绘制第maxLevel层
			offse：可选参数，偏移量，可以改变绘制结果的位置
			image：同参数中的image，执行后原始图中就包含绘制的轮廓了，可以不使用此返回值保存结果


