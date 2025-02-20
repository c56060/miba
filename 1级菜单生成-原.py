import os

def generate_static_html():
    # 配置基础路径
    root_dir = os.getcwd()
    output_folder = os.path.join(root_dir, "001")  # 输出文件夹路径
    output_file = os.path.join(output_folder, "000.html")  # 生成到001文件夹

    # 创建输出目录（如果不存在）
    os.makedirs(output_folder, exist_ok=True)

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
            <input type="text" class="search-input" placeholder="搜索作品/摄影师">
            <img src="../images/search-icon.png" class="search-icon" alt="搜索">
        </div>
    </nav>
    """

    # 生成图片卡片
    def generate_card(image_type, number):
        return f"""
        <div class="photo-card photography-card">
            <img data-src="../images/{image_type}{number}.jpg" alt="摄影作品" loading="lazy">
            <div class="overlay">
                <h3>精选推荐</h3>
                <p></p>
            </div>
        </div>
        """.strip()

    # 自定义样式
    custom_style = """
<style>
    /* 图片卡片标题样式 */
    .photo-card h3 {
        font-size: 26px;                /* 字体大小-大标题尺寸 */
        color: #FFD700;                 /* 字体颜色-金色增强视觉效果 */
        margin: 0 0 15px 0;             /* 外边距-下边距15px创建呼吸空间 */
        position: relative;             /* 定位方式-相对定位基准 */
        top: 20%;                       /* 垂直位置-从默认位置下移20% */
        text-align: center;             /* 对齐方式-水平居中 */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8); /* 文字阴影-增强立体感 */
        font-weight: 600;               /* 字重-半粗体突出显示 */
    }

    /* 摄影师信息样式 */
    .photo-card p {
        font-size: 16px;                /* 字体大小-适中阅读尺寸 */
        color: #F0F8FF;                 /* 字体颜色-淡蓝色提升可读性 */
        margin: 10px 0;                 /* 外边距-上下10px间隔 */
        position: absolute;             /* 定位方式-绝对定位 */
        bottom: 25px;                   /* 底部距离-距容器底部25px */
        left: 50%;                      /* 水平定位-左侧50%位置 */
        transform: translateX(-50%);    /* 位置修正-水平居中对齐 */
        font-family: 'Microsoft YaHei', sans-serif; /* 字体-优先使用微软雅黑 */
        white-space: nowrap;            /* 文本处理-禁止换行 */
    }

    /* 图片覆盖层样式 */
    .overlay {
        padding: 25px;                  /* 内边距-四周25px留白 */
        background: linear-gradient(180deg, 
            rgba(0,0,0,0) 0%,          /* 渐变起点-完全透明 */
            rgba(0,0,0,0.8) 100%);     /* 渐变终点-80%透明度黑色 */
        height: 80%;                   /* 高度-撑满父容器 */
        box-sizing: border-box;         /* 盒模型-包含padding在内的宽度计算 */
        display: flex;                  /* 布局方式-弹性盒子 */
        flex-direction: column;         /* 排列方向-垂直列布局 */
        justify-content: flex-end;      /* 对齐方式-内容底部对齐 */
        
        /* 建议补充 */
        position: relative;             /* 定位基准-为绝对定位子元素提供参照 */
        min-height: 150px;              /* 最小高度-保证文字显示区域 */
    }
</style>
    """

    # 构建完整页面
    html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>摄影写真官网</title>
    <link rel="stylesheet" href="../css/style.css">
    {custom_style.strip()}
</head>
<body>
    {nav_template.strip()}
    
    <main class="main-content">
        <!-- COSER作品区 -->
        <h2 class="section-title">-写真合集- 推荐</h2>
        <div class="grid-container">
            {"".join([generate_card('A', i) for i in range(1,9)])}
        </div>

        <!-- 摄影作品区 -->
        <h2 class="section-title">-精选名站- 推荐</h2>
        <div class="grid-container">
            {"".join([generate_card('B', i) for i in range(1,9)])}
        </div>
        
        <!-- 摄影作品区 -->
        <h2 class="section-title">-摄影机构- 推荐</h2>
        <div class="grid-container">
            {"".join([generate_card('C', i) for i in range(1,9)])}
        </div>
    </main>

    <script src="../js/script.js"></script>
</body>
</html>
    """

    # 写入文件
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"静态HTML已生成到目录：{output_file}")

if __name__ == "__main__":
    generate_static_html()