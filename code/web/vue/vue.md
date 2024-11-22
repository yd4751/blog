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
<title>Vue 测试实例 - 菜鸟教程(runoob.com)</title>
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
``` html
<div>{{ message }}</div>
```

## 指令
指令是带有前缀 v- 的特殊属性，用于在模板中表达逻辑
``` html
<!-- v-bind: 动态绑定一个或多个特性，或一个组件 prop -->
<a v-bind:href="url">Link</a> 
<a :href="url">Link</a> <!-- 简写 -->

<!-- v-if: 条件性地渲染元素 -->
<p v-if="seen">Now you see me</p>

<!-- v-for: 列表渲染 -->
<ul>
  <li v-for="item in items" :key="item.id">{{ item.text }}</li>
</ul>

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
``` html
<!-- my-component -->
const app = createApp({});

app.component('my-component', {
  template: '<div>A custom component!</div>'
});

<!-- 使用组件 -->
<div id="app">
  <my-component></my-component>
</div>

<script>
  const app = createApp({});

  app.component('my-component', {
    template: '<div>A custom component!</div>'
  });

  app.mount('#app');
</script>
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