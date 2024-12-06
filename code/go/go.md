# 安装
下载安装包
* https://go.dev/dl/
* https://golang.google.cn/dl/

# hello world
```go
package main

import "fmt"

func main() {
   /* 这是我的第一个简单的程序 */
   fmt.Println("Hello, World!")
}
```
* 第一行代码 package main 定义了包名。你必须在源文件中非注释的第一行指明这个文件属于哪个包，如：package main。package main表示一个可独立执行的程序，每个 Go 应用程序都包含一个名为 main 的包。

* 下一行 import "fmt" 告诉 Go 编译器这个程序需要使用 fmt 包（的函数，或其他元素），fmt 包实现了格式化 IO（输入/输出）的函数。

* 下一行 func main() 是程序开始执行的函数。main 函数是每一个可执行程序所必须包含的，一般来说都是在启动后第一个执行的函数（如果有 init() 函数则会先执行该函数）。

* 下一行 /*...*/ 是注释，在程序执行时将被忽略。单行注释是最常见的注释形式，你可以在任何地方使用以 // 开头的单行注释。多行注释也叫块注释，均已以 /* 开头，并以 */ 结尾，且不可以嵌套使用，多行注释一般用于包的文档描述或注释成块的代码片段。

* 下一行 fmt.Println(...) 可以将字符串输出到控制台，并在最后自动增加换行字符 \n。
使用 fmt.Print("hello, world\n") 可以得到相同的结果。
Print 和 Println 这两个函数也支持使用变量，如：fmt.Println(arr)。如果没有特别指定，它们会以默认的打印格式将变量 arr 输出到控制台。

* 当标识符（包括常量、变量、类型、函数名、结构字段等等）以一个大写字母开头，如：Group1，那么使用这种形式的标识符的对象就可以被外部包的代码所使用（客户端程序需要先导入这个包），这被称为导出（像面向对象语言中的 public）；标识符如果以小写字母开头，则对包外是不可见的，但是他们在整个包的内部是可见并且可用的（像面向对象语言中的 protected ）。

# 执行 Go 程序
``` shell
# 运行 Go 程序
$ go run hello.go
Hello, World!

# 编译 Go 程序
$ go build hello.go 
$ ls
hello    hello.go
$ ./hello 
Hello, World!
```

# 注释
``` go
// 单行注释
/*
 Author by 菜鸟教程
 我是多行注释
 */
```

# 标识符命名规则
多个字母(A~Z和a~z)数字(0~9)、下划线_组成的序列，第一个字符必须是字母或下划线而不能是数字

# 关键字
<html>
<table class="reference">
<tbody><tr>
<td style="width:25%">break</td><td style="width:25%">default</td><td style="width:25%">func</td><td style="width:25%">interface</td><td style="width:25%">select</td></tr>
<tr><td>case</td><td>defer</td><td>go</td><td>map</td><td>struct</td></tr>
<tr><td>chan</td><td>else</td><td>goto</td><td>package</td><td>switch</td></tr>
<tr><td>const</td><td>fallthrough</td><td>if</td><td>range</td><td>type</td></tr>
<tr><td>continue</td><td>for</td><td>import</td><td>return</td><td>var</td></tr>
</tbody></table>

<p>除了以上介绍的这些关键字，Go 语言还有 36 个预定义标识符：</p>
<table class="reference">
  <tbody><tr>
    <td>append</td>
    <td>bool</td>
    <td>byte</td>
    <td>cap</td>
    <td>close</td>
    <td>complex</td>
    <td>complex64</td>
    <td>complex128</td>
    <td>uint16</td>
  </tr>
  <tr>
    <td>copy</td>
    <td>false</td>
    <td>float32</td>
    <td>float64</td>
    <td>imag</td>
    <td>int</td>
    <td>int8</td>
    <td>int16</td>
    <td>uint32</td>
  </tr>
  <tr>
    <td>int32</td>
    <td>int64</td>
    <td>iota</td>
    <td>len</td>
    <td>make</td>
    <td>new</td>
    <td>nil</td>
    <td>panic</td>
    <td>uint64</td>
  </tr>
  <tr>
    <td>print</td>
    <td>println</td>
    <td>real</td>
    <td>recover</td>
    <td>string</td>
    <td>true</td>
    <td>uint</td>
    <td>uint8</td>
    <td>uintptr</td>
  </tr>
</tbody></table>
<p>
</html>

