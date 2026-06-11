import os, json

PAGES = [
    ('index',      'index.html',      'en/index.html',      'Trang chủ',       'Home'),
    ('gioi-thieu', 'gioi-thieu.html', 'en/about.html',      'Giới thiệu',      'About Us'),
    ('nhom-tan-my','nhom-tan-my.html','en/aluminum.html',   'Nhôm Tân Mỹ',     'Aluminum'),
    ('gia-dung',   'gia-dung.html',   'en/household.html',  'Gia dụng Tân Mỹ', 'Household'),
    ('du-an',      'du-an.html',      'en/projects.html',   'Dự án',           'Projects'),
    ('tin-tuc',    'tin-tuc.html',    'en/news.html',       'Tin tức',         'News'),
    ('lien-he',    'lien-he.html',    'en/contact.html',    'Liên hệ',         'Contact'),
]

TEMPLATE_HEAD = '''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
<script src="https://unpkg.com/swup@4/dist/swup.min.js"></script>
<script>
tailwind.config={{theme:{{fontFamily:{{sans:['Inter','sans-serif']}},extend:{{colors:{{brandBlue:'#014289',brandRed:'#ED1C24',darkBg:'#0f172a'}}}}}}}}
</script>
<style>
html{{scroll-behavior:smooth}}
.hero-mask{{background:linear-gradient(90deg,rgba(1,66,137,0.7) 0%,rgba(15,23,42,0.5) 100%)}}
.glass-nav{{background:rgba(255,255,255,0.93);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px)}}
.nav-scrolled{{box-shadow:0 4px 30px rgba(0,0,0,0.08)!important}}
.section-line{{width:60px;height:4px;background:#ED1C24;border-radius:2px;margin:.75rem auto 0}}
.footer-bar{{width:3px;height:18px;background:#014289;border-radius:2px;display:inline-block;margin-right:8px;vertical-align:middle}}
.float-panel{{transition:all 0.35s cubic-bezier(0.4,0,0.2,1);transform-origin:bottom right}}
.float-panel.show{{opacity:1;visibility:visible;transform:scale(1)}}
.float-panel.hide{{opacity:0;visibility:hidden;transform:scale(0.8)}}
.skiptranslate{{display:none!important}}
body{{top:0!important}}
.transition-fade{{transition:0.4s;opacity:1}}
html.is-animating .transition-fade{{opacity:0}}
.active-nav{{color:#014289!important;border-bottom:2px solid #014289}}
</style>
</head>
<body class="bg-gray-50 text-slate-800 font-sans antialiased overflow-x-hidden">
<div id="google_translate_element" style="position:absolute;left:-9999px;top:-9999px;width:1px;height:1px;overflow:hidden"></div>
'''

NAVBAR_TOP = '''
<nav id="navbar" class="fixed top-0 left-0 w-full z-50 glass-nav" style="transition:all 0.3s ease">
<div class="container mx-auto px-4 py-3 flex items-center justify-between">
<a href="{home_link}" class="flex items-center space-x-3">
<svg viewBox="0 0 550 120" class="h-12 w-auto" xmlns="http://www.w3.org/2000/svg">
<g transform="translate(5,5)"><rect width="110" height="110" fill="white" stroke="#014289" stroke-width="4"/><path d="M 4 80 Q 55 105 106 80 L 106 106 L 4 106 Z" fill="#014289"/><path d="M 4 106 Q 55 90 106 106 Z" fill="white"/><path d="M 55 10 L 25 90 Q 55 75 85 90 Z" fill="#F1C40F"/><path d="M 35 35 L 75 35 M 55 35 L 55 75" stroke="#ED1C24" stroke-width="8" stroke-linecap="square"/><text x="36" y="75" font-family="sans-serif" font-weight="900" font-size="34" fill="#ED1C24">M</text></g>
<text x="135" y="75" font-family="sans-serif" font-weight="900" font-size="82" fill="#014289" letter-spacing="-2">TANMY</text>
<text x="138" y="108" font-family="sans-serif" font-weight="500" font-size="28" fill="#ED1C24">{slogan}</text>
</svg></a>
<nav class="hidden lg:flex items-center space-x-6 text-xs font-black uppercase tracking-wider text-slate-700">
{nav_items}
</nav>
<div class="flex items-center space-x-4">
<button class="text-slate-600 hover:text-brandBlue transition"><i class="fa-solid fa-magnifying-glass"></i></button>
<div class="flex items-center space-x-2">
<a href="{vi_link}" title="Tiếng Việt"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAMAAABBPP0LAAAATlBMVEX+AAD2AADvAQH/eXn+cXL9amr8YmL9Wlr8UlL7TkvoAAD8d0f6Pz/3ODf2Ly/0KSf6R0f6wTv60T31IBz6+jr4+Cv3QybzEhL4bizhAADgATv8AAAAW0lEQVR4AQXBgU3DQBRAMb+7jwKVUPefkQEQTYJqByBENpKUGoZslXoN5LPONH8G9WWZ7pGlOn6XZmaGRce1J/seei4dl+7dPWDqkk7+58e3+igdlySPcYbwBG+lPhCjrtt9EgAAAABJRU5ErkJggg==" alt="VI" width="16" height="11"></a>
<a href="{en_link}" title="English"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAMAAABBPP0LAAAAt1BMVEWSmb66z+18msdig8La3u+tYX9IaLc7W7BagbmcUW+kqMr/q6n+//+hsNv/lIr/jIGMnNLJyOP9/fyQttT/wb3/////aWn+YWF5kNT0oqz0i4ueqtIZNJjhvt/8gn//WVr/6+rN1+o9RKZwgcMPJpX/VFT9UEn+RUX8Ozv2Ly+FGzdYZrfU1e/8LS/lQkG/mbVUX60AE231hHtcdMb0mp3qYFTFwNu3w9prcqSURGNDaaIUMX5FNW5wYt7AAAAAjklEQVR4AR3HNUJEMQCGwf+L8RR36ajR+1+CEuvRdd8kK9MNAiRQNgJmVDAt1yM6kSzYVJUsPNssAk5N7ZFKjVNFAY4co6TAOI+kyQm+LFUEBEKKzuWUNB7rSH/rSnvOulOGk+QlXTBqMIrfYX4tSe2nP3iRa/KNK7uTmWJ5a9+erZ3d+18od4ytiZdvZyuKWy8o3UpTVAAAAABJRU5ErkJggg==" alt="EN" width="16" height="11"></a>
</div>
<button id="mobile-menu-btn" class="lg:hidden text-slate-700 text-xl focus:outline-none"><i class="fa-solid fa-bars"></i></button>
</div></div>
<div id="mobile-menu" class="hidden lg:hidden bg-white border-t border-gray-100 px-4 py-4 space-y-3 font-bold text-sm shadow-inner">
{mobile_items}
</div>
</nav>
<div id="swup" class="transition-fade">
'''

FOOTER_TOP = '''
</div>
<footer class="bg-darkBg text-gray-300 pt-16 pb-6">
<div class="container mx-auto px-4">
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-8 mb-12">
<div class="lg:col-span-2">
<a href="{home_link}" class="inline-block mb-4">
<svg viewBox="0 0 550 120" class="h-10 w-auto" xmlns="http://www.w3.org/2000/svg">
<g transform="translate(5,5)"><rect width="110" height="110" fill="white" stroke="#014289" stroke-width="4"/><path d="M 4 80 Q 55 105 106 80 L 106 106 L 4 106 Z" fill="#014289"/><path d="M 4 106 Q 55 90 106 106 Z" fill="white"/><path d="M 55 10 L 25 90 Q 55 75 85 90 Z" fill="#F1C40F"/><path d="M 35 35 L 75 35 M 55 35 L 55 75" stroke="#ED1C24" stroke-width="8" stroke-linecap="square"/><text x="36" y="75" font-family="sans-serif" font-weight="900" font-size="34" fill="#ED1C24">M</text></g>
<text x="135" y="75" font-family="sans-serif" font-weight="900" font-size="82" fill="white" letter-spacing="-2">TANMY</text>
<text x="138" y="108" font-family="sans-serif" font-weight="500" font-size="28" fill="#ED1C24">{slogan}</text>
</svg></a>
<p class="text-sm text-gray-400 mb-4 leading-relaxed">{intro}</p>
<div class="space-y-2 text-sm">
<p><i class="fa-solid fa-location-dot text-brandRed w-5"></i> {address}</p>
<p><i class="fa-solid fa-phone text-brandRed w-5"></i> 024 32252752</p>
<p><i class="fa-solid fa-envelope text-brandRed w-5"></i> vanphongcongty@tanmygroup.com.vn</p>
</div>
<div class="flex space-x-3 mt-4">
<a href="#" class="w-9 h-9 rounded-full bg-gray-700 flex items-center justify-center hover:bg-brandBlue transition"><i class="fa-brands fa-facebook-f text-sm"></i></a>
<a href="#" class="w-9 h-9 rounded-full bg-gray-700 flex items-center justify-center hover:bg-brandBlue transition"><i class="fa-brands fa-youtube text-sm"></i></a>
<a href="#" class="w-9 h-9 rounded-full bg-gray-700 flex items-center justify-center hover:bg-brandBlue transition"><i class="fa-brands fa-tiktok text-sm"></i></a>
<a href="#" class="w-9 h-9 rounded-full bg-gray-700 flex items-center justify-center hover:bg-brandBlue transition"><i class="fa-brands fa-zalo text-sm"></i></a>
</div></div>
{FCOLUMNS}
</div>
<div class="border-t border-gray-700 pt-6 flex flex-col md:flex-row justify-between items-center text-xs text-gray-500">
<p>&copy; 2024 Tân Mỹ Group. All rights reserved.</p>
<div class="flex space-x-4 mt-2 md:mt-0"><a href="#" class="hover:text-white transition">{privacy}</a><a href="#" class="hover:text-white transition">{terms}</a></div>
</div></div></footer>
<div class="fixed bottom-6 right-6 z-40 flex flex-col items-end space-y-3">
<div id="floatPanel" class="float-panel hide bg-white rounded-2xl shadow-2xl p-3 w-56 border border-gray-100">
<button id="closeFloat" class="float-right text-gray-400 hover:text-gray-700 mb-2"><i class="fa-solid fa-xmark text-lg"></i></button>
<div class="space-y-1">
{a_phone}{a_messenger}{a_facebook}{a_email}
</div></div>
<button id="floatToggle" class="float-btn relative hover:scale-105 transition">
<img src="https://tawk.link/5865e574e7588f12124ea003/var/chat_bubble/15fad47ba0fc899390d661b427f7c12f8eb6d458" alt="Chat" class="h-auto w-[200px]">
</button></div>
'''

