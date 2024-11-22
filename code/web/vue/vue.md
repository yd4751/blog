# 安装
1、在 Vue.js 的官网上直接下载最新版本, 并用 <script> 标签引入
https://unpkg.com/vue@3.5.13/dist/vue.global.js

2、npm
``` shell
#包管理器
npm
yarn
pnpn

# 查看版本
npm -v
2.3.0

#升级 npm
cnpm install npm -g

# 升级或安装 cnpm  
#cnpm：是一个完整 npmjs.org 镜像，可以用此代替官方版本
npm install cnpm -g

#安装依赖并启动开发服务器
npm install
npm run dev

#Vite 是一个 web 开发构建工具
npm init vite-app <project-name>

# 安装 Vue CLI ,Vue CLI提供了一整套标准化的工具和预设配置，使得开发者可以快速启动和配置项目,正确安装Vue CLI是使用Vue命令的第一步
npm install -g @vue/cli

# vite
npm install -g vite
```

# vue和vite
‌Vite和Vue的主要区别在于构建和开发过程的不同。‌‌

构建速度和开发体验：    
‌Vite‌：使用原生ES模块，在开发环境下不需要打包，可以直接运行源代码，提供了更快的启动和刷新速度。Vite将开发服务器和构建过程分离，只需构建一次，提高了开发的效率。     
‌Vue‌：使用传统的Webpack构建方式，需要将所有代码打包成一个或多个文件，这在开发环境下需要重新打包，速度较慢。     
生成环境：      
‌Vite‌：在生产环境中，Vite会将所有的ES模块转换为可部署的代码，以便在现代浏览器中运行。因此，Vite可以与Vue一样用于构建生产级别的应用程序。        
‌Vue‌：在生产环境中，Vue和Vite之间没有太大的区别，都可以用于构建生产级别的应用程序。      


# 创建vue项目,几种不同方式
``` shell
#npm init、create和innit，它们实际上是init命令的别名

npm init vue@latest
#中文提示，方便操作

npm init vite@latest
#可以搭建多种框架



vue create my-project
#vue-cli3.x的初始化方式，目前模板是固定的

vue init webpack 项目名称
#ue-cli2.x的初始化方式，可以使用github上面的一些模板来初始化项目，webpack是官方推荐的标准模板名

vue ui
#图形化界面，可以创建项目，可以选择模板，可以安装插件，可以预览效果
```

# 项目打包
``` shell
#执行完成后，会在 Vue 项目下会生成一个 dist 目录，该目录一般包含 index.html 文件及 static 目录，static 目录包含了静态文件 js、css 以及图片目录 images（如果有图片的话）
npm run build
```

