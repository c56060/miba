import os
import re

# 定义项目根目录为当前工作目录
root_dir = os.getcwd()

# 图片文件夹路径
image_folder = os.path.join(root_dir, "展示图", "机构合集")
# 名称文件路径
name_file = os.path.join(root_dir, "名称", "机构合集.txt")
# 输出网页文件存放路径
output_folder = "002"  # 输出文件夹名称
# 每页显示的图片数量
items_per_page = 24  # 如果删除分页功能，这个值将不再使用

# 如果输出文件夹不存在，则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 定义自然排序函数
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

# 获取所有图片文件名（支持常见图片格式），并按自然排序
image_files = sorted(
    [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpeg', '.jpg', '.png', '.gif'))],
    key=natural_sort_key
)
print(f"获取到的图片文件数量: {len(image_files)}")

# 读取名称文件
with open(name_file, 'r', encoding='utf-8') as file:
    names = file.read().splitlines()

# 确保图片文件数量和名称数量一致
if len(image_files) != len(names):
    raise ValueError("图片文件数量和名称数量不一致，请检查！")

# 生成所有图片卡片的 HTML 代码
all_image_items = []
for index, (image_file, name) in enumerate(zip(image_files, names), start=1):
    formatted_index = f"{index:03d}"
    # 计算相对路径
    relative_path = os.path.relpath(image_folder, start=root_dir)
    image_rel_path = os.path.join(relative_path, image_file).replace('\\', '/')
    item_html = f"""
    <div class="photo-card photography-card">
        <div class="image-container">
            <img data-src="../{image_rel_path}" alt="{name}" loading="lazy">
        </div>
        <a href="detail_{formatted_index}.html" class="name-link">{name}</a>
        <div class="overlay">
            <H2>编号: {formatted_index}</H2>
        </div>
    </div>
    """
    all_image_items.append(item_html)

# 生成主页面的 HTML 模板
main_template = f"""
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>摄影写真官网</title>
    <link rel="stylesheet" href="../css/style.css">
</head>

<body>
    <nav class="navbar">
        <img src="../images/logo.png" class="logo" alt="机构LOGO">
        <div class="nav-buttons">
            <div class="nav-button-wrapper">
                <a href="../001/000.html" class="nav-button">首页</a>
                <ul class="sub-menu"></ul>
            </div>
            <div class="nav-button-wrapper">
                <a href="#" class="nav-button">写真合集</a>
                <ul class="sub-menu">
                    <li><a href="../002/Cosplay合集.html">Cosplay合集</a></li>
                    <li><a href="../002/微密圈.html">微密圈</a></li>
                    <li><a href="../002/B站UP.html">B站UP</a></li>
                    <li><a href="../002/B站UP-收藏集.html">B站UP-收藏集</a></li>
                    <li><a href="../002/微博抖音.html">微博抖音</a></li>
                    <li><a href="../002/主播热舞.html">主播热舞</a></li>
                    <li><a href="../002/充电哄睡.html">充电哄睡</a></li>
                </ul>
            </div>
            <div class="nav-button-wrapper">
                <a href="#" class="nav-button">精选名站</a>
                <ul class="sub-menu">
                    <li><a href="../003/ROSI写真.html">ROSI写真</a></li>
                    <li><a href="../003/YITUYU艺图语.html">YITUYU艺图语</a></li>
                    <li><a href="../003/ISHOW爱秀.html">ISHOW爱秀</a></li>
                    <li><a href="../003/少女秩序.html">少女秩序</a></li>
                    <li><a href="../003/爱尤物.html">爱尤物</a></li>
                    <li><a href="../003/Ligui丽柜.html">Ligui丽柜</a></li>
                    <li><a href="../003/森萝财团.html">森萝财团</a></li>
                    <li><a href="../003/稚乖画册.html">稚乖画册</a></li>
                    <li><a href="../003/紧急企划.html">紧急企划</a></li>
                    <li><a href="../003/YALAYI雅拉伊.html">YALAYI雅拉伊</a></li>
                    <li><a href="../003/Beautyleg.html">Beautyleg</a></li>
                    <li><a href="../003/YouMei尤美.html">YouMei尤美</a></li>
                    <li><a href="../003/物恋传媒.html">物恋传媒</a></li>
                    <li><a href="../003/Ugirls尤果网.html">Ugirls尤果网</a></li>
                    <li><a href="../003/大西瓜爱牙膏.html">大西瓜爱牙膏</a></li>
                    <li><a href="../003/BoLoli波萝社.html">BoLoli波萝社</a></li>
                    <li><a href="../003/TouTiao头条女神.html">TouTiao头条女神</a></li>
                    <li><a href="../003/SLADY猎女神.html">SLADY猎女神</a></li>
                    <li><a href="../003/MSLASS梦丝女神.html">MSLASS梦丝女神</a></li>
                    <li><a href="../003/MISSLEG蜜丝.html">MISSLEG蜜丝</a></li>
                    <li><a href="../003/奈丝写真.html">奈丝写真</a></li>
                    <li><a href="../003/Kimoe激萌文化.html">Kimoe激萌文化</a></li>
                    <li><a href="../003/KeLaGirls克拉女神.html">KeLaGirls克拉女神</a></li>
                    <li><a href="../003/Girlt果团网.html">Girlt果团网</a></li>
                    <li><a href="../003/DISI第四印象.html">DISI第四印象</a></li>
                    <li><a href="../003/51MoDo.html">51MoDo</a></li>
                    <li><a href="../003/丝慕写真.html">丝慕写真</a></li>
                    <li><a href="../003/制服の女生.html">制服の女生</a></li>
                    <li><a href="../003/最爱帆布鞋.html">最爱帆布鞋</a></li>
                    <li><a href="../003/妖精视觉.html">妖精视觉</a></li>
                    <li><a href="../003/SHENSHI绅士.html">SHENSHI绅士</a></li>
                    <li><a href="../003/SunGirl阳光宝贝.html">SunGirl阳光宝贝</a></li>
                    <li><a href="../003/LD零度摄影.html">LD零度摄影</a></li>
                    <li><a href="../003/喵写真.html">喵写真</a></li>
                    <li><a href="../003/轻兰映画.html">轻兰映画</a></li>
                    <li><a href="../003/GALLI嘉丽舞蹈生日记.html">GALLI嘉丽舞蹈生日记</a></li>
                    <li><a href="../003/兔玩映画.html">兔玩映画</a></li>
                    <li><a href="../003/喵糖映画.html">喵糖映画</a></li>
                    <li><a href="../003/风之领域.html">风之领域</a></li>
                    <li><a href="../003/TGOD推女神.html">TGOD推女神</a></li>
                </ul>
            </div>
            <div class="nav-button-wrapper">
                <a href="#" class="nav-button">摄影机构</a>
                <ul class="sub-menu">
                    <li><a href="../003/XIUREN秀人网.html">XIUREN秀人网</a></li>
                    <li><a href="../003/XIAOYU语画界.html">XIAOYU语画界</a></li>
                    <li><a href="../003/IMISS爱蜜社.html">IMISS爱蜜社</a></li>
                    <li><a href="../003/FEILN嗲囡囡.html">FEILN嗲囡囡</a></li>
                    <li><a href="../003/HuaYang花漾.html">HuaYang花漾</a></li>
                    <li><a href="../003/MyGirl美媛馆.html">MyGirl美媛馆</a></li>
                    <li><a href="../003/MiStar魅妍社.html">MiStar魅妍社</a></li>
                    <li><a href="../003/MFStar模范学院.html">MFStar模范学院</a></li>
                    <li><a href="../003/YouMi尤蜜荟.html">YouMi尤蜜荟</a></li>
                    <li><a href="../003/CANDY糖果画报.html">CANDY糖果画报</a></li>
                    <li><a href="../003/YouWu尤物馆.html">YouWu尤物馆</a></li>
                    <li><a href="../003/DKGirl御女郎.html">DKGirl御女郎</a></li>
                    <li><a href="../003/HuaYan花の颜.html">HuaYan花の颜</a></li>
                    <li><a href="../003/XingYan星颜社.html">XingYan星颜社</a></li>
                    <li><a href="../003/RUISG瑞丝馆.html">RUISG瑞丝馆</a></li>
                    <li><a href="../003/LeYuan星乐园.html">LeYuan星乐园</a></li>
                    <li><a href="../003/WingS影私荟.html">WingS影私荟</a></li>
                    <li><a href="../003/MintYe薄荷叶.html">MintYe薄荷叶</a></li>
                    <li><a href="../003/UXING优星馆.html">UXING优星馆</a></li>
                    <li><a href="../003/TASTE顽味生活.html">TASTE顽味生活</a></li>
                </ul>
            </div>
            <div class="nav-button-wrapper">
                <a href="#" class="nav-button">帮助中心</a>
                <ul class="sub-menu">
                    <li><a href="../images/常见问题.html">常见问题</a></li>
                    <li><a href="../images/电脑端解压教程.html">电脑端解压教程</a></li>
                    <li><a href="../images/安卓端解压教程.html">安卓端解压教程</a></li>
                    <li><a href="../images/手机端解压教程.html">手机端解压教程</a></li>
                    <li><a href="../images/联系客服.html">联系客服</a></li>
                </ul>
            </div>
        </div>
        <div class="search-container">
            <input type="text" class="search-input" placeholder="搜索作品/摄影师">
            <img src="../images/search-icon.png" class="search-icon" alt="搜索">
        </div>
    </nav>

    <main class="main-content">
        <!-- COSER作品区 -->
        <div class="grid-container">
            {''.join(all_image_items)}
        </div>
    </main>

    <script src="../js/script.js"></script>
</body>

</html>
"""

# 保存到文件
output_file = os.path.join(output_folder, "机构合集.html")
with open(output_file, "w", encoding="utf-8") as file:
    file.write(main_template)

print(f"HTML代码已生成并保存到 {output_file} 文件中。")