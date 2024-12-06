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
<tr><td><a title="Go if 语句">if 语句</a></td><td><b>if </b> 由一个布尔表达式后紧跟一个或多个语句组成。</td></tr>
<tr><td><a title="Go if...else 语句">if...else </a></td><td><b>if 语句</b> 后可以使用可选的 <b>else 语句</b>, else 语句中的表达式在布尔表达式为 false 时执行。</td></tr>
<tr><td><a title="Go if 嵌套语句"> if </a></td><td>你可以在 <b>if</b> 或 <b>else if</b> 语句中嵌入一个或多个 <b>if</b> 或 <b>else if</b> 语句。</td></tr>
<tr><td><a title="Go switch 语句">switch </a></td><td><b>switch</b> 语句用于基于不同条件执行不同动作。</td></tr>
<tr><td><a title="Go select 语句">select </a></td><td><b>select</b> 语句类似于 <b>switch</b> 语句，但是select会随机执行一个可运行的case。如果没有case可运行，它将阻塞，直到有case可运行。</td></tr>
</tbody></table>

<blockquote><p>注意：Go 没有三目运算符，所以不支持 <strong>?:</strong> 形式的条件判断。</p></blockquote>
</html>

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

