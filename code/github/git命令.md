![预览](https://github.com/yd4751/blog/blob/main/img/a6w5y-lnvzd.png)
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
注意：这边空文件夹是不会被添加到暂存区中的。

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
## 1、查看分支
git branch
``` shell
    git branch                                     // 查看本地分支信息
    git branch -v                                  // 查看相对详细的本地分支信息
    git branch -av                                 // 查看包括远程仓库在内的分支信息
```
注意：在 git branch 的输出内容中，有一个分支，前面带有 * 号，这标识我们当前所在的分支。

## 2、创建分支
git branch 当我们要修复一个 Bug，或者开发一个新特性，甚至是在初学的时候怕打乱原来的代码，都可以新建一个分支来避免对原来代码的影响。
``` shell
    git branch dev                                 // 新建一个名称为 dev 的分支
```

## 3、切换分支
git checkout 当我们创建完分支以后，我们需要切换到新建的分支，否则，所有的修改，还是在原来的分支上。事实上，所有的改动，只能影响到当前所在的分支。
``` shell
    git checkout dev                               // 新建完 dev 分支以后，通过该命令切换到 dev 分支
    git checkout -b dev                            // 新建 dev 分支，并切换到该分支上
```

## 4、合并分支
当我们修复完成一个 Bug，或者开发完成一个新特性，我们就会把相关的 Bug 或者 特性的上修改合并回原来的主分支上，这时候就需要 git merge 来做分支的合并。
``` shell
    git checkout master                            // 切换回 master 分支
    git merge dev                                  // 将 dev 分钟中的修改合并回 master 分支
```

## 5、删除分支
当之前创建的分支，完成了它的使命，如 Bug 修复完，分支合并以后，这个分支就不在需要了，就可以删除它。
``` shell
    git branch -d dev                              // 删除 dev 分支
```

# 远程仓库
## 1、从远程仓库克隆
如果你本地没有仓库，希望从已有的远程仓库上复制一份代码，那么你需要 git clone
``` shell
    git clone https://github.com/git/git.git       // 通过 https 协议，克隆 Github 上 git 仓库的源码
    git clone linfuyan@github.com/git/git.git      // 通过 ssh 协议，克隆 Github 上 git 仓库的源码
```

## 2、添加远程仓库
如果你已经有了一个本地仓库，如之前创建的 git-guide，然后你打算将它发布到远程，供其他人协作。
``` shell
    git remote add origin your_remote_git_repo     // 为本地仓库添加远程仓库
```

## 3、推送本地的内容到远程仓库
当本地仓库中，代码完成提交，就需要将代码等推送到远程仓库，这样其他协作人员可以从远程仓库同步内容。
``` shell
    git push -u origin master                      // 第一次推送时使用，可以简化后面的推送或者拉取命令使用
    git push origin master                         // 将本地 master 分支推送到 origin 远程分支
```
注意： git push -u origin master，第一次使用时，带上 -u 参数，在将本地的 master 分支推送到远程新的 master 分支的同时，还会把本地的 master 分支和远程的 master 分支关联起来。

## 4、从远程仓库获取最新内容
在多人协作过程中，当自己完成了本地仓库中的提交，想要向远程仓库推送前，需要先获取到远程仓库的最新内容。
可以通过 git fetch 和 git pull 来获取远程仓库的内容。
``` shell
    git fetch origin master    
    git pull origin master
```
git fetch 和 git pull 之间的区别：
    · git fetch 是仅仅获取远程仓库的更新内容，并不会自动做合并。
    · git pull 在获取远程仓库的内容后，会自动做合并，可以看成 git fetch 之后 git merge。
注意：建议多使用 git fetch。

## 5、查看远程仓库信息
``` shell
    git remote [-v]        // 显示远程仓库信息
```

## 6、建立本地分支和远程分支的关联
在本地仓库中的分支和远程仓库中的分支是对应的。一般情况下，远程仓库中的分支名称和本地仓库中的分支名称是一致的。
``` shell
    git branch --set-upstream 'local_branch' origin/remote_branch
```

# 标签管理
## 1、创建标签
``` shell
    git tag -a 'tagname' -m 'comment' 'commit_id'
```
-a 参数指定标签名， -m 添加备注信息， 'commit_id' 指定打标签的提交。

## 2、查看所有标签
``` shell
    git tag                                        // 查看本地仓库中的所有标签
```

## 3、查看具体标签信息
``` shell
    git show tagname
```

## 4、删除本地标签
如果打的标签出错，或者不在需要某个标签，则可以删除它。
``` shell
    git tag -d tagname
```

## 5、删除远程标签
``` shell
    git push origin :refs/tags/tagname
    git push origin --delete tagname
    git push origin :tagname
```

## 6、推送标签到远程仓库
打完标签以后，有需要推送到远程仓库。
``` shell
    git push origin tagname                        //推送单个标签到远程仓库
    git push origin --tags                         //一次性推送所有标签到远程仓库
```

# 进阶操作
在执行很多的 Git 操作的时候，是需要保持当前操作的仓库/分支处于 clean 状态，及没有未提交的修改。如 git pull， git merge 等等，如果有未提交的修改，这些将无法操作。

但是做这些事情的时候，你可能修改了比较多的代码，却又不想丢弃它。那么，你需要把这些修改临时保存起来，这就需要用到 git stash。

## 1、临时保存修改
``` shell
    git stash                                      // 保存本地仓库中的临时修改,这样仓库就可以回到 clean 状态
    git stash list                                 // 显示所有临时修改
```
注意：可以多次的 git stash 来保存不同的临时修改

## 2、恢复临时保存的修改
``` shell
    git stash apply                                // 恢复所有保存的临时修改
    git stash pop                                  // 恢复最近一次保存的临时修改
    git stash clear                                // 丢弃所有保存的临时修改
```