HEAD_SCRIPT = '''
<script>
document.cookie='googtrans=;path=/;expires=Thu, 01 Jan 1970 00:00:00 UTC';
function googleTranslateElementInit(){new google.translate.TranslateElement({pageLanguage:"vi",includedLanguages:"vi,en",layout:google.translate.TranslateElement.InlineLayout.SIMPLE,autoDisplay:false},"google_translate_element");}
var gs=document.createElement("script");gs.src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit";document.head.appendChild(gs);
AOS.init({duration:800,once:true,offset:100});
const navbar=document.getElementById("navbar");
window.addEventListener("scroll",function(){navbar.classList.toggle("nav-scrolled",window.scrollY>50);});
document.getElementById("mobile-menu-btn").addEventListener("click",function(){document.getElementById("mobile-menu").classList.toggle("hidden");});
const ft=document.getElementById("floatToggle"),fp=document.getElementById("floatPanel"),cf=document.getElementById("closeFloat");
ft.addEventListener("click",function(){fp.classList.toggle("hide");fp.classList.toggle("show");});
cf.addEventListener("click",function(){fp.classList.add("hide");fp.classList.remove("show");});
const swup=new Swup({containers:["#swup"],plugins:[],animateHistoryBrowsing:true});
swup.on("contentReplaced",function(){AOS.refresh();window.scrollTo(0,0);});
</script>
</body>
</html>
'''

def make(lang, active_key, body_html, title):
    is_en = lang == 'en'

    nav_items = ''
    for pk, vp, ep, lv, le in PAGES:
        href = ep if is_en else vp
        label = le if is_en else lv
        active = 'class="active-nav py-1"' if pk == active_key else 'class="hover:text-brandBlue transition py-1"'
        nav_items += f'<a href="{href}" {active}>{label}</a>\n'

    mobile_items = ''
    for pk, vp, ep, lv, le in PAGES:
        href = ep if is_en else vp
        label = le if is_en else lv
        cls = 'text-brandBlue' if pk == active_key else 'text-slate-700'
        mobile_items += f'<a href="{href}" class="block {cls} hover:text-brandBlue py-1.5 border-b border-gray-50">{label}</a>\n'

    home_link = 'en/index.html' if is_en else 'index.html'
    slogan = 'Enduring through time' if is_en else 'Tr\u01b0\u1eddng t\u1ed3n c\u00f9ng th\u1eddi gian'

    vi_link = vp if not is_en else ('../' + vp) if active_key == 'index' else '../' + vp
    # Actually, simpler approach:
    vi_link = ('../' if is_en else '') + vp
    en_link = ep

    # For index page, the vi_link should be 'index.html'
    if active_key == 'index':
        vi_link = 'index.html' if not is_en else '../index.html'

    intro = 'C\u00f4ng ty c\u1ed5 ph\u1ea7n t\u1eadp \u0111o\u00e0n T\u00e2n M\u1ef9 - \u0110\u1ed1i t\u00e1c tin c\u1eady c\u1ee7a m\u1ecdi nh\u00e0.' if not is_en else 'Tan My Group Corporation - Your trusted partner for every home.'
    address = 'S\u1ed1 77 L\u00ea V\u0103n H\u01b0u, Hai B\u00e0 Tr\u01b0ng, H\u00e0 N\u1ed9i' if not is_en else '77 Le Van Huu, Hai Ba Trung, Hanoi'
    privacy = 'Ch\u00ednh s\u00e1ch b\u1ea3o m\u1eadt' if not is_en else 'Privacy Policy'
    terms = '\u0110i\u1ec1u kho\u1ea3n s\u1eed d\u1ee5ng' if not is_en else 'Terms of Use'

    fcols = ''
    col_data = [
        ('V\u1ec0 CH\u00daNG T\u00d4I' if not is_en else 'ABOUT US',
         ['Gi\u1edbi thi\u1ec7u t\u1ed5ng quan','T\u1ea7m nh\u00ecn - S\u1ee9 m\u1ec7nh','N\u0103ng l\u1ef1c s\u1ea3n xu\u1ea5t','S\u01a1 \u0111\u1ed3 t\u1ed5 ch\u1ee9c'] if not is_en else ['Overview','Vision & Mission','Production Capacity','Organization']),
        ('NH\u00d4M T\u00c2N M\u1ef8' if not is_en else 'ALUMINUM',
         ['H\u1ec7 nh\u00f4m cao c\u1ea5p ZAVA','Nh\u00f4m thanh ki\u1ebfn tr\u00fac','Nh\u00f4m \u0111\u1ecbnh h\u00ecnh c\u00f4ng nghi\u1ec7p','Catalogue s\u1ea3n ph\u1ea9m'] if not is_en else ['ZAVA Premium System','Architectural Profiles','Industrial Profiles','Product Catalog']),
        ('GIA D\u1ee4NG T\u00c2N M\u1ef8' if not is_en else 'HOUSEHOLD',
         ['B\u1ed3n n\u01b0\u1edbc inox T\u00e2n M\u1ef9','B\u1ed3n nh\u1ef1a \u0111a n\u0103ng','B\u1ec3 t\u1ef1 ho\u1ea1i th\u00f4ng minh Septic','M\u00e1y n\u01b0\u1edbc n\u00f3ng NLMT'] if not is_en else ['Stainless Steel Tanks','Multi-purpose Plastic Tanks','Septic Tanks','Solar Water Heaters']),
    ]
    for ct, links in col_data:
        lis = ''.join(f'<li><a href="#" class="hover:text-white transition">{l}</a></li>' for l in links)
        fcols += f'<div><h4 class="text-white font-bold text-sm uppercase mb-4"><span class="footer-bar"></span>{ct}</h4><ul class="space-y-2 text-sm">{lis}</ul></div>'

    def al(label, icon, detail):
        return f'<a href="#" class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-blue-50 transition group"><div class="w-9 h-9 rounded-full bg-brandBlue flex items-center justify-center text-white group-hover:scale-105 transition"><i class="fa-solid {icon}"></i></div><div><div class="text-xs text-gray-400">{label}</div><div class="text-xs font-semibold text-gray-700">{detail}</div></div></a>'

    a_phone = al('G\u1ecdi ngay' if not is_en else 'Call now', 'fa-phone', '024 32252752')
    a_messenger = al('Chat Messenger', 'fa-brands fa-facebook-messenger', 'T\u00e2n M\u1ef9 Group' if not is_en else 'Tan My Group')
    a_facebook = al('Facebook', 'fa-brands fa-facebook', 'T\u00e2n M\u1ef9 Group' if not is_en else 'Tan My Group')
    a_email = al('Email', 'fa-envelope', 'G\u1eedi th\u01b0' if not is_en else 'Send mail')

    html = TEMPLATE_HEAD.format(lang=lang, title=title)
    html += NAVBAR_TOP.format(home_link=home_link, slogan=slogan, nav_items=nav_items, mobile_items=mobile_items, vi_link=vi_link, en_link=en_link)
    html += body_html
    html += FOOTER_TOP.format(home_link=home_link, slogan=slogan, intro=intro, address=address, FCOLUMNS=fcols, privacy=privacy, terms=terms, a_phone=a_phone, a_messenger=a_messenger, a_facebook=a_facebook, a_email=a_email)
    html += HEAD_SCRIPT
    return html

# ============ PAGE BODIES ============

