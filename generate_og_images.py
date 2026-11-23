import os
import subprocess
import base64
import time
from PIL import Image

def get_b64(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

pinyon_b64 = get_b64('assets/media/PinyonScript_Regular-s.p.0bp3qb6u4sz8x.woff2')
bodoni_b64 = get_b64('assets/media/BodoniModa_Variable-s.p.1pue59d5fkmu7.woff2')
cormorant_b64 = get_b64('assets/media/CormorantGaramond_Regular-s.p.363csnitlu50n.woff2')
peacock_b64 = get_b64('assets/images/peacock-ornament-v2.webp')
rings_b64 = get_b64('assets/images/rings-v2.webp')
bouquet_b64 = get_b64('assets/images/bouquet-v2.webp')
ornaments_b64 = get_b64('assets/images/ornaments.webp')

base_css = f"""
@font-face {{
  font-family: 'Pinyon';
  src: url('data:font/woff2;base64,{pinyon_b64}') format('woff2');
  font-weight: normal;
  font-style: normal;
}}
@font-face {{
  font-family: 'Bodoni';
  src: url('data:font/woff2;base64,{bodoni_b64}') format('woff2');
  font-weight: 400 900;
  font-style: normal;
}}
@font-face {{
  font-family: 'Cormorant';
  src: url('data:font/woff2;base64,{cormorant_b64}') format('woff2');
  font-weight: 400 700;
  font-style: normal;
}}

* {{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}}

html, body {{
  width: 1200px;
  height: 630px;
  overflow: hidden;
  background-color: #F8F3EA;
  font-family: 'Cormorant', Georgia, serif;
  color: #493622;
}}

.canvas {{
  position: relative;
  width: 1200px;
  height: 630px;
  background: radial-gradient(100% 70% at 50% 25%, #FFFDF8 0%, #FAF4E8 55%, #F4ECE0 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 32px 48px;
}}

/* Outer Gold Frame */
.frame-outer {{
  position: absolute;
  top: 18px;
  left: 18px;
  right: 18px;
  bottom: 18px;
  border: 1.5px solid #C9AD76;
  border-radius: 8px;
  pointer-events: none;
}}

.frame-inner {{
  position: absolute;
  top: 26px;
  left: 26px;
  right: 26px;
  bottom: 26px;
  border: 1px solid rgba(201, 173, 118, 0.45);
  border-radius: 4px;
  pointer-events: none;
}}

.corner-flower {{
  position: absolute;
  font-size: 14px;
  color: #B48843;
  line-height: 1;
}}
.tl {{ top: 12px; left: 12px; }}
.tr {{ top: 12px; right: 12px; }}
.bl {{ bottom: 12px; left: 12px; }}
.br {{ bottom: 12px; right: 12px; }}

/* Header */
.header {{
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  margin-top: 4px;
}}

.peacock-orn {{
  height: 38px;
  width: auto;
  margin-bottom: 2px;
}}

.eyebrow {{
  font-family: 'Bodoni', serif;
  font-size: 12.5px;
  letter-spacing: 0.32em;
  text-transform: uppercase;
  color: #9E7B3D;
  font-weight: 600;
  margin-bottom: 0px;
}}

.couple-names {{
  font-family: 'Pinyon', cursive;
  font-size: 82px;
  line-height: 1.02;
  color: #6E461A;
  text-shadow: 0 1px 3px rgba(255, 255, 255, 0.9);
  margin: -6px 0 -4px 0;
}}

.invitation-line {{
  font-family: 'Cormorant', serif;
  font-size: 15px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: #7D5D30;
  font-weight: 500;
}}

/* Footer */
.footer {{
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 4px;
}}

.divider-orn {{
  height: 14px;
  width: auto;
  opacity: 0.85;
  margin-bottom: 4px;
}}

.footer-text {{
  font-family: 'Cormorant', serif;
  font-size: 13.5px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #8C6F42;
  font-weight: 600;
}}
"""

# Template 1: Wedding Only
html_wedding = f"""<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<style>
{base_css}

.wedding-card {{
  position: relative;
  width: 980px;
  background: rgba(255, 252, 246, 0.95);
  border: 1.5px solid #D8C49A;
  border-radius: 12px;
  box-shadow: 0 8px 30px rgba(131, 87, 31, 0.08);
  padding: 24px 36px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}}

.wedding-rings {{
  height: 52px;
  width: auto;
  margin-bottom: 6px;
}}

.event-main-title {{
  font-family: 'Bodoni', serif;
  font-size: 26px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #6E461A;
  margin-bottom: 12px;
}}

.schedule-row {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 36px;
  width: 100%;
  padding: 10px 0;
  border-top: 1px solid rgba(201, 173, 118, 0.45);
  border-bottom: 1px solid rgba(201, 173, 118, 0.45);
  margin-bottom: 12px;
}}

.schedule-item {{
  display: flex;
  flex-direction: column;
  align-items: center;
}}

.schedule-label {{
  font-family: 'Bodoni', serif;
  font-size: 11px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #9E7B3D;
  font-weight: 600;
  margin-bottom: 2px;
}}

.schedule-time {{
  font-family: 'Cormorant', serif;
  font-size: 20px;
  font-weight: 700;
  color: #493622;
}}

.schedule-sep {{
  width: 1px;
  height: 32px;
  background: rgba(201, 173, 118, 0.45);
}}

.venue-text {{
  font-family: 'Cormorant', serif;
  font-size: 18px;
  color: #57432B;
  font-weight: 600;
  letter-spacing: 0.04em;
}}

.venue-sub {{
  font-size: 14.5px;
  color: #7D6B55;
  margin-top: 2px;
}}
</style>
</head>
<body>
<div class="canvas">
  <div class="frame-outer"></div>
  <div class="frame-inner"></div>
  <div class="corner-flower tl">✦</div>
  <div class="corner-flower tr">✦</div>
  <div class="corner-flower bl">✦</div>
  <div class="corner-flower br">✦</div>

  <div class="header">
    <img class="peacock-orn" src="data:image/webp;base64,{peacock_b64}" alt="">
    <div class="eyebrow">Wedding Invitation</div>
    <div class="couple-names">Veer & Priyal</div>
    <div class="invitation-line">Request the pleasure of your company to celebrate their wedding</div>
  </div>

  <div class="wedding-card">
    <img class="wedding-rings" src="data:image/webp;base64,{rings_b64}" alt="">
    <div class="event-main-title">Saturday, 12th December 2026</div>
    <div class="schedule-row">
      <div class="schedule-item">
        <span class="schedule-label">Baraat Assembly</span>
        <span class="schedule-time">11.00 A.M.</span>
      </div>
      <div class="schedule-sep"></div>
      <div class="schedule-item">
        <span class="schedule-label">Hast Melap</span>
        <span class="schedule-time">12.39 P.M.</span>
      </div>
      <div class="schedule-sep"></div>
      <div class="schedule-item">
        <span class="schedule-label">Wedding Feast</span>
        <span class="schedule-time">12.30 P.M. Onwards</span>
      </div>
    </div>
    <div class="venue-text">Grand Banquet Hall, Chembur (W), Mumbai</div>
    <div class="venue-sub">Universal Majestic, Opp. Indian Oil Nagar, Ghatkopar Mankhurd Link Road</div>
  </div>

  <div class="footer">
    <img class="divider-orn" src="data:image/webp;base64,{ornaments_b64}" alt="">
    <div class="footer-text">With Best Compliments from Pradip Nathalal Shah & Family</div>
  </div>
</div>
</body>
</html>
"""

# Template 2: Carnival + Wedding
html_carnival = f"""<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<style>
{base_css}

.cards-container {{
  display: flex;
  gap: 24px;
  width: 1040px;
  justify-content: center;
  align-items: stretch;
}}

.event-box {{
  flex: 1;
  border-radius: 12px;
  padding: 20px 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  justify-content: space-between;
}}

/* Left: Carnival Navy Theme */
.box-carnival {{
  background: radial-gradient(120% 90% at 50% 0%, #1D2F57 0%, #12203F 60%, #0A1428 100%);
  border: 1.5px solid rgba(212, 175, 100, 0.7);
  box-shadow: 0 8px 30px rgba(10, 20, 40, 0.25);
  color: #F8F3EA;
}}

.star-icon {{
  font-size: 16px;
  color: #E8C77E;
  margin-bottom: 2px;
}}

.card-title-carnival {{
  font-family: 'Pinyon', cursive;
  font-size: 38px;
  line-height: 1;
  color: #FFFDF8;
  text-shadow: 0 1px 4px rgba(0, 0, 0, 0.4);
}}

.card-subtitle-carnival {{
  font-family: 'Bodoni', serif;
  font-size: 10px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #D5C09B;
  margin-top: 3px;
}}

.card-date-carnival {{
  font-family: 'Bodoni', serif;
  font-size: 17px;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: #E8C77E;
  margin: 10px 0 6px 0;
}}

.card-timing-carnival {{
  font-family: 'Cormorant', serif;
  font-size: 16px;
  font-weight: 600;
  color: #FFFFFF;
  padding: 5px 12px;
  border-top: 1px solid rgba(212, 175, 100, 0.35);
  border-bottom: 1px solid rgba(212, 175, 100, 0.35);
  margin-bottom: 8px;
  width: 90%;
}}

.card-venue-carnival {{
  font-family: 'Cormorant', serif;
  font-size: 14.5px;
  color: #CBD3E1;
}}

/* Right: Wedding Ivory Theme */
.box-wedding {{
  background: rgba(255, 252, 246, 0.95);
  border: 1.5px solid #D8C49A;
  box-shadow: 0 8px 30px rgba(131, 87, 31, 0.08);
  color: #493622;
}}

.card-rings {{
  height: 38px;
  width: auto;
  margin-bottom: -2px;
}}

.card-title-wedding {{
  font-family: 'Pinyon', cursive;
  font-size: 38px;
  line-height: 1;
  color: #6E461A;
}}

.card-subtitle-wedding {{
  font-family: 'Bodoni', serif;
  font-size: 10px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #9E7B3D;
  margin-top: 3px;
}}

.card-date-wedding {{
  font-family: 'Bodoni', serif;
  font-size: 17px;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: #6E461A;
  margin: 10px 0 6px 0;
}}

.card-timing-wedding {{
  font-family: 'Cormorant', serif;
  font-size: 16px;
  font-weight: 700;
  color: #493622;
  padding: 5px 12px;
  border-top: 1px solid rgba(201, 173, 118, 0.45);
  border-bottom: 1px solid rgba(201, 173, 118, 0.45);
  margin-bottom: 8px;
  width: 90%;
}}

.card-venue-wedding {{
  font-family: 'Cormorant', serif;
  font-size: 14.5px;
  color: #6B5539;
  font-weight: 600;
}}
</style>
</head>
<body>
<div class="canvas">
  <div class="frame-outer"></div>
  <div class="frame-inner"></div>
  <div class="corner-flower tl">✦</div>
  <div class="corner-flower tr">✦</div>
  <div class="corner-flower bl">✦</div>
  <div class="corner-flower br">✦</div>

  <div class="header">
    <img class="peacock-orn" src="data:image/webp;base64,{peacock_b64}" alt="">
    <div class="eyebrow">Carnival & Wedding Celebrations</div>
    <div class="couple-names">Veer & Priyal</div>
    <div class="invitation-line">Cordially invite you to join in celebrating their wedding festivities</div>
  </div>

  <div class="cards-container">
    <!-- Carnival Card -->
    <div class="event-box box-carnival">
      <div>
        <div class="star-icon">✦</div>
        <div class="card-title-carnival">Veer & Priyal's Carnival</div>
        <div class="card-subtitle-carnival">An Evening of Fun, Games & Dinner</div>
      </div>
      <div>
        <div class="card-date-carnival">Wednesday, 9th December 2026</div>
        <div class="card-timing-carnival">Carnival 5.00 P.M. · Followed by Dinner</div>
      </div>
      <div class="card-venue-carnival">
        Manek Banquet, Shree Manav Seva Sangh<br>Sion West, Mumbai - 400019
      </div>
    </div>

    <!-- Wedding Card -->
    <div class="event-box box-wedding">
      <div>
        <img class="card-rings" src="data:image/webp;base64,{rings_b64}" alt="">
        <div class="card-title-wedding">The Wedding Ceremony</div>
        <div class="card-subtitle-wedding">Baraat Assembly & Hast Melap</div>
      </div>
      <div>
        <div class="card-date-wedding">Saturday, 12th December 2026</div>
        <div class="card-timing-wedding">Baraat 11.00 A.M. · Hast Melap 12.39 P.M.</div>
      </div>
      <div class="card-venue-wedding">
        Grand Banquet Hall, Universal Majestic<br>Chembur (W), Mumbai - 400043
      </div>
    </div>
  </div>

  <div class="footer">
    <img class="divider-orn" src="data:image/webp;base64,{ornaments_b64}" alt="">
    <div class="footer-text">With Best Compliments from The Shah & Katariya Families</div>
  </div>
</div>
</body>
</html>
"""

# Template 3: Celebrations (All Functions: Ganesh Chandla & Haldi, Carnival, Wedding)
html_celebrations = f"""<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<style>
{base_css}

.cards-container-3 {{
  display: flex;
  gap: 16px;
  width: 1080px;
  justify-content: center;
  align-items: stretch;
}}

.event-col {{
  flex: 1;
  border-radius: 10px;
  padding: 16px 14px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  justify-content: space-between;
}}

.col-haldi {{
  background: rgba(255, 252, 246, 0.95);
  border: 1.5px solid #D8C49A;
  box-shadow: 0 6px 24px rgba(131, 87, 31, 0.08);
  color: #493622;
}}

.col-carnival {{
  background: radial-gradient(120% 90% at 50% 0%, #1D2F57 0%, #12203F 60%, #0A1428 100%);
  border: 1.5px solid rgba(212, 175, 100, 0.7);
  box-shadow: 0 6px 24px rgba(10, 20, 40, 0.25);
  color: #F8F3EA;
}}

.col-wedding {{
  background: rgba(255, 252, 246, 0.95);
  border: 1.5px solid #D8C49A;
  box-shadow: 0 6px 24px rgba(131, 87, 31, 0.08);
  color: #493622;
}}

.icon-orn {{
  height: 32px;
  width: auto;
  margin-bottom: -1px;
}}

.col-title {{
  font-family: 'Pinyon', cursive;
  font-size: 31px;
  line-height: 1;
  margin-top: 1px;
}}

.col-haldi .col-title, .col-wedding .col-title {{
  color: #6E461A;
}}

.col-carnival .col-title {{
  color: #FFFDF8;
}}

.col-subtitle {{
  font-family: 'Bodoni', serif;
  font-size: 9.5px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  margin-top: 2px;
}}

.col-haldi .col-subtitle, .col-wedding .col-subtitle {{
  color: #9E7B3D;
}}

.col-carnival .col-subtitle {{
  color: #D5C09B;
}}

.col-date {{
  font-family: 'Bodoni', serif;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: 0.06em;
  margin: 7px 0 5px 0;
}}

.col-haldi .col-date, .col-wedding .col-date {{
  color: #6E461A;
}}

.col-carnival .col-date {{
  color: #E8C77E;
}}

.col-timing {{
  font-family: 'Cormorant', serif;
  font-size: 14px;
  font-weight: 700;
  padding: 4px 6px;
  width: 95%;
  margin-bottom: 6px;
}}

.col-haldi .col-timing, .col-wedding .col-timing {{
  color: #493622;
  border-top: 1px solid rgba(201, 173, 118, 0.45);
  border-bottom: 1px solid rgba(201, 173, 118, 0.45);
}}

.col-carnival .col-timing {{
  color: #FFFFFF;
  border-top: 1px solid rgba(212, 175, 100, 0.35);
  border-bottom: 1px solid rgba(212, 175, 100, 0.35);
}}

.col-venue {{
  font-family: 'Cormorant', serif;
  font-size: 13.5px;
  line-height: 1.35;
}}

.col-haldi .col-venue, .col-wedding .col-venue {{
  color: #6B5539;
  font-weight: 600;
}}

.col-carnival .col-venue {{
  color: #CBD3E1;
}}
</style>
</head>
<body>
<div class="canvas">
  <div class="frame-outer"></div>
  <div class="frame-inner"></div>
  <div class="corner-flower tl">✦</div>
  <div class="corner-flower tr">✦</div>
  <div class="corner-flower bl">✦</div>
  <div class="corner-flower br">✦</div>

  <div class="header">
    <img class="peacock-orn" src="data:image/webp;base64,{peacock_b64}" alt="">
    <div class="eyebrow">Wedding Celebrations</div>
    <div class="couple-names">Veer & Priyal</div>
    <div class="invitation-line">Join us in celebrating the joyful moments and auspicious festivities</div>
  </div>

  <div class="cards-container-3">
    <!-- 1: Haldi -->
    <div class="event-col col-haldi">
      <div>
        <img class="icon-orn" src="data:image/webp;base64,{bouquet_b64}" alt="">
        <div class="col-title">Ganesh Chandla & Haldi</div>
        <div class="col-subtitle">Auspicious Beginning</div>
      </div>
      <div>
        <div class="col-date">Wed, 9th Dec 2026</div>
        <div class="col-timing">10.30 A.M. · Followed by Lunch</div>
      </div>
      <div class="col-venue">
        Manek Banquet<br>Sion West, Mumbai
      </div>
    </div>

    <!-- 2: Carnival -->
    <div class="event-col col-carnival">
      <div>
        <div class="star-icon" style="font-size:15px;color:#E8C77E;">✦</div>
        <div class="col-title">The Carnival</div>
        <div class="col-subtitle">Games, Prizes & Dinner</div>
      </div>
      <div>
        <div class="col-date">Wed, 9th Dec 2026</div>
        <div class="col-timing">5.00 P.M. · Followed by Dinner</div>
      </div>
      <div class="col-venue">
        Manek Banquet<br>Sion West, Mumbai
      </div>
    </div>

    <!-- 3: Wedding -->
    <div class="event-col col-wedding">
      <div>
        <img class="icon-orn" src="data:image/webp;base64,{rings_b64}" alt="">
        <div class="col-title">The Wedding</div>
        <div class="col-subtitle">Baraat & Hast Melap</div>
      </div>
      <div>
        <div class="col-date">Sat, 12th Dec 2026</div>
        <div class="col-timing">11.00 A.M. · Melap 12.39 P.M.</div>
      </div>
      <div class="col-venue">
        Grand Banquet Hall<br>Chembur (W), Mumbai
      </div>
    </div>
  </div>

  <div class="footer">
    <img class="divider-orn" src="data:image/webp;base64,{ornaments_b64}" alt="">
    <div class="footer-text">With Love & Gratitude · The Shah & Katariya Families</div>
  </div>
</div>
</body>
</html>
"""

with open('temp_og_wedding.html', 'w', encoding='utf-8') as f:
    f.write(html_wedding)

with open('temp_og_carnival.html', 'w', encoding='utf-8') as f:
    f.write(html_carnival)

with open('temp_og_celebrations.html', 'w', encoding='utf-8') as f:
    f.write(html_celebrations)

print("Generated HTML templates.")
