Name:           ros-indigo-rqt-moveit
Version:        0.3.7
Release:        0%{?dist}
Summary:        ROS rqt_moveit package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_moveit
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-rosnode
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rostopic
Requires:       ros-indigo-rqt-gui
Requires:       ros-indigo-rqt-gui-py
Requires:       ros-indigo-rqt-py-common
Requires:       ros-indigo-rqt-topic
Requires:       ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-catkin

%description
An rqt-based tool that assists monitoring tasks for MoveIt! motion planner
developers and users. Currently the following items are monitored if they are
either running, existing or published: Node: /move_group Parameter:
[/robot_description, /robot_description_semantic] Topic: Following types are
monitored. Published &quot;names&quot; are ignored. [sensor_msgs/PointCloud,
sensor_msgs/PointCloud2, sensor_msgs/Image, sensor_msgs/CameraInfo] Since this
package is not made by the MoveIt! development team (although with assistance
from the them), please post issue reports to the designated tracker (not
MoveIt!'s main tracker).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Aug 18 2014 Isaac Isao Saito <130s@alumni.smu.edu> - 0.3.7-0
- Autogenerated by Bloom