HOME_VI = '''
<section class="relative min-h-screen flex items-center overflow-hidden">
<div class="absolute inset-0 bg-cover bg-center" style="background-image:url('https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1920&q=80');background-size:cover;"><div class="absolute inset-0 hero-mask"></div></div>
<div class="container mx-auto px-4 relative z-10">
<div class="grid lg:grid-cols-12 gap-8 items-stretch min-h-screen py-20">
<div class="lg:col-span-7 max-w-2xl flex flex-col justify-center">
<span class="text-brandRed font-black text-sm uppercase tracking-[.25em]">TH\u01af\u01a0NG HI\u1ec6U NH\u00d4M H\u00c0NG \u0110\u1ea6U</span>
<h1 class="text-4xl sm:text-5xl lg:text-6xl font-black text-white leading-tight mt-4 flex flex-col space-y-4"><span class="block">T\u00c2N M\u1ef8</span><span class="block">KI\u1ebeN T\u1ea0O GI\u00c1 TR\u1eca</span><span class="block">B\u1ec0N V\u1eeeNG T\u1eea NH\u00d4M VI\u1ec6T</span></h1>
<p class="text-gray-200 text-lg mt-6 max-w-xl leading-relaxed">Nh\u00e0 s\u1ea3n xu\u1ea5t nh\u00f4m \u0111\u1ecbnh h\u00ecnh, s\u1ea3n ph\u1ea9m gia d\u1ee5ng v\u00e0 gi\u1ea3i ph\u00e1p v\u1eadt li\u1ec7u x\u00e2y d\u1ef1ng h\u00e0ng \u0111\u1ea7u Vi\u1ec7t Nam.</p>
<div class="flex flex-wrap gap-4 mt-8"><a href="gioi-thieu.html" class="inline-flex items-center gap-2 bg-brandRed text-white px-6 py-3.5 rounded-xl font-bold text-sm hover:bg-red-700 transition shadow-lg hover:shadow-red-500/30">Kh\u00e1m ph\u00e1 nh\u00e0 m\u00e1y <i class="fa-solid fa-arrow-right"></i></a><a href="lien-he.html" class="inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm text-white border border-white/30 px-6 py-3.5 rounded-xl font-bold text-sm hover:bg-white/25 transition">Li\u00ean h\u1ec7 t\u01b0 v\u1ea5n <i class="fa-solid fa-phone"></i></a></div>
</div>
<div class="lg:col-span-5 flex items-center justify-center"><div class="relative w-full max-w-md aspect-video rounded-2xl overflow-hidden shadow-2xl border border-white/20" data-aos="fade-left"><div class="absolute inset-0 bg-gradient-to-br from-brandBlue/40 to-darkBg/60 flex items-center justify-center"><div class="text-center"><div class="w-16 h-16 rounded-full bg-white/20 backdrop-blur flex items-center justify-center mx-auto mb-3 pulse-ring cursor-pointer hover:bg-white/30 transition"><i class="fa-solid fa-play text-white text-xl ml-1"></i></div><p class="text-white text-sm font-semibold">Xem Video Gi\u1edbi Thi\u1ec7u</p></div></div></div></div>
</div></div></section>
<section class="py-16 bg-white"><div class="container mx-auto px-4"><div class="grid grid-cols-2 md:grid-cols-5 gap-6" data-aos="fade-up">METRICS_VI</div></div></section>
<section id="about" class="py-20 bg-gray-50"><div class="container mx-auto px-4"><div class="text-center mb-14" data-aos="fade-up"><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">GI\u1edaI THI\u1ec6U</span><h2 class="text-3xl lg:text-4xl font-black text-darkBg mt-2">V\u1ec0 T\u00c2N M\u1ef8 GROUP</h2><div class="section-line"></div><p class="text-gray-500 max-w-2xl mx-auto mt-4">Ti\u00ean phong trong ng\u00e0nh nh\u00f4m \u0111\u1ecbnh h\u00ecnh v\u00e0 gia d\u1ee5ng, cam k\u1ebft ch\u1ea5t l\u01b0\u1ee3ng v\u00e0 \u0111\u1ed5i m\u1edbi kh\u00f4ng ng\u1eebng.</p></div>
<div class="grid md:grid-cols-2 gap-12 items-center" data-aos="fade-up"><div class="rounded-2xl overflow-hidden shadow-xl"><img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=800&q=80" alt="Factory" class="w-full h-80 object-cover"></div><div><p class="text-gray-600 leading-relaxed">T\u00e2n M\u1ef9 Group th\u00e0nh l\u1eadp t\u1eeb n\u0103m 1999, l\u00e0 m\u1ed9t trong nh\u1eefng doanh nghi\u1ec7p h\u00e0ng \u0111\u1ea7u Vi\u1ec7t Nam trong l\u0129nh v\u1ef1c s\u1ea3n xu\u1ea5t nh\u00f4m \u0111\u1ecbnh h\u00ecnh, b\u1ed3n n\u01b0\u1edbc inox, b\u1ed3n nh\u1ef1a, b\u1ec3 t\u1ef1 ho\u1ea1i Septic, ch\u1eadu r\u1eeda inox v\u00e0 m\u00e1y n\u01b0\u1edbc n\u00f3ng n\u0103ng l\u01b0\u1ee3ng m\u1eb7t tr\u1eddi.</p>
<p class="text-gray-600 leading-relaxed mt-4">V\u1edbi h\u1ec7 th\u1ed1ng nh\u00e0 m\u00e1y hi\u1ec7n \u0111\u1ea1i t\u1ea1i Vi\u1ec7t Nam, T\u00e2n M\u1ef9 cung c\u1ea5p c\u00e1c s\u1ea3n ph\u1ea9m ch\u1ea5t l\u01b0\u1ee3ng cao, \u0111\u00e1p \u1ee9ng ti\u00eau chu\u1ea9n qu\u1ed1c t\u1ebf.</p>
<div class="grid grid-cols-3 gap-4 mt-8"><div><div class="text-2xl font-black text-brandRed">25+</div><div class="text-xs text-gray-500">N\u0103m KN</div></div><div><div class="text-2xl font-black text-brandRed">50K+</div><div class="text-xs text-gray-500">T\u1ea5n/n\u0103m</div></div><div><div class="text-2xl font-black text-brandRed">1K+</div><div class="text-xs text-gray-500">\u0110\u1ea1i l\u00fd</div></div></div>
<a href="gioi-thieu.html" class="inline-flex items-center gap-2 mt-6 bg-brandBlue text-white px-5 py-3 rounded-xl font-bold text-sm hover:bg-blue-800 transition">T\u00ecm hi\u1ec3u th\u00eam <i class="fa-solid fa-arrow-right"></i></a></div></div></div></section>
<section id="products" class="py-20 bg-white"><div class="container mx-auto px-4"><div class="text-center mb-14" data-aos="fade-up"><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">S\u1ea2N PH\u1ea8M</span><h2 class="text-3xl lg:text-4xl font-black text-darkBg mt-2">DANH M\u1ee4C S\u1ea2N PH\u1ea8M</h2><div class="section-line"></div></div>
<div class="grid md:grid-cols-2 gap-8"><div class="rounded-2xl overflow-hidden shadow-xl group cursor-pointer" data-aos="fade-right"><div class="h-64 bg-gradient-to-br from-blue-900 to-slate-800 relative overflow-hidden"><img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=600&q=80" class="w-full h-full object-cover opacity-40 group-hover:scale-105 transition duration-700"><div class="absolute inset-0 flex items-center justify-center"><div class="text-center text-white"><div class="text-3xl font-black mb-2">Th\u01b0\u01a1ng hi\u1ec7u ZAVA</div><div class="text-xl font-bold opacity-90">Nh\u00f4m T\u00e2n M\u1ef9 - ZAVA</div></div></div></div><div class="p-6"><ul class="space-y-2 text-sm text-gray-600"><li class="flex items-center gap-2"><i class="fa-solid fa-check-circle text-brandRed text-xs"></i>H\u1ec7 nh\u00f4m ki\u1ebfn tr\u00fac ZAVA cao c\u1ea5p</li><li class="flex items-center gap-2"><i class="fa-solid fa-check-circle text-brandRed text-xs"></i>Nh\u00f4m thanh \u0111\u1ecbnh h\u00ecnh c\u00f4ng nghi\u1ec7p</li><li class="flex items-center gap-2"><i class="fa-solid fa-check-circle text-brandRed text-xs"></i>H\u1ec7 nh\u00f4m x\u00e2y d\u1ef1ng ti\u00eau chu\u1ea9n</li></ul><a href="nhom-tan-my.html" class="inline-flex items-center gap-2 mt-4 text-brandRed font-bold text-sm hover:gap-3 transition">Kh\u00e1m ph\u00e1 ng\u00e0nh nh\u00f4m <i class="fa-solid fa-arrow-right"></i></a></div></div>
<div class="rounded-2xl overflow-hidden shadow-xl group cursor-pointer" data-aos="fade-left"><div class="h-64 bg-gradient-to-br from-orange-700 to-yellow-600 relative overflow-hidden"><img src="https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=600&q=80" class="w-full h-full object-cover opacity-40 group-hover:scale-105 transition duration-700"><div class="absolute inset-0 flex items-center justify-center"><div class="text-center text-white"><div class="text-3xl font-black mb-2">Gia d\u1ee5ng cao c\u1ea5p</div><div class="text-xl font-bold opacity-90">Gia d\u1ee5ng T\u00e2n M\u1ef9</div></div></div></div><div class="p-6"><ul class="space-y-2 text-sm text-gray-600"><li class="flex items-center gap-2"><i class="fa-solid fa-check-circle text-brandRed text-xs"></i>B\u1ed3n n\u01b0\u1edbc Inox</li><li class="flex items-center gap-2"><i class="fa-solid fa-check-circle text-brandRed text-xs"></i>B\u1ed3n nh\u1ef1a \u0111a n\u0103ng</li><li class="flex items-center gap-2"><i class="fa-solid fa-check-circle text-brandRed text-xs"></i>B\u1ec3 ph\u1ed1t th\u00f4ng minh SEPTIC</li><li class="flex items-center gap-2"><i class="fa-solid fa-check-circle text-brandRed text-xs"></i>M\u00e1y n\u01b0\u1edbc n\u00f3ng NLMT</li></ul><a href="gia-dung.html" class="inline-flex items-center gap-2 mt-4 text-brandRed font-bold text-sm hover:gap-3 transition">Kh\u00e1m ph\u00e1 s\u1ea3n ph\u1ea9m <i class="fa-solid fa-arrow-right"></i></a></div></div></div></div></section>
<section class="py-20 bg-gray-50"><div class="container mx-auto px-4"><div class="text-center mb-14" data-aos="fade-up"><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">QUY TR\u00ccNH</span><h2 class="text-3xl lg:text-4xl font-black text-darkBg mt-2">Quy tr\u00ecnh s\u1ea3n xu\u1ea5t hi\u1ec7n \u0111\u1ea1i</h2><div class="section-line"></div></div><div class="grid grid-cols-1 sm:grid-cols-3 lg:grid-cols-5 gap-6" data-aos="fade-up">PROCESS_VI</div></div></section>
<section class="py-20 bg-white"><div class="container mx-auto px-4"><div class="grid md:grid-cols-2 gap-12" data-aos="fade-up"><div><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">CH\u1ee8NG NH\u1eacN</span><h3 class="text-2xl font-black text-darkBg mt-2">Ch\u1ee9ng nh\u1eadn ch\u1ea5t l\u01b0\u1ee3ng</h3><p class="text-gray-500 text-sm mt-3 mb-6">C\u00e1c ch\u1ee9ng ch\u1ec9 v\u00e0 gi\u1ea3i th\u01b0\u1edfng kh\u1eb3ng \u0111\u1ecbnh ch\u1ea5t l\u01b0\u1ee3ng s\u1ea3n ph\u1ea9m d\u1ecbch v\u1ee5.</p><div class="grid grid-cols-2 gap-4">CERTS_VI</div></div>
<div><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">D\u1ef0 \u00c1N</span><h3 class="text-2xl font-black text-darkBg mt-2">D\u1ef1 \u00e1n ti\u00eau bi\u1ec3u</h3><a href="du-an.html" class="text-xs text-brandRed font-bold hover:underline">XEM T\u1ea4T C\u1ea2 <i class="fa-solid fa-arrow-right"></i></a><div class="grid grid-cols-2 gap-4 mt-4">PROJECTS_VI</div></div></div></div></section>
<section id="news" class="py-20 bg-gray-50"><div class="container mx-auto px-4"><div class="text-center mb-14" data-aos="fade-up"><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">TIN T\u1ee8C</span><h2 class="text-3xl lg:text-4xl font-black text-darkBg mt-2">Tin t\u1ee9c n\u1ed5i b\u1eadt</h2><div class="section-line"></div></div>
<div class="grid md:grid-cols-3 gap-8" data-aos="fade-up"><div class="bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-lg transition group"><div class="h-48 overflow-hidden"><img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=600&q=80" class="w-full h-full object-cover group-hover:scale-105 transition duration-700"></div><div class="p-5"><div class="text-xs text-gray-400 mb-2">20/05/2024</div><h4 class="font-bold text-darkBg text-sm mb-3">T\u00e2n M\u1ef9 kh\u00e1nh th\u00e0nh d\u00e2y chuy\u1ec1n s\u01a1n t\u0129nh \u0111i\u1ec7n \u0111\u1ee9ng c\u00f4ng ngh\u1ec7 cao</h4><a href="tin-tuc.html" class="text-brandRed text-xs font-bold hover:underline">Xem chi ti\u1ebft <i class="fa-solid fa-arrow-right"></i></a></div></div>
<div class="space-y-6">NEWS_SIDE_VI</div>
<div class="bg-gradient-to-br from-brandBlue to-darkBg rounded-2xl p-8 text-white flex flex-col justify-center items-center text-center shadow-xl" data-aos="zoom-in"><div class="text-4xl font-black mb-2">T\u00c2N M\u1ef8</div><div class="text-lg font-bold opacity-90 mb-4">H\u00e0nh tr\u00ecnh ph\u00e1t tri\u1ec3n</div><div class="w-16 h-16 rounded-full bg-white/20 backdrop-blur flex items-center justify-center pulse-ring cursor-pointer"><i class="fa-solid fa-play text-white text-xl ml-1"></i></div></div></div></div></section>
'''

