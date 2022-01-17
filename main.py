import dd_query

# dd = dd_query.GetUserFollowingVTB("chinosk")
dd = dd_query.DDImageGenerate("DD情报局")

# 生成图片路径, 关注vtb数量, 关注up总数
image_path, vtb_following_count, total_following_count = dd.image_generate()
