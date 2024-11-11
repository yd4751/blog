![预览](img/683419500-59ed5ebe73ac6.webp)
# 配置
### git config
``` shell
    git config --global user.name "your name"      // 设置全局用户名
    git config --global user.email "your email"    // 设置邮箱

    git config --global color.ui true              // 让 Git 显示不同的颜色
    git config core.ignorecase true                // 让 Git 对仓库中的文件大小写敏感

    git config -l                                  // 查看所有配置
```
# 基础操作
## 1、创建版本库
git init
``` shell
    git init                                       // 新建一个存放版本库的目录，然后进入到该目录执行该命令
```

## 2、添加到暂存区
git add
``` shell
    git add Readme.md                              // 添加单个文件到暂存区
    git add .                                      // 将当前目录下所有修改添加到暂存区，除按照规则忽略的之外
```
#### 注意：这边空文件夹是不会被添加到暂存区中的。

## 3、提交到本地仓库
git commit
``` shell
    git commit                                     // 如果暂存区有文件，则将其中的文件提交到仓库
    git commit -m 'your comments'                  // 带评论提交，用于说明提交内容、变更、作用等
```

## 4、查看仓库状态和修改
git status
``` shell
    git status                                     // 新建了文件，将文件加入暂存区，或者其他的修改等等
```
git diff
``` shell
    git diff                                       // 查看版本库中所有的改动
    git diff Readme.md                             // 查看具体文件的改动
```

## 5、查看仓库提交记录
git log
``` shell
    git log                                        // 显示所有提交的历史记录
    git log --pretty=oneline                       // 单行显示提交历史记录的内容
```

## 6、版本回退
git reset --hard
``` shell
    git reset --hard HEAD^                         // 回退到上一个提交版本
    git reset --hard HEAD^^                        // 回退到上上一个提交版本
    git reset --hard 'commit_id'                   // 会退到 commit_id 指定的提交版本
```

git reflog 回到未来的某个提交
``` shell
    git reflog
    git reset --hard 'commit_id'
```

## 7、撤销修改
git checkout 丢弃工作区中文件的修改
``` shell
    git checkout -- Readme.md                      // 如果 Readme.md 文件在工作区，则丢弃其修改
    git checkout -- .                              // 丢弃当前目录下所有工作区中文件的修改
```
git reset 丢弃已经进入暂存区的修改
``` shell
    git reset HEAD Readme.md                       // 将 Readme.md 恢复到 HEAD 提交版本的状态
```

## 8、删除文件
git rm
``` shell
    git rm Readme.md                               // 删除已经被提交过的 Readme.md
```
注意： git rm 只能删除已经提交到版本库中的文件。其他状态的文件直接用这个命令操作是出错的。

# 分支管理