HOME_EN = '''
<section class="relative min-h-screen flex items-center overflow-hidden">
<div class="absolute inset-0 bg-cover bg-center" style="background-image:url('https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1920&q=80');background-size:cover;"><div class="absolute inset-0 hero-mask"></div></div>
<div class="container mx-auto px-4 relative z-10">
<div class="grid lg:grid-cols-12 gap-8 items-stretch min-h-screen py-20">
<div class="lg:col-span-7 max-w-2xl flex flex-col justify-center">
<span class="text-brandRed font-black text-sm uppercase tracking-[.25em]">LEADING ALUMINUM BRAND</span>
<h1 class="text-4xl sm:text-5xl lg:text-6xl font-black text-white leading-tight mt-4 flex flex-col space-y-4"><span class="block">TAN MY</span><span class="block">CREATING VALUE</span><span class="block">SUSTAINABLY FROM VIETNAM</span></h1>
<p class="text-gray-200 text-lg mt-6 max-w-xl leading-relaxed">Vietnam's leading manufacturer of aluminum profiles, household products, and building material solutions.</p>
<div class="flex flex-wrap gap-4 mt-8"><a href="about.html" class="inline-flex items-center gap-2 bg-brandRed text-white px-6 py-3.5 rounded-xl font-bold text-sm hover:bg-red-700 transition shadow-lg hover:shadow-red-500/30">Explore Factory <i class="fa-solid fa-arrow-right"></i></a><a href="contact.html" class="inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm text-white border border-white/30 px-6 py-3.5 rounded-xl font-bold text-sm hover:bg-white/25 transition">Get a Quote <i class="fa-solid fa-phone"></i></a></div>
</div>
<div class="lg:col-span-5 flex items-center justify-center"><div class="relative w-full max-w-md aspect-video rounded-2xl overflow-hidden shadow-2xl border border-white/20" data-aos="fade-left"><div class="absolute inset-0 bg-gradient-to-br from-brandBlue/40 to-darkBg/60 flex items-center justify-center"><div class="text-center"><div class="w-16 h-16 rounded-full bg-white/20 backdrop-blur flex items-center justify-center mx-auto mb-3 pulse-ring cursor-pointer hover:bg-white/30 transition"><i class="fa-solid fa-play text-white text-xl ml-1"></i></div><p class="text-white text-sm font-semibold">Watch Intro Video</p></div></div></div></div>
</div></div></section>
<section class="py-16 bg-white"><div class="container mx-auto px-4"><div class="grid grid-cols-2 md:grid-cols-5 gap-6" data-aos="fade-up">METRICS_EN</div></div></section>
<section id="about" class="py-20 bg-gray-50"><div class="container mx-auto px-4"><div class="text-center mb-14" data-aos="fade-up"><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">ABOUT US</span><h2 class="text-3xl lg:text-4xl font-black text-darkBg mt-2">ABOUT TAN MY GROUP</h2><div class="section-line"></div><p class="text-gray-500 max-w-2xl mx-auto mt-4">Pioneering in aluminum profiles and household products, committed to quality and continuous innovation.</p></div>
<div class="grid md:grid-cols-2 gap-12 items-center" data-aos="fade-up"><div class="rounded-2xl overflow-hidden shadow-xl"><img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=800&q=80" alt="Factory" class="w-full h-80 object-cover"></div><div><p class="text-gray-600 leading-relaxed">Founded in 1999, Tan My Group is one of Vietnam's leading enterprises in manufacturing aluminum profiles, stainless steel water tanks, plastic tanks, Septic tanks, stainless steel sinks, and solar water heaters.</p>
<p class="text-gray-600 leading-relaxed mt-4">With modern factory systems in Vietnam, Tan My provides high-quality products meeting international standards.</p>
<div class="grid grid-cols-3 gap-4 mt-8"><div><div class="text-2xl font-black text-brandRed">25+</div><div class="text-xs text-gray-500">Years Exp</div></div><div><div class="text-2xl font-black text-brandRed">50K+</div><div class="text-xs text-gray-500">Tons/yr</div></div><div><div class="text-2xl font-black text-brandRed">1K+</div><div class="text-xs text-gray-500">Dealers</div></div></div>
<a href="about.html" class="inline-flex items-center gap-2 mt-6 bg-brandBlue text-white px-5 py-3 rounded-xl font-bold text-sm hover:bg-blue-800 transition">Learn More <i class="fa-solid fa-arrow-right"></i></a></div></div></div></section>
<section id="products" class="py-20 bg-white"><div class="container mx-auto px-4"><div class="text-center mb-14" data-aos="fade-up"><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">PRODUCTS</span><h2 class="text-3xl lg:text-4xl font-black text-darkBg mt-2">PRODUCT CATEGORIES</h2><div class="section-line"></div></div>
<div class="grid md:grid-cols-2 gap-8"><div class="rounded-2xl overflow-hidden shadow-xl group cursor-pointer" data-aos="fade-right"><div class="h-64 bg-gradient-to-br from-blue-900 to-slate-800 relative overflow-hidden"><img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=600&q=80" class="w-full h-full object-cover opacity-40 group-hover:scale-105 transition duration-700"><div class="absolute inset-0 flex items-center justify-center"><div class="text-center text-white"><div class="text-3xl font-black mb-2">ZAVA Brand</div><div class="text-xl font-bold opacity-90">Tan My Aluminum - ZAVA</div></div></div></div><div class="p-6"><ul class="space-y-2 text-sm text-gray-600"><li class="flex items-center gap-2"><i class="fa-solid fa-check-circle text-brandRed text-xs"></i>Premium ZAVA architectural systems</li><li class="flex items-center gap-2"><i class="fa-solid fa-check-circle text-brandRed text-xs"></i>Industrial aluminum profiles</li><li class="flex items-center gap-2"><i class="fa-solid fa-check-circle text-brandRed text-xs"></i>Standard construction systems</li></ul><a href="aluminum.html" class="inline-flex items-center gap-2 mt-4 text-brandRed font-bold text-sm hover:gap-3 transition">Explore Aluminum <i class="fa-solid fa-arrow-right"></i></a></div></div>
<div class="rounded-2xl overflow-hidden shadow-xl group cursor-pointer" data-aos="fade-left"><div class="h-64 bg-gradient-to-br from-orange-700 to-yellow-600 relative overflow-hidden"><img src="https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=600&q=80" class="w-full h-full object-cover opacity-40 group-hover:scale-105 transition duration-700"><div class="absolute inset-0 flex items-center justify-center"><div class="text-center text-white"><div class="text-3xl font-black mb-2">Premium Household</div><div class="text-xl font-bold opacity-90">Tan My Household</div></div></div></div><div class="p-6"><ul class="space-y-2 text-sm text-gray-600"><li class="flex items-center gap-2"><i class="fa-solid fa-check-circle text-brandRed text-xs"></i>Stainless Steel Tanks</li><li class="flex items-center gap-2"><i class="fa-solid fa-check-circle text-brandRed text-xs"></i>Multi-purpose Plastic Tanks</li><li class="flex items-center gap-2"><i class="fa-solid fa-check-circle text-brandRed text-xs"></i>Smart Septic Tanks</li><li class="flex items-center gap-2"><i class="fa-solid fa-check-circle text-brandRed text-xs"></i>Solar Water Heaters</li></ul><a href="household.html" class="inline-flex items-center gap-2 mt-4 text-brandRed font-bold text-sm hover:gap-3 transition">Explore Products <i class="fa-solid fa-arrow-right"></i></a></div></div></div></div></section>
<section class="py-20 bg-gray-50"><div class="container mx-auto px-4"><div class="text-center mb-14" data-aos="fade-up"><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">PROCESS</span><h2 class="text-3xl lg:text-4xl font-black text-darkBg mt-2">Modern Production Process</h2><div class="section-line"></div></div><div class="grid grid-cols-1 sm:grid-cols-3 lg:grid-cols-5 gap-6" data-aos="fade-up">PROCESS_EN</div></div></section>
<section class="py-20 bg-white"><div class="container mx-auto px-4"><div class="grid md:grid-cols-2 gap-12" data-aos="fade-up"><div><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">CERTIFICATIONS</span><h3 class="text-2xl font-black text-darkBg mt-2">Quality Certifications</h3><p class="text-gray-500 text-sm mt-3 mb-6">Certificates and awards affirming product and service quality.</p><div class="grid grid-cols-2 gap-4">CERTS_EN</div></div>
<div><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">PROJECTS</span><h3 class="text-2xl font-black text-darkBg mt-2">Featured Projects</h3><a href="projects.html" class="text-xs text-brandRed font-bold hover:underline">VIEW ALL <i class="fa-solid fa-arrow-right"></i></a><div class="grid grid-cols-2 gap-4 mt-4">PROJECTS_EN</div></div></div></div></section>
<section id="news" class="py-20 bg-gray-50"><div class="container mx-auto px-4"><div class="text-center mb-14" data-aos="fade-up"><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">NEWS</span><h2 class="text-3xl lg:text-4xl font-black text-darkBg mt-2">Featured News</h2><div class="section-line"></div></div>
<div class="grid md:grid-cols-3 gap-8" data-aos="fade-up"><div class="bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-lg transition group"><div class="h-48 overflow-hidden"><img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=600&q=80" class="w-full h-full object-cover group-hover:scale-105 transition duration-700"></div><div class="p-5"><div class="text-xs text-gray-400 mb-2">May 20, 2024</div><h4 class="font-bold text-darkBg text-sm mb-3">Tan My inaugurates high-tech powder coating line</h4><a href="news.html" class="text-brandRed text-xs font-bold hover:underline">Read more <i class="fa-solid fa-arrow-right"></i></a></div></div>
<div class="space-y-6">NEWS_SIDE_EN</div>
<div class="bg-gradient-to-br from-brandBlue to-darkBg rounded-2xl p-8 text-white flex flex-col justify-center items-center text-center shadow-xl" data-aos="zoom-in"><div class="text-4xl font-black mb-2">TAN MY</div><div class="text-lg font-bold opacity-90 mb-4">Development Journey</div><div class="w-16 h-16 rounded-full bg-white/20 backdrop-blur flex items-center justify-center pulse-ring cursor-pointer"><i class="fa-solid fa-play text-white text-xl ml-1"></i></div></div></div></div></section>
'''

