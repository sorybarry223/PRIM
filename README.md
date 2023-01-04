# PRIM PROJECT
This is Sory Ibrahima BARRY's own omplementation of PoC implementation for the USENIX 2022 paper [**AEPIC Leak: Architecturally Leaking Uninitialized Data from the Microarchitecture**](https://aepicleak.com/aepicleak.pdf) by [Pietro Borrello](https://pietroborrello.github.io), [Andreas Kogler](https://andreaskogler.com), [Martin Schwarzl](https://martinschwarzl.at/), [Moritz Lipp](https://mlq.me/), [Daniel Gruss](https://gruss.cc), and [Michael Schwarz](https://misc0110.net).
The official GitHub repository is [**here**](https://github.com/IAIK/AEPIC).
You can clone it to your own laptop.
```bash
$ cd ~
$ mkdir my_project_name
$ cd my_project_name
$ git clone https://github.com/IAIK/AEPIC.git
```
If you don't have git installed yet, you have to install it first.
```bash
$ sudo apt-get update
$ sudo apt-get install git
```

I will do this implementation on Ubuntu 22.04, but it should work on any more recent version. The hole implementation does not take more than 30min.
First you have to check wether your CPU is vulnerable or not in [**Intel's website**](https://www.intel.com/content/www/us/en/developer/topic-technology/software-security-guidance/processors-affected-consolidated-product-cpu-model.html). You can check your CPU version with the following command:
```bash
$ lscpu
```
Then we have to ensure that our machine is booted in xAPIC mode, by providing nox2apic in the Linux kernel command line. Since my bootloader is grub, for me it will be:
```bash
$ cd 
$ sudo nano /etc/default/grub
```
Then adding the nox2apic and dis_ucode_ldr parameters to the comand GRUB_CMDLINE_LINUX.
So it will be 
```bash
GRUB_CMDLINE_LINUX="nox2apic dis_ucode_ldr"
```
We can save and exit the file with crtl-o, enter,ctrl-x.
We will now update the grub:
```bash
$ sudo update-grub
```
Then we will reboot your system:
```bash
$ sudo reboot
```
Let me explain. Grub is a firmware that is responsible for loading and managing your boot process. At boot time, you can give it some parameters. For instance, we are giving it the instruction to boot our device in xAPIC mode by providing it the parameter nox2apic. The second parameter is to avoid applying microcode updates that include SGX mitigations if you want to attack it.
The next step will be to install g++ 11:
```bash
$ sudo apt install -y g++-11
```
If you have another g++ version you should try to downgrade it to this specific version.
Of course if you dont have the gcc installed yet you have to do it also:
```bash
$ sudo apt-get install gcc
```
A kernel module is provided to dump the content of the APIC MMIO region. This confirms that the APIC leaks data on the machine tested.
```bash
$ cd src/apic_dump
$ make run
```
As you can see we have an error from the official repository. We can correct it by deleting line 60 and changing it to 
```C
volatile unsigned char* local_apic = ioremap_cache(0xfee00000, 0x1000);
```
basically we just change change the function ioremap_nocache() to ioremap_cache().
Now re-run the make run command again and observe the output.
If your CPU is vulnerable, running the apic_dump you will observe spurious memory returned by the APIC, as opposed to 0x00 bytes. Which means you can observe values different from zeros.

## 1. Dependencies
In order to build the project, we first need to build the sgx-step SDK and library. If you don't know what a software development kit is. I suggest you check it on [**wikipedia**](https://en.wikipedia.org/wiki/Software_development_kit). 
Here is becomes tricky. The official repository does not give us the complete sgx-step directory in which we can install the development tools needed to build the project. So we need to download it on this [**repository**](https://github.com/jovanbulck/sgx-step). If you are still in the src/apic_dump directory:
```bash
$ cd ..
$ git clone https://github.com/jovanbulck/sgx-step.git
```
Which will install all the tools needed.
We can now init this submodule:
```bash
$ git submodule init
$ cd sgx-step
$ cd sdk/intel-sdk/ && ./install_SGX_SDK.sh && source /opt/intel/sgxsdk/environment
$ cd ..
$ cd ..
$ cd libsgxstep && make && cd ..
```
This will take some times but after that our tools we be there for us.

## 2. Build

This step builds the Custom SGX Driver and the attack PoCs. Change your directory to src/

```bash
$ cd ..
$ cd ..
$ cd src
$ make
```
As we can see, we have another error coming from the official repository. We will correct in the file src/common/aepic_interface.h
At line 13, we change the script
```C
typedef uint64_t __u64; 
```
to
```C
__extension__ typedef unsigned long long __u64;
```
Then you can rebuild your code mith
```bash
$ make
```

## 3. Load the Custom SGX Driver

```bash
$ cd src
$ make load
```
Oups, we have again an error. Normal, as the first one, we have to change line 455 in src/linux-sgx-driver/sgx_ioctl.c
Again, change the ioremap_nocache() function to ioremap_cache(). And again in line 550.

## 4. Run the experiments

### Victim Enclaves

Victim runner to experiment:
* aes: to leak Intel IPPC AES
* egetkey: to leak seal key
* memory: to leak simple memory content
* rdrand: to leak rdrand content
* rsa: to leak rsa private key
* simple_ssa: to leak SSA region

### Intel's SGX software installation:
In order to leak data, we first need to install intel's SDK software. We can follow the steps in Intel's [**website**](https://download.01.org/intel-sgx/sgx-dcap/1.11/linux/docs/Intel_SGX_SW_Installation_Guide_for_Linux.pdf).
We first need to do:
```bash
$ sudo apt-get install build-essential ocaml automake autoconf libtool wget python libssl-dev dkms
```
As we can see, python command is deprecated so we need to re-adjust the latest command by replacing python by python-is-python3
```bash
$ sudo apt-get install build-essential ocaml automake autoconf libtool wget python-is-python3 libssl-dev dkms
```

# GEM5 SIMULATION

## 1. Building
You can build gem5 from the official [**website**](https://www.gem5.org/documentation/general_docs/building)
## 2. Running
After building your Python simulation script, you can run it with:
```bash
build/X86/gem5.opt [complete path to your simulation script]
```
But you have to be in the gem5 folder first. It is simply the folder you obtain after cloning the gem5 project from the official github repository.