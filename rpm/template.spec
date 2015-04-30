Name:           ros-jade-rqt-pose-view
Version:        0.4.1
Release:        0%{?dist}
Summary:        ROS rqt_pose_view package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_pose_view
Source0:        %{name}-%{version}.tar.gz

Requires:       PyOpenGL
Requires:       PyQt4
Requires:       python-rospkg
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-python-qt-binding
Requires:       ros-jade-rospy
Requires:       ros-jade-rostopic
Requires:       ros-jade-rqt-gui
Requires:       ros-jade-rqt-gui-py
Requires:       ros-jade-tf
BuildRequires:  ros-jade-catkin

%description
rqt_pose_view provides a GUI plugin for visualizing 3D poses.

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
* Thu Apr 30 2015 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.4.1-0
- Autogenerated by Bloom

