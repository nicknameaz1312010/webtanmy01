html = '''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tân Mỹ Group - Nhôm định hình ZAVA, gia dụng hàng đầu Việt Nam</title>
  <meta name="description" content="Tân Mỹ Group - Nhà sản xuất nhôm định hình ZAVA, bồn nước inox, bồn nhựa, bể tự hoại Septic, chậu rửa inox và máy nước nóng NLMT hàng đầu Việt Nam.">
  <meta name="keywords" content="Tân Mỹ, nhôm định hình ZAVA, bồn nước inox, bồn nhựa, bể tự hoại, chậu rửa inox, máy nước nóng NLMT">
  <meta name="author" content="Tân Mỹ Group">
  <meta property="og:title" content="Tân Mỹ Group - Nhôm ZAVA & Gia dụng hàng đầu Việt Nam">
  <meta property="og:description" content="Nhôm định hình ZAVA, bồn nước inox 304, bảo hành 5 năm, 1000+ đại lý toàn quốc.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://nicknameaz1312010.github.io/webtanmy/">
  <meta name="robots" content="index, follow">
  <link rel="icon" href="https://tanmygroup.com.vn/wp-content/uploads/2026/03/cropped-logo-ko-chu-scaled-1-32x32.png">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brand: '#014289',
            accent: '#ED1C24',
          }
        }
      }
    }
  </script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    * { font-family: 'Inter', sans-serif; }
    html { scroll-behavior: smooth; }
    .glass-nav { background: rgba(255,255,255,0.92); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); }
    .pulse-ring { animation: pulseRing 2s ease-in-out infinite; }
    @keyframes pulseRing { 0% { box-shadow: 0 0 0 0 rgba(255,255,255,0.5); } 70% { box-shadow: 0 0 0 20px rgba(255,255,255,0); } 100% { box-shadow: 0 0 0 0 rgba(255,255,255,0); } }
    .globe-spin { animation: spin 12s linear infinite; display: inline-block; }
    @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    .dropdown:hover .dropdown-menu { opacity: 1; visibility: visible; transform: translateY(0); }
    .dropdown-menu { opacity: 0; visibility: hidden; transform: translateY(8px); transition: all 0.2s ease; }
    .project-card:hover img { transform: scale(1.08); }
    .project-card img { transition: transform 0.5s ease; }
    .hero-overlay { background: linear-gradient(135deg, rgba(1,66,137,0.7) 0%, rgba(1,66,137,0.3) 100%); }
    .scroll-nav { transition: all 0.3s ease; }
    .nav-scrolled { background: #fff !important; box-shadow: 0 4px 20px rgba(0,0,0,0.08); }
    .mobile-menu { transition: all 0.3s ease; }
    .underline-red { position: relative; display: inline-block; }
    .underline-red::after { content: ''; position: absolute; bottom: -4px; left: 50%; transform: translateX(-50%); width: 60px; height: 3px; background: #ED1C24; border-radius: 2px; }
    @media (max-width: 1023px) {
      .desktop-only { display: none !important; }
      .mobile-only { display: block !important; }
    }
    @media (min-width: 1024px) {
      .mobile-only { display: none !important; }
    }
  </style>
</head>
<body class="bg-white text-gray-900 antialiased overflow-x-hidden">

<!-- NAVBAR -->
<header id="navbar" class="scroll-nav fixed top-0 left-0 w-full z-50 glass-nav">
  <div class="max-w-7xl mx-auto px-4 lg:px-8">
    <div class="flex items-center justify-between h-16 lg:h-20">
      <!-- Logo -->
      <div class="flex items-center gap-3">
        <a href="#" class="flex items-baseline gap-0">
          <span class="text-2xl lg:text-3xl font-black tracking-widest" style="color:#014289">TÂN</span>
          <span class="text-2xl lg:text-3xl font-black tracking-widest" style="color:#ED1C24">MỸ</span>
        </a>
        <div class="hidden lg:block w-px h-8 bg-gray-300"></div>
        <div class="hidden lg:flex flex-col leading-tight">
          <span class="text-[9px] font-bold text-gray-400 tracking-widest">THƯƠNG HIỆU</span>
          <span class="text-[9px] font-bold text-gray-400 tracking-widest">UY TÍN</span>
        </div>
      </div>

      <!-- Desktop Nav -->
      <nav class="desktop-only flex items-center gap-1 lg:gap-2">
        <a href="#" class="px-3 py-2 text-sm font-semibold text-brand border-b-2 border-brand">TRANG CHỦ</a>
        <a href="#about" class="px-3 py-2 text-sm font-semibold text-gray-600 hover:text-brand transition">GIỚI THIỆU</a>
        <div class="dropdown relative px-3 py-2 text-sm font-semibold text-gray-600 hover:text-brand transition cursor-pointer">
          NHÔM TÂN MỸ <i class="fas fa-chevron-down text-[10px] ml-1"></i>
          <div class="dropdown-menu absolute top-full left-0 bg-white shadow-xl rounded-lg py-2 min-w-[200px] z-50">
            <a href="#" class="block px-4 py-2.5 text-sm text-gray-700 hover:bg-gray-50 hover:text-brand">Hệ nhôm ZAVA cao cấp</a>
            <a href="#" class="block px-4 py-2.5 text-sm text-gray-700 hover:bg-gray-50 hover:text-brand">Nhôm thanh kiến trúc</a>
            <a href="#" class="block px-4 py-2.5 text-sm text-gray-700 hover:bg-gray-50 hover:text-brand">Nhôm định hình công nghiệp</a>
          </div>
        </div>
        <div class="dropdown relative px-3 py-2 text-sm font-semibold text-gray-600 hover:text-brand transition cursor-pointer">
          GIA DỤNG TÂN MỸ <i class="fas fa-chevron-down text-[10px] ml-1"></i>
          <div class="dropdown-menu absolute top-full left-0 bg-white shadow-xl rounded-lg py-2 min-w-[200px] z-50">
            <a href="#" class="block px-4 py-2.5 text-sm text-gray-700 hover:bg-gray-50 hover:text-brand">Bồn nước Inox</a>
            <a href="#" class="block px-4 py-2.5 text-sm text-gray-700 hover:bg-gray-50 hover:text-brand">Bồn nhựa đa năng</a>
            <a href="#" class="block px-4 py-2.5 text-sm text-gray-700 hover:bg-gray-50 hover:text-brand">Bể tự hoại Septic</a>
          </div>
        </div>
        <a href="#projects" class="px-3 py-2 text-sm font-semibold text-gray-600 hover:text-brand transition">DỰ ÁN</a>
        <a href="#news" class="px-3 py-2 text-sm font-semibold text-gray-600 hover:text-brand transition">TIN TỨC</a>
        <a href="#contact" class="px-3 py-2 text-sm font-semibold text-gray-600 hover:text-brand transition">TUYỂN DỤNG</a>
        <a href="#contact" class="px-3 py-2 text-sm font-semibold text-gray-600 hover:text-brand transition">LIÊN HỆ</a>
      </nav>

      <!-- Right Tools -->
      <div class="flex items-center gap-3">
        <button class="text-gray-500 hover:text-brand transition text-lg"><i class="fas fa-search"></i></button>
        <div class="hidden lg:flex items-center border border-gray-300 rounded-md px-2.5 py-1 text-xs font-bold gap-1">
          <span style="color:#014289">VI</span>
          <span class="text-gray-300">|</span>
          <span class="text-gray-400">EN</span>
        </div>
        <button id="mobileToggle" class="mobile-only text-2xl text-gray-700" onclick="toggleMobile()"><i class="fas fa-bars"></i></button>
      </div>
    </div>
  </div>
</header>

<!-- Mobile Menu -->
<div id="mobileMenu" class="mobile-only fixed inset-0 z-40 bg-white pt-20 px-6 py-8 hidden">
  <div class="flex flex-col gap-4">
    <a href="#" class="text-lg font-bold text-brand border-b border-gray-100 pb-3">TRANG CHỦ</a>
    <a href="#about" class="text-lg font-semibold text-gray-700 border-b border-gray-100 pb-3">GIỚI THIỆU</a>
    <div class="border-b border-gray-100 pb-3">
      <button onclick="this.nextElementSibling.classList.toggle('hidden')" class="w-full text-left text-lg font-semibold text-gray-700 flex justify-between items-center">
        NHÔM TÂN MỸ <i class="fas fa-chevron-down text-sm"></i>
      </button>
      <div class="hidden mt-3 pl-4 flex flex-col gap-2">
        <a href="#" class="text-sm text-gray-500 py-1">Hệ nhôm ZAVA cao cấp</a>
        <a href="#" class="text-sm text-gray-500 py-1">Nhôm thanh kiến trúc</a>
        <a href="#" class="text-sm text-gray-500 py-1">Nhôm định hình công nghiệp</a>
      </div>
    </div>
    <div class="border-b border-gray-100 pb-3">
      <button onclick="this.nextElementSibling.classList.toggle('hidden')" class="w-full text-left text-lg font-semibold text-gray-700 flex justify-between items-center">
        GIA DỤNG TÂN MỸ <i class="fas fa-chevron-down text-sm"></i>
      </button>
      <div class="hidden mt-3 pl-4 flex flex-col gap-2">
        <a href="#" class="text-sm text-gray-500 py-1">Bồn nước Inox</a>
        <a href="#" class="text-sm text-gray-500 py-1">Bồn nhựa đa năng</a>
        <a href="#" class="text-sm text-gray-500 py-1">Bể tự hoại Septic</a>
      </div>
    </div>
    <a href="#projects" class="text-lg font-semibold text-gray-700 border-b border-gray-100 pb-3">DỰ ÁN</a>
    <a href="#news" class="text-lg font-semibold text-gray-700 border-b border-gray-100 pb-3">TIN TỨC</a>
    <a href="#contact" class="text-lg font-semibold text-gray-700 border-b border-gray-100 pb-3">LIÊN HỆ</a>
  </div>
</div>

<main>
<!-- HERO -->
<section class="relative min-h-screen flex items-center" style="margin-top:0">
  <div class="absolute inset-0">
    <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1600&q=80" alt="Nhà máy sản xuất nhôm hiện đại" class="w-full h-full object-cover">
    <div class="absolute inset-0 hero-overlay"></div>
  </div>
  <div class="relative z-10 max-w-7xl mx-auto px-4 lg:px-8 w-full pt-24 lg:pt-0">
    <div class="flex flex-col lg:flex-row items-center lg:items-center justify-between gap-10 lg:gap-0">
      <div class="lg:w-3/5 text-center lg:text-left" data-aos="fade-right">
        <h1 class="text-4xl sm:text-5xl lg:text-6xl xl:text-7xl font-black text-white leading-tight">
          TÂN MỸ <br>
          <span class="text-yellow-400">KIẾN TẠO GIÁ TRỊ</span> <br>
          BỀN VỮNG TỪ NHÔM VIỆT
        </h1>
        <p class="mt-6 text-base sm:text-lg lg:text-xl text-gray-200 max-w-2xl leading-relaxed font-light">
          Nhà sản xuất nhôm định hình, sản phẩm gia dụng và giải pháp vật liệu xây dựng hàng đầu Việt Nam.
        </p>
        <div class="mt-8 flex flex-wrap gap-4 justify-center lg:justify-start">
          <a href="#" class="inline-flex items-center gap-2 bg-brand text-white font-bold px-8 py-3.5 rounded-lg hover:opacity-90 transition text-sm tracking-wider">
            <i class="fas fa-industry"></i> KHÁM PHÁ NHÀ MÁY
          </a>
          <a href="#contact" class="inline-flex items-center gap-2 border-2 border-white text-white font-semibold px-8 py-3.5 rounded-lg hover:bg-white hover:text-brand transition text-sm tracking-wider">
            <i class="fas fa-phone-alt"></i> LIÊN HỆ TƯ VẤN
          </a>
        </div>
      </div>
      <div class="lg:w-2/5 flex flex-col items-center lg:items-end" data-aos="fade-left">
        <button onclick="alert('Video giới thiệu Tân Mỹ Group')" class="flex flex-col items-center gap-3 group">
          <div class="w-20 h-20 lg:w-24 lg:h-24 rounded-full bg-white flex items-center justify-center pulse-ring cursor-pointer group-hover:scale-105 transition">
            <i class="fas fa-play text-2xl lg:text-3xl ml-1" style="color:#014289"></i>
          </div>
          <span class="text-white text-sm font-bold tracking-widest mt-2">XEM VIDEO GIỚI THIỆU</span>
        </button>
      </div>
    </div>
  </div>
</section>

<!-- STRATEGIC METRICS -->
<section class="relative z-20 max-w-7xl mx-auto px-4 lg:px-8 -mt-16 lg:-mt-20">
  <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 bg-white rounded-2xl shadow-2xl overflow-hidden divide-x divide-gray-100">
    <div class="p-6 lg:p-8 text-center" data-aos="zoom-in" data-aos-delay="0">
      <div class="text-3xl lg:text-4xl font-black" style="color:#014289">25+</div>
      <div class="text-xs lg:text-sm text-gray-500 font-semibold mt-2 leading-tight">Năm kinh nghiệm</div>
    </div>
    <div class="p-6 lg:p-8 text-center" data-aos="zoom-in" data-aos-delay="100">
      <div class="text-3xl lg:text-4xl font-black" style="color:#014289">50.000+</div>
      <div class="text-xs lg:text-sm text-gray-500 font-semibold mt-2 leading-tight">Tấn nhôm mỗi năm</div>
    </div>
    <div class="p-6 lg:p-8 text-center" data-aos="zoom-in" data-aos-delay="200">
      <div class="text-3xl lg:text-4xl font-black" style="color:#014289">1.000+</div>
      <div class="text-xs lg:text-sm text-gray-500 font-semibold mt-2 leading-tight">Đại lý & đối tác</div>
    </div>
    <div class="p-6 lg:p-8 text-center" data-aos="zoom-in" data-aos-delay="300">
      <div class="text-3xl lg:text-4xl font-black" style="color:#014289">63</div>
      <div class="text-xs lg:text-sm text-gray-500 font-semibold mt-2 leading-tight">Tỉnh thành phân phối</div>
    </div>
    <div class="p-6 lg:p-8 text-center col-span-2 md:col-span-1" data-aos="zoom-in" data-aos-delay="400">
      <div class="text-3xl lg:text-4xl font-black" style="color:#014289">
        <span class="globe-spin"><i class="fas fa-globe-asia"></i></span>
      </div>
      <div class="text-xs lg:text-sm text-gray-500 font-semibold mt-2 leading-tight">Xuất khẩu nhiều quốc gia</div>
    </div>
  </div>
</section>

<!-- ABOUT -->
<section id="about" class="py-16 lg:py-24 bg-gray-50">
  <div class="max-w-7xl mx-auto px-4 lg:px-8">
    <div class="text-center mb-12" data-aos="fade-up">
      <h2 class="text-2xl lg:text-4xl font-black text-brand">VỀ TÂN MỸ GROUP</h2>
      <div class="w-16 h-1 bg-accent mx-auto mt-4 rounded"></div>
      <p class="text-gray-500 mt-4 max-w-2xl mx-auto">Tiên phong trong ngành nhôm định hình và gia dụng, cam kết chất lượng và đổi mới không ngừng.</p>
    </div>
    <div class="grid lg:grid-cols-2 gap-10 items-center">
      <div data-aos="fade-right">
        <img src="https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?w=800&q=80" alt="Nhà máy Tân Mỹ" class="rounded-2xl shadow-lg w-full">
      </div>
      <div data-aos="fade-left">
        <p class="text-gray-600 leading-relaxed mb-6">
          Tân Mỹ Group thành lập từ năm 1999, là một trong những doanh nghiệp hàng đầu Việt Nam trong lĩnh vực sản xuất nhôm định hình, bồn nước inox, bồn nhựa, bể tự hoại Septic, chậu rửa inox và máy nước nóng năng lượng mặt trời.
        </p>
        <p class="text-gray-600 leading-relaxed mb-6">
          Với hệ thống nhà máy hiện đại tại Việt Nam, Tân Mỹ cung cấp các sản phẩm chất lượng cao, đáp ứng tiêu chuẩn quốc tế, phục vụ thị trường trong nước và xuất khẩu sang nhiều quốc gia.
        </p>
        <div class="grid grid-cols-3 gap-4 mb-8">
          <div class="bg-white rounded-xl p-4 text-center shadow-sm"><div class="text-2xl font-black text-brand">25+</div><div class="text-xs text-gray-500 mt-1">Năm kinh nghiệm</div></div>
          <div class="bg-white rounded-xl p-4 text-center shadow-sm"><div class="text-2xl font-black text-brand">50K+</div><div class="text-xs text-gray-500 mt-1">Tấn nhôm/năm</div></div>
          <div class="bg-white rounded-xl p-4 text-center shadow-sm"><div class="text-2xl font-black text-brand">1K+</div><div class="text-xs text-gray-500 mt-1">Đại lý toàn quốc</div></div>
        </div>
        <a href="#contact" class="inline-flex items-center gap-2 bg-brand text-white font-bold px-6 py-3 rounded-lg hover:opacity-90 transition text-sm">
          <i class="fas fa-handshake"></i> Liên hệ hợp tác
        </a>
      </div>
    </div>
  </div>
</section>

<!-- CORE PRODUCTS -->
<section class="py-16 lg:py-24 bg-white">
  <div class="max-w-7xl mx-auto px-4 lg:px-8">
    <div class="grid lg:grid-cols-2 gap-8">
      <!-- Left Card: Aluminum -->
      <div class="relative rounded-2xl overflow-hidden" data-aos="fade-right" style="background: linear-gradient(135deg, #1e293b 0%, #111827 100%);">
        <div class="p-8 lg:p-10 relative z-10">
          <div class="text-xs font-bold tracking-[0.2em] text-green-400 mb-2">THƯƠNG HIỆU ZAVA</div>
          <h3 class="text-2xl lg:text-3xl font-black text-white mb-6">NHÔM TÂN MỸ - ZAVA</h3>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3 text-gray-300"><i class="fas fa-check-circle text-green-400 mt-1"></i> Hệ nhôm kiến trúc ZAVA cao cấp</li>
            <li class="flex items-start gap-3 text-gray-300"><i class="fas fa-check-circle text-green-400 mt-1"></i> Nhôm thanh định hình công nghiệp</li>
            <li class="flex items-start gap-3 text-gray-300"><i class="fas fa-check-circle text-green-400 mt-1"></i> Hệ nhôm xây dựng tiêu chuẩn</li>
          </ul>
          <a href="#" class="inline-flex items-center gap-2 bg-white text-brand font-bold px-6 py-3 rounded-lg hover:bg-gray-100 transition text-sm">Khám phá ngành nhôm <i class="fas fa-arrow-right"></i></a>
        </div>
        <div class="absolute bottom-0 right-0 w-40 h-40 lg:w-48 lg:h-48 overflow-hidden opacity-40">
          <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=400&q=80" alt="Cửa kính biệt thự" class="w-full h-full object-cover">
        </div>
      </div>

      <!-- Right Card: Appliances -->
      <div class="relative rounded-2xl overflow-hidden" data-aos="fade-left" style="background: linear-gradient(135deg, #eff6ff 0%, #f3f4f6 100%);">
        <div class="p-8 lg:p-10 relative z-10">
          <div class="text-xs font-bold tracking-[0.2em] text-blue-500 mb-2">GIA DỤNG CAO CẤP</div>
          <h3 class="text-2xl lg:text-3xl font-black text-brand mb-6">GIA DỤNG TÂN MỸ</h3>
          <ul class="space-y-3 mb-8">
            <li class="flex items-start gap-3 text-gray-700"><i class="fas fa-check-circle text-blue-500 mt-1"></i> Bồn nước Inox</li>
            <li class="flex items-start gap-3 text-gray-700"><i class="fas fa-check-circle text-blue-500 mt-1"></i> Bồn nhựa đa năng</li>
            <li class="flex items-start gap-3 text-gray-700"><i class="fas fa-check-circle text-blue-500 mt-1"></i> Bể phốt thông minh SEPTIC</li>
            <li class="flex items-start gap-3 text-gray-700"><i class="fas fa-check-circle text-blue-500 mt-1"></i> Máy nước nóng NLMT</li>
          </ul>
          <a href="#" class="inline-flex items-center gap-2 bg-brand text-white font-bold px-6 py-3 rounded-lg hover:opacity-90 transition text-sm">Khám phá sản phẩm <i class="fas fa-arrow-right"></i></a>
        </div>
        <div class="absolute bottom-0 right-0 w-36 h-36 lg:w-44 lg:h-44 overflow-hidden opacity-30">
          <img src="https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=400&q=80" alt="Bồn nước inox" class="w-full h-full object-cover">
        </div>
      </div>
    </div>
  </div>
</section>

<!-- PRODUCTION PROCESS -->
<section class="py-16 lg:py-24 bg-gray-50">
  <div class="max-w-7xl mx-auto px-4 lg:px-8">
    <div class="text-center mb-14" data-aos="fade-up">
      <h2 class="text-2xl lg:text-4xl font-black text-brand underline-red">QUY TRÌNH SẢN XUẤT HIỆN ĐẠI</h2>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6 lg:gap-4">
      <div class="text-center" data-aos="fade-up" data-aos-delay="0">
        <div class="w-12 h-12 rounded-full bg-brand text-white flex items-center justify-center text-lg font-black mx-auto mb-4">1</div>
        <div class="rounded-xl overflow-hidden mb-4 shadow-md">
          <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400&q=80" alt="Phôi nhôm thô" class="w-full h-36 object-cover">
        </div>
        <h4 class="font-bold text-gray-900 mb-2">Nguyên liệu Billet</h4>
        <p class="text-xs text-gray-500 leading-relaxed">Hợp kim nhôm nhập khẩu đạt chất lượng tiêu chuẩn quốc tế.</p>
      </div>
      <div class="text-center" data-aos="fade-up" data-aos-delay="100">
        <div class="w-12 h-12 rounded-full bg-brand text-white flex items-center justify-center text-lg font-black mx-auto mb-4">2</div>
        <div class="rounded-xl overflow-hidden mb-4 shadow-md">
          <img src="https://images.unsplash.com/photo-1581092795360-fd1ca04f0952?w=400&q=80" alt="Máy đùn ép" class="w-full h-36 object-cover">
        </div>
        <h4 class="font-bold text-gray-900 mb-2">Hệ thống đùn ép</h4>
        <p class="text-xs text-gray-500 leading-relaxed">Máy đùn ép áp lực cao tạo hình thanh nhôm chính xác.</p>
      </div>
      <div class="text-center" data-aos="fade-up" data-aos-delay="200">
        <div class="w-12 h-12 rounded-full bg-brand text-white flex items-center justify-center text-lg font-black mx-auto mb-4">3</div>
        <div class="rounded-xl overflow-hidden mb-4 shadow-md">
          <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400&q=80" alt="Sơn tĩnh điện" class="w-full h-36 object-cover">
        </div>
        <h4 class="font-bold text-gray-900 mb-2">Xử lý sơn tĩnh điện</h4>
        <p class="text-xs text-gray-500 leading-relaxed">Phủ bề mặt hạt sơn bám dính chắc chắn, chống oxy hóa.</p>
      </div>
      <div class="text-center" data-aos="fade-up" data-aos-delay="300">
        <div class="w-12 h-12 rounded-full bg-brand text-white flex items-center justify-center text-lg font-black mx-auto mb-4">4</div>
        <div class="rounded-xl overflow-hidden mb-4 shadow-md">
          <img src="https://images.unsplash.com/photo-1581092795360-fd1ca04f0952?w=400&q=80" alt="Kiểm định chất lượng" class="w-full h-36 object-cover">
        </div>
        <h4 class="font-bold text-gray-900 mb-2">Kiểm định chất lượng</h4>
        <p class="text-xs text-gray-500 leading-relaxed">Đội ngũ QA/QC đo đạc thông số kỹ thuật nghiêm ngặt.</p>
      </div>
      <div class="text-center" data-aos="fade-up" data-aos-delay="400">
        <div class="w-12 h-12 rounded-full bg-brand text-white flex items-center justify-center text-lg font-black mx-auto mb-4">5</div>
        <div class="rounded-xl overflow-hidden mb-4 shadow-md">
          <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400&q=80" alt="Đóng gói thành phẩm" class="w-full h-36 object-cover">
        </div>
        <h4 class="font-bold text-gray-900 mb-2">Thành phẩm đóng gói</h4>
        <p class="text-xs text-gray-500 leading-relaxed">Đóng bọc màng bảo vệ và lưu kho xuất xưởng phân phối.</p>
      </div>
    </div>
  </div>
</section>

<!-- CERTIFICATIONS & PROJECTS -->
<section id="projects" class="py-16 lg:py-24 bg-white">
  <div class="max-w-7xl mx-auto px-4 lg:px-8">
    <div class="flex flex-col lg:flex-row gap-8">
      <!-- Left: Certifications -->
      <div class="lg:w-1/3" data-aos="fade-right">
        <h3 class="text-xl lg:text-2xl font-black text-brand mb-4">CHỨNG NHẬN CHẤT LƯỢNG</h3>
        <p class="text-sm text-gray-500 mb-6 leading-relaxed">Các chứng chỉ và giải thưởng khẳng định chất lượng sản phẩm dịch vụ của Tân Mỹ Group.</p>
        <div class="grid grid-cols-2 gap-3">
          <div class="bg-gray-50 border border-gray-100 rounded-xl p-4 text-center"><div class="text-sm font-black text-brand">ISO<br>9001:2015</div><div class="text-[10px] text-gray-400 mt-1">Quản lý chất lượng</div></div>
          <div class="bg-gray-50 border border-gray-100 rounded-xl p-4 text-center"><div class="text-sm font-black text-brand">QUATEST<br>3</div><div class="text-[10px] text-gray-400 mt-1">Kiểm định chất lượng</div></div>
          <div class="bg-gray-50 border border-gray-100 rounded-xl p-4 text-center"><div class="text-sm font-black text-brand">QUALI<br>COAT</div><div class="text-[10px] text-gray-400 mt-1">Sơn tĩnh điện</div></div>
          <div class="bg-gray-50 border border-gray-100 rounded-xl p-4 text-center"><div class="text-sm font-black text-brand">EURO<br>TIÊU CHUẨN</div><div class="text-[10px] text-gray-400 mt-1">Xuất khẩu Châu Âu</div></div>
        </div>
      </div>

      <!-- Right: Projects -->
      <div class="lg:w-2/3" data-aos="fade-left">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-xl lg:text-2xl font-black text-brand">DỰ ÁN TIÊU BIỂU</h3>
          <a href="#" class="text-sm font-semibold text-brand flex items-center gap-1 hover:underline">XEM TẤT CẢ <i class="fas fa-arrow-right text-xs"></i></a>
        </div>
        <div class="grid grid-cols-2 gap-4">
          <div class="project-card relative rounded-xl overflow-hidden group cursor-pointer">
            <img src="https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=400&q=80" alt="Vinhomes Ocean Park" class="w-full h-48 object-cover">
            <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent"></div>
            <div class="absolute bottom-0 left-0 right-0 p-4"><span class="text-white font-bold text-sm">Vinhomes Ocean Park</span></div>
          </div>
          <div class="project-card relative rounded-xl overflow-hidden group cursor-pointer">
            <img src="https://images.unsplash.com/photo-1486325212027-8081e485255e?w=400&q=80" alt="Sunshine City" class="w-full h-48 object-cover">
            <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent"></div>
            <div class="absolute bottom-0 left-0 right-0 p-4"><span class="text-white font-bold text-sm">Sunshine City</span></div>
          </div>
          <div class="project-card relative rounded-xl overflow-hidden group cursor-pointer">
            <img src="https://images.unsplash.com/photo-1534430480872-3498386e7856?w=400&q=80" alt="FLC Quy Nhơn" class="w-full h-48 object-cover">
            <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent"></div>
            <div class="absolute bottom-0 left-0 right-0 p-4"><span class="text-white font-bold text-sm">FLC Quy Nhơn Resort</span></div>
          </div>
          <div class="project-card relative rounded-xl overflow-hidden group cursor-pointer">
            <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=400&q=80" alt="Biệt thự cao cấp" class="w-full h-48 object-cover">
            <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent"></div>
            <div class="absolute bottom-0 left-0 right-0 p-4"><span class="text-white font-bold text-sm">Biệt thự cao cấp</span></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- NEWS -->
<section id="news" class="py-16 lg:py-24 bg-gray-50">
  <div class="max-w-7xl mx-auto px-4 lg:px-8">
    <div class="flex items-center gap-4 mb-10" data-aos="fade-up">
      <h2 class="text-2xl lg:text-3xl font-black text-brand">TIN TỨC NỔI BẬT</h2>
      <div class="flex-1 h-px bg-gray-300"></div>
    </div>
    <div class="grid lg:grid-cols-4 gap-6" data-aos="zoom-in">
      <!-- Featured News -->
      <div class="lg:col-span-2 relative rounded-2xl overflow-hidden group cursor-pointer">
        <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=800&q=80" alt="Nhà máy Tân Mỹ" class="w-full h-80 lg:h-96 object-cover group-hover:scale-105 transition duration-500">
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
        <div class="absolute bottom-0 left-0 right-0 p-6 lg:p-8">
          <span class="inline-block bg-accent text-white text-xs font-bold px-3 py-1 rounded mb-3">20/05/2024</span>
          <h3 class="text-white font-bold text-lg lg:text-xl leading-snug">Tân Mỹ khánh thành dây chuyền sơn tĩnh điện đứng công nghệ cao hiện đại</h3>
          <a href="#" class="text-white/80 text-sm font-semibold mt-3 inline-flex items-center gap-1 hover:text-white transition">Xem chi tiết <i class="fas fa-arrow-right"></i></a>
        </div>
      </div>

      <!-- Small News -->
      <div class="flex flex-col gap-4">
        <div class="bg-white rounded-xl p-4 flex gap-4 shadow-sm">
          <img src="https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=150&q=80" alt="News" class="w-20 h-20 rounded-lg object-cover flex-shrink-0">
          <div>
            <span class="text-[11px] text-gray-400 font-semibold">15/05/2024</span>
            <h4 class="text-sm font-bold text-gray-800 mt-1 leading-snug">Xu hướng kiến trúc nhôm kính 2024 với ZAVA cao cấp</h4>
          </div>
        </div>
        <div class="bg-white rounded-xl p-4 flex gap-4 shadow-sm">
          <img src="https://images.unsplash.com/photo-1486325212027-8081e485255e?w=150&q=80" alt="News" class="w-20 h-20 rounded-lg object-cover flex-shrink-0">
          <div>
            <span class="text-[11px] text-gray-400 font-semibold">10/05/2024</span>
            <h4 class="text-sm font-bold text-gray-800 mt-1 leading-snug">Tân Mỹ Group tham gia triển lãm Vietbuild Hà Nội 2024</h4>
          </div>
        </div>
      </div>

      <!-- Video Banner -->
      <div class="relative rounded-2xl overflow-hidden" style="background: #014289;">
        <div class="p-8 flex flex-col items-center justify-center text-center h-full">
          <div class="text-white/20 text-6xl font-black leading-none mb-6">TÂN MỸ</div>
          <h3 class="text-white font-black text-xl leading-tight mb-4">HÀNH TRÌNH<br>PHÁT TRIỂN</h3>
          <button onclick="alert('Video Tân Mỹ Group')" class="inline-flex items-center gap-2 bg-accent text-white font-bold px-6 py-3 rounded-lg hover:opacity-90 transition text-sm">
            <i class="fas fa-play"></i> Xem Video
          </button>
        </div>
      </div>
    </div>
  </div>
</section>
</main>

<!-- FOOTER -->
<footer id="contact" class="bg-[#111827] text-gray-400 pt-16 pb-0">
  <div class="max-w-7xl mx-auto px-4 lg:px-8">
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-8 lg:gap-10 pb-12">
      <!-- Col 1 -->
      <div class="lg:col-span-1">
        <div class="flex items-baseline gap-0 mb-4">
          <span class="text-2xl font-black tracking-widest" style="color:#014289">TÂN</span>
          <span class="text-2xl font-black tracking-widest" style="color:#ED1C24">MỸ</span>
          <span class="text-[10px] font-bold text-gray-500 ml-2">GROUP</span>
        </div>
        <p class="text-xs leading-relaxed mb-4">Công ty cổ phần tập đoàn Tân Mỹ - Đối tác tin cậy của mọi nhà.</p>
        <p class="text-xs mb-1"><i class="fas fa-map-marker-alt w-4 text-brand"></i> KCN Thạch Thất, Hà Nội</p>
        <p class="text-xs mb-1"><i class="fas fa-phone w-4 text-brand"></i> 0123 456 789</p>
        <p class="text-xs mb-4"><i class="fas fa-envelope w-4 text-brand"></i> info@tanmygroup.com.vn</p>
        <div class="flex gap-2">
          <a href="#" class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center hover:bg-brand transition text-sm"><i class="fab fa-facebook-f"></i></a>
          <a href="#" class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center hover:bg-brand transition text-sm"><i class="fab fa-youtube"></i></a>
          <a href="#" class="w-8 h-8 rounded-full bg-gray-700 flex items-center justify-center hover:bg-brand transition text-sm"><i class="fab fa-linkedin-in"></i></a>
        </div>
      </div>

      <!-- Col 2 -->
      <div>
        <h4 class="text-white font-bold text-sm mb-5 flex items-center gap-2"><span class="w-1 h-4 bg-brand rounded-full inline-block"></span> VỀ CHÚNG TÔI</h4>
        <ul class="space-y-2.5 text-xs">
          <li><a href="#" class="hover:text-white transition">Giới thiệu tổng quan</a></li>
          <li><a href="#" class="hover:text-white transition">Tầm nhìn - Sứ mệnh</a></li>
          <li><a href="#" class="hover:text-white transition">Năng lực sản xuất</a></li>
          <li><a href="#" class="hover:text-white transition">Sơ đồ tổ chức</a></li>
        </ul>
      </div>

      <!-- Col 3 -->
      <div>
        <h4 class="text-white font-bold text-sm mb-5 flex items-center gap-2"><span class="w-1 h-4 bg-brand rounded-full inline-block"></span> NHÔM TÂN MỸ</h4>
        <ul class="space-y-2.5 text-xs">
          <li><a href="#" class="hover:text-white transition">Hệ nhôm cao cấp ZAVA</a></li>
          <li><a href="#" class="hover:text-white transition">Nhôm thanh kiến trúc</a></li>
          <li><a href="#" class="hover:text-white transition">Nhôm định hình công nghiệp</a></li>
          <li><a href="#" class="hover:text-white transition">Catalogue sản phẩm</a></li>
        </ul>
      </div>

      <!-- Col 4 -->
      <div>
        <h4 class="text-white font-bold text-sm mb-5 flex items-center gap-2"><span class="w-1 h-4 bg-brand rounded-full inline-block"></span> GIA DỤNG TÂN MỸ</h4>
        <ul class="space-y-2.5 text-xs">
          <li><a href="#" class="hover:text-white transition">Bồn nước inox Tân Mỹ</a></li>
          <li><a href="#" class="hover:text-white transition">Bồn nhựa đa năng Tân Mỹ</a></li>
          <li><a href="#" class="hover:text-white transition">Bể tự hoại thông minh Septic</a></li>
          <li><a href="#" class="hover:text-white transition">Máy nước nóng NLMT</a></li>
        </ul>
      </div>

      <!-- Col 5 -->
      <div>
        <h4 class="text-white font-bold text-sm mb-5 flex items-center gap-2"><span class="w-1 h-4 bg-brand rounded-full inline-block"></span> ĐĂNG KÝ THÔNG TIN</h4>
        <p class="text-xs mb-4">Nhận thông tin khuyến mãi và sản phẩm mới nhất từ Tân Mỹ Group.</p>
        <div class="flex">
          <input type="email" placeholder="Email của bạn..." class="bg-gray-800 text-white text-xs px-4 py-2.5 rounded-l-lg w-full outline-none border border-gray-700 focus:border-brand">
          <button class="bg-brand text-white px-4 rounded-r-lg hover:opacity-90 transition"><i class="fas fa-paper-plane"></i></button>
        </div>
      </div>
    </div>

    <!-- Copyright -->
    <div class="border-t border-gray-800 py-5 flex flex-col lg:flex-row items-center justify-between text-[11px]">
      <p>© 2024 <strong class="text-white font-semibold">Tân Mỹ Group</strong>. All rights reserved.</p>
      <div class="flex gap-4 mt-2 lg:mt-0">
        <a href="#" class="hover:text-white transition">Chính sách bảo mật</a>
        <a href="#" class="hover:text-white transition">Điều khoản sử dụng</a>
      </div>
    </div>
  </div>
</footer>

<script>
  AOS.init({ duration: 800, once: true, offset: 100 });

  function toggleMobile() {
    const menu = document.getElementById('mobileMenu');
    const icon = document.querySelector('#mobileToggle i');
    menu.classList.toggle('hidden');
    if (menu.classList.contains('hidden')) {
      icon.className = 'fas fa-bars';
    } else {
      icon.className = 'fas fa-times';
    }
  }

  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', function() {
    if (window.scrollY > 50) {
      navbar.classList.add('nav-scrolled');
    } else {
      navbar.classList.remove('nav-scrolled');
    }
  });
</script>
</body>
</html>'''

import sys
with open('E:/webtanmy/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Written {len(html)} chars to index.html")
'''