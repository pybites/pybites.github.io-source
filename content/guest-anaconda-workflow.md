Title: My Anaconda Workflow: Python environment and package management made easy
Date: 2018-07-24 20:00
Category: Tools
Tags: Anaconda, Anaconda workflow, conda, pip, virtual environment, packages, packaging, distribution, configuration, YAML, python3.7
Slug: guest-anaconda-workflow
Authors: Martin Uribe
summary: in this article martin provides an easy-to-follow reference guide of his anaconda workflow. he uses this to make his life easier managing the his python environment and package dependencies. and to great avail as you will soon discover. not only will you learn the basics of the powerful conda tool, he also goes into more depth on the more niche/advanced features like using alternate channels, distributing and cloning environments, updating anaconda, and setting environment variables. warning: this might get you on anaconda, and if you are already you probably want to keep this one nearby for reference.
cover: images/featured/pb-guest.png

In this article Martin provides an easy-to-follow reference guide of his Anaconda workflow. He uses this to make his life easier managing the his Python environment and package dependencies. And to great avail as you will soon discover. Not only will you learn the basics of the powerful conda tool, he also goes into more depth on the more niche/advanced features like using alternate channels, distributing and cloning environments, updating Anaconda, and setting environment variables. Warning: this might get you on Anaconda, and if you are already you probably want to keep this one nearby for reference. Enter Martin:

# My Anaconda Workflow
I've been working with [Anaconda](https://anaconda.org/) for a while now and I've been relatively pleased with it. I'll admit, there was a bit of a learning curve at first, but hopefully I can get you past that initial hump with this write-up. There are lots of commands and covering them all is better done in the official [documentation](https://docs.anaconda.com/anaconda-cloud/user-guide/).

> What I've covered here is just what I use most often and should get you comfortable with using Anaconda.

