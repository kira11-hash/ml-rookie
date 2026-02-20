# Git 入门与常用命令（给陈庆安）

## 1. Git 是什么
Git 是版本管理工具。  
你可以把它理解成“代码时间机器”：
1. 每次 `commit` 都是一个可回看的快照。
2. 代码改坏了可以回退。
3. 能清楚知道“什么时候改了什么”。

---

## 2. Git 的三个区域（核心概念）
1. 工作区（Working Directory）：
你正在编辑的文件。
2. 暂存区（Staging Area）：
准备提交的文件。
3. 仓库历史（Repository）：
已经提交的版本历史。

对应关系：
1. `git add`：工作区 -> 暂存区
2. `git commit`：暂存区 -> 历史版本

---

## 3. 最常用命令（高频）

### 3.1 看状态
```bash
git status
```
看哪些文件改了、哪些已暂存、哪些未跟踪。

### 3.2 添加改动
```bash
git add .
```
把当前目录下的改动加入暂存区。

也可以只加某个文件：
```bash
git add day4/day4_handwrite.py
```

### 3.3 提交版本
```bash
git commit -m "day4 完成 clean_file"
```
`-m` 是提交说明（message）。

### 3.4 看历史
```bash
git log --oneline -n 10
```
`--oneline` 一行显示，`-n 10` 显示最近 10 条。

### 3.5 看当前未提交差异
```bash
git diff
```

### 3.6 看“已暂存但未提交”差异
```bash
git diff --staged
```

### 3.7 看某次提交改了什么
```bash
git show <commit_id>
```

---

## 4. 去哪里看老版本代码（CLI）

### 4.1 看某次提交的某个文件内容
```bash
git show <commit_id>:<file_path>
```
例子：
```bash
git show b99ed3a:day4/day4_handwrite.py
```

### 4.2 对比两个提交之间的变化
```bash
git diff <old_commit> <new_commit> -- <file_path>
```

### 4.3 临时切到旧提交看整个项目
```bash
git switch --detach <commit_id>
```
看完回到主分支：
```bash
git switch main
```

---

## 5. GUI 看老版本代码（你问的重点）
可以，完全可以。

### 5.1 VS Code（推荐）
1. 打开左侧 Source Control（源代码管理）。
2. 点击某个文件可直接看 diff。
3. 在终端执行 `git log --oneline` 拿到 commit id 后，
   用命令面板或 GitLens 打开该提交文件。

### 5.2 GitLens（VS Code 插件）
1. 安装 GitLens。
2. 右键文件 -> `Open File History`。
3. 直接点某个历史版本看内容和 diff。

### 5.3 GitHub Desktop / SourceTree（可选）
图形界面更直观，适合看历史、分支、提交对比。

---

## 6. 你的日常最小流程（建议固定）
```bash
git status
git add .
git commit -m "今天完成了什么"
git log --oneline -n 3
```

---

## 7. 常见报错

### 7.1 `git add` 报 Nothing specified
原因：你没告诉 Git 要加哪些文件。  
修复：用 `git add .` 或 `git add <file>`。

### 7.2 commit 报“请先配置 user.name / user.email”
修复：
```bash
git config --global user.name "Chen Qingan"
git config --global user.email "your_email@example.com"
```

---

## 8. 现阶段你先做到什么程度
当前阶段只要做到：
1. 会 `status/add/commit/log`
2. 会看 diff
3. 会看某个文件历史版本

这就够支撑 Pre Week 和 Week1 了。