# 数据类型
* 布尔型 bool
* 整型 int、int8、int16、int32、int64
* 无符号整型 uint、uint8、uint16、uint32、uint64
* 浮点型 float32、float64
* 复数型 complex64、complex128
* 字节型 byte
* 字符串型 string
* 切片型 []T（其中 T 是任意数据类型）
* 数组型 [n]T（其中 n 是常量整数，T 是任意数据类型）
* 结构体型 struct { ... }
* 指针型 *T（其中 T 是任意数据类型）
* 接口型 interface { ... }
* 函数型 func( ... ) ( ... )
* 映射型 map[K]V（其中 K 和 V 是任意数据类型）
* 通道型 chan T（其中 T 是任意数据类型）

# 变量声明
``` go
var a int // 声明一个整型变量 a
var b, c int = 1, 2 // 声明两个整型变量 b 和 c，并初始化
var d = 10 // 声明一个整型变量 d，并初始化
var e int = 10 // 声明一个整型变量 e，并初始化
var f, g int // 声明两个整型变量 f 和 g
var h, i, j int = 1, 2, 3 // 声明三个整型变量 h、i 和 j，并初始化
var k = 10, 20 // 声明两个整型变量 k，并初始化
var l, m = 10, 20 // 声明两个整型变量 l 和 m，并初始化
```

# 常量声明
``` go
const a = 10 // 声明一个常量 a，并初始化
const b, c = 1, 2 // 声明两个常量 b 和 c，并初始化
const d = 10 // 声明一个常量 d，并初始化
const e int = 10 // 声明一个整型常量 e，并初始化
const f, g int = 1, 2 // 声明两个整型常量 f 和 g，并初始化
const h, i, j int = 1, 2, 3 // 声明三个整型常量 h、i 和 j，并初始化
const k = 10, 20 // 声明两个整型常量 k，并初始化
const l, m = 10, 20 // 声明两个整型常量 l 和 m，并初始化
```

# 变量作用域
* 函数内定义的变量称为局部变量
* 函数外定义的变量称为全局变量,全局变量可以在整个包甚至外部包（被导出后）使用
* 函数定义中的变量称为形式参数

# 变量默认值
在go语言中，任何类型在声明后没有赋值的情况下，都对应一个零值。

* 整形如int8、byte、int16、uint、uintprt等，默认值为0。
* 浮点类型如float32、float64，默认值为0。
* 布尔类型bool的默认值为false。
* 复数类型如complex64、complex128，默认值为0+0i。
* 字符串string的默认值为""。
* 错误类型error的默认值为nil。
* 对于一些复合类型，如指针、切片、字典、通道、接口，默认值为nil。而数组的默认值要根据其数据类型来确定。
例如：var a [4]int，其默认值为[0 0 0 0]。


# 赋值操作符 := 
var a int =10 可简写为 a := 10
var a,b int =10,10 可简写为 a,b := 10,10
* 若在当前作用域a/b已经声明过,则:=会报错

# 枚举
* iota，特殊常量，可以认为是一个可以被编译器修改的常量
* iota 在 const关键字出现时将被重置为 0，const中每出现一次 iota 值加 1
``` go
//写法1
const (
    a = iota
    b = iota
    c = iota
)
//写法2
const (
    a = iota
    b
    c
)
//其它
const (
    a = iota   //0
    b          //1
    c          //2
    d = "ha"   //独立值，iota += 1
    e          //"ha"   iota += 1
    f = 100    //iota +=1
    g          //100  iota +=1
    h = iota   //7,恢复计数
    i          //8
)
//特别用法
const (
    i=1<<iota
    j=3<<iota
    k
    l
)
```

# 算术运算符
<html>
<p>下表列出了所有Go语言的算术运算符。假定 A 值为 10，B 值为 20。</p>
<table class="reference">
<tbody><tr><th style="width:10%">运算符</th><th style="width:55%;">描述</th><th>实例</th></tr>
<tr><td>+</td><td>相加</td><td> A + B 输出结果 30</td></tr>
<tr><td>-</td><td>相减</td><td> A - B 输出结果 -10</td></tr>
<tr><td>*</td><td>相乘</td><td> A * B 输出结果 200</td></tr>
<tr><td>/</td><td>相除</td><td> B / A 输出结果 2</td></tr>
<tr><td>%</td><td>求余</td><td> B % A 输出结果 0</td></tr>
<tr><td>++</td><td>自增</td><td> A++ 输出结果 11</td></tr>
<tr><td>--</td><td>自减</td><td> A-- 输出结果 9</td></tr>
</html>

