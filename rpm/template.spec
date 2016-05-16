Name:           ros-kinetic-rqt-tf-tree
Version:        0.5.3
Release:        0%{?dist}
Summary:        ROS rqt_tf_tree package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_tf_tree
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-python-qt-binding >= 0.2.19
Requires:       ros-kinetic-qt-dotgraph
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rqt-graph
Requires:       ros-kinetic-rqt-gui
Requires:       ros-kinetic-rqt-gui-py
Requires:       ros-kinetic-tf2
Requires:       ros-kinetic-tf2-msgs
Requires:       ros-kinetic-tf2-ros
BuildRequires:  python-mock
BuildRequires:  ros-kinetic-catkin

%description
rqt_tf_tree provides a GUI plugin for visualizing the ROS TF frame tree.

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
* Mon May 16 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.3-0
- Autogenerated by Bloom

* Fri Apr 29 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.2-1
- Autogenerated by Bloom

* Fri Apr 29 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.2-0
- Autogenerated by Bloom

* Thu Apr 28 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.5.1-0
- Autogenerated by Bloom

