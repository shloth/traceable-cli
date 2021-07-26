import platform
import os
import requests
import re


os_info = platform.platform()
#nginx_v = os.system("nginx -v")

def nginx_install():
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


#def platform_install():






# Use os_info variable to determine which link to use (below)
# If contains UBUNTU | CENTOS | BIONIC | FOCAL | AMZN -- use LINUX link
# If contains ALPINE | virthardened -- use Alpine link


# LINUX download from here
# https://downloads.traceable.ai/agent/nginx/latest/linux-x86_64-nginx-$NGINX_V-ngx_http_module.so.tgz

# Alpine download from here
# https://downloads.traceable.ai/agent/nginx/latest/alpine-3.9-x86_64-nginx-$NGINX_V-ngx_http_module.so.tgz