# 关系运算符
<html>
<p>下表列出了所有Go语言的关系运算符。假定 A 值为 10，B 值为 20。</p>
<table class="reference">
<tbody><tr><th style="width:10%">运算符</th><th style="width:55%;">描述</th><th>实例</th></tr>
<tr><td>==</td><td> 检查两个值是否相等，如果相等返回 True 否则返回 False。</td><td> (A == B)  为 False </td></tr>
<tr><td>!=</td><td> 检查两个值是否不相等，如果不相等返回 True 否则返回 False。</td><td> (A != B) 为 True </td></tr>
<tr><td>&gt;</td><td>检查左边值是否大于右边值，如果是返回 True 否则返回 False。</td><td> (A &gt; B) 为 False</td></tr>
<tr><td>&lt;</td><td>检查左边值是否小于右边值，如果是返回 True 否则返回 False。</td><td> (A &lt; B) 为 True </td></tr>
<tr><td>&gt;=</td><td>检查左边值是否大于等于右边值，如果是返回 True 否则返回 False。</td><td> (A &gt;= B) 为 False </td></tr>
<tr><td>&lt;=</td><td> 检查左边值是否小于等于右边值，如果是返回 True 否则返回 False。</td><td> (A &lt;= B) 为 True </td></tr>
</tbody></table>
</html>

# 逻辑运算符
<html>
<p>下表列出了所有Go语言的逻辑运算符。假定 A 值为 True，B 值为 False。</p>
<table class="reference">
<tbody><tr><th style="width:10%">运算符</th><th style="width:55%;">描述</th><th>实例</th></tr>
<tr><td>&amp;&amp;</td><td> 逻辑 AND 运算符。 如果两边的操作数都是 True，则条件 True，否则为 False。 </td><td> (A &amp;&amp; B) 为 False</td></tr>
<tr><td>||</td><td>逻辑 OR 运算符。 如果两边的操作数有一个 True，则条件 True，否则为 False。</td><td> (A || B) 为 True </td></tr>
<tr><td>!</td><td>逻辑 NOT 运算符。 如果条件为 True，则逻辑 NOT 条件 False，否则为 True。</td><td> !(A &amp;&amp; B) 为 True </td></tr>
</tbody></table>
</html>

# 位运算符
<html>
<p>Go 语言支持的位运算符如下表所示。假定 A 为60，B 为13：</p>
<table class="reference">
<tbody><tr><th style="width:10%">运算符</th><th style="width:55%;">描述</th><th>实例</th></tr>
<tr><td>&amp;</td><td> 按位与运算符"&"是双目运算符。 其功能是参与运算的两数各对应的二进位相与。 </td><td> (A &amp; B) 结果为 12,  二进制为 0000 1100</td></tr>
<tr><td>|</td><td>按位或运算符"|"是双目运算符。 其功能是参与运算的两数各对应的二进位相或</td><td> (A | B) 结果为 61, 二进制为 0011 1101</td></tr>
<tr><td>^</td><td> 按位异或运算符"^"是双目运算符。 其功能是参与运算的两数各对应的二进位相异或，当两对应的二进位相异时，结果为1。</td><td> (A ^ B) 结果为 49, 二进制为 0011 0001</td></tr>
<tr><td>&lt;&lt;</td><td> 左移运算符"&lt;&lt;"是双目运算符。左移n位就是乘以2的n次方。 其功能把"&lt;&lt;"左边的运算数的各二进位全部左移若干位，由"&lt;&lt;"右边的数指定移动的位数，高位丢弃，低位补0。 </td><td> A &lt;&lt; 2 结果为 240 ，二进制为 1111 0000</td></tr>
<tr><td>&gt;&gt;</td><td> 右移运算符"&gt;&gt;"是双目运算符。右移n位就是除以2的n次方。
其功能是把"&gt;&gt;"左边的运算数的各二进位全部右移若干位，"&gt;&gt;"右边的数指定移动的位数。 </td><td> A &gt;&gt; 2 结果为 15 ，二进制为 0000 1111</td></tr>
</tbody></table>
</html>

