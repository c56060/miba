import os

# 假设 nav_template 已经定义，这里简单模拟一下
nav_template = """
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
                    <li><a href="../004/output.html">ROSI写真</a></li>
                    <li><a href="../004/output.html">YITUYU艺图语</a></li>
                    <li><a href="../004/output.html">ISHOW爱秀</a></li>
                    <li><a href="../004/output.html">少女秩序</a></li>
                    <li><a href="../004/output.html">爱尤物</a></li>
                    <li><a href="../004/output.html">Ligui丽柜</a></li>
                    <li><a href="../004/output.html">森萝财团</a></li>
                    <li><a href="../004/output.html">稚乖画册</a></li>
                    <li><a href="../004/output.html">紧急企划</a></li>
                    <li><a href="../004/output.html">YALAYI雅拉伊</a></li>
                    <li><a href="../004/output.html">Beautyleg</a></li>
                    <li><a href="../004/output.html">YouMei尤美</a></li>
                    <li><a href="../004/output.html">物恋传媒</a></li>
                    <li><a href="../004/output.html">Ugirls尤果网</a></li>
                    <li><a href="../004/output.html">大西瓜爱牙膏</a></li>
                    <li><a href="../004/output.html">BoLoli波萝社</a></li>
                    <li><a href="../004/output.html">TouTiao头条女神</a></li>
                    <li><a href="../004/output.html">SLADY猎女神</a></li>
                    <li><a href="../004/output.html">MSLASS梦丝女神</a></li>
                    <li><a href="../004/output.html">MISSLEG蜜丝</a></li>
                    <li><a href="../004/output.html">奈丝写真</a></li>
                    <li><a href="../004/output.html">Kimoe激萌文化</a></li>
                    <li><a href="../004/output.html">KeLaGirls克拉女神</a></li>
                    <li><a href="../004/output.html">Girlt果团网</a></li>
                    <li><a href="../004/output.html">DISI第四印象</a></li>
                    <li><a href="../004/output.html">51MoDo</a></li>
                    <li><a href="../004/output.html">丝慕写真</a></li>
                    <li><a href="../004/output.html">制服の女生</a></li>
                    <li><a href="../004/output.html">最爱帆布鞋</a></li>
                    <li><a href="../004/output.html">妖精视觉</a></li>
                    <li><a href="../004/output.html">SHENSHI绅士</a></li>
                    <li><a href="../004/output.html">SunGirl阳光宝贝</a></li>
                    <li><a href="../004/output.html">LD零度摄影</a></li>
                    <li><a href="../004/output.html">喵写真</a></li>
                    <li><a href="../004/output.html">轻兰映画</a></li>
                    <li><a href="../004/output.html">GALLI嘉丽舞蹈生日记</a></li>
                    <li><a href="../004/output.html">兔玩映画</a></li>
                    <li><a href="../004/output.html">喵糖映画</a></li>
                    <li><a href="../004/output.html">风之领域</a></li>
                    <li><a href="../004/output.html">TGOD推女神</a></li>
                </ul>
            </div>
            <div class="nav-button-wrapper">
                <a href="#" class="nav-button">摄影机构</a>
                <ul class="sub-menu">
                    <li><a href="../004/output.html">XIUREN秀人网</a></li>
                    <li><a href="../004/output.html">XIAOYU语画界</a></li>
                    <li><a href="../004/output.html">IMISS爱蜜社</a></li>
                    <li><a href="../004/output.html">FEILN嗲囡囡</a></li>
                    <li><a href="../004/output.html">HuaYang花漾</a></li>
                    <li><a href="../004/output.html">MyGirl美媛馆</a></li>
                    <li><a href="../004/output.html">MiStar魅妍社</a></li>
                    <li><a href="../004/output.html">MFStar模范学院</a></li>
                    <li><a href="../004/output.html">YouMi尤蜜荟</a></li>
                    <li><a href="../004/output.html">CANDY糖果画报</a></li>
                    <li><a href="../004/output.html">YouWu尤物馆</a></li>
                    <li><a href="../004/output.html">DKGirl御女郎</a></li>
                    <li><a href="../004/output.html">HuaYan花の颜</a></li>
                    <li><a href="../004/output.html">XingYan星颜社</a></li>
                    <li><a href="../004/output.html">RUISG瑞丝馆</a></li>
                    <li><a href="../004/output.html">LeYuan星乐园</a></li>
                    <li><a href="../004/output.html">WingS影私荟</a></li>
                    <li><a href="../004/output.html">MintYe薄荷叶</a></li>
                    <li><a href="../004/output.html">UXING优星馆</a></li>
                    <li><a href="../004/output.html">TASTE顽味生活</a></li>
                </ul>
            </div>
            <div class="nav-button-wrapper">
                <a href="#" class="nav-button">帮助中心</a>
                <ul class="sub-menu">
                    <li><a href="../004/output.html">常见问题</a></li>
                    <li><a href="../004/output.html">电脑端解压教程</a></li>
                    <li><a href="../004/output.html">安卓端解压教程</a></li>
                    <li><a href="../004/output.html">手机端解压教程</a></li>
                    <li><a href="../004/output.html">联系客服</a></li>
                </ul>
            </div>
        </div>
        <div class="search-container">
            <input type="text" class="search-input" id="search-input" placeholder="搜索作品/摄影师">
            <img src="../images/search-icon.png" class="search-icon" alt="搜索">
        </div>
    </nav>
"""