## Index
* [Create Virtual Environment](#create-virtual-environment)
* [List Virtual Environments](#list_virtual_environments)
* [Remove Virtual Environment](#remove_virtual_environment)
* [Search for Packages](#search_for_packages)
* [Install Packages](#install_packages)
  * [Current Environment](#current_environment)
  * [Other Environment](#other_environment)
* [Install Packages Not Found](#install_packages_not_found)
  * [Search Alternate Channels](#search_alternate_channels)
    * [Install Package From A Channel](#install_package_from_a_channel)
  * [Add Additional Channels](#add_additional_channels)
  * [Install Packages With Pip](#install_packages_with_pip)
* [Remove Packages](#remove_packages)
* [Install Packages While Creating Environment](#install_packages_while_creating_environment)
* [Export Environment Configuration](#export_environment_configuration)
* [Create Environment From File](#create_environment_from_yaml_file)
* [Prepare Environment YAML For Distribution](#prepare_environment_yaml_for_distribution)
* [List Packages](#list_packages)
* [Clone An Environment](#clone_an_environment)
* [Updates](#updates)
* [Environment Variables](#environment_variables)
* [TL;DR](#tl;dr)

<a name="create-virtual-environment"></a>
## Create Virtual Environment
Creating a virtual environment with Anaconda is pretty simple. If you do not specify a Python version, whatever your current default one is will be used. Don't know your default version? Simple run `python --version` to find out.

Let's create one that uses Python 3.7 and is called pybites:

```
conda create --name pybites python=3.7
Solving environment: done

## Package Plan ##

  environment location: /home/mohh/anaconda3/envs/pybites

  added / updated specs:
    - python=3.7


The following NEW packages will be INSTALLED:

    ca-certificates: 2018.03.07-0           
    certifi:         2018.4.16-py37_0       
    libedit:         3.1.20170329-h6b74fdf_2
    libffi:          3.2.1-hd88cf55_4       
    libgcc-ng:       7.2.0-hdf63c60_3       
    libstdcxx-ng:    7.2.0-hdf63c60_3       
    ncurses:         6.1-hf484d3e_0         
    openssl:         1.0.2o-h20670df_0      
    pip:             10.0.1-py37_0          
    python:          3.7.0-hc3d631a_0       
    readline:        7.0-ha6073c6_4         
    setuptools:      39.2.0-py37_0          
    sqlite:          3.24.0-h84994c4_0      
    tk:              8.6.7-hc745277_3       
    wheel:           0.31.1-py37_0          
    xz:              5.2.4-h14c3975_4       
    zlib:            1.2.11-ha838bed_2      

Proceed ([y]/n)?

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate pybites
#
# To deactivate an active environment, use
#
#     $ conda deactivate
#
```

The comments at the end show you how to activate/deactivate your new environment.

<a name="list_virtual_environments"></a>
## List Virtual Environments
Don't remember what you named your environment? Just what to see which ones you have created? You can view them all with `conda env list`. The name of the environment will be shown as well as its location:

```
conda env list
# conda environments:
#
base                  *  /home/mohh/anaconda3
animpy                   /home/mohh/anaconda3/envs/animpy
comic_snagger            /home/mohh/anaconda3/envs/comic_snagger
cv                       /home/mohh/anaconda3/envs/cv
ml                       /home/mohh/anaconda3/envs/ml
pybites                  /home/mohh/anaconda3/envs/pybites
toepack                  /home/mohh/anaconda3/envs/toepack
```

<a name="remove_virtual_environment"></a>
## Remove Virtual Environment
If you ever have the need to remove an environment, `conda env remove --name ENVNAME` will remove it and every package installed in it:

```
conda env remove --name pybites

Remove all packages in environment /home/mohh/anaconda3/envs/pybites:


## Package Plan ##

  environment location: /home/mohh/anaconda3/envs/pybites


The following packages will be REMOVED:

    ca-certificates: 2018.03.07-0           
    certifi:         2018.4.16-py37_0       
    libedit:         3.1.20170329-h6b74fdf_2
    libffi:          3.2.1-hd88cf55_4       
    libgcc-ng:       7.2.0-hdf63c60_3       
    libstdcxx-ng:    7.2.0-hdf63c60_3       
    ncurses:         6.1-hf484d3e_0         
    openssl:         1.0.2o-h20670df_0      
    pip:             10.0.1-py37_0          
    python:          3.7.0-hc3d631a_0       
    readline:        7.0-ha6073c6_4         
    setuptools:      39.2.0-py37_0          
    sqlite:          3.24.0-h84994c4_0      
    tk:              8.6.7-hc745277_3       
    wheel:           0.31.1-py37_0          
    xz:              5.2.4-h14c3975_4       
    zlib:            1.2.11-ha838bed_2      

Proceed ([y]/n)?
```

<a name="search_for_packages"></a>
## Search for Packages
Normally, before attempting to install a new package, I search for it to see if Anaconda supports it. I already know that *beautifulsoup4* is supported, but I'll go ahead and show you what that would look like:

```
conda search beautifulsoup4
Loading channels: done
# Name                  Version           Build  Channel             
beautifulsoup4            4.4.0          py27_0  pkgs/free           
beautifulsoup4            4.4.0          py34_0  pkgs/free           
beautifulsoup4            4.4.0          py35_0  pkgs/free           
beautifulsoup4            4.4.1          py27_0  pkgs/free           
beautifulsoup4            4.4.1          py34_0  pkgs/free           
beautifulsoup4            4.4.1          py35_0  pkgs/free           
beautifulsoup4            4.5.1          py27_0  pkgs/free           
beautifulsoup4            4.5.1          py34_0  pkgs/free           
beautifulsoup4            4.5.1          py35_0  pkgs/free           
beautifulsoup4            4.5.1          py36_0  pkgs/free           
beautifulsoup4            4.5.3          py27_0  pkgs/free           
beautifulsoup4            4.5.3          py34_0  pkgs/free           
beautifulsoup4            4.5.3          py35_0  pkgs/free           
beautifulsoup4            4.5.3          py36_0  pkgs/free           
beautifulsoup4            4.6.0          py27_0  pkgs/free           
beautifulsoup4            4.6.0          py27_1  pkgs/main           
beautifulsoup4            4.6.0  py27h3f86ba9_1  pkgs/main           
beautifulsoup4            4.6.0          py34_0  pkgs/free           
beautifulsoup4            4.6.0          py35_0  pkgs/free           
beautifulsoup4            4.6.0  py35h442a8c9_1  pkgs/main           
beautifulsoup4            4.6.0          py36_0  pkgs/free           
beautifulsoup4            4.6.0          py36_1  pkgs/main           
beautifulsoup4            4.6.0  py36h49b8c8c_1  pkgs/main           
beautifulsoup4            4.6.0          py37_1  pkgs/main
```

<a name="install_packages"></a>
## Install Packages
Installing packages is simple. You can either install them into your current environment or you can specify the environment to install them into. If you are not currently in an "active"  environment, Anaconda will assume that you want to install to the *root*/**base** environment.

<a name="current_environment"></a>
### Current Environment
Installing to the current environment is as simple as:
```
conda install beautifulsoup4
```

<a name="other_environment"></a>
### Other Environment
If you are not currently in the active environment that you want to install to, you can still install into that environment by specifying its name:
```
conda install --name pybites beautifulsoup4
```

<a name="install_packages_not_found"></a>
## Installing Packages Not Found
A list of all available packages can be found at  [Anaconda](https://docs.anaconda.com/anaconda/packages/pkg-docs). Now, what do you do if the package that you want isn't available?

```
conda search black
Loading channels: done

PackagesNotFoundError: The following packages are not available from current channels:

  - black

Current channels:

  - https://repo.anaconda.com/pkgs/main/linux-64
  - https://repo.anaconda.com/pkgs/main/noarch
  - https://repo.anaconda.com/pkgs/free/linux-64
  - https://repo.anaconda.com/pkgs/free/noarch
  - https://repo.anaconda.com/pkgs/r/linux-64
  - https://repo.anaconda.com/pkgs/r/noarch
  - https://repo.anaconda.com/pkgs/pro/linux-64
  - https://repo.anaconda.com/pkgs/pro/noarch

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.
```

<a name="search_alternate_channels"></a>
### Search Alternate Channels
As you can see `black` is not in Anaconda's default "channels". A channel is like a repository of packages. Anaconda allows you to specify different channels as well, with the use of the **-c** flag. For example:

```
conda search -c conda-forge black
Loading channels: done
# Name                  Version           Build  Channel             
black                    18.4a4            py_0  conda-forge         
black                    18.5b0            py_0  conda-forge         
black                    18.5b1            py_0  conda-forge         
black                    18.6b2            py_0  conda-forge
```

<a name="install_package_from_a_channel"></a>
#### Install Package From A Channel
You already know what the **Channel** column is showing you, so I won't cover that again. The **Version** column shows the version of the package and the **Build** column shows you what version of Python it's for. The cool thing about Anaconda is that if you need a certain version of a package, you just specify it and it will select the one that will work with the version of Python that you are currently using.

Installing packages from a channel is relatively similar to searching for packages. I'll demonstrate by installing `black` from the *conda-forge* channel:

```
conda install -c conda-forge black
Solving environment: done

## Package Plan ##

  environment location: /home/mohh/anaconda3/envs/pybites

  added / updated specs:
    - black


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    appdirs-1.4.3              |             py_1          11 KB  conda-forge
    black-18.6b2               |             py_0          67 KB  conda-forge
    attrs-18.1.0               |             py_1          25 KB  conda-forge
    click-6.7                  |             py_1          54 KB  conda-forge
    toml-0.9.4                 |             py_0          14 KB  conda-forge
    ca-certificates-2018.4.16  |                0         139 KB  conda-forge
    openssl-1.0.2o             |                0         3.5 MB  conda-forge
    ------------------------------------------------------------
                                           Total:         3.8 MB

The following NEW packages will be INSTALLED:

    appdirs:         1.4.3-py_1        conda-forge
    attrs:           18.1.0-py_1       conda-forge
    black:           18.6b2-py_0       conda-forge
    click:           6.7-py_1          conda-forge
    toml:            0.9.4-py_0        conda-forge

The following packages will be UPDATED:

    ca-certificates: 2018.03.07-0                  --> 2018.4.16-0 conda-forge
    openssl:         1.0.2o-h20670df_0             --> 1.0.2o-0    conda-forge

Proceed ([y]/n)?


Downloading and Extracting Packages
appdirs-1.4.3        |   11 KB | ####################################### | 100%
black-18.6b2         |   67 KB | ####################################### | 100%
attrs-18.1.0         |   25 KB | ####################################### | 100%
click-6.7            |   54 KB | ####################################### | 100%
toml-0.9.4           |   14 KB | ####################################### | 100%
ca-certificates-2018 |  139 KB | ####################################### | 100%
openssl-1.0.2o       |  3.5 MB | ####################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```

<a name="add_additional_channels"></a>
### Add Additional Channels
If you would like to add a certain channel to the ones that are search by default, the following command will do:

```
conda config --add channels conda-forge
```

<a name="install_packages_with_pip"></a>
### Install Packages With Pip
I haven't added any channels to my setup. I'm only covering it here because it was mentioned on Slack. It's been my experience that the Anaconda packages usually lag behind a bit from what's bleeding edge. So If you still are not able to find a channel that has your package, or you just want to use a more up to date package, you can just install it with `pip`.

I searched for **black** with `pip search black` and discovered that the latest version of black available was *18.6b4*. The latest one in *conda-forge* at the time of this writing was *18.6b2*.

```
pip install black
```

<a name="remove_packages"></a>
## Remove Packages
> I forgot to mention it earlier when installing a package, but multiple packages can be installed at the same time, just like one or more can be removed at the same time.

Didn't use a package that you added and now want to remove it? Simple enough:

```
conda remove beautifulsoup4 black
Solving environment: done

## Package Plan ##

  environment location: /home/mohh/anaconda3/envs/pybites

  removed specs:
    - beautifulsoup4
    - black


The following packages will be REMOVED:

    black:           18.6b2-py_0 conda-forge

The following packages will be UPDATED:

    openssl:         1.0.2o-0    conda-forge --> 1.0.2o-h20670df_0

The following packages will be DOWNGRADED:

    ca-certificates: 2018.4.16-0 conda-forge --> 2018.03.07-0     

Proceed ([y]/n)?

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```

<a name="install_packages_while_creating_environment"></a>
## Install Packages While Creating Environment
If you've been following along, I'm sure you've noticed that installing packages takes a bit of time. You could streamline your process by combining the commands and running them all at once!

```
conda create --name pybites python=3.7 beautifulsoup4 requests pytest        
Solving environment: done

## Package Plan ##

  environment location: /home/mohh/anaconda3/envs/pybites

  added / updated specs:
    - beautifulsoup4
    - pytest
    - python=3.7
    - requests


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    pytest-3.6.3               |           py37_0         300 KB

The following NEW packages will be INSTALLED:

    asn1crypto:      0.24.0-py37_0          
    atomicwrites:    1.1.5-py37_0           
    attrs:           18.1.0-py37_0          
    beautifulsoup4:  4.6.0-py37_1           
    ca-certificates: 2018.03.07-0           
    certifi:         2018.4.16-py37_0       
    cffi:            1.11.5-py37h9745a5d_0  
    chardet:         3.0.4-py37_1           
    cryptography:    2.2.2-py37h14c3975_0   
    idna:            2.7-py37_0             
    libedit:         3.1.20170329-h6b74fdf_2
    libffi:          3.2.1-hd88cf55_4       
    libgcc-ng:       7.2.0-hdf63c60_3       
    libstdcxx-ng:    7.2.0-hdf63c60_3       
    more-itertools:  4.2.0-py37_0           
    ncurses:         6.1-hf484d3e_0         
    openssl:         1.0.2o-h20670df_0      
    pip:             10.0.1-py37_0          
    pluggy:          0.6.0-py37_0           
    py:              1.5.4-py37_0           
    pycparser:       2.18-py37_1            
    pyopenssl:       18.0.0-py37_0          
    pysocks:         1.6.8-py37_0           
    pytest:          3.6.3-py37_0           
    python:          3.7.0-hc3d631a_0       
    readline:        7.0-ha6073c6_4         
    requests:        2.19.1-py37_0          
    setuptools:      39.2.0-py37_0          
    six:             1.11.0-py37_1          
    sqlite:          3.24.0-h84994c4_0      
    tk:              8.6.7-hc745277_3       
    urllib3:         1.23-py37_0            
    wheel:           0.31.1-py37_0          
    xz:              5.2.4-h14c3975_4       
    zlib:            1.2.11-ha838bed_2      

Proceed ([y]/n)?


Downloading and Extracting Packages
pytest-3.6.3         |  300 KB | ####################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate pybites
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

If you had previously added the *conda-forge* channel, `black` could have been specified as well. In this case, I would have to install it separately with `pip` so that I would be running the most recent one.

<a name="export_environment_configuration"></a>
## Export Environment Configuration
You've put a lot of work into creating the perfect environment. Wouldn't it be nice to be able to recreate the environment from a file, like `pip` does with requirements.txt? Anaconda has you covered! With `pip` you use `pip freeze` to create the file; with Anaconda its done with `conda env export`:

```
conda env export
name: pybites
channels:
  - defaults
dependencies:
  - asn1crypto=0.24.0=py37_0
  - atomicwrites=1.1.5=py37_0
  - attrs=18.1.0=py37_0
  - beautifulsoup4=4.6.0=py37_1
  - ca-certificates=2018.03.07=0
  - certifi=2018.4.16=py37_0
  - cffi=1.11.5=py37h9745a5d_0
  - chardet=3.0.4=py37_1
  - cryptography=2.2.2=py37h14c3975_0
  - idna=2.7=py37_0
  - libedit=3.1.20170329=h6b74fdf_2
  - libffi=3.2.1=hd88cf55_4
  - libgcc-ng=7.2.0=hdf63c60_3
  - libstdcxx-ng=7.2.0=hdf63c60_3
  - more-itertools=4.2.0=py37_0
  - ncurses=6.1=hf484d3e_0
  - openssl=1.0.2o=h20670df_0
  - pip=10.0.1=py37_0
  - pluggy=0.6.0=py37_0
  - py=1.5.4=py37_0
  - pycparser=2.18=py37_1
  - pyopenssl=18.0.0=py37_0
  - pysocks=1.6.8=py37_0
  - pytest=3.6.3=py37_0
  - python=3.7.0=hc3d631a_0
  - readline=7.0=ha6073c6_4
  - requests=2.19.1=py37_0
  - setuptools=39.2.0=py37_0
  - six=1.11.0=py37_1
  - sqlite=3.24.0=h84994c4_0
  - tk=8.6.7=hc745277_3
  - urllib3=1.23=py37_0
  - wheel=0.31.1=py37_0
  - xz=5.2.4=h14c3975_4
  - zlib=1.2.11=ha838bed_2
  - pip:
    - appdirs==1.4.3
    - black==18.6b4
    - click==6.7
    - toml==0.9.4
prefix: /home/mohh/anaconda3/envs/pybites
```

> Notice how packages that are installed with *pip* are shown. Those all happen to be dependencies of black.

Just like the `pip` command, this must be *piped* into a text file. Anaconda uses the YAML format, so the command would be `conda env export > environment.yml`.

<a name="create_environment_from_yaml_file"></a>
## Create Environment From File
As it is, the *environemnt.yml* file can be used to recreate your environment on your platform and on your machine only. If you are in the directory with the YAML file, simply use `conda env create`. Anaconda will automatically detect the file and create it.

```
conda env create
Solving environment: done

Downloading and Extracting Packages
py-1.5.4             |   63 KB | ####################################### | 100%
ncurses-6.1          |  1.2 MB | ####################################### | 100%
idna-2.7             |   50 KB | ####################################### | 100%
python-3.7.0         | 22.1 MB | ####################################### | 100%
chardet-3.0.4        |   96 KB | ####################################### | 100%
more-itertools-4.2.0 |   38 KB | ####################################### | 100%
zlib-1.2.11          |   93 KB | ####################################### | 100%
tk-8.6.8             |  3.1 MB | ####################################### | 100%
libffi-3.2.1         |   47 KB | ####################################### | 100%
sqlite-3.24.0        |  1.5 MB | ####################################### | 100%
xz-5.2.3             |  854 KB | ####################################### | 100%
pycparser-2.18       |   84 KB | ####################################### | 100%
pluggy-0.6.0         |   13 KB | ####################################### | 100%
asn1crypto-0.24.0    |   72 KB | ####################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate pybites
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

<a name="prepare_environment_yaml_for_distribution"></a>
## Prepare Environment YAML For Distribution
As stated above, it's only good for your current machine. What if you want to share it with others or recreate it on another machine? You'll first have to edit the file:

* Remove the *prefix* line at the end of the file, since it's specific to your user name and file structure.
* Remove everything after the last `=` sign, to include the `=`, from the last parts of the package names.

Since a lot of the packages listed are dependencies of the packages that you've added, I normally remove them all and only leave the ones that I specifically installed myself. Not sure if that's best practice, but it's worked fine for me so far.

Once done, your file should look like this:

```
name: pybites
channels:
  - defaults
dependencies:
  - beautifulsoup4=4.6.0
  - pytest=3.6.3
  - python=3.7.0
  - requests=2.19.1
  - pip:
    - black==18.6b4
```

<a name="list_packages"></a>
## List Packages
To view what packages are installed in your environment `conda list` will get the job done:

> Note that you can also tell which were installed with pip.

```
conda list
# packages in environment at /home/mohh/anaconda3/envs/pybites:
#
# Name                    Version                   Build  Channel
appdirs                   1.4.3                     <pip>
asn1crypto                0.24.0                   py37_0  
atomicwrites              1.1.5                    py37_0  
attrs                     18.1.0                   py37_0  
beautifulsoup4            4.6.0                    py37_1  
black                     18.6b4                    <pip>
ca-certificates           2018.03.07                    0  
certifi                   2018.4.16                py37_0  
cffi                      1.11.5           py37h9745a5d_0  
chardet                   3.0.4                    py37_1  
click                     6.7                       <pip>
cryptography              2.2.2            py37h14c3975_0  
idna                      2.7                      py37_0  
libedit                   3.1.20170329         h6b74fdf_2  
libffi                    3.2.1                hd88cf55_4  
libgcc-ng                 7.2.0                hdf63c60_3  
libstdcxx-ng              7.2.0                hdf63c60_3  
more-itertools            4.2.0                    py37_0  
ncurses                   6.1                  hf484d3e_0  
openssl                   1.0.2o               h20670df_0  
pip                       10.0.1                   py37_0  
pluggy                    0.6.0                    py37_0  
py                        1.5.4                    py37_0  
pycparser                 2.18                     py37_1  
pyopenssl                 18.0.0                   py37_0  
pysocks                   1.6.8                    py37_0  
pytest                    3.6.3                    py37_0  
python                    3.7.0                hc3d631a_0  
readline                  7.0                  ha6073c6_4  
requests                  2.19.1                   py37_0  
setuptools                39.2.0                   py37_0  
six                       1.11.0                   py37_1  
sqlite                    3.24.0               h84994c4_0  
tk                        8.6.7                hc745277_3  
toml                      0.9.4                     <pip>
urllib3                   1.23                     py37_0  
wheel                     0.31.1                   py37_0  
xz                        5.2.4                h14c3975_4  
zlib                      1.2.11               ha838bed_2
```

<a name="clone_an_environment"></a>
## Clone An Environment
There might come a time when you have a need to clone an existing environment. I like to have an environment with all packages installed to play around with, so I clone the *base* environment. That way I can keep *base* vanilla, yet still be able to install any package that I want into the clone without messing anything up in *base*.

```
conda create --clone base --name ml
Source:      /home/mohh/anaconda3
Destination: /home/mohh/anaconda3/envs/ml
The following packages cannot be cloned out of the root environment:
 - conda-4.5.8-py36_0
 - conda-build-3.10.9-py36_0
 - conda-env-2.6.0-1
Packages: 259
Files: 68
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate ml
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

If you do clone the *base* environment, you will get the above message about certain packages not being copied. It's completely normal and should not be displayed when cloning any other environment.

<a name="updates"></a>
## Updates
Updating Anaconda can be a confusing mess. You would think that using the GUI Navigator (`anaconda-navigator`) would be easier to use, but I haven't had much luck with it. It's clunky and slow.

Looking for instructions online is also a big fat mess. Everyone contradicts each other with their own opinions. I've tried several of them and this is what has worked for me.

Use the following commands in the order shown instead:

1. `conda update conda`
2. `conda update anaconda`
3. `conda update --all`

> NOTE: Make sure to read the messages that you get while updating anaconda. The last time I did it, I skipped it because it wanted to downgrade my version of Python from 3.6.6 to 3.6.5. It must have been to satisfy the dependency of one of the updated packages, so I skipped it and only ran steps `1` & `2`.

<a name="environment_variables"></a>
## Environment Variables
There will come a time when you will need to pass a password or an API key to your programs. The easiest way is to just put it into your code and remove it before committing your code, but that is a very good way to publish your secrets by accident. A much better way is to use environment variables. With Anaconda, you can add environment variables that are specific to each environment. This takes a bit of work on your part, but it works great and I've used it with great success in the past.

You will need to know where your virtual environment resides. If you remember from above, you can find that out with `conda env list`. You will need to navigate to that directory and create the following structure and files:

```
etc/
└── conda
    ├── activate.d
    │   └── env_vars.sh
    └── deactivate.d
        └── env_vars.sh
```

The *etc* directory may or may not exist. It sometimes gets created by certain packages. For Windows users, instead of **env_vars.sh** name the files **env_vars.bat**.

The file in *activate.d* will look something like this on Linux and perhaps on Mac's as well. I don't own a Mac, so can't confirm:

###### activate.d/env_vars.sh:
```
export API_KEY="cc2a491aee9e40f32b1a184cc62902b11cae33da9f6620ffc47077da179aa800"
```

The one under *deactivate.d* clears the assignment:

###### deactivate.d/env_vars.sh:
```
export API_KEY=""
```

> For Windows, I think that you do not need the export command. If someone could verify for me, that would be great!

The next time that you activate your environment, the script in *activate.d* runs and sets your variables. Similarly, when you deactivate the environment the script in *deactivate.d* clears it.

<a name="tl;dr"></a>
## TL;DR
**T**oo **L**ong**;** **D**int't **R**ead? I've got you covered!

| Task | Command |
| ----------- | -------:|
| Create virtual environment | `conda create --name ENVNAME` |
| Activate environment | `conda activate ENVNAME` |
| Deactivate environment | `conda deactivate` |
| List virtual environments | `conda env list` |
| Remove virtual environment | `conda env remove --name ENVNAME` |
| Search for packages | `conda search PACKAGENAME` |
| Install packages | `conda install PACKAGE1 PACKAGE2...` |
| Install package in other env | `conda install --name ENVNAME PACKAGENAME` |
| Search alternate channel | `conda search -c CHANNELNAME PACKAGENAME` |
| Install from channel | `conda install -c CHANNELNAME PACKAGENAME` |
| Add additional channel | `conda config --add channels CHANNELNAME` |
| Remove packages | `conda remove PACKAGE1 PACKAGE2...` |
| Create env and install packages | `conda create --name ENVNAME PACKAGE1 PACKAGE2...` |
| Export env config | `conda env export > environment.yml` |
| Create env from environment.yml | `conda env create` |
| List packages | `conda list` |
| Clone environment | `conda create --clone ORIGINALENV --name NEWENV` |
| Update conda | `conda update conda` |
| Update Anaconda | `conda update anaconda` |
| Update all packages | `conda update --all` |

---

Keep Calm and Code in Python!

-- [Martin](pages/guests.html#martinuribe)