# 赋值运算符
<html>
<p>下表列出了所有Go语言的赋值运算符。</p>
<table class="reference">
<tbody><tr><th style="width:10%">运算符</th><th style="width:55%;">描述</th><th>实例</th></tr>
<tr><td>=</td><td>简单的赋值运算符，将一个表达式的值赋给一个左值</td><td> C = A + B 将 A + B 表达式结果赋值给 C</td></tr>
<tr><td>+=</td><td>相加后再赋值</td><td> C += A 等于 C = C + A</td></tr>
<tr><td>-=</td><td>相减后再赋值</td><td> C -= A 等于 C = C - A</td></tr>
<tr><td>*=</td><td>相乘后再赋值</td><td> C *= A 等于 C = C * A</td></tr>
<tr><td>/=</td><td>相除后再赋值</td><td> C /= A 等于 C = C / A</td></tr>
<tr><td>%=</td><td>求余后再赋值</td><td> C %= A 等于 C = C % A</td></tr>
<tr><td>&lt;&lt;=</td><td>左移后赋值 </td><td> C &lt;&lt;= 2 等于  C = C &lt;&lt; 2</td></tr>
<tr><td>&gt;&gt;=</td><td>右移后赋值 </td><td> C &gt;&gt;= 2 等于  C = C &gt;&gt; 2</td></tr>
<tr><td>&amp;=</td><td>按位与后赋值</td><td> C &amp;= 2 等于  C = C &amp; 2</td></tr>
<tr><td>^=</td><td>按位异或后赋值</td><td> C ^= 2 等于  C = C ^ 2</td></tr>
<tr><td>|=</td><td>按位或后赋值</td><td> C |= 2 等于  C = C | 2</td></tr>
</tbody></table>
</html>

# 其他运算符
<html>
<table class="reference">
<tbody><tr><th style="width:10%">运算符</th><th style="width:55%;">描述</th><th>实例</th></tr>
<tr>
<td>&amp;</td><td>返回变量存储地址</td><td>&amp;a; 将给出变量的实际地址。</td>
</tr>
<tr>
<td>*</td><td>指针变量。</td><td>*a; 是一个指针变量</td>
</tr>
</tbody></table>
</html>

# 运算符优先级
<html>
<p>有些运算符拥有较高的优先级，二元运算符的运算方向均是从左至右。下表列出了所有运算符以及它们的优先级，由上至下代表优先级由高到低：</p>
<table class="reference">
<tr><th>
优先级</th><th>运算符</th></tr><tr><td>
 5  </td><td>    *  /  %  <<  >>  &  &^</td></tr><tr><td>

 4   </td><td>   +  -  |  ^</td></tr><tr><td>
 3  </td><td>    ==  !=  <  <=  >  >=</td></tr><tr><td>
 2  </td><td>    &&</td></tr><tr><td>
 1  </td><td>    ||</td></tr></table>
<p>当然，你可以通过使用括号来临时提升某个表达式的整体运算优先级。</p>
</html>

# 条件语句
<html>
<table class="reference">
<tbody><tr><th style="width:35%">语句</th><th>描述</th></tr>
<tr><td><a title="Go if 语句">if</a></td><td><b>if </b> 由一个布尔表达式后紧跟一个或多个语句组成。</td></tr>
<tr><td><a title="Go if...else 语句">if...else </a></td><td><b>if</b> 后可以使用可选的 <b>else </b>, else 语句中的表达式在布尔表达式为 false 时执行。</td></tr>
<tr><td><a title="Go if 嵌套语句"> if </a></td><td>你可以在 <b>if</b> 或 <b>else if</b> 语句中嵌入一个或多个 <b>if</b> 或 <b>else if</b> 语句。</td></tr>
<tr><td><a title="Go switch 语句">switch </a></td><td><b>switch</b> 语句用于基于不同条件执行不同动作。</td></tr>
<tr><td><a title="Go select 语句">select </a></td><td><b>select</b> 语句类似于 <b>switch</b> 语句，但是select会随机执行一个可运行的case。如果没有case可运行，它将阻塞，直到有case可运行。</td></tr>
</tbody></table>

<blockquote><p>注意：Go 没有三目运算符，所以不支持 <strong>?:</strong> 形式的条件判断。</p></blockquote>
</html>
``` go
if x > 0 {
    fmt.Println("x is positive")
} else if x < 0 {
    fmt.Println("x is negative")
}
```