def metrics(items):
    return ''.join(f'<div class="text-center p-6 rounded-xl bg-gray-50 hover:bg-brandBlue hover:text-white transition group"><div class="text-3xl font-black text-brandRed group-hover:text-white transition">{n}</div><div class="text-xs font-bold uppercase mt-1 tracking-wider">{l}</div></div>' for n,l in items)

def process(items):
    return ''.join(f'<div class="text-center p-6 bg-white rounded-xl shadow-sm hover:shadow-lg transition"><div class="w-12 h-12 rounded-full bg-brandRed text-white flex items-center justify-center font-black text-lg mx-auto mb-4">{n}</div><h4 class="font-bold text-darkBg text-sm mb-2">{t}</h4><p class="text-xs text-gray-500">{d}</p></div>' for n,t,d in items)

def certs(items):
    return ''.join(f'<div class="p-4 border border-gray-200 rounded-xl text-center hover:border-brandBlue transition"><div class="font-black text-brandBlue text-sm">{c}</div><div class="text-xs text-gray-500 mt-1">{d}</div></div>' for c,d in items)

def projects(items):
    return ''.join(f'<div class="project-card rounded-xl overflow-hidden shadow-sm group cursor-pointer"><div class="h-36 overflow-hidden"><img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=400&q=80" class="w-full h-full object-cover"></div><div class="p-3 bg-white"><div class="text-xs font-bold text-darkBg">{p}</div></div></div>' for p in items)

def news_side(items):
    return ''.join(f'<div class="flex gap-4 bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition"><div class="w-20 h-20 rounded-lg overflow-hidden flex-shrink-0"><img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=200&q=80" class="w-full h-full object-cover"></div><div><div class="text-xs text-gray-400">{d}</div><div class="text-sm font-bold text-darkBg leading-snug">{t}</div></div></div>' for d,t in items)

def make_home(lang):
    is_en = lang == 'en'
    if is_en:
        m = metrics([('25+','Years Experience'),('50K+','Tons/year'),('1K+','Dealers'),('63','Provinces'),('\U0001f30d','Export')])
        p = process([('1','Billet Material','Imported aluminum alloy meeting international standards.'),('2','Extrusion System','High-pressure extrusion machines shape profiles precisely.'),('3','Powder Coating','Surface coating with durable anti-oxidation adhesion.'),('4','Quality Control','QA/QC team rigorously measures technical specs.'),('5','Packaging','Protective film wrapping and warehouse storage.')])
        c = certs([('ISO9001:2015','Quality Management'),('QUATEST3','Quality Testing'),('QUALICOAT','Powder Coating'),('EURO','Export Standards')])
        pj = projects(['Vinhomes Ocean Park','Sunshine City','FLC Quy Nhon Resort','Luxury Villas'])
        ns = news_side([('May 15, 2024','2024 glass-aluminum trends with ZAVA'),('May 10, 2024','Tan My at Vietbuild Hanoi 2024')])
        body = HOME_EN.replace('METRICS_EN',m).replace('PROCESS_EN',p).replace('CERTS_EN',c).replace('PROJECTS_EN',pj).replace('NEWS_SIDE_EN',ns)
        title = 'Tan My Group - Premium Aluminum & Smart Home Solution'
    else:
        m = metrics([('25+','N\u0103m kinh nghi\u1ec7m'),('50.000+','T\u1ea5n nh\u00f4m/n\u0103m'),('1.000+','\u0110\u1ea1i l\u00fd & \u0111\u1ed1i t\u00e1c'),('63','T\u1ec9nh th\u00e0nh'),('\U0001f30d','Xu\u1ea5t kh\u1ea9u')])
        p = process([('1','Nguy\u00ean li\u1ec7u Billet','H\u1ee3p kim nh\u00f4m nh\u1eadp kh\u1ea9u \u0111\u1ea1t ch\u1ea5t l\u01b0\u1ee3ng qu\u1ed1c t\u1ebf.'),('2','H\u1ec7 th\u1ed1ng \u0111\u00f9n \u00e9p','M\u00e1y \u0111\u00f9n \u00e9p \u00e1p l\u1ef1c cao t\u1ea1o h\u00ecnh thanh nh\u00f4m ch\u00ednh x\u00e1c.'),('3','X\u1eed l\u00fd s\u01a1n t\u0129nh \u0111i\u1ec7n','Ph\u1ee7 b\u1ec1 m\u1eb7t h\u1ea1t s\u01a1n b\u00e1m d\u00ednh ch\u1eafc ch\u1eafn, ch\u1ed1ng oxy h\u00f3a.'),('4','Ki\u1ec3m \u0111\u1ecbnh ch\u1ea5t l\u01b0\u1ee3ng','\u0110\u1ed9i ng\u0169 QA/QC \u0111o \u0111\u1ea1c th\u00f4ng s\u1ed1 k\u1ef9 thu\u1eadt nghi\u00eam ng\u1eb7t.'),('5','Th\u00e0nh ph\u1ea9m \u0111\u00f3ng g\u00f3i','\u0110\u00f3ng b\u1ecdc m\u00e0ng b\u1ea3o v\u1ec7 v\u00e0 l\u01b0u kho xu\u1ea5t x\u01b0\u1edfng ph\u00e2n ph\u1ed1i.')])
        c = certs([('ISO9001:2015','Qu\u1ea3n l\u00fd ch\u1ea5t l\u01b0\u1ee3ng'),('QUATEST3','Ki\u1ec3m \u0111\u1ecbnh CL'),('QUALICOAT','S\u01a1n t\u0129nh \u0111i\u1ec7n'),('EURO','Ti\u00eau chu\u1ea9n Xu\u1ea5t kh\u1ea9u')])
        pj = projects(['Vinhomes Ocean Park','Sunshine City','FLC Quy Nh\u01a1n Resort','Bi\u1ec7t th\u1ef1 cao c\u1ea5p'])
        ns = news_side([('15/05/2024','Xu h\u01b0\u1edbng ki\u1ebfn tr\u00fac nh\u00f4m k\u00ednh 2024 v\u1edbi ZAVA'),('10/05/2024','T\u00e2n M\u1ef9 Group tham gia tri\u1ec3n l\u00e3m Vietbuild H\u00e0 N\u1ed9i 2024')])
        body = HOME_VI.replace('METRICS_VI',m).replace('PROCESS_VI',p).replace('CERTS_VI',c).replace('PROJECTS_VI',pj).replace('NEWS_SIDE_VI',ns)
        title = 'T\u00e2n M\u1ef9 Group - Ki\u1ebfn T\u1ea1o Gi\u00e1 Tr\u1ecb B\u1ec1n V\u1eefng T\u1eeb Nh\u00f4m Vi\u1ec7t'
    return make(lang, 'index', body, title)

