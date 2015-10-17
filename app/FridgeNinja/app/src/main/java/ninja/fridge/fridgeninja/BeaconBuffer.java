package ninja.fridge.fridgeninja;

import org.altbeacon.beacon.Beacon;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;

/**
 * Created by Benedikt on 17.10.2015.
 */
public class BeaconBuffer implements BeaconsUpdateCallback {
    private boolean monitoring = false;
    public static class BeaconInfo {
        public BeaconInfo() { }
        public BeaconInfo(Beacon beacon) {
            this.beacon = beacon;
            this.minDistance = beacon.getDistance();
        }

        Beacon beacon;
        double minDistance = Float.MAX_VALUE;
    }


    private HashMap<String, BeaconInfo> knownBeacons = new HashMap<>();

    @Override
    public void beaconsChanged(Collection<Beacon> newBeacons) {
        if(monitoring) {
            for(Beacon beacon : newBeacons) {
                String id = beacon.getBluetoothAddress();
                if(!knownBeacons.containsKey(id)) {
                    knownBeacons.put(id, new BeaconInfo(beacon));
                } else {
                    BeaconInfo info = knownBeacons.get(id);
                    if(beacon.getDistance() < info.minDistance) {
                        info.minDistance = beacon.getDistance();
                    }
                }
            }
        }
    }

    public void reset() {
        monitoring = false;
        knownBeacons.clear();
    }

    public void startMonitoring() {
        monitoring = true;
    }

    public void stopMonitoring() {
        monitoring = false;
    }

    public List<BeaconInfo> orderedResults() {
        Collection<BeaconInfo> beacons = knownBeacons.values();
        List<BeaconInfo> list = new ArrayList<BeaconInfo>(beacons);
        Collections.sort(list, new Comparator<BeaconInfo>() {
            @Override
            public int compare(BeaconInfo lhs, BeaconInfo rhs) {
                return (int)(rhs.minDistance - lhs.minDistance);
            }
        });
        return list;
    }
}