# 循环语句
<html>
<table class="reference">
<thead>
<tr>
<th>循环类型 </th>
<th> 描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><a>for</a> </td>
<td> 重复执行语句块</td>
</tr>
<tr>
<td><a>循环嵌套</a>  </td>
<td> 在 for 循环中嵌套一个或多个 for</td>
</tr>
</tbody>
</table>

<h2>循环控制语句</h2>

<p>循环控制语句可以控制循环体内语句的执行过程。</p>

<p>GO 语言支持以下几种循环控制语句：</p>

<table class="reference">
<thead>
<tr>
<th>控制语句 </th>
<th> 描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><a>break</a> </td>
<td> 经常用于中断当前 for 循环或跳出 switch </td>
</tr>
<tr>
<td><a>continue</a> </td>
<td> 跳过当前循环的剩余语句，然后继续进行下一轮循环。</td>
</tr>
<tr>
<td><a>goto</a> </td>
<td> 将控制转移到被标记的语句。</td>
</tr>
</tbody>
</table>
<hr />
</html>

``` go
// 
for i := 0; i < 10; i++ {
    if i == 5 {
        break // 跳出当前循环
    }else{
        continue // 跳过当前循环的剩余语句，然后继续进行下一轮循环
    }
    fmt.Println(i)
}
//
for true{
    fmt.Println("无限循环")
}
```

# 函数
``` go
//
func swap(x string) string {
   return x
}
//
func swap(x string, y string) (string, string) {
   return y, x
}
//
func swap(x, y string) (string, string) {
   return y, x
}
//调用
a, b := swap("Google", "Runoob")
```

# 闭包函数
``` go
package main

import "fmt"

func getSequence() func() int {
   i:=0
   return func() int {
      i+=1
     return i  
   }
}

func main(){
   /* nextNumber 为一个函数，函数 i 为 0 */
   nextNumber := getSequence()  

   /* 调用 nextNumber 函数，i 变量自增 1 并返回 */
   fmt.Println(nextNumber())
   fmt.Println(nextNumber())
   fmt.Println(nextNumber())
   
   /* 创建新的函数 nextNumber1，并查看结果 */
   nextNumber1 := getSequence()  
   fmt.Println(nextNumber1())
   fmt.Println(nextNumber1())
}
```

# 函数参数
* 参数分为值参数和引用参数*
* 默认情况下，Go 语言使用的是值传递，即在调用过程中不会影响到实际参数
``` go
/* 值*/
func swap(x int, y int)
/* 引用*/
func swap(x *int, y *int)
```

# 类型转换
* go不支持隐式转换类型
``` go
// 整型转浮点
var a int = 10
var b float64 = float64(a)

// 字符串转整型
//注意，strconv.Atoi 函数返回两个值，第一个是转换后的整型值，第二个是可能发生的错误，我们可以使用空白标识符 _ 来忽略这个错误
var str string = "10"
var num int
num, _ = strconv.Atoi(str)

// 整形转字符串
num := 123
str := strconv.Itoa(num)

// 字符串转浮点
str := "3.14"
num, _ := strconv.ParseFloat(str, 64)

// 浮点转字符串
num := 3.14
str := strconv.FormatFloat(num, 'f', 2, 64)
```

## 接口类型转换
### 类型断言
用于将接口类型转换为指定类型 语法:value.(type) 或 value.(T)
``` go
var i interface{} = "Hello, World"
str, ok := i.(string)
```
### 类型转换
用于将一个接口类型的值转换为另一个接口类型 语法:T(value)
``` go
// 定义一个接口 Writer
type Writer interface {
    Write([]byte) (int, error)
}
// 实现 Writer 接口的结构体 StringWriter
type StringWriter struct {
    str string
}
// 实现 Write 方法
func (sw *StringWriter) Write(data []byte) (int, error) {
    sw.str += string(data)
    return len(data), nil
}
// 创建一个 StringWriter 实例并赋值给 Writer 接口变量
var w Writer = &StringWriter{}
// 将 Writer 接口类型转换为 StringWriter 类型
sw := w.(*StringWriter)
// 修改 StringWriter 的字段
sw.str = "Hello, World"
// 打印 StringWriter 的字段值
fmt.Println(sw.str)
```