def make_about(lang):
    is_en = lang == 'en'
    if is_en:
        body = '<section class="relative pt-28 pb-16 overflow-hidden"><div class="absolute inset-0 bg-cover bg-center" style="background-image:url(\'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1920&q=80\');background-size:cover;"><div class="absolute inset-0 hero-mask"></div></div><div class="container mx-auto px-4 relative z-10 text-center"><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">BRAND STORY</span><h1 class="text-4xl lg:text-5xl font-black text-white mt-3">About Tan My Group</h1><p class="text-gray-300 max-w-2xl mx-auto mt-4">25 years of creating sustainable value from Vietnamese aluminum.</p></div></section><section class="py-20 bg-white"><div class="container mx-auto px-4 max-w-4xl"><div class="relative" data-aos="fade-up">' + ''.join(f'<div class="flex gap-6 mb-12"><div class="flex flex-col items-center"><div class="w-8 h-8 rounded-full bg-brandRed text-white flex items-center justify-center font-black text-sm flex-shrink-0">{y}</div><div class="w-0.5 h-full bg-gray-200 mt-2"></div></div><div><div class="text-xs text-brandRed font-bold">{d}</div><h3 class="text-lg font-black text-darkBg mt-1">{t}</h3><p class="text-sm text-gray-600 mt-1">{p}</p></div></div>' for y,t,p,d in [('1999','1999','Founded','Tan My was established.'),('2005','2005','Expansion','Modern extrusion lines, 10K tons/yr.'),('2010','2010','ZAVA Launch','Premium ZAVA brand launched.'),('2015','2015','ISO 9001:2015','Quality management certified.'),('2020','2020','50K+ Capacity','Expanded to 50K+ tons/yr.'),('2024','2024','Market Leader','#1 aluminum & household brand.')]) + '</div></div></section>'
        title = 'About Tan My Group | 25+ Years of Aluminum Excellence'
    else:
        body = '<section class="relative pt-28 pb-16 overflow-hidden"><div class="absolute inset-0 bg-cover bg-center" style="background-image:url(\'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1920&q=80\');background-size:cover;"><div class="absolute inset-0 hero-mask"></div></div><div class="container mx-auto px-4 relative z-10 text-center"><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">C\u00c2U CHUY\u1ec6N TH\u01af\u01a0NG HI\u1ec6U</span><h1 class="text-4xl lg:text-5xl font-black text-white mt-3">V\u1ec1 T\u00e2n M\u1ef9 Group</h1><p class="text-gray-300 max-w-2xl mx-auto mt-4">25 n\u0103m ki\u1ebfn t\u1ea1o gi\u00e1 tr\u1ecb b\u1ec1n v\u1eefng t\u1eeb nh\u00f4m Vi\u1ec7t.</p></div></section><section class="py-20 bg-white"><div class="container mx-auto px-4 max-w-4xl"><div class="relative" data-aos="fade-up">' + ''.join(f'<div class="flex gap-6 mb-12"><div class="flex flex-col items-center"><div class="w-8 h-8 rounded-full bg-brandRed text-white flex items-center justify-center font-black text-sm flex-shrink-0">{y}</div><div class="w-0.5 h-full bg-gray-200 mt-2"></div></div><div><div class="text-xs text-brandRed font-bold">{d}</div><h3 class="text-lg font-black text-darkBg mt-1">{t}</h3><p class="text-sm text-gray-600 mt-1">{p}</p></div></div>' for y,t,p,d in [('1999','1999','Th\u00e0nh l\u1eadp','T\u00e2n M\u1ef9 Group \u0111\u01b0\u1ee3c th\u00e0nh l\u1eadp.'),('2005','2005','M\u1edf r\u1ed9ng','\u0110\u1ea7u t\u01b0 d\u00e2y chuy\u1ec1n \u0111\u00f9n \u00e9p hi\u1ec7n \u0111\u1ea1i.'),('2010','2010','Ra m\u1eaft ZAVA','Th\u01b0\u01a1ng hi\u1ec7u ZAVA ra m\u1eaft.'),('2015','2015','Ch\u1ee9ng nh\u1eadn ISO','\u0110\u1ea1t ISO 9001:2015.'),('2020','2020','C\u00f4ng su\u1ea5t 50K+','N\u00e2ng c\u00f4ng su\u1ea5t 50.000+ t\u1ea5n/n\u0103m.'),('2024','2024','D\u1eabn \u0111\u1ea7u','V\u1ecb th\u1ebf s\u1ed1 1 ng\u00e0nh nh\u00f4m.')]) + '</div></div></section>'
        title = 'Gi\u1edbi thi\u1ec7u T\u00e2n M\u1ef9 Group | 25+ N\u0103m D\u1eabn \u0110\u1ea7u Ng\u00e0nh Nh\u00f4m'
    return make(lang, 'gioi-thieu', body, title)

def make_aluminum(lang):
    is_en = lang == 'en'
    if is_en:
        body = '<section class="relative pt-28 pb-16 overflow-hidden"><div class="absolute inset-0 bg-cover bg-center" style="background-image:url(\'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1920&q=80\');background-size:cover;"><div class="absolute inset-0 hero-mask"></div></div><div class="container mx-auto px-4 relative z-10 text-center"><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">ZAVA PREMIUM</span><h1 class="text-4xl lg:text-5xl font-black text-white mt-3">Tan My Aluminum - ZAVA</h1><p class="text-gray-300 max-w-2xl mx-auto mt-4">Premium architectural aluminum systems, industrial profiles and sustainable building solutions.</p></div></section><section class="py-20 bg-white"><div class="container mx-auto px-4"><div class="grid md:grid-cols-3 gap-8"><div class="rounded-2xl overflow-hidden shadow-lg group hover:shadow-xl transition" data-aos="fade-up"><div class="h-56 bg-gradient-to-br from-gray-800 to-gray-600 relative overflow-hidden"><img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=600&q=80" class="w-full h-full object-cover opacity-50 group-hover:scale-105 transition duration-700"></div><div class="p-6"><h3 class="font-black text-darkBg mb-2">ZAVA Systems</h3><p class="text-sm text-gray-500">Premium facade architecture, European standard.</p></div></div><div class="rounded-2xl overflow-hidden shadow-lg group hover:shadow-xl transition" data-aos="fade-up"><div class="h-56 bg-gradient-to-br from-gray-800 to-gray-600 relative overflow-hidden"><img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=600&q=80" class="w-full h-full object-cover opacity-50 group-hover:scale-105 transition duration-700"></div><div class="p-6"><h3 class="font-black text-darkBg mb-2">Architectural Profiles</h3><p class="text-sm text-gray-500">Diverse types for all construction projects.</p></div></div><div class="rounded-2xl overflow-hidden shadow-lg group hover:shadow-xl transition" data-aos="fade-up"><div class="h-56 bg-gradient-to-br from-gray-800 to-gray-600 relative overflow-hidden"><img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=600&q=80" class="w-full h-full object-cover opacity-50 group-hover:scale-105 transition duration-700"></div><div class="p-6"><h3 class="font-black text-darkBg mb-2">Industrial Profiles</h3><p class="text-sm text-gray-500">Technical solutions for manufacturing industries.</p></div></div></div></div></section>'
        title = 'Tan My Aluminum - ZAVA | Premium Architectural Systems'
    else:
        body = '<section class="relative pt-28 pb-16 overflow-hidden"><div class="absolute inset-0 bg-cover bg-center" style="background-image:url(\'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1920&q=80\');background-size:cover;"><div class="absolute inset-0 hero-mask"></div></div><div class="container mx-auto px-4 relative z-10 text-center"><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">ZAVA CAO C\u1ea4P</span><h1 class="text-4xl lg:text-5xl font-black text-white mt-3">Nh\u00f4m T\u00e2n M\u1ef9 - ZAVA</h1><p class="text-gray-300 max-w-2xl mx-auto mt-4">H\u1ec7 nh\u00f4m ki\u1ebfn tr\u00fac cao c\u1ea5p, nh\u00f4m thanh \u0111\u1ecbnh h\u00ecnh c\u00f4ng nghi\u1ec7p v\u00e0 gi\u1ea3i ph\u00e1p x\u00e2y d\u1ef1ng b\u1ec1n v\u1eefng.</p></div></section><section class="py-20 bg-white"><div class="container mx-auto px-4"><div class="grid md:grid-cols-3 gap-8"><div class="rounded-2xl overflow-hidden shadow-lg group hover:shadow-xl transition" data-aos="fade-up"><div class="h-56 bg-gradient-to-br from-gray-800 to-gray-600 relative overflow-hidden"><img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=600&q=80" class="w-full h-full object-cover opacity-50 group-hover:scale-105 transition duration-700"></div><div class="p-6"><h3 class="font-black text-darkBg mb-2">H\u1ec7 nh\u00f4m ZAVA</h3><p class="text-sm text-gray-500">Ki\u1ebfn tr\u00fac m\u1eb7t d\u1ef1ng cao c\u1ea5p, \u0111\u1ea1t ti\u00eau chu\u1ea9n Ch\u00e2u \u00c2u.</p></div></div><div class="rounded-2xl overflow-hidden shadow-lg group hover:shadow-xl transition" data-aos="fade-up"><div class="h-56 bg-gradient-to-br from-gray-800 to-gray-600 relative overflow-hidden"><img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=600&q=80" class="w-full h-full object-cover opacity-50 group-hover:scale-105 transition duration-700"></div><div class="p-6"><h3 class="font-black text-darkBg mb-2">Nh\u00f4m thanh ki\u1ebfn tr\u00fac</h3><p class="text-sm text-gray-500">\u0110a d\u1ea1ng ch\u1ee7ng lo\u1ea1i, ph\u00f9 h\u1ee3p m\u1ecdi c\u00f4ng tr\u00ecnh.</p></div></div><div class="rounded-2xl overflow-hidden shadow-lg group hover:shadow-xl transition" data-aos="fade-up"><div class="h-56 bg-gradient-to-br from-gray-800 to-gray-600 relative overflow-hidden"><img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=600&q=80" class="w-full h-full object-cover opacity-50 group-hover:scale-105 transition duration-700"></div><div class="p-6"><h3 class="font-black text-darkBg mb-2">Nh\u00f4m \u0111\u1ecbnh h\u00ecnh CN</h3><p class="text-sm text-gray-500">Gi\u1ea3i ph\u00e1p nh\u00f4m k\u1ef9 thu\u1eadt cho ng\u00e0nh c\u00f4ng nghi\u1ec7p.</p></div></div></div></div></section>'
        title = 'Nh\u00f4m T\u00e2n M\u1ef9 - ZAVA | H\u1ec7 Nh\u00f4m Ki\u1ebfn Tr\u00fac Cao C\u1ea5p'
    return make(lang, 'nhom-tan-my', body, title)

