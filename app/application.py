import platform
import subprocess
from subprocess import PIPE
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
    # BASELINE URL WITH EMBEDDED VARS

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
    url = 'https://downloads.traceable.ai/agent/nginx/latest/{}-x86_64-nginx-{}-ngx_http_module.so.tgz'.format(os, nginx_raw_v)
    r = requests.get(url, allow_redirects=True)
    open('{}-x86_64-nginx-{}-ngx_http_module.so.tgz'.format(os, nginx_raw_v), 'wb').write(r.content)
    print(os)
#def platform_install():






# Use os_info variable to determine which link to use (below)
# If contains UBUNTU | CENTOS | BIONIC | FOCAL | AMZN -- use LINUX link
# If contains ALPINE | virthardened -- use Alpine link


# LINUX download from here
# https://downloads.traceable.ai/agent/nginx/latest/linux-x86_64-nginx-$NGINX_V-ngx_http_module.so.tgz

# Alpine download from here
# https://downloads.traceable.ai/agent/nginx/latest/alpine-3.9-x86_64-nginx-$NGINX_V-ngx_http_module.so.tgz