# 定义三组表格的配置，你可以手动修改这里的 h1 标签内容和 txt 文本路径以及备注 txt 路径
table_configs = [
    {
        "h1_title": "B站UP",
        "txt_path": "名称/B站UP.txt",
        "remark_txt_path": "名称/B站UP - 备注.txt"
    },
    {
        "h1_title": "B站UP-收藏集",
        "txt_path": "名称/B站UP-收藏集.txt",
        "remark_txt_path": "名称/B站UP-收藏集 - 备注.txt"
    },
    {
        "h1_title": "充电哄睡",
        "txt_path": "名称/充电哄睡.txt",
        "remark_txt_path": "名称/充电哄睡 - 备注.txt"
    },
    {
        "h1_title": "机构合集",
        "txt_path": "名称/机构合集.txt",
        "remark_txt_path": "名称/机构合集 - 备注.txt"
    },
    {
        "h1_title": "Cosplay合集",
        "txt_path": "名称/Cosplay合集.txt",
        "remark_txt_path": "名称/Cosplay合集 - 备注.txt"
    },
    {
        "h1_title": "模特专辑",
        "txt_path": "名称/模特专辑.txt",
        "remark_txt_path": "名称/模特专辑 - 备注.txt"
    },
    {
        "h1_title": "微博抖音",
        "txt_path": "名称/微博抖音.txt",
        "remark_txt_path": "名称/微博抖音 - 备注.txt"
    },
    {
        "h1_title": "微密圈",
        "txt_path": "名称/微密圈.txt",
        "remark_txt_path": "名称/微密圈 - 备注.txt"
    },
    {
        "h1_title": "主播热舞",
        "txt_path": "名称/主播热舞.txt",
        "remark_txt_path": "名称/主播热舞 - 备注.txt"
    }
]

def generate_static_html():
    # 配置基础路径
    root_dir = os.getcwd()
    subpage_folder = os.path.join(root_dir, "004")  # 子网页输出文件夹路径

    # 创建输出目录
    os.makedirs(subpage_folder, exist_ok=True)

    html_file_name = "output.html"
    html_path = os.path.join(subpage_folder, html_file_name)

    # 生成表格内容
    table_content = ""
    for config in table_configs:
        h1_title = config["h1_title"]
        txt_path = os.path.join(root_dir, config["txt_path"])
        remark_txt_path = os.path.join(root_dir, config["remark_txt_path"])

        try:
            with open(txt_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            print(f"读取文件 {txt_path} 失败: {str(e)}")
            continue

        try:
            with open(remark_txt_path, "r", encoding="utf-8") as f:
                remarks = f.readlines()
        except Exception as e:
            print(f"读取备注文件 {remark_txt_path} 失败: {str(e)}")
            remarks = []

        # 生成表格的 HTML 代码
        table = f'<h1 id="{h1_title.replace(" ", "_")}" style="font-size: 32px; color: #111; text-align: center; text-shadow: 1px 1px 1px #ccc;">{h1_title}</h1>'
        table += '<table style="width: 80%; margin: 20px auto; border-collapse: collapse; text-align: center;">'
        table += '<thead><tr><th style="border: 1px solid #ccc; padding: 10px; font-size: 18px; color: #333;">编号</th><th style="border: 1px solid #ccc; padding: 10px; font-size: 18px; color: #333;">名称</th><th style="border: 1px solid #ccc; padding: 10px; font-size: 18px; color: #333;">备注</th></tr></thead>'
        table += '<tbody>'
        for i, line in enumerate(lines, start=1):
            line = line.strip()
            if i - 1 < len(remarks):
                remark = remarks[i - 1].strip()
            else:
                remark = ""
            table += f'<tr><td style="border: 1px solid #ccc; padding: 10px; font-size: 16px; color: #666;">{i}</td><td style="border: 1px solid #ccc; padding: 10px; font-size: 16px; color: #666;">{line}</td><td style="border: 1px solid #ccc; padding: 10px; font-size: 16px; color: #666;">{remark}</td></tr>'
        table += '</tbody></table>'
        table_content += table

    # 生成 HTML 内容，添加外部 CSS 和 JavaScript 引用
    html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>详细列表 - 表格展示</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    {nav_template.strip()}
    
    <main class="detail-content">
        {table_content}
    </main>

    <footer class="detail-footer">
        <p>&copy; 2024 摄影写真官网. All rights reserved.</p>
    </footer>

    <script src="../js/script.js"></script>
</body>
</html>
    """

    # 写入 HTML 文件
    try:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content.strip())
        print(f"成功生成：{html_path}")
    except Exception as e:
        print(f"写入文件 {html_path} 失败: {str(e)}")

    print(f"\n子网页已生成到目录：{subpage_folder}")

if __name__ == "__main__":
    generate_static_html()