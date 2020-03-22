import neo_ws_awss_switch as sw
import neo_ws_awss_funcs as f

keepOnOff = sw.isOn()
sw.setOnOff(True)   
f.AutoSetWorkset()
sw.setOnOff(keepOnOff)