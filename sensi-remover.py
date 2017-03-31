import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--passfile',help="file in which sensitive information is stored.")
parser.add_argument('--repo',help="your github repo directory name")
args = parser.parse_args()

sensitive_list = []
if args.passfile:
    with open(args.passfile,'r') as f:
        for i in f:
            sensitive_list.append(i)

def remover(sensitive_string,folder):
    REPLACEMENT='***REMOVED***'
    for path, dirs, files in os.walk(folder):
        for fname in files:
            fpath=os.path.join(path, fname)
            print "processing >>",fpath
            with open(fpath) as f:
                s = f.read()
            s = s.replace(sensitive_string,REPLACEMENT)
            with open(fpath,'w') as f:
                f.write(s)

repo = args.repo
for i in sensitive_list:
    remover(i,repo)
