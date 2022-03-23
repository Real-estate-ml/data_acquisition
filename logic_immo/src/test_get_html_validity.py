my_file = open("Export3/html/apartment_ad_1_12-01-2022.html", "r")
my_page = my_file.read()
my_page2 = "test html captcha dd  d d  d d  < < <  < < <    < < <  < <<<,n,s  s sjs d n jz z zs  d, d z  ;  <; w ;< w; ;w ,w <;<;<  w"

def get_validity_html_page(page):
    if len(page) < 5000:
        raise Exception("Captcha")

print(get_validity_html_page(my_page))
print(get_validity_html_page(my_page2))

my_file.close()