def make_household(lang):
    is_en = lang == 'en'
    if is_en:
        body = '<section class="relative pt-28 pb-16 overflow-hidden"><div class="absolute inset-0 bg-cover bg-center" style="background-image:url(\'https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=1920&q=80\');background-size:cover;"><div class="absolute inset-0 hero-mask"></div></div><div class="container mx-auto px-4 relative z-10 text-center"><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">PREMIUM HOUSEHOLD</span><h1 class="text-4xl lg:text-5xl font-black text-white mt-3">Tan My Household</h1><p class="text-gray-300 max-w-2xl mx-auto mt-4">High-quality household products, durable, and environmentally friendly.</p></div></section><section class="py-20 bg-white"><div class="container mx-auto px-4"><div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6"><div class="bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition group" data-aos="fade-up"><div class="h-48 bg-gradient-to-br from-blue-100 to-blue-50 flex items-center justify-center"><i class="fa-solid fa-shower text-5xl text-brandBlue opacity-60 group-hover:scale-110 transition"></i></div><div class="p-5"><h3 class="font-black text-darkBg text-sm">Steel Water Tanks</h3><p class="text-xs text-gray-500 mt-1">Premium SS304, durable, 100L to 2000L.</p></div></div><div class="bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition group" data-aos="fade-up"><div class="h-48 bg-gradient-to-br from-blue-100 to-blue-50 flex items-center justify-center"><i class="fa-solid fa-tint text-5xl text-brandBlue opacity-60 group-hover:scale-110 transition"></i></div><div class="p-5"><h3 class="font-black text-darkBg text-sm">Plastic Tanks</h3><p class="text-xs text-gray-500 mt-1">Safe virgin plastic, lightweight, easy installation.</p></div></div><div class="bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition group" data-aos="fade-up"><div class="h-48 bg-gradient-to-br from-blue-100 to-blue-50 flex items-center justify-center"><i class="fa-solid fa-toilet text-5xl text-brandBlue opacity-60 group-hover:scale-110 transition"></i></div><div class="p-5"><h3 class="font-black text-darkBg text-sm">Septic Tanks</h3><p class="text-xs text-gray-500 mt-1">Smart, thorough treatment, eco-friendly.</p></div></div><div class="bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition group" data-aos="fade-up"><div class="h-48 bg-gradient-to-br from-blue-100 to-blue-50 flex items-center justify-center"><i class="fa-solid fa-sun text-5xl text-brandBlue opacity-60 group-hover:scale-110 transition"></i></div><div class="p-5"><h3 class="font-black text-darkBg text-sm">Solar Heaters</h3><p class="text-xs text-gray-500 mt-1">Energy-saving, vacuum tube technology.</p></div></div></div></div></section>'
        title = 'Tan My Household | Water Tanks, Septic Tanks, Solar Heaters'
    else:
        body = '<section class="relative pt-28 pb-16 overflow-hidden"><div class="absolute inset-0 bg-cover bg-center" style="background-image:url(\'https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=1920&q=80\');background-size:cover;"><div class="absolute inset-0 hero-mask"></div></div><div class="container mx-auto px-4 relative z-10 text-center"><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">GIA D\u1ee4NG CAO C\u1ea4P</span><h1 class="text-4xl lg:text-5xl font-black text-white mt-3">Gia d\u1ee5ng T\u00e2n M\u1ef9</h1><p class="text-gray-300 max-w-2xl mx-auto mt-4">S\u1ea3n ph\u1ea9m gia d\u1ee5ng ch\u1ea5t l\u01b0\u1ee3ng cao, b\u1ec1n b\u1ec9, th\u00e2n thi\u1ec7n m\u00f4i tr\u01b0\u1eddng.</p></div></section><section class="py-20 bg-white"><div class="container mx-auto px-4"><div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6"><div class="bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition group" data-aos="fade-up"><div class="h-48 bg-gradient-to-br from-blue-100 to-blue-50 flex items-center justify-center"><i class="fa-solid fa-shower text-5xl text-brandBlue opacity-60 group-hover:scale-110 transition"></i></div><div class="p-5"><h3 class="font-black text-darkBg text-sm">B\u1ed3n n\u01b0\u1edbc Inox</h3><p class="text-xs text-gray-500 mt-1">Inox 304 cao c\u1ea5p, b\u1ec1n b\u1ec9, dung t\u00edch \u0111a d\u1ea1ng.</p></div></div><div class="bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition group" data-aos="fade-up"><div class="h-48 bg-gradient-to-br from-blue-100 to-blue-50 flex items-center justify-center"><i class="fa-solid fa-tint text-5xl text-brandBlue opacity-60 group-hover:scale-110 transition"></i></div><div class="p-5"><h3 class="font-black text-darkBg text-sm">B\u1ed3n nh\u1ef1a \u0111a n\u0103ng</h3><p class="text-xs text-gray-500 mt-1">Nh\u1ef1a nguy\u00ean sinh an to\u00e0n, nh\u1eb9, d\u1ec5 l\u1eafp \u0111\u1eb7t.</p></div></div><div class="bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition group" data-aos="fade-up"><div class="h-48 bg-gradient-to-br from-blue-100 to-blue-50 flex items-center justify-center"><i class="fa-solid fa-toilet text-5xl text-brandBlue opacity-60 group-hover:scale-110 transition"></i></div><div class="p-5"><h3 class="font-black text-darkBg text-sm">B\u1ec3 t\u1ef1 ho\u1ea1i SEPTIC</h3><p class="text-xs text-gray-500 mt-1">Th\u00f4ng minh, x\u1eed l\u00fd tri\u1ec7t \u0111\u1ec3, th\u00e2n thi\u1ec7n m\u00f4i tr\u01b0\u1eddng.</p></div></div><div class="bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition group" data-aos="fade-up"><div class="h-48 bg-gradient-to-br from-blue-100 to-blue-50 flex items-center justify-center"><i class="fa-solid fa-sun text-5xl text-brandBlue opacity-60 group-hover:scale-110 transition"></i></div><div class="p-5"><h3 class="font-black text-darkBg text-sm">M\u00e1y n\u01b0\u1edbc n\u00f3ng NLMT</h3><p class="text-xs text-gray-500 mt-1">Ti\u1ebft ki\u1ec7m \u0111i\u1ec7n, c\u00f4ng ngh\u1ec7 \u1ed1ng ch\u00e2n kh\u00f4ng.</p></div></div></div></div></section>'
        title = 'Gia d\u1ee5ng T\u00e2n M\u1ef9 | B\u1ed3n N\u01b0\u1edbc, B\u1ec3 Ph\u1ed1t, M\u00e1y N\u01b0\u1edbc N\u00f3ng'
    return make(lang, 'gia-dung', body, title)

def make_projects(lang):
    is_en = lang == 'en'
    projects_data = [
        ('Vinhomes Ocean Park','Vinhomes Ocean Park',
         'Khu \u0111\u00f4 th\u1ecb th\u00f4ng minh ven bi\u1ec3n, h\u1ec7 nh\u00f4m ZAVA cao c\u1ea5p.',
         'Smart coastal urban area, premium ZAVA systems.'),
        ('Sunshine City','Sunshine City',
         'T\u00f2a th\u00e1p v\u0103n ph\u00f2ng m\u1eb7t d\u1ef1ng k\u00ednh - nh\u00f4m hi\u1ec7n \u0111\u1ea1i.',
         'Modern glass-aluminum facade office tower.'),
        ('FLC Quy Nh\u01a1n Resort','FLC Quy Nhon Resort',
         'Resort 5 sao v\u1edbi ki\u1ebfn tr\u00fac nh\u00f4m k\u00ednh bi\u1ec3n \u0111\u1eb3ng c\u1ea5p.',
         '5-star resort with premium seaside architecture.'),
        ('Times City','Times City',
         'Khu c\u0103n h\u1ed9 cao c\u1ea5p s\u1eed d\u1ee5ng ZAVA to\u00e0n b\u1ed9.',
         'Luxury apartments using ZAVA throughout.'),
        ('Lotte Mall H\u00e0 N\u1ed9i','Lotte Mall Hanoi',
         'Trung t\u00e2m th\u01b0\u01a1ng m\u1ea1i ti\u00eau chu\u1ea9n qu\u1ed1c t\u1ebf.',
         'International standard shopping mall.'),
        ('Ecopark','Ecopark',
         'Khu \u0111\u00f4 th\u1ecb xanh, gi\u1ea3i ph\u00e1p nh\u00f4m b\u1ec1n v\u1eefng.',
         'Green urban area, sustainable aluminum solutions.'),
    ]
    cards = ''
    for vn, en, dv, de in projects_data:
        name = en if is_en else vn
        desc = de if is_en else dv
        cards += f'<div class="project-card rounded-2xl overflow-hidden shadow-md group" data-aos="fade-up"><div class="h-56 overflow-hidden"><img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&q=80" class="w-full h-full object-cover"></div><div class="p-5 bg-white"><h3 class="font-black text-darkBg text-sm">{name}</h3><p class="text-xs text-gray-500 mt-1">{desc}</p></div></div>'
    title_en = 'Featured Projects | Tan My Group'
    title_vi = 'D\u1ef1 \u00e1n ti\u00eau bi\u1ec3u | T\u00e2n M\u1ef9 Group'
    hero_label = 'PROJECTS' if is_en else 'C\u00d4NG TR\u00ccNH'
    hero_title = 'Featured Projects' if is_en else 'D\u1ef1 \u00e1n ti\u00eau bi\u1ec3u'
    hero_desc = 'Hundreds of projects nationwide trust Tan My products.' if is_en else 'H\u00e0ng tr\u0103m c\u00f4ng tr\u00ecnh l\u1edbn nh\u1ecf tr\u00ean kh\u1eafp c\u1ea3 n\u01b0\u1edbc \u0111\u00e3 tin d\u00f9ng s\u1ea3n ph\u1ea9m T\u00e2n M\u1ef9.'
    body = f'<section class="relative pt-28 pb-16 overflow-hidden"><div class="absolute inset-0 bg-cover bg-center" style="background-image:url(\'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1920&q=80\');background-size:cover;"><div class="absolute inset-0 hero-mask"></div></div><div class="container mx-auto px-4 relative z-10 text-center"><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">{hero_label}</span><h1 class="text-4xl lg:text-5xl font-black text-white mt-3">{hero_title}</h1><p class="text-gray-300 max-w-2xl mx-auto mt-4">{hero_desc}</p></div></section><section class="py-20 bg-white"><div class="container mx-auto px-4"><div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">{cards}</div></div></section>'
    return make(lang, 'du-an', body, title_vi if not is_en else title_en)

