Name:           ros-jade-rqt-robot-monitor
Version:        0.4.2
Release:        0%{?dist}
Summary:        ROS rqt_robot_monitor package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_robot_monitor
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
Requires:       ros-jade-diagnostic-msgs
Requires:       ros-jade-python-qt-binding
Requires:       ros-jade-qt-gui
Requires:       ros-jade-qt-gui-py-common
Requires:       ros-jade-rospy
Requires:       ros-jade-rqt-bag
Requires:       ros-jade-rqt-gui
Requires:       ros-jade-rqt-gui-py
Requires:       ros-jade-rqt-py-common
BuildRequires:  ros-jade-catkin

%description
rqt_robot_monitor displays diagnostics_agg topics messages that are published by
diagnostic_aggregator. rqt_robot_monitor is a direct port to rqt of
robot_monitor. All diagnostics are fall into one of three tree panes depending
on the status of diagnostics (normal, warning, error/stale). Status are shown in
trees to represent their hierarchy. Worse status dominates the higher level
status. Ex. 'Computer' category has 3 sub devices. 2 are green but 1 is error.
Then 'Computer' becomes error. You can look at the detail of each status by
double-clicking the tree nodes. Currently re-usable API to other pkgs are not
explicitly provided.

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
* Fri Jul 24 2015 Austin Hendrix <namniart@gmail.com> - 0.4.2-0
- Autogenerated by Bloom

* Thu Apr 30 2015 Austin Hendrix <namniart@gmail.com> - 0.4.1-0
- Autogenerated by Bloom

