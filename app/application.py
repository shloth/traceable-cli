import platform
import subprocess
import sys
import requests
import re

# Version Details
os_info = platform.platform()
#nginx_v = os.system('nginx -v')
# Cleanup nginx version
nginx_v = subprocess.run(
    ["nginx", "-v"],
)
nginx_raw_v = re.sub('\D', '', "f{nginx_v.stdout}")
print(nginx_raw_v)

def nginx_install():
    # DETECT Operating System
    if 'ubuntu' in os_info:
        print('Detected OS: Ubuntu')
    elif 'bionic' in os_info:
        print('Detected OS: Ubuntu-Bionic installation')
    elif 'focal' in os_info:
        print('Detected OS: Ubuntu-Focal')
    elif 'amzn' in os_info:
        print('Detected OS: Amazon Linux')
    elif 'centos' in os_info:
        print('Detected OS: CentOS')
    elif 'virthardened' in os_info:
        print('Detected OS: Alpine Linux')
    else:
        print('Could not determine OS, please enter one of the following - use the corresponding number\n1-Ubuntu \n2-Centos\n3-Alpine')
    # Confirm detected version of NGINX


#def platform_install():






# Use os_info variable to determine which link to use (below)
# If contains UBUNTU | CENTOS | BIONIC | FOCAL | AMZN -- use LINUX link
# If contains ALPINE | virthardened -- use Alpine link


# LINUX download from here
# https://downloads.traceable.ai/agent/nginx/latest/linux-x86_64-nginx-$NGINX_V-ngx_http_module.so.tgz

# Alpine download from here
# https://downloads.traceable.ai/agent/nginx/latest/alpine-3.9-x86_64-nginx-$NGINX_V-ngx_http_module.so.tgz