# 初始项目目录说明
![预览](https://github.com/yd4751/blog/blob/main/img/1.png)
![预览](https://github.com/yd4751/blog/blob/main/img/2.png)
![预览](https://github.com/yd4751/blog/blob/main/img/3.png)

# vue示例
``` html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Vue 测试实例</title>
<script src="https://lf3-cdn-tos.bytecdntp.com/cdn/expire-1-M/vue/3.2.26/vue.global.min.js"></script>
</head>
<body>
<div id="hello-vue" class="demo">
  {{ message }}
</div>

<script>
const HelloVueApp = {
  data() {
    return {
      message: 'Hello Vue!!'
    }
  }
}

Vue.createApp(HelloVueApp).mount('#hello-vue')
</script>
</body>
</html>
```
## {{ message }}:
* 这是 Vue.js 的模板语法，用于将 Vue 实例中的 message 数据绑定到页面上
* 当 Vue 实例中的 message 数据变化时，页面上的内容也会随之更新

## JavaScript 部分说明：
### Vue 实例定义:
``` js
const HelloVueApp = {
  data() {
    return {
      message: 'Hello Vue!!'
    }
  }
}
```
* HelloVueApp 是一个普通的 JavaScript 对象，包含了 Vue 组件选项
* data() 方法返回一个包含 message 属性的对象，这个属性的初始值是 'Hello Vue!!'

### 创建并挂载 Vue 应用:
* Vue.createApp() 方法用于创建一个 Vue 应用实例，参数是一个包含组件选项的对象（这里是 HelloVueApp）
* .mount('#hello-vue') 方法将 Vue 应用实例挂载到页面中具有 id="hello-vue" 的 DOM 元素上

### 执行过程
* 页面加载时，浏览器解析 HTML 和 JavaScript
* Vue.js 脚本执行时，创建了一个 Vue 应用实例，并将其绑定到 <div id="hello-vue"> 元素上
* Vue 应用实例根据 data() 中的初始数据，将 message 的值渲染到页面上的 {{ message }} 处
* 当 message 数据发生变化时（例如通过用户交互或异步操作），页面会自动更新以反映这些变化


# vue语法
## 插值
使用双大括号 {{ }} 来表示文本插值
{{...}} 标签的内容将会被替代为对应组件实例中 message 属性的值，如果 message 属性的值发生了改变，{{...}} 标签内容也会更新
如果不想改变标签的内容，可以通过使用 v-once 指令执行一次性地插值，当数据改变时，插值处的内容不会更新
``` html
<!-- 动态绑定 message 属性 -->
<div>{{ message }}</div>
<!-- 一次性地绑定 message 属性 -->
<div v-once>{{ message }}</div>
```

v-html 指令用于输出 html 代码
``` html
<p>使用双大括号的文本插值: {{ rawHtml }}</p>
<p>使用 v-html 指令: <span v-html="rawHtml"></span></p>
```


## 指令
指令是带有前缀 v- 的特殊属性，用于在模板中表达逻辑
``` html
<!-- v-bind: 动态绑定一个或多个特性，或一个组件 prop -->
<a v-bind:href="url">Link</a> 
<a :href="url">Link</a> <!-- 简写 -->

<!-- v-if/v-else-if/v-else: 条件性地渲染元素 -->
<p v-if="showMessage">Hello Vue!</p>
<p v-else-if>Goodbye Vue!</p>
<p v-else>Goodbye Vue!</p>

<!-- v-for: 列表渲染 -->
<ul>
  <li v-for="item in items" :key="item.id">{{ item.text }}</li>
</ul>

<!-- v-show: 条件性地显示或隐藏元素 -->
<div v-show="lightOn"></div>
<img src="https://static.jyshare.com/images/svg/img_lightBulb.svg">

<!-- v-model: 双向数据绑定 -->
<input v-model="message" placeholder="edit me">
<p>Message is: {{ message }}</p>

<!-- v-on: 事件监听器 -->
<button v-on:click="doSomething">Click me</button>
<button @click="doSomething">Click me</button> <!-- 简写 -->
```

## 事件处理
在 Vue.js 中，你可以使用 v-on 指令来监听 DOM 事件，并在触发时执行一些 JavaScript 代码
``` html
<div id="app">
  <button @click="greet">Greet</button>
</div>

<script>
  createApp({
    methods: {
      greet() {
        alert('Hello!');
      }
    }
  }).mount('#app');
</script>

修饰符
修饰符是以半角句号 . 指明的特殊后缀，用于指出一个指令应该以特殊方式绑定。例如，.prevent 修饰符告诉 v-on 指令对于触发的事件调用 event.preventDefault()：
``` html
<form v-on:submit.prevent="onSubmit"></form>
```

## 计算属性
计算属性是基于其依赖进行缓存的属性。计算属性只有在其相关依赖发生变化时才会重新计算
``` html
<div id="app">
  <p>{{ reversedMessage }}</p>
</div>

<script>
  createApp({
    data() {
      return {
        message: 'Hello'
      };
    },
    computed: {
      reversedMessage() {
        return this.message.split('').reverse().join('');
      }
    }
  }).mount('#app');
</script>
```

## 组件
组件是 Vue.js 最强大的功能之一。组件允许你使用小型、独立和通常可复用的组件构建大型应用
每个 Vue 组件都是一个独立的 Vue 实例，具有自己的模板、数据、方法和生命周期钩子，使得组件可以自包含地定义和管理自己的功能和样式
## 全局组件
``` html
<div id="app">
  <my-component></my-component>
</div>

<script>
  // 创建一个Vue 应用
  const app = Vue.createApp({});

  // 定义一个名为 my-component的全局组件
  app.component('my-component', {
    template: '<div>A custom component!</div>'
  });

  // 挂载到app元素上
  app.mount('#app');
</script>
```

## 局部组件
``` html
<div id="app">
    <comp-a></comp-a>
</div>
<script>
var compA = {
  template: '<h1>自定义组件!</h1>'
}
 
const app = Vue.createApp({
  components: {
    'comp-a': compA
  }
})
 
app.mount('#app')
</script>
```

## 单文件组件 (.vue 文件)
使用单文件组件能够更好地组织和管理 Vue 组件，一个组件通常由三部分组成：模板、脚本和样式
``` html
<!-- MyComponent.vue -->
<template>
  <div>
    <p>{{ message }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: 'Hello from MyComponent',
      count: 0
    };
  },
  methods: {
    increment() {
      this.count++;
    }
  }
};
</script>

<style scoped>
/* 组件私有样式 */
p {
  color: blue;
}
</style>
```

## Props
Props 用于在组件之间传递数据
``` html
<div id="app">
  <blog-post title="My journey with Vue"></blog-post>
</div>

<script>
  const app = createApp({
    data() {
      return {};
    }
  });

  app.component('blog-post', {
    props: ['title'],
    template: '<h3>{{ title }}</h3>'
  });

  app.mount('#app');
</script>
```

## 事件
子组件通过 $emit 触发事件，父组件可以监听这些事件
``` html
<div id="app">
  <button-counter @increment="incrementTotal"></button-counter>
  <p>Total clicks: {{ total }}</p>
</div>

<script>
  const app = createApp({
    data() {
      return {
        total: 0
      };
    },
    methods: {
      incrementTotal() {
        this.total++;
      }
    }
  });

  app.component('button-counter', {
    template: '<button @click="increment">You clicked me {{ count }} times.</button>',
    data() {
      return {
        count: 0
      };
    },
    methods: {
      increment() {
        this.count++;
        this.$emit('increment');
      }
    }
  });

  app.mount('#app');
</script>
```

# computed
计算属性
* 计算属性用于根据其他数据的变化动态计算衍生出来的属性值，而且具有缓存机制，只有相关依赖发生变化时才会重新计算
* methods 来替代 computed，效果上两个都是一样的，但是 computed 是基于它的依赖缓存，只有相关依赖发生改变时才会重新取值。而使用 methods ，在重新渲染的时候，
函数总会重新调用执行
* computed 属性默认只有 getter ，也可以定义一个 setter 
``` js
//写法1 再setup中使用 computed 函数来定义计算属性
export default {
  setup() {
    //计算属性
    const productName = computed(() => {
        return `优惠 ${state.name}`;
    });
    // 方法
    const increasePrice = () => {
        state.price += 100;
    };
}
//写法2  在 setup 函数中使用 computed 函数来定义计算属性
const app = {
    computed: {
        //计算属性
        site: {
            // getter
            get: function () {
                return this.name + ' ' + this.url
            },
            // setter
            set: function (newValue) {
                var names = newValue.split(' ')
                this.name = names[0]
                this.url = names[names.length - 1]
            }
        }
    }
}

```

# watch
监听属性
* 用于监测响应式属性的变化，并在属性发生改变时执行特定的操作
``` js
//监听counter 变化
<div id = "app">
    <p style = "font-size:25px;">计数器: {{ counter }}</p>
    <button @click = "counter++" style = "font-size:25px;">点我</button>
</div>
    
<script>
const app = {
  data() {
    return {
      counter: 1
    }
  }
}
vm = Vue.createApp(app).mount('#app')
vm.$watch('counter', function(nval, oval) {
    alert('计数器值的变化 :' + oval + ' 变为 ' + nval + '!');
});
</script>
```

# v-bind 样式绑定
* class 与 style 是 HTML 元素的属性，用于设置元素的样式，我们可以用 v-bind 来设置样式属性
* v-bind 在处理 class 和 style 时， 表达式除了可以使用字符串之外，还可以是对象或数组
* v-bind:class 可以简写为 :class
* 自定义组件上使用 class 属性时，这些 class 将被添加到该元素中。此元素上的现有 class 将不会被覆盖
``` html
<div id="app">
    <div class="static" :class="classObject"></div>
</div>

<script>
const app = {
    data() {
        return {
            isActive: true,
            error: null
        }
    },
    computed: {
        classObject() {
            return {
            active: this.isActive && !this.error,
            'text-danger': this.error && this.error.type === 'fatal'
            }
        }
    }
}
vm = Vue.createApp(app).mount('#app')
</script>

<!-- 数组语法 -->
<div class="static" :class="[activeClass, errorClass]"></div>
<!-- 三元表达式语法 -->
<div class="static" :class="[isActive ? activeClass : '', errorClass]"></div>
<!-- 内联样式 -->
<div :style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
<!-- 多重值,为 style 绑定中的 property 提供一个包含多个值的数组,这样写只会渲染数组中最后一个被浏览器支持的值 -->
<div :style="{ display: ['-webkit-box', '-ms-flexbox', 'flex'] }"></div>

<!-- 如果你的组件有多个根元素，你需要定义哪些部分将接收这个类。可以使用 $attrs 组件属性执行此操作 -->
<div id="app">
    <comp class="classA"></comp>
    <comp ></comp>
</div>
 
<script>
const app = Vue.createApp({})
 
app.component('comp', {
  template: `
    <p :class="$attrs.class">I like comp!</p>
    <span>这是一个子组件</span>
  `
})
 
app.mount('#app')
</script>
```

# v-on 事件处理
v-on 指令来监听 DOM 事件，从而执行 JavaScript 代码
v-on 指令可以缩写为 @ 符号
## v-on 提供了事件修饰符来处理 DOM 事件细节
* .stop - 阻止冒泡
* .prevent - 阻止默认事件
* .capture - 阻止捕获
* .self - 只监听触发该元素的事件
* .once - 只触发一次
* .left - 左键事件
* .right - 右键事件
* .middle - 中间滚轮事件
``` js
<div id="app">
  <button @click="say('hi')">Say hi</button>
  <button @click="say('what')">Say what</button>
  <button @click="greet">点我</button>
</div>
 
<script>
const app = {
  data() {
   
  },
  methods: {
    say(message) {
      alert(message)
    },
    greet(event) {
      // `methods` 内部的 `this` 指向当前活动实例
      alert('Hello ' + this.name + '!')
      // `event` 是原生 DOM event
      if (event) {
        alert(event.target.tagName)
      }
    }
  }
}
 
Vue.createApp(app).mount('#app')
</script>

<!-- 修饰符 -->

<!-- 阻止单击事件冒泡 -->
<a v-on:click.stop="doThis"></a>
<!-- 提交事件不再重载页面 -->
<form v-on:submit.prevent="onSubmit"></form>
<!-- 修饰符可以串联  -->
<a v-on:click.stop.prevent="doThat"></a>
<!-- 只有修饰符 -->
<form v-on:submit.prevent></form>
<!-- 添加事件侦听器时使用事件捕获模式 -->
<div v-on:click.capture="doThis">...</div>
<!-- 只当事件在该元素本身（而不是子元素）触发时触发回调 -->
<div v-on:click.self="doThat">...</div>

<!-- click 事件只能点击一次，2.1.4版本新增 -->
<a v-on:click.once="doThis"></a>

<!-- 按键修饰符 -->

<input v-on:keyup.13="submit"> <!-- 只有在 keyCode 是 13 时调用 vm.submit() -->
<input v-on:keyup.enter="submit">
```

## 全部的按键别名
* .enter
* .tab
* .delete (捕获 "删除" 和 "退格" 键)
* .esc
* .space
* .up
* .down
* .left
* .right
## 系统修饰键：
* .ctrl
* .alt
* .shift
* .meta
## 鼠标按钮修饰符
* .left
* .right
* .middle
## .exact 修饰符
.exact 修饰符允许你控制由精确的系统修饰符组合触发的事件
``` html
<!-- 即使 Alt 或 Shift 被一同按下时也会触发 -->
<button @click.ctrl="onClick">A</button>

<!-- 有且只有 Ctrl 被按下的时候才触发 -->
<button @click.ctrl.exact="onCtrlClick">A</button>

<!-- 没有任何系统修饰符被按下的时候才触发 -->
<button @click.exact="onClick">A</button>
```

# 表单
可以用 v-model 指令在表单 <input>、<textarea> 及 <select> 等元素上创建双向数据绑定
* v-model 会根据控件类型自动选取正确的方法来更新元素。
* v-model 会忽略所有表单元素的 value、checked、selected 属性的初始值，使用的是 data 选项中声明初始值。

## v-model 在内部为不同的输入元素使用不同的属性并抛出不同的事件
* text 和 textarea 元素使用 value 属性和 input 事件；
* checkbox 和 radio 使用 checked 属性和 change 事件；
* select 字段将 value 作为属性并将 change 作为事件。