def make_news(lang):
    is_en = lang == 'en'
    news_items = [
        ('20/05/2024','May 20, 2024',
         'Kh\u00e1nh th\u00e0nh d\u00e2y chuy\u1ec1n s\u01a1n t\u0129nh \u0111i\u1ec7n',
         'New Powder Coating Line Inaugurated',
         'C\u00f4ng ngh\u1ec7 cao hi\u1ec7n \u0111\u1ea1i, n\u00e2ng c\u00f4ng su\u1ea5t l\u00ean 50.000 t\u1ea5n/n\u0103m.',
         'High-tech line boosts capacity to 50,000 tons/year.'),
        ('15/05/2024','May 15, 2024',
         'Xu h\u01b0\u1edbng ki\u1ebfn tr\u00fac nh\u00f4m k\u00ednh 2024',
         '2024 Glass-Aluminum Trends',
         'ZAVA d\u1eabn \u0111\u1ea7u xu h\u01b0\u1edbng v\u1edbi gi\u1ea3i ph\u00e1p m\u1eb7t d\u1ef1ng th\u00f4ng minh.',
         'ZAVA leads with smart facade solutions.'),
        ('10/05/2024','May 10, 2024',
         'Tri\u1ec3n l\u00e3m Vietbuild H\u00e0 N\u1ed9i',
         'Vietbuild Hanoi Exhibition',
         'T\u00e2n M\u1ef9 gi\u1edbi thi\u1ec7u b\u1ed9 s\u01b0u t\u1eadp nh\u00f4m ZAVA th\u1ebf h\u1ec7 m\u1edbi.',
         'Tan My showcases new ZAVA collection.'),
        ('05/05/2024','May 5, 2024',
         'T\u00e2n M\u1ef9 m\u1edf r\u1ed9ng nh\u00e0 m\u00e1y',
         'Factory Expansion',
         '\u0110\u1ea7u t\u01b0 th\u00eam 03 d\u00e2y chuy\u1ec1n \u0111\u00f9n \u00e9p hi\u1ec7n \u0111\u1ea1i t\u1eeb \u0110\u1ee9c.',
         'Invested in 3 new German extrusion lines.'),
        ('28/04/2024','Apr 28, 2024',
         'B\u1ed3n n\u01b0\u1edbc Inox T\u00e2n M\u1ef9',
         'Tan My Steel Water Tanks',
         'S\u1ea3n ph\u1ea9m \u0111\u1ea1t chu\u1ea9n xu\u1ea5t kh\u1ea9u sang Nh\u1eadt B\u1ea3n.',
         'Products certified for export to Japan.'),
        ('20/04/2024','Apr 20, 2024',
         'T\u00e2n M\u1ef9 h\u1ee3p t\u00e1c chi\u1ebfn l\u01b0\u1ee3c',
         'Strategic Partnership',
         'K\u00fd k\u1ebft h\u1ee3p t\u00e1c v\u1edbi \u0111\u1ed1i t\u00e1c H\u00e0n Qu\u1ed1c.',
         'Signed partnership with Korean partner.'),
    ]
    cards = ''
    for dv, de, tv, te, pv, pe in news_items:
        d = de if is_en else dv
        t = te if is_en else tv
        p = pe if is_en else pv
        cards += f'<div class="flex gap-5 p-5 bg-gray-50 rounded-2xl hover:shadow-lg transition" data-aos="fade-up"><div class="w-32 h-24 rounded-xl overflow-hidden flex-shrink-0"><img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=300&q=80" class="w-full h-full object-cover"></div><div><div class="text-xs text-gray-400">{d}</div><h3 class="font-bold text-darkBg text-sm mt-1">{t}</h3><p class="text-xs text-gray-500 mt-1">{p}</p></div></div>'
    hero_label = 'NEWS & EVENTS' if is_en else 'TIN T\u1ee8C & S\u1ef0 KI\u1ec6N'
    hero_title = 'Tan My News' if is_en else 'Tin t\u1ee9c T\u00e2n M\u1ef9'
    hero_desc = 'Updates on activities, events, and industry trends.' if is_en else 'C\u1eadp nh\u1eadt ho\u1ea1t \u0111\u1ed9ng, s\u1ef1 ki\u1ec7n v\u00e0 xu h\u01b0\u1edbng ng\u00e0nh.'
    body = f'<section class="relative pt-28 pb-16 overflow-hidden"><div class="absolute inset-0 bg-cover bg-center" style="background-image:url(\'https://images.unsplash.com/photo-1504711434969-e33886168d6c?w=1920&q=80\');background-size:cover;"><div class="absolute inset-0 hero-mask"></div></div><div class="container mx-auto px-4 relative z-10 text-center"><span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">{hero_label}</span><h1 class="text-4xl lg:text-5xl font-black text-white mt-3">{hero_title}</h1><p class="text-gray-300 max-w-2xl mx-auto mt-4">{hero_desc}</p></div></section><section class="py-20 bg-white"><div class="container mx-auto px-4"><div class="grid lg:grid-cols-2 gap-8">{cards}</div></div></section>'
    return make(lang, 'tin-tuc', body, 'Tin t\u1ee9c & S\u1ef1 ki\u1ec7n | T\u00e2n M\u1ef9 Group' if not is_en else 'News & Events | Tan My Group')

def make_contact(lang):
    is_en = lang == 'en'
    body = f'''<section class="relative pt-28 pb-16 overflow-hidden">
<div class="absolute inset-0 bg-cover bg-center" style="background-image:url('https://images.unsplash.com/photo-1423666639041-f56000c27a9a?w=1920&q=80');background-size:cover;"><div class="absolute inset-0 hero-mask"></div></div>
<div class="container mx-auto px-4 relative z-10 text-center">
<span class="text-brandRed font-black text-xs uppercase tracking-[.2em]">{'CONTACT' if is_en else 'LI\u00caN H\u1ec6'}</span>
<h1 class="text-4xl lg:text-5xl font-black text-white mt-3">{'Contact Us' if is_en else 'Li\u00ean h\u1ec7 v\u1edbi ch\u00fang t\u00f4i'}</h1>
<p class="text-gray-300 max-w-2xl mx-auto mt-4">{'Leave your information and we will get back to you shortly.' if is_en else 'H\u00e3y \u0111\u1ec3 l\u1ea1i th\u00f4ng tin, ch\u00fang t\u00f4i s\u1ebd li\u00ean h\u1ec7 l\u1ea1i trong th\u1eddi gian s\u1edbm nh\u1ea5t.'}</p>
</div></section>
<section class="py-20 bg-white"><div class="container mx-auto px-4">
<div class="grid lg:grid-cols-2 gap-12" data-aos="fade-up">
<div><h3 class="text-2xl font-black text-darkBg mb-6">{'Send Request' if is_en else 'G\u1eedi y\u00eau c\u1ea7u'}</h3>
<form action="https://formsubmit.co/ajax/nicknameaz13.1.2010@gmail.com" method="POST" class="space-y-4" id="contactForm">
<input type="hidden" name="_subject" value="{'Request from Tan My Group Website' if is_en else 'Y\u00eau c\u1ea7u t\u1eeb Website T\u00e2n M\u1ef9 Group'}">
<input type="text" name="name" placeholder="{'Full Name' if is_en else 'H\u1ecd v\u00e0 t\u00ean'}" required class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-brandBlue focus:ring-2 focus:ring-brandBlue/20 outline-none text-sm">
<input type="tel" name="phone" placeholder="{'Phone Number' if is_en else 'S\u1ed1 \u0111i\u1ec7n tho\u1ea1i'}" required class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-brandBlue focus:ring-2 focus:ring-brandBlue/20 outline-none text-sm">
<input type="email" name="email" placeholder="Email" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-brandBlue focus:ring-2 focus:ring-brandBlue/20 outline-none text-sm">
<textarea name="message" rows="4" placeholder="{'Your Message' if is_en else 'L\u1eddi nh\u1eafn'}" required class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-brandBlue focus:ring-2 focus:ring-brandBlue/20 outline-none text-sm"></textarea>
<button type="submit" class="w-full bg-brandBlue text-white py-3.5 rounded-xl font-bold text-sm hover:bg-blue-800 transition shadow-lg">{'Send Now' if is_en else 'G\u1eedi ngay'} <i class="fa-solid fa-paper-plane ml-2"></i></button>
</form></div>
<div><h3 class="text-2xl font-black text-darkBg mb-6">{'Contact Info' if is_en else 'Th\u00f4ng tin li\u00ean h\u1ec7'}</h3>
<div class="space-y-5">{''.join(f'<div class="flex items-start gap-4"><div class="w-10 h-10 rounded-full bg-brandRed/10 flex items-center justify-center flex-shrink-0"><i class="fa-solid {i} text-brandRed"></i></div><div><div class="font-bold text-sm">{t}</div><div class="text-sm text-gray-500">{d}</div></div></div>' for i,t,d in [('fa-location-dot','Address' if is_en else '\u0110\u1ecba ch\u1ec9','77 Le Van Huu, Hai Ba Trung, Hanoi' if is_en else 'S\u1ed1 77 L\u00ea V\u0103n H\u01b0u, Hai B\u00e0 Tr\u01b0ng, H\u00e0 N\u1ed9i'),('fa-phone','Phone' if is_en else '\u0110i\u1ec7n tho\u1ea1i','024 32252752 / 024 3558 5841'),('fa-envelope','Email','vanphongcongty@tanmygroup.com.vn')])}</div>
<div class="mt-8 rounded-2xl overflow-hidden shadow-lg border border-gray-100">
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3724.634!2d105.853!3d21.019!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3135ab9c0f1f1c39%3A0x8826c6d89c0b1e2b!2zNzcgTMOqIFbEg24gxJDDonUsIEjDoGkgQsOgIFRyxrBuZywgSGFub2k!5e0!3m2!1svi!2s!4v1" width="100%" height="250" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
</div></div></div></div></section>'''
    return make(lang, 'lien-he', body, 'Li\u00ean h\u1ec7 T\u00e2n M\u1ef9 Group | Hotline 024 32252752' if not is_en else 'Contact Tan My Group | Hotline 024 32252752')

GENERATORS = {
    'index': make_home,
    'gioi-thieu': make_about,
    'nhom-tan-my': make_aluminum,
    'gia-dung': make_household,
    'du-an': make_projects,
    'tin-tuc': make_news,
    'lien-he': make_contact,
}

if __name__ == '__main__':
    for lang in ['vi', 'en']:
        for pk, vp, ep, lv, le in PAGES:
            path = ep if lang == 'en' else vp
            gen_func = GENERATORS[pk]
            html = gen_func(lang)
            parent = os.path.dirname(path)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f'Written {path}  ({len(html)} chars)')
