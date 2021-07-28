import platform
import subprocess
from subprocess import PIPE
import shutil, glob
import requests
import re

# Version Details
os_info = platform.platform()
# Cleanup nginx version
nginx_v = subprocess.getoutput(
    ["nginx -v"]
)

# NGINX Version to be used in download URL
nginx_raw_v = re.sub('[^\d\.]', '', nginx_v)

def nginx_install():
    # Get Modules path and --with-compat info
    nginx_details = subprocess.getoutput(
        ["nginx -V"]
    )

    nginx_modpath = re.search(r'(?<=--modules-path=)[^\s]*',nginx_details)
    #print(nginx_details)
    path = nginx_modpath.group(0)

    # Find if --with-compat flag is present
    if "--with-compat" in nginx_details:
        print('Detected "--with-compat" flag proceeding with installation')
    else:
        print('"--with-compat" flag not detected aborting installation')
        exit
    # DETECT Operating System and use Nginx Version to download correct tar.gz
    if 'ubuntu' in os_info:
        print('Detected OS: Ubuntu')
        os = 'linux'
    elif 'bionic' in os_info:
        print('Detected OS: Ubuntu-Bionic installation')
        os = 'linux'
    elif 'focal' in os_info:
        print('Detected OS: Ubuntu-Focal')
        os = 'linux'
    elif 'amzn' in os_info:
        print('Detected OS: Amazon Linux')
        os = 'linux'
    elif 'centos' in os_info:
        print('Detected OS: CentOS')
        os = 'linux'
    elif 'virthardened' in os_info:
        print('Detected OS: Alpine Linux')
        os = 'alpine-3.9'
    else:
        print('Could not determine OS, please enter one of the following - use the corresponding number\n1-Ubuntu \n2-Centos\n3-Alpine')
    # Confirm detected version of NGINX
    
    
    # Use gathered info to download correct tgz file
    url = 'https://downloads.traceable.ai/agent/nginx/latest/{}-x86_64-nginx-{}-ngx_http_module.so.tgz'.format(os, nginx_raw_v)
    r = requests.get(url, allow_redirects=True)
    open('{}-x86_64-nginx-{}-ngx_http_module.so.tgz'.format(os, nginx_raw_v), 'wb').write(r.content)
    file_name = '{}-x86_64-nginx-{}-ngx_http_module.so.tgz'.format(os, nginx_raw_v)
    subprocess.run(["tar", "-xvzf", "{}".format(file_name)])
    # Store pwd
    pwd = subprocess.getoutput("pwd")
    # Move extracted .so files to nginx modules_path
    print(path)
    #subprocess.run(["cp", "{}/*.so".format(pwd), "{}/".format(path)], shell=True)
    for file in glob.glob('{}/*so*'):
        shutil.copy(file, "{}/".format(path))
    subprocess.getoutput("ls -la {}".format(path))
#def platform_install():






# Use os_info variable to determine which link to use (below)
# If contains UBUNTU | CENTOS | BIONIC | FOCAL | AMZN -- use LINUX link
# If contains ALPINE | virthardened -- use Alpine link


# LINUX download from here
# https://downloads.traceable.ai/agent/nginx/latest/linux-x86_64-nginx-$NGINX_V-ngx_http_module.so.tgz

# Alpine download from here
# https://downloads.traceable.ai/agent/nginx/latest/alpine-3.9-x86_64-nginx-$NGINX_V-ngx_http_module.so.tgz

