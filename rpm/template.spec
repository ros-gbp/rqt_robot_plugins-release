Name:           ros-kinetic-rqt-robot-plugins
Version:        0.5.4
Release:        0%{?dist}
Summary:        ROS rqt_robot_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_robot_plugins
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-rqt-moveit
Requires:       ros-kinetic-rqt-nav-view
Requires:       ros-kinetic-rqt-pose-view
Requires:       ros-kinetic-rqt-robot-dashboard
Requires:       ros-kinetic-rqt-robot-monitor
Requires:       ros-kinetic-rqt-robot-steering
Requires:       ros-kinetic-rqt-runtime-monitor
Requires:       ros-kinetic-rqt-rviz
Requires:       ros-kinetic-rqt-tf-tree
BuildRequires:  ros-kinetic-catkin

%description
Metapackage of rqt plugins that are particularly used with robots during its
operation. To run any rqt plugins, just type in a single command
&quot;rqt&quot;, then select any plugins you want from the GUI that launches
afterwards. rqt consists of three following metapackages: rqt - provides a
container window where all rqt tools can be docked at. rqt plugin developers
barely needs to pay attention. rqt_common_plugins - ROS backend tools suite that
can be used on/off of robot runtime. rqt_robot_plugins (You're here!)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Sep 19 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.4-0
- Autogenerated by Bloom

* Mon May 16 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.3-0
- Autogenerated by Bloom

* Fri Apr 29 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.2-1
- Autogenerated by Bloom

* Fri Apr 29 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.2-0
- Autogenerated by Bloom

* Thu Apr 28 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.1-0
- Autogenerated by Bloom

