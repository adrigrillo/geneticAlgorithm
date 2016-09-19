import urllib2


def main():
    body = "http://163.117.164.230/age/?f=test&c="
    bina = "0000000000000000000000000000000000000000000000000000000000000000"
    pagina = body+bina
    conn = urllib2.urlopen(pagina).read()
    print(conn) 

main()

