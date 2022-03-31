# DjangoBlog

## 运行环境：

 1. 虚拟环境：  `pipenv`
 2. Django版本： `django2.2.3` (后因为 https://pypi.org/sample/ 里没有 2.2.3 版本, 故修改为:
   `django>=2.2.3,<2.3`.)

## 使用:

1. `git clone https://github.com/zengjiapei3000/DjangoBlog.git`
2. `cd DjangoBlog`
3. 运行 `pipenv verify` to verify the `Pipfile.lock` 是否过时, 如果过时, 
   运行 `pipenv lock` 来更新; 如果没有过时, 去到步骤4.
4. 运行 `pipenv sync` 来安装 所有在 Pipfile.lock 里指定的包.
5. 运行 `pipenv shell` 来进入 pipenv 虚拟环境, 此时命令行应该形如 `(DjangoBlog) {user}@{hostname}` 的格式, 说明此时进入虚拟环境成功.
6. 运行 `python -m manage runserver` 来在本地运行 DjangoBlog 项目.

## 结束使用:
1. 如果上面的步骤6的本地的服务器还在运行, 先 CTRL+C 结束运行.
2. 再 `exit` 退出 pipenv 的虚拟环境.

---

## 已实现功能：

1. 文章支持 Markdown 语法和 代码高亮;
2. Markdown 文章自动生成目录, 支持多重子目录;
3. 自动生成文章摘要;
4. 页面侧边栏用自定义标签实现, 包括 最近文章、
   按日期归档、分类、标签云;
5. 文章详情页的评论功能;
6. 文章阅读量统计功能;
7. 使用 Faker 模块批量生成测试数据;
8. 使用第三方应用 django-pure-pagination 实现分页效果;


## TODO list:

1.  :ballot_box_with_check: ~~完全汉化, 包括 admin;~~ 
2.  :ballot_box_with_check: ~~博客支持 Markdown 语法和代码高亮;~~
3.  :ballot_box_with_check: ~~Markdown 文章自动生成目录;~~
4.  :ballot_box_with_check: ~~自动生成文章摘要;~~
5.  :ballot_box_with_check: ~~侧边栏: 使用自定义模板标签;~~
6.  :ballot_box_with_check: ~~分类、归档、标签;~~
7.  :ballot_box_with_check: ~~评论功能;~~
8.  :ballot_box_with_check: ~~脚本中使用 ORM:Faker 批量生成测试数据;~~
9.  :ballot_box_with_check: ~~简单分页;~~
10. :ballot_box_with_check:~~完整的分页效果;~~
11. 统计各个分类和标签下文章数;
12. RSS;
13. 全文搜索;
14. 单元测试;
15. 统计测试覆盖率;
