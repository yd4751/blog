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
