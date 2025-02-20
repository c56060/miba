import os
import re

def generate_static_html():
    # 配置基础路径
    root_dir = os.getcwd()
    detail_folder = os.path.join(root_dir, "详细目录")  # 详细信息文件夹路径
    subpage_folder = os.path.join(root_dir, "003")   # 子网页输出文件夹路径

    # 创建输出目录
    os.makedirs(subpage_folder, exist_ok=True)

    # 完整导航栏模板（保留所有原始菜单结构）
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
    """

    # 直接指定要读取的文件路径
    detail_file = "ROSI写真.txt"
    subpage_title = os.path.splitext(detail_file)[0]
    txt_path = os.path.join(detail_folder, detail_file)
    # 生成 HTML 文件名，使用 TXT 文件名
    html_file_name = f"{subpage_title}.html"
    html_path = os.path.join(subpage_folder, html_file_name)

    # 读取文件内容
    try:
        with open(txt_path, "r", encoding="utf-8") as f:
            detail_content = f.read()
    except Exception as e:
        print(f"读取文件 {detail_file} 失败: {str(e)}")
        return

    # 生成 HTML 内容
    html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{subpage_title} - 详细信息</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    {nav_template.strip()}
    
    <main class="detail-content">
        <div class="content-container">
            <h1 class="detail-title">{subpage_title}</h1>
            <div class="notice-box">
                <p>目录更新可能不及时，具体以实际资源为准</p>
            </div>
            <pre class="detail-text">{detail_content}</pre>
        </div>
    </main>

    <footer class="detail-footer">
        <p>&copy; 2024 摄影写真官网. All rights reserved.</p>
    </footer>
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