# 错误处理
错误处理采用显式返回错误的方式，而非传统的异常处理机制 
主要围绕以下机制展开:
* error 接口：标准的错误表示。
``` go
//标准库定义了一个 error 接口，任何实现了该接口的类型都可以作为错误值。
type error interface {
    Error() string
}
//
func Sqrt(f float64) (float64, error) {
    if f < 0 {
        return 0, errors.New("math: square root of negative number")
    }
    // 实现
}
```
* 显式返回值：通过函数的返回值返回错误
``` go
func divide(a, b int) (int, error) {
        if b == 0 {
                return 0, errors.New("division by zero")
        }
        return a / b, nil
}
```
* 自定义错误：可以通过标准库或自定义的方式创建错误
``` go
type DivideError struct {
        Dividend int
        Divisor  int
}

func (e *DivideError) Error() string {
        return fmt.Sprintf("cannot divide %d by %d", e.Dividend, e.Divisor)
}

func divide(a, b int) (int, error) {
        if b == 0 {
                return 0, &DivideError{Dividend: a, Divisor: b}
        }
        return a / b, nil
}
```
从 Go 1.13 开始，errors 包引入了 errors.Is 和 errors.As 用于处理错误链
``` go
//errors.Is 检查某个错误是否是特定错误或由该错误包装而成
package main

import (
        "errors"
        "fmt"
)

var ErrNotFound = errors.New("not found")

func findItem(id int) error {
        return fmt.Errorf("database error: %w", ErrNotFound)
}

func main() {
        err := findItem(1)
        if errors.Is(err, ErrNotFound) {
                fmt.Println("Item not found")
        } else {
                fmt.Println("Other error:", err)
        }
}
```
``` go
//errors.As 将错误转换为特定类型以便进一步处理
package main

import (
        "errors"
        "fmt"
)

type MyError struct {
        Code int
        Msg  string
}

func (e *MyError) Error() string {
        return fmt.Sprintf("Code: %d, Msg: %s", e.Code, e.Msg)
}

func getError() error {
        return &MyError{Code: 404, Msg: "Not Found"}
}

func main() {
        err := getError()
        var myErr *MyError
        if errors.As(err, &myErr) {
                fmt.Printf("Custom error - Code: %d, Msg: %s\n", myErr.Code, myErr.Msg)
        }
}
```
* panic 和 recover：处理不可恢复的严重错误
``` go
//panic 用于处理不可恢复的错误，recover 用于从 panic 中恢复
/*
panic:
    导致程序崩溃并输出堆栈信息。
    常用于程序无法继续运行的情况。
recover:
    捕获 panic，避免程序崩溃。
 */
package main

import "fmt"

func safeFunction() {
        defer func() {
                if r := recover(); r != nil {
                        fmt.Println("Recovered from panic:", r)
                }
        }()
        panic("something went wrong")
}

func main() {
        fmt.Println("Starting program...")
        safeFunction()
        fmt.Println("Program continued after panic")
}
/*
输出：
Starting program...
Recovered from panic: something went wrong
Program continued after panic
 */
```

# 并发
Go 语言支持并发，通过 goroutines 和 channels 提供了一种简洁且高效的方式来实现并发 

Goroutines： 
Go 中的并发执行单位，类似于轻量级的线程
* Goroutine 的调度由 Go 运行时管理，用户无需手动分配线程
* 使用 go 关键字启动 Goroutine
* Goroutine 是非阻塞的，可以高效地运行成千上万个 Goroutine

Channel： 
Go 中用于在 Goroutine 之间通信的机制 
* 支持同步和数据共享，避免了显式的锁机制
* 使用 chan 关键字创建，通过 <- 操作符发送和接收数据

Scheduler（调度器）： 
Go 的调度器基于 GMP 模型，调度器会将 Goroutine 分配到系统线程中执行，并通过 M 和 P 的配合高效管理并发 
* G：Goroutine。
* M：系统线程（Machine）
* P：逻辑处理器（Processor）

## WaitGroup
sync.WaitGroup 用于等待多个 Goroutine 完成 
``` go
package main

import (
        "fmt"
        "sync"
)

func worker(id int, wg *sync.WaitGroup) {
        defer wg.Done() // Goroutine 完成时调用 Done()
        fmt.Printf("Worker %d started\n", id)
        fmt.Printf("Worker %d finished\n", id)
}

func main() {
        var wg sync.WaitGroup

        for i := 1; i <= 3; i++ {
                wg.Add(1) // 增加计数器
                go worker(i, &wg)
        }

        wg.Wait() // 等待所有 Goroutine 完成
        fmt.Println("All workers done")
}
```

