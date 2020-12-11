from pymavlink import mavutil, mavwp

master = mavutil.mavlink_connection('tcp:localhost:11520')

master.wait_heartbeat(blocking=True)


wp = mavwp.MAVWPLoader()
seq = 1
frame = mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT
radius = 1
for i in range(N):
            wp.add(mavutil.mavlink.MAVLink_mission_item_message(master.target_system,
                         master.target_component,
                         seq,
                         frame,
                         mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
                         0, 0, 0, radius, 0, 0,
                         lat[i],lon[i],alt[i]))
            seq += 1

master.waypoint_clear_all_send()
master.waypoint_count_send(wp.count())