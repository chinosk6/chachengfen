# 成分查询器

- 一键生成vtb关注列表图片, 快速查成分！
- 关注列表使用B站接口查询，vtb数据通过[vtbs.moe](https://vtbs.moe/)获取
- 用途: 你可以快速自查, 或者查别人。你还可以稍微修改一下, 把它做到Bot上



# 用法

- `Python 3`环境
- 输入`pip install -r requirements.txt`安装依赖

```
requests
configobj
pydantic
Pillow
```

- 最简单的用法

```python
import dd_query

dd = dd_query.DDImageGenerate("DD情报局")

# 生成图片路径, 关注vtb数量, 关注up总数
image_path, vtb_following_count, total_following_count = dd.image_generate()
```

- 您也可以直接运行`main.py`



# 已知问题

- B站最多只能拉取最近关注的250人, 所以可能会查不全

- 图片有点丑, 欢迎会排版的耶叶PR



# 效果预览

![](https://raw.githubusercontent.com/chinosk114514/chachengfen/main/dd_query/temp/000.jpg)