## Buffered Channel
创建有缓冲的 Channel
``` go
ch := make(chan int, 2)
```

## Context：
用于控制 Goroutine 的生命周期
``` go
context.WithCancel、context.WithTimeout
```

## Mutex 和 RWMutex
sync.Mutex 提供互斥锁，用于保护共享资源
``` go 
var mu sync.Mutex
mu.Lock()
// critical section
mu.Unlock()
```

## 协程使用示例
``` go
//通过两个 goroutine 来计算数字之和，在 goroutine 完成计算后，它会计算两个结果的和
package main

import "fmt"

func sum(s []int, c chan int) {
    sum := 0
    for _, v := range s {
        sum += v
    }
    c <- sum // 把 sum 发送到通道 c
}

func main() {
    s := []int{7, 2, 8, -9, 4, 0}

    c := make(chan int)
    go sum(s[:len(s)/2], c)
    go sum(s[len(s)/2:], c)
    x, y := <-c, <-c // 从通道 c 中接收

    fmt.Println(x, y, x+y)
}
```

# go常用命令
* go mod init
初始化go mod， 生成go.mod文件，后可接参数指定 module 名，上面已经演示过。
* go mod download
手动触发下载依赖包到本地cache（默认为$GOPATH/pkg/mod目录）
* go mod graph
打印项目的模块依赖结构
* go mod tidy
添加缺少的包，且删除无用的包
* go mod verify
校验模块是否被篡改过
* go mod why
查看为什么需要依赖
* go mod vendor
导出项目所有依赖到vendor下
* go mod edit
编辑go.mod文件，接 -fmt 参数格式化 go.mod 文件，接 -require=golang.org/x/text 添加依赖，接 -droprequire=golang.org/x/text 删除依赖，详情可参考 go help mod edit
* go list -m -json all
以 json 的方式打印依赖详情 
* go get -u
将会升级到最新的次要版本或者修订版本(x.y.z, z是修订版本号， y是次要版本号)
* go get -u=patch
将会升级到最新的修订版本
* go get package@version
将会升级到指定的版本号version

# 常用包
* 雪花算法
github.com/bwmarrin/snowflak 

* redis
github.com/go-redis/redis

* sqlserver
github.com/microsoft/go-mssqldb

* mysql
github.com/go-sql-driver/mysql

* protobuf 
github.com/golang/protobuf已被弃用
google.golang.org/protobuf
https://developer.aliyun.com/article/1169702

* zap
zap 是 uber 开源的一个高性能，结构化，分级记录的日志记录包。
github.com/uber-go/zap

# vscode 插件
* FittenCode
智能代码生成

* GO
GGO语言插件

* Material Icon Theme
文件图标

* Remote SSH
vscode 远程链接linux开发

* 其它插件
https://www.cnblogs.com/xuweihui/p/18181582

# 参考资料
* Go中文文档
http://go.p2hp.com/go.dev/doc/
* 标准包文档
https://pkg.go.dev/std
* GO圣经(中文版)
https://gopl-zh.codeyu.com/
* GO高级编程
https://chai2010.cn/advanced-go-programming-book/
* go语法糖
https://blog.csdn.net/kevin_tech/article/details/125954995
* dll生成
https://www.cnblogs.com/Kingram/p/12088087.html
* 多路复用(grpc、http等共用端口)
https://github.com/soheilhy/cmux
* protobuf介绍
https://www.jb51.net/jiaoben/3108797gd.htm
* 分布式框架
https://github.com/dobyte/due
* 文件读写
https://www.cnblogs.com/dibtp/p/18083986


# 问题记录
* GOPATH目录下有go.mod时,子目录下工程执行go mod tidy会提示go: go.mod file not found in current directory or any parent directory 
解决方法:
删除该go.mod

* binary.Write注意事项 
1、必须使用指定长度类型，例如int是不允许的，必须int32等 
2、结构体unsafe.Sizeof是会进行内存对齐的，但是binary.Write结果是无内存对齐的，所以写入时需要保存长度信息 

* import "C"提示找不到go file 
开启cgo 
go env -w CGO_ENABLED=1 

* go run a.go只会查找a.go,涉及多文件时命令: 
go run a.go b.go c.go ... 

* GOPROXY代理 
gov1.13默认为https://proxy.golang.org 
国内建议
go env -w GOPROXY=https://goproxy.cn,direct