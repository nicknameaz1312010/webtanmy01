html = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tân Mỹ Group - Kiến Tạo Giá Trị Bền Vững Từ Nhôm Việt</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        tailwind.config = {
            theme: {
                fontFamily: { sans: ['Inter', 'sans-serif'] },
                extend: {
                    colors: { brandBlue: '#014289', brandRed: '#ED1C24', darkBg: '#0f172a' }
                }
            }
        }
    </script>
    <style>
        html { scroll-behavior: smooth; }
        .hero-mask { background: linear-gradient(90deg, rgba(1,66,137,0.7) 0%, rgba(15,23,42,0.5) 100%); }
        .glass-nav { background: rgba(255,255,255,0.93); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); }
        .scroll-nav { transition: all 0.3s ease; }
        .nav-scrolled { box-shadow: 0 4px 30px rgba(0,0,0,0.08) !important; }
        .pulse-ring { animation: pulseRing 2.2s ease-in-out infinite; }
        @keyframes pulseRing { 0% { box-shadow: 0 0 0 0 rgba(255,255,255,0.55); } 70% { box-shadow: 0 0 0 24px rgba(255,255,255,0); } 100% { box-shadow: 0 0 0 0 rgba(255,255,255,0); } }
        .section-line { width: 60px; height: 4px; background: #ED1C24; border-radius: 2px; margin: 0.75rem auto 0; }
        .footer-bar { width: 3px; height: 18px; background: #014289; border-radius: 2px; display: inline-block; margin-right: 8px; vertical-align: middle; }
        .project-card img { transition: transform 0.6s ease; }
        .project-card:hover img { transform: scale(1.1); }
        .process-arrow { display: flex; align-items: center; justify-content: center; font-size: 1.5rem; color: #d1d5db; }
        @media (max-width: 1023px) { .process-arrow { display: none; } }
        .float-btn { transition: all 0.3s ease; }
        .float-btn:hover { transform: scale(1.1); }
        .float-panel { transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1); transform-origin: bottom right; }
        .float-panel.show { opacity: 1; visibility: visible; transform: scale(1); }
        .float-panel.hide { opacity: 0; visibility: hidden; transform: scale(0.8); }
    </style>
</head>
<body class="bg-gray-50 text-slate-800 font-sans antialiased overflow-x-hidden">

<!-- KHỐI 1: NAVIGATION BAR -->
<header id="navbar" class="scroll-nav fixed top-0 left-0 w-full z-50 glass-nav">
    <div class="container mx-auto px-4 py-3 flex items-center justify-between">
        <div class="flex items-center space-x-3">
            <svg viewBox="0 0 550 120" class="h-12 w-auto" xmlns="http://www.w3.org/2000/svg">
                <!-- 1. KHỐI BIỂU TƯỢNG HÌNH VUÔNG (ICON BÊN TRÁI) -->
                <g transform="translate(5, 5)">
                    <rect width="110" height="110" fill="white" stroke="#014289" stroke-width="4"/>
                    <path d="M 4 80 Q 55 105 106 80 L 106 106 L 4 106 Z" fill="#014289"/>
                    <path d="M 4 106 Q 55 90 106 106 Z" fill="white"/>
                    <path d="M 55 10 L 25 90 Q 55 75 85 90 Z" fill="#F1C40F"/>
                    <path d="M 35 35 L 75 35 M 55 35 L 55 75" stroke="#ED1C24" stroke-width="8" stroke-linecap="square"/>
                    <text x="36" y="75" font-family="sans-serif" font-weight="900" font-size="34" fill="#ED1C24">M</text>
                </g>
                <!-- 2. PHẦN CHỮ THƯƠNG HIỆU "TANMY" -->
                <text x="135" y="75" font-family="sans-serif" font-weight="900" font-size="82" fill="#014289" letter-spacing="-2">TANMY</text>
                <!-- 3. PHẦN SLOGAN -->
                <text x="138" y="108" font-family="sans-serif" font-weight="500" font-size="28" fill="#ED1C24">Trường tồn cùng thời gian</text>
            </svg>
        </div>

        <nav class="hidden lg:flex items-center space-x-6 text-xs font-black uppercase tracking-wider text-slate-700">
            <a href="#" class="text-brandBlue border-b-2 border-brandBlue pb-1">Trang chủ</a>
            <a href="#about" class="hover:text-brandBlue transition">Giới thiệu</a>
            <a href="#products" class="hover:text-brandBlue transition">Nhôm Tân Mỹ</a>
            <a href="#products" class="hover:text-brandBlue transition">Gia dụng Tân Mỹ</a>
            <a href="#projects" class="hover:text-brandBlue transition">Dự án</a>
            <a href="#news" class="hover:text-brandBlue transition">Tin tức</a>
            <a href="#contact" class="hover:text-brandBlue transition">Liên hệ</a>
        </nav>

        <div class="flex items-center space-x-4">
            <button class="text-slate-600 hover:text-brandBlue transition"><i class="fa-solid fa-magnifying-glass"></i></button>
            <div class="flex items-center space-x-1 text-[10px] font-black border border-gray-300 px-2 py-0.5 rounded bg-gray-50">
                <span class="text-brandBlue">VI</span><span class="text-gray-300">|</span><span class="text-gray-400">EN</span>
            </div>
            <button id="mobile-menu-btn" class="lg:hidden text-slate-700 text-xl focus:outline-none"><i class="fa-solid fa-bars"></i></button>
        </div>
    </div>

    <div id="mobile-menu" class="hidden lg:hidden bg-white border-t border-gray-100 px-4 py-4 space-y-3 font-bold text-sm shadow-inner">
        <a href="#" class="block text-brandBlue py-1.5 border-b border-gray-50">Trang chủ</a>
        <a href="#about" class="block text-slate-700 hover:text-brandBlue py-1.5 border-b border-gray-50">Giới thiệu</a>
        <a href="#products" class="block text-slate-700 hover:text-brandBlue py-1.5 border-b border-gray-50">Nhôm Tân Mỹ</a>
        <a href="#products" class="block text-slate-700 hover:text-brandBlue py-1.5 border-b border-gray-50">Gia dụng Tân Mỹ</a>
        <a href="#projects" class="block text-slate-700 hover:text-brandBlue py-1.5 border-b border-gray-50">Dự án</a>
        <a href="#news" class="block text-slate-700 hover:text-brandBlue py-1.5 border-b border-gray-50">Tin tức</a>
        <a href="#contact" class="block text-slate-700 hover:text-brandBlue py-1.5">Liên hệ</a>
    </div>
</header>

<!-- KHỐI 2: HERO BANNER -->
<section class="relative min-h-screen flex items-center bg-cover bg-center pt-20" style="background-image: url('https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1600&q=85');">
    <div class="absolute inset-0 hero-mask"></div>

    <div class="container mx-auto px-4 z-10 w-full grid lg:grid-cols-12 gap-8 items-stretch min-h-screen py-20">
        <div class="lg:col-span-7 flex flex-col justify-center space-y-6 text-white max-w-2xl" data-aos="fade-right">
            <!-- Khối tiêu đề 3 dòng cách đều -->
            <div class="flex flex-col space-y-4 text-4xl sm:text-6xl lg:text-7xl font-black uppercase tracking-tight leading-none">
                <span>TÂN MỸ</span>
                <span class="text-yellow-400">KIẾN TẠO GIÁ TRỊ</span>
                <span>BỀN VỮNG TỪ NHÔM VIỆT</span>
            </div>

            <!-- Khối mô tả và nút bấm được di chuyển dịch xuống dưới -->
            <div>
                <p class="text-xs sm:text-sm md:text-base text-gray-100 max-w-xl font-normal leading-relaxed opacity-95">
                    Nhà sản xuất nhôm định hình, sản phẩm gia dụng và giải pháp vật liệu xây dựng hàng đầu Việt Nam.
                </p>
                <div class="flex flex-wrap gap-4 mt-6">
                    <a href="#" class="bg-brandBlue text-white font-extrabold text-[11px] tracking-wider px-7 py-4 rounded shadow-lg uppercase">Khám phá nhà máy</a>
                    <a href="#contact" class="border-2 border-white text-white font-extrabold text-[11px] tracking-wider px-6 py-3.5 rounded uppercase">Liên hệ tư vấn</a>
                </div>
            </div>
        </div>

        <div class="lg:col-span-5 flex justify-start lg:justify-end items-end pb-8 lg:pb-12" data-aos="fade-left">
            <div class="flex items-center space-x-3 cursor-pointer group bg-black/20 p-3 rounded-full backdrop-blur-sm hover:bg-black/30 transition">
                <div class="w-16 h-16 rounded-full bg-white flex items-center justify-center shadow-lg transition duration-300 group-hover:scale-105 pulse-ring">
                    <i class="fa-solid fa-play text-lg text-brandBlue ml-0.5"></i>
                </div>
                <span class="text-white font-black tracking-wider text-xs sm:text-sm uppercase pr-3">Xem Video Giới Thiệu</span>
            </div>
        </div>
    </div>
</section>

<!-- KHỐI 3: STRATEGIC METRICS -->
<section class="relative z-20 -mt-16 container mx-auto px-4">
    <div class="bg-white shadow-[0_15px_40px_rgba(0,0,0,0.08)] rounded-xl p-6 md:p-8 grid grid-cols-2 md:grid-cols-5 gap-6 text-center border border-gray-100/50">
        <div class="p-2 space-y-1">
            <div class="text-2xl md:text-3xl font-black text-brandBlue" data-aos="zoom-in" data-aos-delay="0">25+</div>
            <div class="text-[10px] md:text-xs text-gray-500 font-extrabold uppercase tracking-wider">Năm kinh nghiệm</div>
        </div>
        <div class="p-2 space-y-1 pt-4 md:pt-2">
            <div class="text-2xl md:text-3xl font-black text-brandBlue" data-aos="zoom-in" data-aos-delay="100">50.000+</div>
            <div class="text-[10px] md:text-xs text-gray-500 font-extrabold uppercase tracking-wider">Tấn nhôm mỗi năm</div>
        </div>
        <div class="p-2 space-y-1 pt-4 md:pt-2">
            <div class="text-2xl md:text-3xl font-black text-brandBlue" data-aos="zoom-in" data-aos-delay="200">1.000+</div>
            <div class="text-[10px] md:text-xs text-gray-500 font-extrabold uppercase tracking-wider">Đại lý & đối tác</div>
        </div>
        <div class="p-2 space-y-1 pt-4 md:pt-2">
            <div class="text-2xl md:text-3xl font-black text-brandBlue" data-aos="zoom-in" data-aos-delay="300">63</div>
            <div class="text-[10px] md:text-xs text-gray-500 font-extrabold uppercase tracking-wider">Tỉnh thành phân phối</div>
        </div>
        <div class="p-2 space-y-1 pt-4 md:pt-2 flex flex-col items-center justify-center">
            <i class="fa-solid fa-earth-asia text-xl text-brandBlue mb-1" data-aos="zoom-in" data-aos-delay="400"></i>
            <div class="text-[10px] md:text-xs text-gray-500 font-extrabold uppercase tracking-wider">Xuất khẩu nhiều quốc gia</div>
        </div>
    </div>
</section>

<!-- KHỐI 4: ABOUT -->
<section id="about" class="py-20 bg-white">
    <div class="container mx-auto px-4">
        <div class="text-center mb-14" data-aos="fade-up">
            <h2 class="text-3xl lg:text-5xl font-black text-brandBlue uppercase tracking-tight">VỀ TÂN MỸ GROUP</h2>
            <div class="section-line"></div>
            <p class="text-gray-500 mt-4 max-w-2xl mx-auto text-sm">Tiên phong trong ngành nhôm định hình và gia dụng, cam kết chất lượng và đổi mới không ngừng.</p>
        </div>
        <div class="grid lg:grid-cols-2 gap-14 items-center">
            <div data-aos="fade-right">
                <img src="https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?w=800&q=85" alt="Nhà máy Tân Mỹ" class="rounded-2xl shadow-xl w-full">
            </div>
            <div data-aos="fade-left">
                <p class="text-gray-600 leading-relaxed mb-6 text-sm">Tân Mỹ Group thành lập từ năm 1999, là một trong những doanh nghiệp hàng đầu Việt Nam trong lĩnh vực sản xuất nhôm định hình, bồn nước inox, bồn nhựa, bể tự hoại Septic, chậu rửa inox và máy nước nóng năng lượng mặt trời.</p>
                <p class="text-gray-600 leading-relaxed mb-8 text-sm">Với hệ thống nhà máy hiện đại tại Việt Nam, Tân Mỹ cung cấp các sản phẩm chất lượng cao, đáp ứng tiêu chuẩn quốc tế, phục vụ thị trường trong nước và xuất khẩu sang nhiều quốc gia.</p>
                <div class="grid grid-cols-3 gap-5 mb-8">
                    <div class="bg-gray-50 rounded-xl p-5 text-center shadow-sm border border-gray-100"><div class="text-2xl font-black text-brandBlue">25+</div><div class="text-xs text-gray-500 font-bold mt-1">Năm kinh nghiệm</div></div>
                    <div class="bg-gray-50 rounded-xl p-5 text-center shadow-sm border border-gray-100"><div class="text-2xl font-black text-brandBlue">50K+</div><div class="text-xs text-gray-500 font-bold mt-1">Tấn nhôm/năm</div></div>
                    <div class="bg-gray-50 rounded-xl p-5 text-center shadow-sm border border-gray-100"><div class="text-2xl font-black text-brandBlue">1K+</div><div class="text-xs text-gray-500 font-bold mt-1">Đại lý toàn quốc</div></div>
                </div>
                <a href="#contact" class="inline-flex items-center gap-2 bg-brandBlue text-white font-bold px-6 py-3.5 rounded-lg hover:opacity-90 transition text-sm"><i class="fa-solid fa-handshake"></i> Liên hệ hợp tác</a>
            </div>
        </div>
    </div>
</section>

<!-- KHỐI 5: TWO PRODUCT CARDS -->
<section id="products" class="py-20 bg-gray-50">
    <div class="container mx-auto px-4">
        <div class="grid lg:grid-cols-2 gap-8">
            <div class="relative rounded-2xl overflow-hidden" data-aos="fade-right" style="background:linear-gradient(135deg,#1e293b 0%,#111827 100%)">
                <div class="p-8 lg:p-12 relative z-10">
                    <div class="text-xs font-black tracking-[0.25em] text-green-400 mb-3 uppercase">Thương hiệu ZAVA</div>
                    <h3 class="text-2xl lg:text-4xl font-black text-white mb-8 leading-tight uppercase">Nhôm Tân Mỹ - ZAVA</h3>
                    <ul class="space-y-4 mb-10">
                        <li class="flex items-start gap-3 text-gray-300 text-sm"><i class="fa-solid fa-check-circle text-green-400 mt-0.5"></i> Hệ nhôm kiến trúc ZAVA cao cấp</li>
                        <li class="flex items-start gap-3 text-gray-300 text-sm"><i class="fa-solid fa-check-circle text-green-400 mt-0.5"></i> Nhôm thanh định hình công nghiệp</li>
                        <li class="flex items-start gap-3 text-gray-300 text-sm"><i class="fa-solid fa-check-circle text-green-400 mt-0.5"></i> Hệ nhôm xây dựng tiêu chuẩn</li>
                    </ul>
                    <a href="#" class="inline-flex items-center gap-2 bg-white text-brandBlue font-black px-6 py-3.5 rounded-xl hover:bg-gray-100 transition text-sm">Khám phá ngành nhôm <i class="fa-solid fa-arrow-right"></i></a>
                </div>
                <div class="absolute bottom-0 right-0 w-44 h-44 lg:w-52 lg:h-52 overflow-hidden opacity-30 rounded-tl-3xl">
                    <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=400&q=85" alt="Cửa kính" class="w-full h-full object-cover">
                </div>
            </div>
            <div class="relative rounded-2xl overflow-hidden" data-aos="fade-left" style="background:linear-gradient(135deg,#eff6ff 0%,#f3f4f6 100%)">
                <div class="p-8 lg:p-12 relative z-10">
                    <div class="text-xs font-black tracking-[0.25em] text-brandBlue mb-3 uppercase">Gia dụng cao cấp</div>
                    <h3 class="text-2xl lg:text-4xl font-black text-brandBlue mb-8 leading-tight uppercase">Gia dụng Tân Mỹ</h3>
                    <ul class="space-y-4 mb-10">
                        <li class="flex items-start gap-3 text-gray-700 text-sm"><i class="fa-solid fa-check-circle text-brandBlue mt-0.5"></i> Bồn nước Inox</li>
                        <li class="flex items-start gap-3 text-gray-700 text-sm"><i class="fa-solid fa-check-circle text-brandBlue mt-0.5"></i> Bồn nhựa đa năng</li>
                        <li class="flex items-start gap-3 text-gray-700 text-sm"><i class="fa-solid fa-check-circle text-brandBlue mt-0.5"></i> Bể phốt thông minh SEPTIC</li>
                        <li class="flex items-start gap-3 text-gray-700 text-sm"><i class="fa-solid fa-check-circle text-brandBlue mt-0.5"></i> Máy nước nóng NLMT</li>
                    </ul>
                    <a href="#" class="inline-flex items-center gap-2 bg-brandBlue text-white font-black px-6 py-3.5 rounded-xl hover:opacity-90 transition text-sm">Khám phá sản phẩm <i class="fa-solid fa-arrow-right"></i></a>
                </div>
                <div class="absolute bottom-0 right-0 w-40 h-40 lg:w-48 lg:h-48 overflow-hidden opacity-25 rounded-tl-3xl">
                    <img src="https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=400&q=85" alt="Bồn nước" class="w-full h-full object-cover">
                </div>
            </div>
        </div>
    </div>
</section>

<!-- KHỐI 6: PRODUCTION PROCESS -->
<section class="py-20 bg-white">
    <div class="container mx-auto px-4">
        <div class="text-center mb-16" data-aos="fade-up">
            <h2 class="text-3xl lg:text-5xl font-black text-brandBlue uppercase tracking-tight">Quy trình sản xuất hiện đại</h2>
            <div class="section-line"></div>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6 lg:gap-0 relative">
            <div class="text-center px-3" data-aos="fade-up" data-aos-delay="0">
                <div class="w-14 h-14 rounded-full bg-brandBlue text-white flex items-center justify-center text-xl font-black mx-auto mb-5 shadow-lg">1</div>
                <div class="rounded-xl overflow-hidden mb-4 shadow-md"><img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400&q=85" alt="Phôi nhôm" class="w-full h-36 object-cover"></div>
                <h4 class="font-black text-gray-900 mb-2 text-sm">Nguyên liệu Billet</h4>
                <p class="text-xs text-gray-500 leading-relaxed">Hợp kim nhôm nhập khẩu đạt chất lượng tiêu chuẩn quốc tế.</p>
            </div>
            <div class="process-arrow"><i class="fa-solid fa-chevron-right"></i></div>
            <div class="text-center px-3" data-aos="fade-up" data-aos-delay="100">
                <div class="w-14 h-14 rounded-full bg-brandBlue text-white flex items-center justify-center text-xl font-black mx-auto mb-5 shadow-lg">2</div>
                <div class="rounded-xl overflow-hidden mb-4 shadow-md"><img src="https://images.unsplash.com/photo-1581092795360-fd1ca04f0952?w=400&q=85" alt="Máy đùn" class="w-full h-36 object-cover"></div>
                <h4 class="font-black text-gray-900 mb-2 text-sm">Hệ thống đùn ép</h4>
                <p class="text-xs text-gray-500 leading-relaxed">Máy đùn ép áp lực cao tạo hình thanh nhôm chính xác.</p>
            </div>
            <div class="process-arrow"><i class="fa-solid fa-chevron-right"></i></div>
            <div class="text-center px-3" data-aos="fade-up" data-aos-delay="200">
                <div class="w-14 h-14 rounded-full bg-brandBlue text-white flex items-center justify-center text-xl font-black mx-auto mb-5 shadow-lg">3</div>
                <div class="rounded-xl overflow-hidden mb-4 shadow-md"><img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400&q=85" alt="Sơn tĩnh điện" class="w-full h-36 object-cover"></div>
                <h4 class="font-black text-gray-900 mb-2 text-sm">Xử lý sơn tĩnh điện</h4>
                <p class="text-xs text-gray-500 leading-relaxed">Phủ bề mặt hạt sơn bám dính chắc chắn, chống oxy hóa.</p>
            </div>
            <div class="process-arrow"><i class="fa-solid fa-chevron-right"></i></div>
            <div class="text-center px-3" data-aos="fade-up" data-aos-delay="300">
                <div class="w-14 h-14 rounded-full bg-brandBlue text-white flex items-center justify-center text-xl font-black mx-auto mb-5 shadow-lg">4</div>
                <div class="rounded-xl overflow-hidden mb-4 shadow-md"><img src="https://images.unsplash.com/photo-1581092795360-fd1ca04f0952?w=400&q=85" alt="Kiểm định" class="w-full h-36 object-cover"></div>
                <h4 class="font-black text-gray-900 mb-2 text-sm">Kiểm định chất lượng</h4>
                <p class="text-xs text-gray-500 leading-relaxed">Đội ngũ QA/QC đo đạc thông số kỹ thuật nghiêm ngặt.</p>
            </div>
            <div class="process-arrow"><i class="fa-solid fa-chevron-right"></i></div>
            <div class="text-center px-3" data-aos="fade-up" data-aos-delay="400">
                <div class="w-14 h-14 rounded-full bg-brandBlue text-white flex items-center justify-center text-xl font-black mx-auto mb-5 shadow-lg">5</div>
                <div class="rounded-xl overflow-hidden mb-4 shadow-md"><img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400&q=85" alt="Đóng gói" class="w-full h-36 object-cover"></div>
                <h4 class="font-black text-gray-900 mb-2 text-sm">Thành phẩm đóng gói</h4>
                <p class="text-xs text-gray-500 leading-relaxed">Đóng bọc màng bảo vệ và lưu kho xuất xưởng phân phối.</p>
            </div>
        </div>
    </div>
</section>

<!-- KHỐI 7: CERTIFICATIONS + PROJECTS -->
<section id="projects" class="py-20 bg-gray-50">
    <div class="container mx-auto px-4">
        <div class="flex flex-col lg:flex-row gap-10 lg:gap-14">
            <div class="lg:w-1/3" data-aos="fade-right">
                <h3 class="text-2xl lg:text-3xl font-black text-brandBlue mb-4 uppercase tracking-tight">Chứng nhận chất lượng</h3>
                <p class="text-sm text-gray-500 mb-8 leading-relaxed">Các chứng chỉ và giải thưởng khẳng định chất lượng sản phẩm dịch vụ của Tân Mỹ Group.</p>
                <div class="grid grid-cols-2 gap-4">
                    <div class="bg-white border border-gray-200 rounded-xl p-5 text-center shadow-sm hover:shadow-md transition"><div class="text-sm font-black text-brandBlue leading-tight">ISO<br>9001:2015</div><div class="text-[10px] text-gray-400 font-semibold mt-2">Quản lý chất lượng</div></div>
                    <div class="bg-white border border-gray-200 rounded-xl p-5 text-center shadow-sm hover:shadow-md transition"><div class="text-sm font-black text-brandBlue leading-tight">QUATEST<br>3</div><div class="text-[10px] text-gray-400 font-semibold mt-2">Kiểm định CL</div></div>
                    <div class="bg-white border border-gray-200 rounded-xl p-5 text-center shadow-sm hover:shadow-md transition"><div class="text-sm font-black text-brandBlue leading-tight">QUALI<br>COAT</div><div class="text-[10px] text-gray-400 font-semibold mt-2">Sơn tĩnh điện</div></div>
                    <div class="bg-white border border-gray-200 rounded-xl p-5 text-center shadow-sm hover:shadow-md transition"><div class="text-sm font-black text-brandBlue leading-tight">EURO<br>TIÊU CHUẨN</div><div class="text-[10px] text-gray-400 font-semibold mt-2">Xuất khẩu Âu</div></div>
                </div>
            </div>
            <div class="lg:w-2/3" data-aos="fade-left">
                <div class="flex items-center justify-between mb-8">
                    <h3 class="text-2xl lg:text-3xl font-black text-brandBlue uppercase tracking-tight">Dự án tiêu biểu</h3>
                    <a href="#" class="text-sm font-bold text-brandBlue flex items-center gap-1 hover:underline">XEM TẤT CẢ <i class="fa-solid fa-arrow-right text-xs"></i></a>
                </div>
                <div class="grid grid-cols-2 gap-6">
                    <div><div class="project-card relative rounded-xl overflow-hidden group cursor-pointer"><img src="https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=400&q=85" alt="Vinhomes" class="w-full h-48 lg:h-56 object-cover"><div class="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent opacity-0 group-hover:opacity-100 transition"></div></div><div class="text-sm font-bold text-gray-800 mt-3 tracking-wide uppercase">Vinhomes Ocean Park</div></div>
                    <div><div class="project-card relative rounded-xl overflow-hidden group cursor-pointer"><img src="https://images.unsplash.com/photo-1486325212027-8081e485255e?w=400&q=85" alt="Sunshine" class="w-full h-48 lg:h-56 object-cover"><div class="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent opacity-0 group-hover:opacity-100 transition"></div></div><div class="text-sm font-bold text-gray-800 mt-3 tracking-wide uppercase">Sunshine City</div></div>
                    <div><div class="project-card relative rounded-xl overflow-hidden group cursor-pointer"><img src="https://images.unsplash.com/photo-1534430480872-3498386e7856?w=400&q=85" alt="FLC" class="w-full h-48 lg:h-56 object-cover"><div class="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent opacity-0 group-hover:opacity-100 transition"></div></div><div class="text-sm font-bold text-gray-800 mt-3 tracking-wide uppercase">FLC Quy Nhơn Resort</div></div>
                    <div><div class="project-card relative rounded-xl overflow-hidden group cursor-pointer"><img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=400&q=85" alt="Biệt thự" class="w-full h-48 lg:h-56 object-cover"><div class="absolute inset-0 bg-gradient-to-t from-black/40 to-transparent opacity-0 group-hover:opacity-100 transition"></div></div><div class="text-sm font-bold text-gray-800 mt-3 tracking-wide uppercase">Biệt thự cao cấp</div></div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- KHỐI 8: NEWS -->
<section id="news" class="py-20 bg-white">
    <div class="container mx-auto px-4">
        <div class="flex items-center gap-5 mb-12" data-aos="fade-up">
            <h2 class="text-3xl lg:text-4xl font-black text-brandBlue uppercase tracking-tight">Tin tức nổi bật</h2>
            <div class="flex-1 h-px bg-gray-300"></div>
        </div>
        <div class="grid lg:grid-cols-4 gap-6" data-aos="zoom-in">
            <div class="lg:col-span-2 relative rounded-2xl overflow-hidden group cursor-pointer h-96 lg:h-[440px]">
                <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=900&q=85" alt="Nhà máy" class="w-full h-full object-cover group-hover:scale-105 transition duration-700">
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/10 to-transparent"></div>
                <div class="absolute bottom-0 left-0 right-0 p-6 lg:p-8">
                    <span class="inline-block bg-brandRed text-white text-xs font-bold px-3 py-1.5 rounded mb-4">20/05/2024</span>
                    <h3 class="text-white font-black text-lg lg:text-2xl leading-snug max-w-lg">Tân Mỹ khánh thành dây chuyền sơn tĩnh điện đứng công nghệ cao hiện đại</h3>
                    <a href="#" class="text-white/80 text-sm font-bold mt-4 inline-flex items-center gap-1 hover:text-white transition">Xem chi tiết <i class="fa-solid fa-arrow-right"></i></a>
                </div>
            </div>
            <div class="flex flex-col gap-5">
                <div class="bg-gray-50 rounded-xl p-5 flex gap-4 shadow-sm border border-gray-100">
                    <img src="https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=150&q=85" alt="Tin tức" class="w-24 h-24 rounded-xl object-cover flex-shrink-0">
                    <div><span class="text-[0.7rem] text-gray-400 font-semibold tracking-wider">15/05/2024</span><h4 class="text-sm font-bold text-gray-800 mt-1.5 leading-snug">Xu hướng kiến trúc nhôm kính 2024 với ZAVA cao cấp</h4></div>
                </div>
                <div class="bg-gray-50 rounded-xl p-5 flex gap-4 shadow-sm border border-gray-100">
                    <img src="https://images.unsplash.com/photo-1486325212027-8081e485255e?w=150&q=85" alt="Tin tức" class="w-24 h-24 rounded-xl object-cover flex-shrink-0">
                    <div><span class="text-[0.7rem] text-gray-400 font-semibold tracking-wider">10/05/2024</span><h4 class="text-sm font-bold text-gray-800 mt-1.5 leading-snug">Tân Mỹ Group tham gia triển lãm Vietbuild Hà Nội 2024</h4></div>
                </div>
            </div>
            <div class="relative rounded-2xl overflow-hidden" style="background:#0f172a">
                <div class="p-8 lg:p-10 flex flex-col items-center justify-center text-center h-full min-h-[320px]">
                    <div class="text-white/10 text-7xl font-black leading-none mb-8 tracking-wider uppercase">TÂN<br>MỸ</div>
                    <h3 class="text-white font-black text-2xl leading-tight mb-6 uppercase">Hành trình<br>phát triển</h3>
                    <a href="#" class="inline-flex items-center gap-2 bg-brandRed text-white font-bold px-6 py-3.5 rounded-xl hover:opacity-90 transition text-sm tracking-wide shadow-lg"><i class="fa-solid fa-play"></i> Xem Video</a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- KHỐI 9: CHĂM SÓC KHÁCH HÀNG (CHAT WIDGET) -->
<section class="bg-[#f8fafc] py-14 border-t border-gray-200">
    <div class="container mx-auto px-4">
        <div class="max-w-4xl mx-auto">
            <div class="bg-white rounded-2xl shadow-lg overflow-hidden border border-gray-100">
                <div class="bg-brandBlue p-5 flex items-center gap-4">
                    <div class="w-12 h-12 rounded-full bg-white flex items-center justify-center flex-shrink-0 shadow-md overflow-hidden">
                        <img src="https://tawk.link/5865e574e7588f12124ea003/var/chat_bubble/15fad47ba0fc899390d661b427f7c12f8eb6d458" alt="Tân Mỹ" class="w-full h-full object-cover">
                    </div>
                    <div>
                        <h3 class="text-white font-black text-lg">Chăm sóc khách hàng</h3>
                        <p class="text-blue-200 text-xs">Tân Mỹ Group luôn sẵn sàng hỗ trợ bạn</p>
                    </div>
                    <div class="ml-auto hidden sm:flex items-center gap-3">
                        <span class="flex items-center gap-1.5 text-blue-200 text-xs"><span class="w-2 h-2 rounded-full bg-green-400 inline-block animate-pulse"></span> Đang hoạt động</span>
                    </div>
                </div>
                <div class="p-6 lg:p-8">
                    <div class="flex items-start gap-4 mb-6">
                        <div class="w-10 h-10 rounded-full bg-brandBlue/10 flex items-center justify-center flex-shrink-0 overflow-hidden">
                            <img src="https://tawk.link/5865e574e7588f12124ea003/var/chat_bubble/15fad47ba0fc899390d661b427f7c12f8eb6d458" alt="Tân Mỹ" class="w-full h-full object-cover">
                        </div>
                        <div class="bg-gray-100 rounded-2xl rounded-tl-none px-5 py-3.5 max-w-lg">
                            <p class="text-sm text-gray-700">Xin chào! Tân Mỹ Group rất hân hạnh được phục vụ quý khách. <br class="hidden sm:block">Vui lòng lựa chọn kênh liên hệ dưới đây:</p>
                        </div>
                    </div>
                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                        <a href="tel:02432252752" class="group flex items-center gap-4 bg-blue-50 hover:bg-blue-100 transition rounded-xl p-4 border border-blue-100 hover:border-blue-200">
                            <div class="w-11 h-11 rounded-full bg-brandBlue flex items-center justify-center flex-shrink-0 group-hover:scale-105 transition">
                                <i class="fa-solid fa-phone text-white"></i>
                            </div>
                            <div>
                                <div class="text-xs font-bold text-brandBlue uppercase tracking-wide">Hotline</div>
                                <div class="text-sm font-black text-gray-800">024 32252752</div>
                                <div class="text-xs text-gray-500">024 3558 5841</div>
                            </div>
                        </a>
                        <a href="mailto:vanphongcongty@tanmygroup.com.vn" class="group flex items-center gap-4 bg-blue-50 hover:bg-blue-100 transition rounded-xl p-4 border border-blue-100 hover:border-blue-200">
                            <div class="w-11 h-11 rounded-full bg-brandBlue flex items-center justify-center flex-shrink-0 group-hover:scale-105 transition">
                                <i class="fa-solid fa-envelope text-white"></i>
                            </div>
                            <div>
                                <div class="text-xs font-bold text-brandBlue uppercase tracking-wide">Email</div>
                                <div class="text-xs font-medium text-gray-700 break-all">vanphongcongty@<br>tanmygroup.com.vn</div>
                            </div>
                        </a>
                        <div class="group flex items-center gap-4 bg-blue-50 rounded-xl p-4 border border-blue-100">
                            <div class="w-11 h-11 rounded-full bg-brandBlue flex items-center justify-center flex-shrink-0">
                                <i class="fa-solid fa-location-dot text-white"></i>
                            </div>
                            <div>
                                <div class="text-xs font-bold text-brandBlue uppercase tracking-wide">Trụ sở</div>
                                <div class="text-xs text-gray-700">Số 77 Lê Văn Hưu,<br>Hai Bà Trưng, Hà Nội</div>
                            </div>
                        </div>
                    </div>
                    <div class="mt-6 pt-5 border-t border-gray-100 flex flex-wrap items-center justify-between gap-4">
                        <div class="flex items-center gap-4">
                            <span class="text-xs text-gray-500 font-semibold">Kết nối với Tân Mỹ:</span>
                            <a href="#" class="w-8 h-8 rounded-full bg-[#1877F2] flex items-center justify-center text-white text-xs hover:opacity-90 transition"><i class="fa-brands fa-facebook-f"></i></a>
                            <a href="#" class="w-8 h-8 rounded-full bg-[#0068FF] flex items-center justify-center text-white text-xs hover:opacity-90 transition"><i class="fa-solid fa-comment-dots"></i></a>
                            <a href="#" class="w-8 h-8 rounded-full bg-[#c4302b] flex items-center justify-center text-white text-xs hover:opacity-90 transition"><i class="fa-brands fa-youtube"></i></a>
                        </div>
                        <span class="text-xs text-gray-400">Phản hồi trong vòng 24h</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- KHỐI 10: FOOTER -->
<footer id="contact" class="bg-[#0f172a] text-gray-400 pt-16 lg:pt-20 pb-0">
    <div class="container mx-auto px-4">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-10 lg:gap-8 pb-14">
            <div class="lg:col-span-1">
                <svg viewBox="0 0 550 120" class="h-14 w-auto mb-5" xmlns="http://www.w3.org/2000/svg">
                    <!-- 1. KHỐI BIỂU TƯỢNG HÌNH VUÔNG (ICON BÊN TRÁI) -->
                    <g transform="translate(5, 5)">
                        <rect width="110" height="110" fill="white" stroke="#014289" stroke-width="4"/>
                        <path d="M 4 80 Q 55 105 106 80 L 106 106 L 4 106 Z" fill="#014289"/>
                        <path d="M 4 106 Q 55 90 106 106 Z" fill="white"/>
                        <path d="M 55 10 L 25 90 Q 55 75 85 90 Z" fill="#F1C40F"/>
                        <path d="M 35 35 L 75 35 M 55 35 L 55 75" stroke="#ED1C24" stroke-width="8" stroke-linecap="square"/>
                        <text x="36" y="75" font-family="sans-serif" font-weight="900" font-size="34" fill="#ED1C24">M</text>
                    </g>
                    <!-- 2. PHẦN CHỮ THƯƠNG HIỆU "TANMY" -->
                    <text x="135" y="75" font-family="sans-serif" font-weight="900" font-size="82" fill="#014289" letter-spacing="-2">TANMY</text>
                    <!-- 3. PHẦN SLOGAN -->
                    <text x="138" y="108" font-family="sans-serif" font-weight="500" font-size="28" fill="#ED1C24">Trường tồn cùng thời gian</text>
                </svg>
                <p class="text-xs leading-relaxed mb-5 text-gray-500">Công ty cổ phần tập đoàn Tân Mỹ - Đối tác tin cậy của mọi nhà.</p>
                <p class="text-xs mb-2 text-gray-400"><i class="fa-solid fa-map-marker-alt w-4 text-brandBlue mr-1"></i> KCN Thạch Thất, Hà Nội</p>
                <p class="text-xs mb-2 text-gray-400"><i class="fa-solid fa-phone w-4 text-brandBlue mr-1"></i> 0123 456 789</p>
                <p class="text-xs mb-5 text-gray-400"><i class="fa-solid fa-envelope w-4 text-brandBlue mr-1"></i> info@tanmygroup.com.vn</p>
                <div class="flex gap-3">
                    <a href="#" class="w-9 h-9 rounded-full bg-gray-800 flex items-center justify-center hover:bg-brandBlue transition text-sm text-gray-400 hover:text-white"><i class="fa-brands fa-facebook-f"></i></a>
                    <a href="#" class="w-9 h-9 rounded-full bg-gray-800 flex items-center justify-center hover:bg-brandBlue transition text-sm text-gray-400 hover:text-white"><i class="fa-brands fa-youtube"></i></a>
                    <a href="#" class="w-9 h-9 rounded-full bg-gray-800 flex items-center justify-center hover:bg-brandBlue transition text-sm text-gray-400 hover:text-white"><i class="fa-brands fa-linkedin-in"></i></a>
                </div>
            </div>
            <div><h4 class="text-white font-bold text-sm mb-6"><span class="footer-bar"></span> VỀ CHÚNG TÔI</h4><ul class="space-y-3 text-xs"><li><a href="#" class="hover:text-white transition">Giới thiệu tổng quan</a></li><li><a href="#" class="hover:text-white transition">Tầm nhìn - Sứ mệnh</a></li><li><a href="#" class="hover:text-white transition">Năng lực sản xuất</a></li><li><a href="#" class="hover:text-white transition">Sơ đồ tổ chức</a></li></ul></div>
            <div><h4 class="text-white font-bold text-sm mb-6"><span class="footer-bar"></span> NHÔM TÂN MỸ</h4><ul class="space-y-3 text-xs"><li><a href="#" class="hover:text-white transition">Hệ nhôm cao cấp ZAVA</a></li><li><a href="#" class="hover:text-white transition">Nhôm thanh kiến trúc</a></li><li><a href="#" class="hover:text-white transition">Nhôm định hình công nghiệp</a></li><li><a href="#" class="hover:text-white transition">Catalogue sản phẩm</a></li></ul></div>
            <div><h4 class="text-white font-bold text-sm mb-6"><span class="footer-bar"></span> GIA DỤNG TÂN MỸ</h4><ul class="space-y-3 text-xs"><li><a href="#" class="hover:text-white transition">Bồn nước inox Tân Mỹ</a></li><li><a href="#" class="hover:text-white transition">Bồn nhựa đa năng Tân Mỹ</a></li><li><a href="#" class="hover:text-white transition">Bể tự hoại thông minh Septic</a></li><li><a href="#" class="hover:text-white transition">Máy nước nóng NLMT</a></li></ul></div>
            <div><h4 class="text-white font-bold text-sm mb-6"><span class="footer-bar"></span> ĐĂNG KÝ THÔNG TIN</h4><p class="text-xs mb-4 text-gray-500">Nhận thông tin khuyến mãi và sản phẩm mới nhất từ Tân Mỹ Group.</p><div class="flex"><input type="email" placeholder="Email của bạn..." class="bg-gray-800 text-white text-xs px-4 py-3 rounded-l-xl w-full outline-none border border-gray-700 focus:border-brandBlue"><button class="bg-brandBlue text-white px-5 rounded-r-xl hover:opacity-90 transition"><i class="fa-solid fa-paper-plane"></i></button></div></div>
        </div>
        <div class="border-t border-gray-800 py-6 flex flex-col lg:flex-row items-center justify-between text-[11px] text-gray-500">
            <p>&copy; 2024 <strong class="text-white font-semibold">Tân Mỹ Group</strong>. All rights reserved.</p>
            <div class="flex gap-6 mt-2 lg:mt-0">
                <a href="#" class="hover:text-white transition">Chính sách bảo mật</a>
                <a href="#" class="hover:text-white transition">Điều khoản sử dụng</a>
            </div>
        </div>
    </div>
</footer>

<!-- FLOATING CONTACT WIDGET -->
<div class="fixed bottom-6 right-6 z-50">
    <div id="floatPanel" class="float-panel hide mb-4">
        <div class="bg-white rounded-2xl shadow-2xl border border-gray-100 w-64 overflow-hidden">
            <div class="bg-brandBlue p-3.5 flex items-center gap-3">
                <div class="w-8 h-8 rounded-full bg-white flex items-center justify-center flex-shrink-0 shadow-sm overflow-hidden">
                    <img src="https://tawk.link/5865e574e7588f12124ea003/var/chat_bubble/15fad47ba0fc899390d661b427f7c12f8eb6d458" alt="Tân Mỹ" class="w-full h-full object-cover">
                </div>
                <div class="text-white text-sm font-bold">Tân Mỹ hỗ trợ</div>
                <button id="closeFloat" class="ml-auto text-white/70 hover:text-white text-sm"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <div class="p-3 space-y-2">
                <a href="tel:02432252752" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-blue-50 transition group">
                    <div class="w-9 h-9 rounded-full bg-green-500 flex items-center justify-center text-white group-hover:scale-105 transition"><i class="fa-solid fa-phone"></i></div>
                    <div><div class="text-xs text-gray-400">Gọi ngay</div><div class="text-sm font-bold text-gray-800">024 32252752</div></div>
                </a>
                <a href="#" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-blue-50 transition group">
                    <div class="w-9 h-9 rounded-full bg-[#0068FF] flex items-center justify-center text-white group-hover:scale-105 transition"><i class="fa-brands fa-facebook-messenger"></i></div>
                    <div><div class="text-xs text-gray-400">Chat Messenger</div><div class="text-xs font-semibold text-gray-700">Tân Mỹ Group</div></div>
                </a>
                <a href="#" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-blue-50 transition group">
                    <div class="w-9 h-9 rounded-full bg-[#1877F2] flex items-center justify-center text-white group-hover:scale-105 transition"><i class="fa-brands fa-facebook-f"></i></div>
                    <div><div class="text-xs text-gray-400">Facebook</div><div class="text-xs font-semibold text-gray-700">Tân Mỹ Group</div></div>
                </a>
                <a href="mailto:vanphongcongty@tanmygroup.com.vn" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-blue-50 transition group">
                    <div class="w-9 h-9 rounded-full bg-brandBlue flex items-center justify-center text-white group-hover:scale-105 transition"><i class="fa-solid fa-envelope"></i></div>
                    <div><div class="text-xs text-gray-400">Email</div><div class="text-xs font-semibold text-gray-700">Gửi thư</div></div>
                </a>
            </div>
        </div>
    </div>
    <button id="floatToggle" class="float-btn w-14 h-14 rounded-full bg-brandBlue shadow-xl flex items-center justify-center text-white text-2xl hover:shadow-2xl relative">
        <i id="floatIcon" class="fa-solid fa-headset"></i>
        <span class="absolute -top-1 -right-1 w-4 h-4 bg-green-400 rounded-full border-2 border-white animate-pulse"></span>
    </button>
</div>

<script>
AOS.init({duration:800,once:true,offset:100});
const navbar=document.getElementById('navbar');
window.addEventListener('scroll',function(){navbar.classList.toggle('nav-scrolled',window.scrollY>50);});
document.getElementById('mobile-menu-btn').addEventListener('click',function(){document.getElementById('mobile-menu').classList.toggle('hidden');});
const floatToggle=document.getElementById('floatToggle');
const floatPanel=document.getElementById('floatPanel');
const floatIcon=document.getElementById('floatIcon');
const closeFloat=document.getElementById('closeFloat');
floatToggle.addEventListener('click',function(){floatPanel.classList.toggle('hide');floatPanel.classList.toggle('show');floatIcon.classList.toggle('fa-headset');floatIcon.classList.toggle('fa-xmark');});
closeFloat.addEventListener('click',function(){floatPanel.classList.add('hide');floatPanel.classList.remove('show');floatIcon.classList.add('fa-headset');floatIcon.classList.remove('fa-xmark');});
</script>

</body>
</html>'''

with open('E:/webtanmy/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Written {len(html)} chars to index.html")
