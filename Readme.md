# 成分查询器（HttpApi 版)

- 一键生成vtb关注列表图片, 快速查成分！
- 关注列表使用B站接口查询，vtb数据通过[vtbs.moe](https://vtbs.moe/)获取
- 用途: 你可以快速自查, 或者查别人。你还可以稍微修改一下, 把它做到Bot上
- 支持通过 HTTP 调用

# 用法

- `Python 3`环境
- 输入`pip install -r requirements.txt`安装依赖
- 在 `./dd_query/api.py`中的第101-102行修改请求`vtbs.moe`时使用的代理地址。如果您不需要代理，请将`在这填入代理地址`这几个字删掉。如下图所示：  
![](https://dimg04.c-ctrip.com/images/0Z015120009tozjgbE6CA.png)

- 最简单的用法

```python
import dd_query

dd = dd_query.DDImageGenerate("DD情报局")

# 生成图片路径, 关注vtb数量, 关注up总数
image_path, vtb_following_count, total_following_count = dd.image_generate()
```

- 您也可以直接运行`main.py`

- 您也可以通过`HTTP`方式进行调用
  - 启动(带命令行): python run.py
  - 启动(不带命令行): pythonw run.py  
  HTTP 伺服器将会运行在`1145`端口,可以在`run.py`中修改
  。  
  以下是 api 接口：

# Api

| 访问地址 | 功能 | 备注 |
| --- | --- | --- |
| example.com/ | 检测运行状态 | 返回码默认`200`。
| example.com/chachengfen/`<username>`| 查指定`用户名` | `GET` 返回 json,自行尝试。 |
| example.com/output/`<username>` | 下载用户的成分图，格式为`jpg` | `GET` 需要先调用`chachengfen`接口才能调用本接口 |

# 添加账户

- 众所周知, 查询别人的关注列表, 只能查询前5页, 也就是250个人. 251及以后的关注是查不到的. 因此会出现数据遗漏的情况
- 但是, 查询共同关注是没有限制的. 所以, 只要用几个账号关注所有vtb, 就可以查到完整的数据了
- 如果你懒得折腾, 也可以直接用, 只查前250个人也不少了

## 添加方法

- 首先准备至少两个B站账号, 分别获取这些账号的`UID`, `cookies`

  - `UID`的获取不再赘述。`cookie`中的`SESSDATA`和`bili_jct`请单独复制出来
- 运行`make_dd_account.py`, 按照中文提示, 在对应地方填入信息, 脚本将自动关注所有vtb
- 一个账号关注满, 需要切换账户时, 脚本会导出未关注的vtb数据, 再次运行脚本, 根据提示将导出的vtb数据路径填入即可
- 账户关注完成后, 使用数据库软件打开`dd_query/cookies/bili_dd_account.db`, 在表内添加账号即可。cookie的有效期大约是半年, cookie失效后在数据库更新一下即可

# 已知问题

- 图片有点丑, 欢迎会排版的耶叶PR
- 使用`查看共同关注`的方式无法获取用户关注时间.

# 效果预览

![](https://raw.githubusercontent.com/chinosk114514/chachengfen/main/dd_query/temp/000.jpg)
