Title: Building Open vSwitch RPMs for Oracle Unbreakable Enterprise Linux 6
Date: 2014-05-11
Category: guide
Tags: openvswitch, guide, networking, virtualization, lab
Slug: ovs-uek-build-install
Author: S.S.

<!-- PELICAN_BEGIN_SUMMARY -->

[Open vSwitch](http://openvswitch.org/) (OVS) has become the de facto software virtual switch in cloud computing deployments where multi-tenancy is a primary requirement. From the website,
> *OVS is a production quality, multilayer virtual switch designed to enable massive network automation through programmatic extension, while 
still supporting standard management interfaces and protocols.*

The complete feature list can be found [here](http://openvswitch.org/features/). In this post, we will walk through the steps necessary to build OVS RPMs for Oracle's Unbreakable Enterprise Kernel v6. <!-- PELICAN_END_SUMMARY -->

### Environment
I will be using the following OL6 Kernel and OVS version 2.1.2:

	:::bash
	bash-4.1# uname -r
	2.6.39-400.109.4.el6uek.x86_64

	bash-4.1# ls openvswitch*
	openvswitch-2.1.2.tar.gz

### Build OVS RPMs
1. Get the OL6 yum configuration file from Oracle's public yum server.

        :::bash
        bash-4.1# cd /etc/yum.repos.d
        bash-4.1# wget http://public-yum.oracle.com/public-yum-ol6.repo

2. Edit the *public-yum-ol6.repo* configuration file to enable the **OL6_UEK_latest** repository.

        :::text
        [ol6_UEK_latest]
        name=Latest Unbreakable Enterprise Kernel for Oracle Linux $releasever ($basearch)
        baseurl=http://public-yum.oracle.com/repo/OracleLinux/OL6/UEK/latest/$basearch/
        gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-oracle
        gpgcheck=1
        enabled=1

3. Update yum and install the packages listed below.

		:::bash
		bash-4.1# yum update
		bash-4.1# yum install -y autoconf automake gcc libtool rpm-build 
		bash-4.1# yum install -y openssl-devel python-devel kernel-uek-debug-devel 
		bash-4.1# yum install -y kernel-uek-devel redhat-rpm-config kabi-whitelists

4. OL6 has a broken **build** symbolic link. A **ls** command on **/lib/modules/\`uname -r\`/build/** should result in a directory listing from **/usr/src/kernel/\`uname -r\`**. On OL6, it results in a "No such file or directory" error. We need to fix this. 

		:::bash
		bash-4.1# rm /lib/modules/`uname -r`/build
        bash-4.1# ln -s /usr/src/kernels/`uname -r` /lib/modules/`uname -r`/build

5. Create the RPM building environment,

		:::bash
		bash-4.1# mkdir -p ~/rpmbuild/{SOURCES,RPMS,BUILD,SPECS,SRPMS}

6. Copy over the Open vSwitch source tar.gz file to the RPM SOURCES directory, and untar it. Copy the **openvswitch-kmod.files** file to the RPM SOURCES directory as well.

		:::bash
		bash-4.1# cp ~/openvswitch-2.1.2.tar.gz ~/rpmbuild/SOURCES
		bash-4.1# cd ~/rpmbuild/SOURCES; tar -xzf openvswitch-2.1.2.tar.gz
		bash-4.1# cp openvswitch-2.1.2/rhel/openvswitch-kmod.files ./

7. Next, build userspace component of OVS

		:::bash
		bash-4.1# cd openvswitch-2.1.2
		bash-4.1# rpmbuild -bb rhel/openvswitch.spec

8. Build the OVS kernel module

		:::bash
		bash-4.1# rpmbuild -bb -D "kversion `uname -r`" -D "kflavors default debug" rhel/openvswitch-kmod-rhel6.spec

9. This results in the following four RPMs:

		:::bash
		bash-4.1# ls ~/rpmbuild/RPMS/x86_64/
		kmod-openvswitch-2.1.2-1.el6.x86_64.rpm  kmod-openvswitch-debug-2.1.2-1.el6.x86_64.rpm	openvswitch-2.1.2-1.x86_64.rpm	openvswitch-debuginfo-2.1.2-1.x86_64.rpm

kmod-\* are the OVS kernel module RPMs and openvswitch-\* are the RPMs for the userspace component of OVS. 

As is evident, this guide is very specific to Oracle's UEKv6. In a future post, I will be talking more about the features and capabilities that OVS provides. I will also show how OVS can be used to create multi-tenant virtual network overlays using VXLAN/GRE tunnels.
 



















