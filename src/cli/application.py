import platform
import fileinput
import subprocess
from subprocess import PIPE
import shutil, glob
from sys import stdout
import requests
import re, mmap
import readline

# Version Details
os_info = platform.platform()
print(f'{ os_info }')
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
    
    #compile regex
    nginx_modpath = re.search(r'(?<=--modules-path=)[^\s]*',nginx_details)
    nginx_confpath = re.search(r'(?<=--conf-path=)[^\s]*',nginx_details)
    
    #store regex results
    mod_path = nginx_modpath.group(0)
    conf_file = nginx_confpath.group(0)

    # Find if --with-compat flag is present
    if "--with-compat" in nginx_details:
        print('Detected "--with-compat" flag proceeding with installation')
    else:
        print('"--with-compat" flag not detected aborting installation, please re-install with --with-compat see https://docs.traceable.ai/install/ta/nginx/compiling-nginx')
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
    # Extract the downloaded tgz
    subprocess.run(["tar", "-xvzf", "{}".format(file_name)], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    subprocess.run(["rm", "-rf", "{}".format(file_name)])
    # Store pwd
    pwd = subprocess.getoutput("pwd")
    # Move extracted .so files to nginx modules_path
    for file in glob.glob('{}/*so*'.format(pwd)):
        shutil.copy(file, "{}/".format(mod_path))
    
    # remove *.so files after copying
    subprocess.run(["rm", "-rf", "ngx_http_traceableai_module.so".format(pwd)])
    subprocess.run(["rm", "-rf", "libtraceable.so".format(pwd)])

    # Get TPA hostname
    tpa_hostname = input('Enter the host name for the Traceable Platform Agent: ')
    service_name = input("Enter the name you'd like to use to identify this application/service: ")
    
    
    # edit nginx conf file
    user_regex = re.compile("user.+") # To find where to insert "load_module"
    nginx_conf = f"http {{\n\ttraceableai {{\n\t\tservice_name {service_name};\n\t\tcollector_host {tpa_hostname};\n\t\tcollector_port 9411;\n\t\tblocking on;\n\t\topa_server http://{tpa_hostname}:8181/;\n\t\topa_log_dir /tmp/;\n}}\n\topentracing on;\n\topentracing_propagate_context;\n\tblocking on;\n"
    trace_regex = re.compile("traceable.+")

    with open(conf_file, 'r+') as f:
        data = mmap.mmap(f.fileno(), 0)
        traceable_present = re.search(b'traceableai', data)
        if traceable_present: 
            print ("Traceable NGINX plugin already configured, aborting installation please check", conf_file)
        else: 
            with fileinput.FileInput(conf_file, inplace=True, backup='.bak') as file:
                for line in file:
                    if re.match(user_regex, line):
                        line=line.replace(line,line+"load_module modules/ngx_http_traceableai_module.so;\n")
                    print(line.replace("http {", nginx_conf), end='')
                fileinput.close()
                print("Traceable.ai NGINX Plugin succesfully configured, start sending data!")
    

def platform_install():
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
    # Confirm detect






# Use os_info variable to determine which link to use (below)
# If it contains UBUNTU | CENTOS | BIONIC | FOCAL | AMZN -- use LINUX link
# If it contains ALPINE | virthardened -- use Alpine link


# LINUX download from here
# https://downloads.traceable.ai/agent/nginx/latest/linux-x86_64-nginx-$NGINX_V-ngx_http_module.so.tgz

# Alpine download from here
# https://downloads.traceable.ai/agent/nginx/latest/alpine-3.9-x86_64-nginx-$NGINX_V-ngx_http_module.so.tgz

