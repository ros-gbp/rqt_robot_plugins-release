Name:           ros-jade-rqt-robot-plugins
Version:        0.5.5
Release:        0%{?dist}
Summary:        ROS rqt_robot_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_robot_plugins
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-rqt-moveit
Requires:       ros-jade-rqt-nav-view
Requires:       ros-jade-rqt-pose-view
Requires:       ros-jade-rqt-robot-dashboard
Requires:       ros-jade-rqt-robot-monitor
Requires:       ros-jade-rqt-robot-steering
Requires:       ros-jade-rqt-runtime-monitor
Requires:       ros-jade-rqt-rviz
Requires:       ros-jade-rqt-tf-tree
BuildRequires:  ros-jade-catkin

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
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Nov 02 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.5-0
- Autogenerated by Bloom

* Tue Mar 08 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.4.3-0
- Autogenerated by Bloom

* Fri Jul 24 2015 Aaron Blasdel <ablasdel@gmail.com> - 0.4.2-0
- Autogenerated by Bloom

* Thu Apr 30 2015 Aaron Blasdel <ablasdel@gmail.com> - 0.4.1-0
- Autogenerated by Bloom

